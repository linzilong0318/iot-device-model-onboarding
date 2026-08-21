# Artifact 契约（schema 2.1）

创建或消费 `points.json`、`match.json`、`model_spec.json`、`type_spec.json`、`point_reg.json` 或模型 catalog 时阅读本文件。所有新 JSON artifact 均以下字段开头：

```json
{"schema_version": "2.1", "artifact_type": "model_spec"}
```

生成器会临时兼容未声明这些字段的旧版 spec，并打印迁移警告。显式声明未知版本或错误的 `artifact_type` 属于错误。

在交给下一阶段前，必须先校验 artifact：

```bash
python scripts/validate_artifact.py --type points points.json
python scripts/validate_artifact.py --type match match.json
```

## 点位通用规则

- ID 使用 ASCII 字母、数字和下划线，以字母开头，在同一维度内唯一。
- `Attribute`：`*ID`、`*Name_default`、`*DataType`、`*IsRequired`。
- `MeasurePoint`：`*ID`、`*Name_default`、`*DataType`、`*R/W`。
- `Event`：`*ID`、`*Name_default`、`*EventType`、`*Output`、`*Condition`。
- `Service`：`*ID`、`*Name_default`；`*Input` 和 `Output` 可为空。
- `DataDefine` 存在时为 JSON 对象或数组。`ENUM` 要求非空的 `DataDefine.enum` 对象。非法 JSON 必须报错，而非变成空值。
- 事件和服务的引用只能解析到 Attribute 和 MeasurePoint 的 ID。同 ID 的事件或服务不满足引用要求。

## points 与 match

`points` 记录来源设备、来源证据、四个维度数组、推断标记和汇总。推断事件需要证据，且在用户确认前必须标记 `need_user_confirm: true`。`match` 记录相同的设备标识、候选公有类型 ID、按维度的映射和未覆盖点位。两者都要求 `device`；新生产者还需写入通用 schema 字段。

## model_spec

要求 `raw_doc`、`model`、`select` 和 `add`。`model.id` 以 `project_` 开头，`model.device_type` 以 `public_` 开头。每个被选中的 ID 必须存在于匹配的 raw 文档对应维度中。`add` 遵循点位通用规则。

生成时还会写出 `<模型xlsx文件名>.catalog.json`。catalog 是最终模型的权威扁平化四维度视图。每个条目记录 `dimension`、`source`（`public` 或 `private`）、标准名称、模型数据类型、单位和原始字段。点表生成使用此文件，确保引用的公有点位不丢失元数据。

## type_spec

要求 `type` 和 `points`。`type.id` 以 `project_` 开头；`points` 遵循点位通用规则。

## point_reg

要求 `protocol`、`model_xlsx` 和 `rows`。`model_catalog` 为可选，默认取 `model_xlsx` 旁的 catalog。`rows` 的每个 key 是模型 MeasurePoint 的 ID。协议相关的必填字段定义见 [protocol-profiles.md](protocol-profiles.md)。
