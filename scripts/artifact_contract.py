#!/usr/bin/env python3
"""生成器与校验器共享的 artifact 校验和协议规则。

本模块是整个技能流水线的契约层，定义了：
  - schema 版本与四维度常量
  - 各协议的 profile（必填字段、定位字段、标准列）
  - artifact（points/match/model_spec/type_spec/point_reg）的校验逻辑
  - 点位分组校验与引用完整性校验
  - 工作簿/JSON 的原子写入工具

被以下脚本导入：
  - pipeline_v2.py：生成器与校验器的核心实现
  - validate_artifact.py：独立 artifact 校验入口
  - gen_device_model.py / gen_device_type.py / gen_point_table.py / verify_output.py：
    通过 pipeline_v2 间接依赖本模块
"""
from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path

# 当前 artifact schema 版本，所有新 JSON artifact 必须声明此版本
SCHEMA_VERSION = "2.1"
# 物模型四维度，贯穿所有校验与生成逻辑
DIMS = ("Attribute", "MeasurePoint", "Event", "Service")
# 点位 ID 命名规则：以字母开头，只含字母、数字、下划线
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")

# 各枚举字段的合法取值集合，校验时逐行比对
ALLOWED = {
    "*DataType": {"INT", "FLOAT", "STRING", "ENUM", "BOOL", "DATETIME"},
    "*R/W": {"R", "W", "RW"},
    "*IsRequired": {"True", "False", True, False},
    "*EventType": {"INFO", "ALARM", "FAULT"},
}

# 各协议族的 profile 定义：
#   required  —— 每行必填字段（缺失则在替换输出文件前报错）
#   locator   —— 定位字段（决定该测点是否生成点表行）
#   columns   —— 单列占位模板被扩展时的标准列集
PROTOCOL_PROFILES = {
    "modbus": {
        "required": ("address", "registerCount", "functionCode"), "locator": "address",
        "columns": ("pointName", "pointKey", "unit", "dataType", "address", "registerCount",
                    "functionCode", "coefficient", "order", "mask", "map", "basicValue",
                    "parentKey", "wait"),
    },
    "mqtt": {
        "required": ("topic", "jsonpath"), "locator": "topic",
        "columns": ("pointName", "pointKey", "unit", "dataType", "topic", "jsonpath",
                    "coefficient", "map", "wait"),
    },
    "opcua": {
        "required": ("tag",), "locator": "tag",
        "columns": ("pointName", "pointKey", "unit", "dataType", "tag", "coefficient", "map", "wait"),
    },
    "iec104": {
        "required": ("pointNum", "pointType"), "locator": "pointNum",
        "columns": ("pointName", "pointKey", "unit", "dataType", "pointNum", "pointType",
                    "coefficient", "map", "wait"),
    },
    "dlt645": {
        "required": ("dataTag", "dataLength", "ctrlCode"), "locator": "dataTag",
        "columns": ("pointName", "pointKey", "unit", "dataType", "dataFormat", "dataEncoding",
                    "frontCode", "dataTag", "dataLength", "ctrlCode", "frameInterval",
                    "coefficient", "map", "wait"),
    },
    "dlt698": {
        "required": ("OAD", "operationCode"), "locator": "OAD",
        "columns": ("pointName", "pointKey", "unit", "dataType", "OAD", "operationCode",
                    "coefficient", "map", "wait"),
    },
    "gateway": {
        "required": ("southSample",), "locator": "southSample",
        "columns": ("pointName", "pointKey", "unit", "dataType", "southSample", "precision",
                    "coefficient", "map", "wait"),
    },
}


class ContractError(ValueError):
    """契约校验失败异常，所有校验函数以此异常表达失败，由调用方捕获并转为 JSON 报告。"""
    pass


def protocol_family(name: str) -> str:
    """根据协议名识别其所属协议族。

    输入：
      name —— 协议名（如 "ModbusRTU_Vega_ARM64_V1.1.0"、"MQTT_Vega_ARM64_V1.0.0"）
    输出：
      协议族标识字符串（"modbus"/"mqtt"/"opcua"/"iec104"/"dlt645"/"dlt698"/"gateway"）
    作用：
      将大小写/分隔符各异的协议名归一化为协议族 key，用于查 PROTOCOL_PROFILES。
    被调用：
      pipeline_v2.validate_protocol_rows / generate_point_table；
      validate_artifact.validate_artifact（point_reg 分支）。
    """
    key = re.sub(r"[^a-z0-9]", "", (name or "").lower())
    if key.startswith("modbus"):
        return "modbus"
    if key.startswith("mqtt"):
        return "mqtt"
    if key.startswith("opcua"):
        return "opcua"
    if key.startswith("iec104"):
        return "iec104"
    if key.startswith("dlt645"):
        return "dlt645"
    if key.startswith("dlt698"):
        return "dlt698"
    if key.startswith("gateway"):
        return "gateway"
    raise ContractError(f"不支持或无法识别的协议: {name!r}")


def _require(obj, fields, where, errors):
    """检查对象是否包含所有必填字段，缺失则追加错误到 errors 列表。

    输入：
      obj    —— 待检查的 dict
      fields —— 必填字段名元组
      where  —— 错误定位描述（如 "model_spec.model"）
      errors —— 错误收集列表（就地追加）
    输出：无（通过 errors 副作用返回）
    作用：校验字段存在且非 None/空字符串。
    被调用：validate_artifact 内部各分支。
    """
    for field in fields:
        if field not in obj or obj[field] is None or obj[field] == "":
            errors.append(f"{where} 缺少必填字段 {field}")


def parse_datadefine(value, where="DataDefine"):
    """解析 DataDefine 字段为 Python 对象（dict/list）。

    输入：
      value —— DataDefine 原始值，可为 None/空、dict/list、JSON 字符串
               （raw 文档中含 <br> 换行标记，会被替换为换行符再解析）
      where —— 错误定位描述
    输出：
      None（空值）或解析后的 dict/list
    作用：
      将 raw 文档中 HTML 换行形式的 JSON 解析为标准对象，非法 JSON 抛 ContractError。
    被调用：
      normalize_datadefine；validate_point_groups（ENUM 枚举校验）；
      pipeline_v2.fill_sheet（写入工作簿前规范化）。
    """
    if value in (None, ""):
        return None
    if isinstance(value, (dict, list)):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = json.loads(value.replace("<br>", "\n"))
        except json.JSONDecodeError as exc:
            raise ContractError(f"{where} 非法 JSON: {exc.msg}") from exc
    else:
        raise ContractError(f"{where} 必须是 JSON 对象、数组或 JSON 字符串")
    if not isinstance(parsed, (dict, list)):
        raise ContractError(f"{where} 顶层必须是对象或数组")
    return parsed


def normalize_datadefine(value, where="DataDefine"):
    """将 DataDefine 规范化为 JSON 字符串（用于写入 Excel 单元格）。

    输入：
      value —— DataDefine 原始值（同 parse_datadefine）
      where —— 错误定位描述
    输出：
      None（空值）或 JSON 字符串（ensure_ascii=False，紧凑无空格）
    作用：parse_datadefine 的包装，输出序列化后的字符串。
    被调用：pipeline_v2.fill_sheet。
    """
    parsed = parse_datadefine(value, where)
    return None if parsed is None else json.dumps(parsed, ensure_ascii=False)


def validate_point_groups(groups, label="points"):
    """校验四维度点位分组的结构完整性（必填字段、ID 命名、枚举、事件等式等）。

    输入：
      groups —— {"Attribute": [...], "MeasurePoint": [...], "Event": [...], "Service": [...]}
      label  —— 错误定位前缀（如 "model_spec.add"、"type_spec.points"）
    输出：无（校验失败抛 ContractError，含所有错误行）
    作用：
      - 检查每行必填字段是否齐全
      - 检查 *ID 命名规则与维度内唯一性
      - 检查枚举字段取值合法性
      - 检查 ENUM 数据类型是否有非空 DataDefine.enum
      - 检查事件 *Condition 是否为"点位 = 值"等式，且不得用累计计数点位
      - 检查推断事件是否有 user_confirmed=true
      - 检查 Attribute 与 MeasurePoint 无重复 ID
    被调用：
      validate_artifact（model_spec.add / type_spec.points 分支）；
      pipeline_v2.verify_model / verify_type（校验已生成的工作簿）。
    """
    errors = []
    required = {
        "Attribute": ("*ID", "*Name_default", "*DataType", "*IsRequired"),
        "MeasurePoint": ("*ID", "*Name_default", "*DataType", "*R/W"),
        "Event": ("*ID", "*Name_default", "*EventType", "*Output", "*Condition"),
        "Service": ("*ID", "*Name_default"),
    }
    for dim in DIMS:
        rows = groups.get(dim, [])
        if not isinstance(rows, list):
            errors.append(f"{label}.{dim} 必须是数组")
            continue
        seen = set()
        for index, row in enumerate(rows):
            where = f"{label}.{dim}[{index}]"
            if not isinstance(row, dict):
                errors.append(f"{where} 必须是对象")
                continue
            _require(row, required[dim], where, errors)
            pid = row.get("*ID")
            if pid:
                if not ID_RE.fullmatch(str(pid)):
                    errors.append(f"{where} *ID 不符合命名规则: {pid!r}")
                if pid in seen:
                    errors.append(f"{label}.{dim} 存在重复 *ID: {pid}")
                seen.add(pid)
            for field, allowed in ALLOWED.items():
                if field in row and row[field] not in (None, "") and row[field] not in allowed:
                    errors.append(f"{where} {field} 非法: {row[field]!r}")
            try:
                dd = parse_datadefine(row.get("DataDefine"), f"{where}.DataDefine")
                if row.get("*DataType") == "ENUM":
                    enum = dd.get("enum") if isinstance(dd, dict) else None
                    if not isinstance(enum, dict) or not enum:
                        errors.append(f"{where} ENUM 必须提供非空 DataDefine.enum 对象")
            except ContractError as exc:
                errors.append(str(exc))
            if dim == "Event" and row.get("*Condition"):
                match = re.fullmatch(r"\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*(.+?)\s*", str(row["*Condition"]))
                if not match:
                    errors.append(f"{where} *Condition 必须是 '点位 = 值' 等式")
                elif re.search(r"(?:Number|Count|Times)$", match.group(1), re.I):
                    errors.append(f"{where} 不得用累计计数点位推断实时事件: {match.group(1)}")
                if row.get("inferred") and not row.get("user_confirmed"):
                    errors.append(f"{where} 是推断事件，缺少 user_confirmed=true")
    attributes = {row.get("*ID") for row in groups.get("Attribute", []) if isinstance(row, dict)}
    measures = {row.get("*ID") for row in groups.get("MeasurePoint", []) if isinstance(row, dict)}
    ambiguous = sorted((attributes & measures) - {None, ""})
    if ambiguous:
        errors.append(f"{label} Attribute 与 MeasurePoint 存在重复 ID: {ambiguous}")
    if errors:
        raise ContractError("\n".join(errors))


def validate_point_references(groups, label="points"):
    """校验事件/服务引用的点位是否存在于 Attribute/MeasurePoint 中。

    输入：
      groups —— 四维度点位分组（同 validate_point_groups）
      label  —— 错误定位前缀
    输出：无（校验失败抛 ContractError）
    作用：
      - 事件 *Output（逗号分隔的点位列表）和 *Condition 等式左侧点位必须存在
      - 服务 *Input 和 Output 引用的点位必须存在
      - 同 ID 的事件/服务本身不满足引用（必须指向 Attribute/MeasurePoint）
    被调用：validate_artifact（type_spec.points 分支）。
    """
    point_ids = {
        row.get("*ID") for dim in ("Attribute", "MeasurePoint")
        for row in groups.get(dim, []) if isinstance(row, dict) and row.get("*ID")
    }
    errors = []
    for row in groups.get("Event", []):
        for ref in str(row.get("*Output") or "").split(","):
            ref = ref.strip()
            if ref and ref not in point_ids:
                errors.append(f"{label}.Event/{row.get('*ID')} *Output 引用不存在的点位 {ref}")
        match = re.fullmatch(r"\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*(.+?)\s*", str(row.get("*Condition") or ""))
        if match and match.group(1) not in point_ids:
            errors.append(f"{label}.Event/{row.get('*ID')} *Condition 引用不存在的点位 {match.group(1)}")
    for row in groups.get("Service", []):
        for field in ("*Input", "Output"):
            for ref in str(row.get(field) or "").split(","):
                ref = ref.strip()
                if ref and ref not in point_ids:
                    errors.append(f"{label}.Service/{row.get('*ID')} {field} 引用不存在的点位 {ref}")
    if errors:
        raise ContractError("\n".join(errors))


def validate_artifact(spec, artifact_type, allow_legacy=True):
    """校验 artifact 是否符合 schema 2.1 契约（顶层字段 + 类型特定规则）。

    输入：
      spec           —— artifact 字典
      artifact_type  —— 期望的 artifact 类型（"points"/"match"/"model_spec"/"type_spec"/"point_reg"）
      allow_legacy   —— 是否兼容未声明 schema_version/artifact_type 的旧版 artifact
    输出：
      warnings 列表（校验通过时返回警告，如旧版迁移提示）
    作用：
      - 检查 schema_version 和 artifact_type 是否正确
      - 按类型分支检查必填字段、ID 前缀、点位分组、引用完整性等
      - model_spec：检查 model.id 以 project_ 开头、device_type 以 public_ 开头、
        select/add 互斥、新增事件需有 evidence 或 user_confirmed
      - type_spec：检查 type.id 以 project_ 开头、点位引用完整
      - point_reg：检查协议必填字段、pointKey 命名
      - points/match：检查容器结构和维度完整性
    被调用：
      pipeline_v2.generate_model / generate_type / generate_point_table（生成前校验）；
      validate_artifact.py（独立校验入口，allow_legacy=False）。
    """
    errors, warnings = [], []
    version = spec.get("schema_version")
    actual_type = spec.get("artifact_type")
    if version is None and allow_legacy:
        warnings.append(f"旧版 {artifact_type} artifact 未声明 schema_version; 按 2.1 兼容读取")
    elif version != SCHEMA_VERSION:
        errors.append(f"schema_version 必须为 {SCHEMA_VERSION}, 当前: {version!r}")
    if actual_type is None and allow_legacy:
        warnings.append(f"旧版 artifact 未声明 artifact_type={artifact_type}")
    elif actual_type != artifact_type:
        errors.append(f"artifact_type 必须为 {artifact_type!r}, 当前: {actual_type!r}")

    if artifact_type == "model_spec":
        _require(spec, ("raw_doc", "model", "select", "add"), "model_spec", errors)
        if isinstance(spec.get("model"), dict):
            _require(spec["model"], ("id", "name", "device_type"), "model_spec.model", errors)
            if spec["model"].get("id") and not spec["model"]["id"].startswith("project_"):
                errors.append("model_spec.model.id 必须以 project_ 开头")
            if spec["model"].get("device_type") and not spec["model"]["device_type"].startswith("public_"):
                errors.append("model_spec.model.device_type 必须以 public_ 开头")
        if not isinstance(spec.get("select"), dict):
            errors.append("model_spec.select 必须是对象")
        else:
            for dim in DIMS:
                if not isinstance(spec["select"].get(dim, []), list):
                    errors.append(f"model_spec.select.{dim} 必须是数组")
            attr_ids = set(spec["select"].get("Attribute", []))
            measure_ids = set(spec["select"].get("MeasurePoint", []))
            ambiguous = sorted(attr_ids & measure_ids)
            if ambiguous:
                errors.append(f"model_spec.select Attribute 与 MeasurePoint 存在重复 ID: {ambiguous}")
        if not isinstance(spec.get("add"), dict):
            errors.append("model_spec.add 必须是对象")
        else:
            try:
                validate_point_groups(spec["add"], "model_spec.add")
            except ContractError as exc:
                errors.extend(str(exc).splitlines())
            for index, row in enumerate(spec["add"].get("Event", [])):
                if not row.get("evidence") and not row.get("user_confirmed"):
                    errors.append(
                        f"model_spec.add.Event[{index}] 缺少 evidence 或 user_confirmed=true; "
                        "设备模型不得无依据新增事件"
                    )
    elif artifact_type == "type_spec":
        _require(spec, ("type", "points"), "type_spec", errors)
        if isinstance(spec.get("type"), dict):
            _require(spec["type"], ("id", "name"), "type_spec.type", errors)
            if spec["type"].get("id") and not spec["type"]["id"].startswith("project_"):
                errors.append("type_spec.type.id 必须以 project_ 开头")
        if not isinstance(spec.get("points"), dict):
            errors.append("type_spec.points 必须是对象")
        else:
            try:
                validate_point_groups(spec["points"], "type_spec.points")
                validate_point_references(spec["points"], "type_spec.points")
            except ContractError as exc:
                errors.extend(str(exc).splitlines())
    elif artifact_type == "point_reg":
        _require(spec, ("protocol", "model_xlsx", "rows"), "point_reg", errors)
        if not isinstance(spec.get("rows"), dict):
            errors.append("point_reg.rows 必须是对象")
        elif spec.get("protocol"):
            try:
                family = protocol_family(spec["protocol"])
                required = PROTOCOL_PROFILES[family]["required"]
                for pid, row in spec["rows"].items():
                    if not ID_RE.fullmatch(str(pid)):
                        errors.append(f"point_reg.rows 的 pointKey 非法: {pid!r}")
                    if not isinstance(row, dict):
                        errors.append(f"point_reg.rows.{pid} 必须是对象")
                    else:
                        _require(row, required, f"point_reg.rows.{pid}", errors)
            except ContractError as exc:
                errors.append(str(exc))
    elif artifact_type in ("points", "match"):
        required = ("device", "summary", "points") if artifact_type == "points" else ("device", "matches")
        _require(spec, required, artifact_type, errors)
        if artifact_type == "points" and not isinstance(spec.get("points"), dict):
            errors.append("points.points 必须是对象")
        elif artifact_type == "points":
            # 解析器 artifact 使用面向来源的字段，此处只强制容器和维度存在性
            for dim in DIMS:
                if dim not in spec["points"]:
                    errors.append(f"points.points 缺少维度 {dim}")
                elif not isinstance(spec["points"][dim], list):
                    errors.append(f"points.points.{dim} 必须是数组")
        if artifact_type == "match" and not isinstance(spec.get("matches"), dict):
            errors.append("match.matches 必须是对象")
        elif artifact_type == "match":
            for key, value in spec["matches"].items():
                if not isinstance(value, dict):
                    errors.append(f"match.matches.{key} 必须是对象")
                    continue
                if value.get("dim") not in DIMS:
                    errors.append(f"match.matches.{key}.dim 非法: {value.get('dim')!r}")
                matched = bool(value.get("matched_type_id"))
                uncovered = value.get("uncovered") is True
                if matched == uncovered:
                    errors.append(f"match.matches.{key} 必须且只能声明 matched_type_id 或 uncovered=true")
    else:
        errors.append(f"未知 artifact_type: {artifact_type}")
    if errors:
        raise ContractError("\n".join(errors))
    return warnings


def atomic_save_workbook(workbook, output):
    """原子保存 openpyxl 工作簿到指定路径（先写临时文件再替换，失败不覆盖正式文件）。

    输入：
      workbook —— openpyxl.Workbook 对象
      output   —— 输出文件路径
    输出：无（文件写入磁盘）
    作用：
      通过 tempfile.mkstemp 创建临时文件，保存成功后 os.replace 原子替换目标文件；
      异常时清理临时文件，保证已有正式文件不被破坏。
    被调用：
      pipeline_v2.generate_model / generate_type / generate_point_table。
    """
    output = os.path.abspath(output)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    fd, temp_path = tempfile.mkstemp(prefix=".tmp-", suffix=".xlsx", dir=os.path.dirname(output))
    os.close(fd)
    try:
        workbook.save(temp_path)
        os.replace(temp_path, output)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def atomic_write_json(value, output):
    """原子写入 JSON 文件（先写临时文件再替换，UTF-8 编码、LF 换行）。

    输入：
      value  —— 待序列化的 Python 对象
      output —— 输出文件路径
    输出：无（文件写入磁盘）
    作用：同 atomic_save_workbook，用于写 model catalog 等 JSON 产物。
    被调用：pipeline_v2.generate_model（写 catalog）。
    """
    output = os.path.abspath(output)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    fd, temp_path = tempfile.mkstemp(prefix=".tmp-", suffix=".json", dir=os.path.dirname(output))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_path, output)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def catalog_path_for(model_xlsx):
    """根据设备模型 Excel 路径推导对应的 catalog JSON 路径。

    输入：
      model_xlsx —— 设备模型 Excel 文件路径
    输出：
      同名但后缀为 .catalog.json 的路径（如 "xxx.xlsx" -> "xxx.catalog.json"）
    作用：
      catalog 与模型 Excel 同目录同名，此函数统一推导逻辑。
    被调用：
      pipeline_v2.generate_model / generate_point_table / verify_model / verify_point。
    """
    return str(Path(model_xlsx).with_suffix(".catalog.json"))
