# 多 Agent 编排方案（可选工作流）

> 本文件描述把「设备接入物模型」流程落地为「主 agent + 子 agent」的编排。
> 它是默认路径：主 agent 按本方案编排，解析/匹配/构造交给子 agent（理由见
> SKILL.md「默认多 agent 编排」——接入模型长上下文弱，需上下文隔离）。
> 仅当说明书极小且用户明确要求全程单 agent 盯细节时才退回单 agent。
> 前提：已启用会话工作目录约定（见 SKILL.md「产物目录约定」），
> 子 agent 之间靠磁盘 artifact 通信，主 agent 不搬运全量中间数据。

## 0. 为什么这样设计

- 中间产物多（points/match/各 spec/catalog/Excel），且每个都是「读上一个 artifact、
  产出下一个 artifact」的独立推理任务 → 天然适合隔离成独立子 agent。
- 子 agent 的产出都有客观校验闸门（`validate_artifact.py` / `verify_output.py`），
  主 agent 不必信子 agent 自报，重跑校验/抽查产物即可核验事实。
- 每种子 agent 只持有本步所需上下文，主 agent 与子 agent 的上下文都被大幅瘦身，
  避免大份 points/match 全文、多页 wiki 阅读、生成-校验迭代日志灌进主 agent。

## 1. 角色

| 角色 | 职责 | 能否提问 |
| --- | --- | --- |
| M 主 agent | 编排、用户确认、最终决策、交付、复核子 agent 产物 | 能 |
| S1 解析子 agent | 说明书 → `points.json` | 否 |
| S2a/S2b/S2c 匹配子 agent (x3) | `points.json`+wiki → 各维映射片段 | 否 |
| S3 构造子 agent | 决策 + `match.json` → spec 并生成+校验自迭代 | 否 |

所有子 agent 都是 leaf（`delegate_task` 当前为单层，编排者会被强制降级为 leaf），
即"主 agent 起一层子 agent"，正好够用。

## 2. 数据流（含产物路径）

```
说明书文件
   │ ① M: execute_code 跑 extract_input.py（机械，不派 agent）
   ▼
<ws>/extract_output.json                  ← 会话工作目录 <ws>
   │ ② 派 S1（context：extract 路径、SCHEMA 摘要、四维规则、pitfalls）
   ▼
<ws>/points.json
   │ ③ 派 S2a/S2b/S2c（并行3个，各认领一维；context：points.json路径 + wiki候选）
   ▼ ┌──────────┬──────────┬────────────┐
 Attribute段   MeasurePoint段  Event+Service段     ← 3个 <ws>/match.*.segment.json
   │ ④ M: execute_code 合并 → match.json（机械合并）
   ▼
<ws>/match.json
   │ ⑤ M: 向用户 present 覆盖/未覆盖/推断 → 用户选分支 + 确认协议/推断事件
   ▼   （用户交互只有主 agent 能做）
决策（仅存于 M 上下文，不入盘）
   │ ⑥ 派 S3-model / S3-point / S3-type（可并行；context：match.json路径+决策+pitfalls）
   ▼
<ws>/<model_id>.xlsx + <model_id>.catalog.json / <model_id>_<协议>.xlsx / <type_id>.xlsx
   │ ⑦ M: 复核（execute_code 重跑 verify_output.py fail-fast + 抽查 catalog）
   ▼
通过 → 交付 + 追加 wiki/log.md
```

`<ws>` = `/opt/data/workspace/<sessionId>/`（用 `scripts/workspace.py` 解析）。

## 3. 每个子 agent 的契约

统一模板：子 agent 的 `context` 必须自包含（它不知道主 agent 已读过什么），
至少包含：任务目标、明确的输入文件绝对路径、输出的绝对路径、产出 schema 约束、
以及所需规则/候选。产物一律写盘，只把一份紧凑摘要返回主 agent。

### S1 解析子 agent
- 输入(context)：`extract_output.json` 绝对路径、`wiki/SCHEMA.md` 与四维度提取规则摘要、pitfalls 相关条目
- 产出(写盘)：`<ws>/points.json`（schema 2.1，四维度完整点位，含 `inferred` / `need_user_confirm`）
- 只还 M：设备名、各维度点数、推断项清单、来源证据简表
- 校验：主 agent 跑 `validate_artifact.py --type points` 验 schema

### S2 匹配子 agent ×3（并行，各认领一维）
- 分片：Attribute / MeasurePoint / Event+Service（受 `max_concurrent_children=3` 约束）
- 输入(context)：`<ws>/points.json` 中对应维度、`wiki/index.md` 候选公有类型 ID 清单、
  对应实体页 + 测点子页全文（子 agent 内自行读）
- 产出(写盘)：`<ws>/match.Attribute.segment.json`（同理 MeasurePoint / EventService），
  该维每个用户点位 → `matched_type_id` 或 `uncovered`
  **关键：每个 `matched_type_id` 映射条目必须同时写明 `matched_point`（命中的具体公有点位标识符，取自公有类型原始定义、不臆造）**。只记类型不记具体点位，merge 后会出现大量缺 `matched_point` 条目，需另派补齐子 agent，属返工，应避免。
- 只还 M：推荐公有类型 ID、覆盖数/未覆盖数、争议项
- 校验：主 agent 读三段 JSON 做结构抽查后 execute_code 合并

### S3 构造子 agent（按分支实例化 S3-model / S3-point / S3-type）
- 输入(context)：`<ws>/match.json` 全量、用户已确认决策（分支/协议/推断事件取舍）、
  `reference/pitfalls.md` 关键条目、`reference/artifact-schemas.md` 摘要
- 职责：写 `<ws>/<名>_spec.json` → 跑对应 `gen_*.py` → 跑 `verify_output.py` →
  有错自动修 → 直到 `passed:true`（把生成-校验-改-重验的迭代噪音关在里面）
- 产出(写盘)：spec.json + 最终 Excel（+ catalog）
- 只还 M：行数、推荐类型、未覆盖、取舍决定、最终校验 passed 报告
- 校验：主 agent 必须亲自重跑 `verify_output.py --kind ...` 确认

## 4. 并行度与依赖

- 必须串行：S1 → 合并 → S2 三片 → 合并 → 用户确认 → S3 → 主 agent 复核
- 可并行窗口（每窗口 ≤3）：
  - S2a/S2b/S2c 三片并行
  - 多本说明书时 S1 按本并行
  - 用户同时要模型+点表时：S3-model 与 S3-point 可并行（point 依赖 model 的
    catalog，但 model 先完成即可，不阻塞各自生成）

## 5. 主 agent 的信任与复核策略

`delegate_task` 铁律：子 agent 自报 ≠ 事实。本方案用「客观闸门 + 主 agent 抽查」对冲：
1. 每个子 agent 写盘后，主 agent 先跑 `validate_artifact.py` 验 schema（便宜、快）；
2. S3 交付 Excel 后，主 agent 必须亲自重跑 `verify_output.py --kind ...` 确认 `passed`；
3. 主 agent 读 catalog/产物关键字段做抽样比对（model_id 前缀、FromDeviceType 互斥），
   不看子 agent 的漂亮话。
这样"孩子做了啥"由文件 + 校验脚本说了算，主 agent 只做最终裁决。

## 6. 哪些地方【不】派 agent

- `extract_input.py` / 合并片段 / 跑 verify —— 机械单次调用 → `execute_code`
- 用户确认（第 3 步）—— 子 agent 无权提问，只有主 agent 能
- 最终校验闸门 —— 主 agent 亲自跑（信任边界）
- 任何只需 1 次工具调用的步骤 —— 不派 agent

## 7. 局限与风险

- 子 agent 继承主模型，无法独立换更强模型；"质量提升"来自上下文隔离 + 单一职责，
  而非更强模型。
- 深度被压平（单层）：S3 无法再往下拆子 agent，当前 2 层已够。
- 并发上限 `delegation.max_concurrent_children`（默认 3）：并行窗口 ≤3，
  想并行更多需调 config。
- 上下文隔离是双刃剑：子 agent 看不到主 agent 历史，必要上下文必须显式塞进
  `context` 字段；要维护稳定的 artifact 路径约定来减少重复传递。

## 8. 何时启用 / 何时不用

默认启用（多 agent 是主路径）：
- 说明书大、点位多（points.json / 匹配分析很长，会灌爆主上下文）；
- 需要并行匹配多个维度或多本说明书；
- 生成-校验迭代日志多，想关在子 agent 里；
- 主模型长上下文理解弱 —— 默认应启用，靠上下文隔离瘦身主 agent。

退回单 agent 串行（需用户明确要求）：
- 说明书极小、点位极少，主线上下文完全无压力；
- 用户需要全程盯每一步的分析细节（子 agent 只回摘要，细粒度被折叠）。

## 9. 落地清单（启用时逐条核对）

- [ ] 产物目录已按 `scripts/workspace.py --mkdir` 建好，所有路径都用它解析
- [ ] S1/S2/S3 的 context 字段全部自包含（目标+输入路径+输出路径+schema+规则）
- [ ] 每个子 agent 的产物都写了 schema_version/artifact_type
- [ ] 用户确认发生在主 agent（S2 之后，S3 之前），未确认不派 S3
- [ ] 主 agent 亲自重跑 `verify_output.py` 确认 `passed:true` 后才交付
- [ ] 只有交付成功后主 agent 追加 `wiki/log.md`
