#!/usr/bin/env python3
"""校验 schema 2.1 流水线 JSON artifact。

本脚本是独立的 artifact 校验入口，用于在生成 Excel 之前验证 spec JSON
是否符合 schema 2.1 契约。与 pipeline_v2 内嵌的校验不同，本脚本以
allow_legacy=False 严格模式校验（不兼容未声明 schema_version 的旧版 artifact）。

支持的 artifact 类型：
  --type points      说明书提取结果（points.json）
  --type match       公有类型匹配结果（match.json）
  --type model_spec  设备模型配置（分支 A 输入）
  --type type_spec   设备类型配置（分支 B 输入）
  --type point_reg   协议点表配置（分支 A2 输入）

用法：
  python validate_artifact.py --type <类型> <artifact.json>

输出：JSON 格式校验报告
  - 通过：{"passed": true, "warnings": [...]}
  - 失败：{"passed": false, "errors": [...]}
退出码：0=通过 1=失败
"""
import argparse
import json
import sys

from artifact_contract import ContractError, validate_artifact


def main():
    """命令行入口：读取 artifact JSON，调用 validate_artifact 校验，输出报告。

    流程：
      1. argparse 解析 --type 和 json_file 参数
      2. 读取 JSON 文件
      3. validate_artifact 以 allow_legacy=False 严格校验
      4. 输出 JSON 报告，返回退出码（0=通过 1=失败）

    异常处理：
      捕获 OSError（文件不存在）、JSONDecodeError（JSON 格式错误）、
      ContractError（契约校验失败），统一转为 {"passed": false, "errors": [...]} 报告。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True,
                        choices=("points", "match", "model_spec", "type_spec", "point_reg"))
    parser.add_argument("json_file")
    args = parser.parse_args()
    try:
        with open(args.json_file, encoding="utf-8") as handle:
            value = json.load(handle)
        warnings = validate_artifact(value, args.type, allow_legacy=False)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(json.dumps({"passed": False, "errors": str(exc).splitlines()}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"passed": True, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
