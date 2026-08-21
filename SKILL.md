---
name: iot-device-model-onboarding
description: Use when 用户提供物联网设备说明书(PDF/DOC/DOCX/XLS/XLSX)，需要匹配泰无界平台物模型设备类型，并交互式生成私有设备模型、设备类型或协议点表。
version: 2.4.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [iot, thing-model, tsl, device, excel, wiki]
    category: iot
    related_skills: [llm-wiki, xlsx, pdf, docx, ocr-and-documents]
---

# 设备接入物模型辅助工作流（泰无界平台）

## 目标与边界

把设备说明书整理为四维度点位，匹配 `wiki/` 中的公有设备类型，经用户确认后生成平台可导入的私有设备模型、私有设备类型，以及可选的协议点表。

层级关系：设备类型（抽象点位全集）→ 设备模型（从类型选择点位并补充私有点位）→ 点表（模型测点的取数定义）。点表只包含 `MeasurePoint`；Attribute、Event、Service 不进入点表。

ID 约束：知识库公有类型使用 `public_`；所有生成物使用 `project_`。私有产物不得回灌公有知识库。

本技能不用于单纯知识库问答、单纯文档转换或与物模型无关的 Excel 制作。

## 资源路由

- 开始检索知识库时读 `wiki/SCHEMA.md`、`wiki/index.md` 和 `wiki/log.md` 末尾 30 行。
- 创建或消费 JSON artifact 时读 [reference/artifact-schemas.md](reference/artifact-schemas.md)。
- 构造 `point_reg.json`、选择点表模板或诊断点表时读 [reference/protocol-profiles.md](reference/protocol-profiles.md)。
- 解析寄存器描述串/寄存器点表到 points.json、构造 `point_reg.json` 的寄存器字符串解析、Modbus 区间→四维度映射、点表不足/未覆盖处理时读 [reference/pitfalls.md](reference/pitfalls.md) §八。
- 遇到历史平台导入、字段来源或事件建模问题时读 [reference/pitfalls.md](reference/pitfalls.md)。
- 编排默认走「主 agent + 子 agent」多 agent 流程（原因见「默认多 agent 编排」）；具体角色分工、数据流、子 agent 契约与复核策略读 [reference/multi-agent-design.md](reference/multi-agent-design.md)。

## 产物目录约定

本次会话的所有中间产物（`points.json`、`match.json`、各 `*_spec.json` 及临时文件）与最终 Excel 统一落盘到会话工作目录：

```
/opt/data/workspace/<sessionId>/
```

- `sessionId` 取自环境变量 `HERMES_SESSION_ID`；未设置时回退为 `default`。工作目录根可用 `HERMES_WORKSPACE_ROOT` 覆盖。
- 解析工作目录统一走 `scripts/workspace.py`（主 agent 与子 agent 都从这里取路径），不要各自臆造目录：
  ```bash
  python scripts/workspace.py --mkdir        # 打印并创建会话工作目录
  python scripts/workspace.py                # 仅打印路径（不创建）
  ```
- 生成器默认即落到该目录（`gen_device_model/gen_device_type/gen_point_table/extract_input` 在未给输出路径时自动解析），文件名按规范派生；显式的 CLI 输出路径或 `spec.output` 优先于目录约定。
- 多个同会话产物按上述默认命名共存，互不覆盖：模型 `<model_id>.xlsx`（连同 `<model_id>.catalog.json`）、类型 `<type_id>.xlsx`、点表 `<模型名>_<协议>.xlsx`、原始抽取 `extract_output.json`。
- 知识库 `wiki/` 仍只读，绝不写入产物。

## 任务进度与用户反馈（Feishu）

本技能步骤多、耗时长，用户经 Feishu 使用时常希望看到进度而不仅是最终结果。用户看到的反馈走 `interim_assistant_messages`（自然语言中间消息）承载，它独立于 `tool_progress`——即使 Feishu 上用 `tool_progress: off` 隐藏了工具调用，中间进度消息仍正常发给用户，界面干净又不失进度感。

- 反馈通道：用中间助手消息（interim assistant messages）播报进度，不用 `tool_progress`，也不通过 `todo` 向用户暴露工具调用。
- 里程碑粒度：在【解析 → 匹配 → 用户确认 → 构造/生成 → 校验 → 交付】每个里程碑完成后，发一条简洁中间消息，如「① 说明书已解析出 N 个测点」「④ 已生成模型 project_xxx，共四维 Y 个点位」。切勿长时间静默。
- 简洁纯文本：Feishu 消息尽量纯文本/极简格式，一条一个要点。
- 粒度控制：里程碑级一条，勿微步刷屏。
- 多 agent 模式的转发：子 agent 的进度由主 agent 汇总为一条简洁中间消息转发给用户，不因多 agent 而拆成多段杂乱播报。
- `todo` 仅作内部计划辅助（不影响用户界面）：条目写清「id + 一句话任务」，便于上下文压缩后恢复方向；它不再作为用户可见的反馈通道。

## 默认多 agent 编排

本流程默认以「主 agent + 子 agent」多 agent 模式执行：主 agent 负责编排、用户确认、最终裁决与交付；
解析(S1)、匹配(S2 ×3 并行)、构造生成(S3)交给子 agent，靠磁盘 artifact 通信。

原因：接入模型对长上下文理解能力弱，多 agent 把大份 points/多页 wiki 阅读/生成-校验迭代都关进子
agent，主 agent 只保留紧凑摘要与最终决策，上下文大幅瘦身、单一职责更稳。

默认采用，除非：说明书极小且用户明确要求全程单 agent 盯分析细节，才退回单 agent。
子 agent 契约、数据流、复核策略见 [reference/multi-agent-design.md](reference/multi-agent-design.md)。

## 工作流

### 1. 解析说明书

支持 `.pdf`、`.doc`、`.docx`、`.xls`、`.xlsx`。优先使用当前环境中已有的文档能力；也可运行：

```bash
python scripts/extract_input.py <说明书路径>
# 产物默认写到会话工作目录 extract_output.json；可用 --output <路径> 覆盖
```

格式约束：

- `.docx` 用 `python-docx`；`.xlsx` 用 `openpyxl`。
- `.xls` 用 `xlrd>=2.0.1`，不能用 `openpyxl` 读取。
- `.doc` 需要 `antiword`、`catdoc` 或 LibreOffice。系统均未安装时明确告知依赖并停止该文件解析；不能宣称 `python-docx` 支持 `.doc`。
- PDF 扫描页需要 OCR；表格优先按表格结构提取。
- Excel 先识别寄存器点表、物模型点位清单或混合形态，再遍历所有 sheet 合并。

输出 `points.json`，包含设备信息、来源证据、Attribute / MeasurePoint / Event / Service 四个数组和汇总。事实与推断分离；推断项标记 `inferred: true`。推断事件还必须保留证据并标记 `need_user_confirm: true`。

提取时主动检查：

- Attribute：技术参数、规格和静态配置。
- MeasurePoint：通讯点表、数据点表和实时状态。
- Event：明确的告警、故障或状态标志；累计次数不能自动推导为实时事件。
- Service：远程控制、复位、清零、阈值设置和参数下发。

### 2. 匹配公有设备类型

从 `wiki/index.md` 的 Entities 选择 2 至 5 个候选，读取候选实体页；实体页指向 `*-measure-points.md` 时必须继续读取完整测点子页。按名称语义、单位、数据类型和枚举交叉验证，不要求用户标识符与公有类型标识符相同。

输出 `match.json`：记录候选、推荐类型、四维度映射、未覆盖点和待确认项。每个用户点位必须有维度明确的 `matched_type_id` 或 `uncovered` 结论，不用单一百分比替代覆盖明细。

引用公有点位时，Excel 字段全部取自 `wiki/raw/papers/<源文档>.md`；用户说明书只决定选哪些点和协议取数信息。不得把说明书中的临时名称、类型或单位覆盖公有标准定义。

### 3. 用户确认

分析完成后先汇报：设备信息、推荐类型、四维度覆盖/未覆盖清单、推断和争议项。未经用户明确选择，不生成 Excel。

一次询问只要求用户选择：

1. 基于推荐公有类型生成私有设备模型；可同时选择协议生成点表。
2. 不使用现有公有类型，生成私有设备类型。
3. 仅保留分析结论。

生成点表前必须确认协议。推断事件必须逐项获得用户确认，未确认项不得进入 spec。

### 4. 构造 artifact 并生成

所有新 JSON artifact 使用 `schema_version: "2.1"` 和正确的 `artifact_type`。详细字段见 artifact schema 参考。

分支 A，设备模型：

```bash
python scripts/gen_device_model.py <model_spec.json> [输出路径]
python scripts/verify_output.py --kind model --xlsx <模型.xlsx>
```

生成器同时写出 `<模型文件名>.catalog.json`。FromDeviceType 只列公有类型引用；四张子表只写私有新增点位，两者互斥。缺失的 selected ID、重复 ID、非法 DataDefine、无效事件引用均须失败。

新增点位三条平台铁律（生成器已内置校验）：①类型里已存在 ID 的点位**不得在子表自定义同名点位**，方向/字段与类型不符时从类型引用并用私有 Service 补下发能力；② `*DataType` 为 INT/FLOAT 的数值型新增点位**必须带 DataDefine**（含 minValue/maxValue，范围未知填 `{"minValue":"","maxValue":""}`）；③ `*DataType` 为 ENUM 的新增点位，其 DataDefine 必须用平台格式 `{"mappingItemList":[...],"enumKeyCode":"INT"}`（旧式 `{"enum":{...}}` 生成时自动转换，交付物一定是 mappingItemList 格式）。

分支 A2，协议点表：

```bash
python scripts/gen_point_table.py <point_reg.json> [输出路径]
python scripts/verify_output.py --kind point --xlsx <点表.xlsx> --model <模型.xlsx> --protocol <协议名>
```

点表从 model catalog 获取引用点位和新增点位的标准名称、单位、模型数据类型。每个协议按 profile 判断定位字段；不能假设所有协议都有 `address`。说明书缺少该协议定位信息的测点不生成行，并在总结中列出。

分支 B，私有设备类型：

```bash
python scripts/gen_device_type.py <type_spec.json> [输出路径]
python scripts/verify_output.py --kind type --xlsx <类型.xlsx>
```

生成器按目标模板表头映射字段，不依赖固定列号。所有生成器先完成契约校验，并通过临时文件原子替换输出；失败时不得覆盖已有正式文件。

### 5. 交付

只有校验报告 `passed: true` 的 Excel 才能交付。总结直接回复用户，不另写分析报告 md，至少包含：

- 生成路径、私有 ID、所用模板与四维度数量。
- 推荐类型与未覆盖能力。
- 推断项和用户确认结果。
- 点表协议、行数、未生成测点、dataType 推断与地址进制转换。

生成成功后按既有格式追加 `wiki/log.md`；私有类型/模型不登记 `wiki/index.md`。发现公有知识库错误时只提出建议，未经授权不修改 `wiki/`。

## 最终检查

- [ ] 所有中间产物与最终 Excel 已落盘到 `scripts/workspace.py --mkdir` 解析出的会话工作目录（`/opt/data/workspace/<sessionId>/`）。
- [ ] `points.json` 与 `match.json` 使用 2.1 schema，四维度和证据完整。
- [ ] 候选实体页及其完整测点子页已读取，所有映射维度明确。
- [ ] 用户已确认生成分支；点表协议和推断事件已确认。
- [ ] 公有引用字段来自 raw 标准定义，生成物 ID 为 `project_`。
- [ ] FromDeviceType 与新增子表互斥，事件/服务引用只指向 Attribute 或 MeasurePoint。
- [ ] 新增点位无同名冲突：子表 Attribute/MeasurePoint 的 ID 不能存在于设备类型对应维度（平台铁律）。
- [ ] 数值型新增点位（INT/FLOAT）均带 DataDefine（含 minValue/maxValue；范围未知填空对象）。
- [ ] ENUM 新增点位 DataDefine 为平台格式（mappingItemList + enumKeyCode），非旧式 {"enum":{...}}。
- [ ] model catalog 与模型四维度一致，点表名称、标识符、单位与 catalog 一致。
- [ ] 协议必填字段、Modbus 宽度/功能码/地址重叠/mask/map 已校验。
- [ ] 每个 Excel 重新打开并通过 `verify_output.py`；失败产物未覆盖正式输出。
- [ ] 结论已回复用户；仅在成功交付后追加日志，未修改公有知识库索引。
