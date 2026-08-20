# Wiki Schema

## 领域 (Domain)

公司内部 IoT 设备的**物模型**(Thing Model / TSL)。覆盖:

- 设备与设备类型:传感器、执行器、网关、控制器等;设备大类分普通类型 (NORMAL) 与网关类型 (GATEWAY)
- 物模型四维度:属性 (Attribute)、测点 (MeasurePoint)、事件 (Event)、服务 (Service)
- 数据类型、单位、取值范围、数据点定义
- 通信协议与接入方式
- 物模型标准/规范、版本演进、历史变更

四维度定义:
- **属性 (Attribute)**:设备静态/配置信息(如 SN、安装位置、软硬件版本、额定参数),多为 STRING/INT,少数可写
- **测点 (MeasurePoint)**:设备实时测量/状态量(如温度、电压、功率、运行状态),含 R/W 方向,多为 FLOAT/ENUM/INT
- **事件 (Event)**:设备主动上报的告警/故障/信息,事件类型分 FAULT、ALARM、INFO 三类
- **服务 (Service)**:平台可下发的控制/设置指令(如分合闸、阈值设置、复位)

## 约定 (Conventions)

- 文件名:英文小写、短横线、无空格(如 `temperature-sensor.md`);中文标题写在 frontmatter 的 `title` 字段
- 每个 wiki 页面以 YAML frontmatter 开头(见下)
- 用 `[[wikilinks]]` 在页面间互链(每页至少 2 个出链)
- 更新页面时必须更新 `updated` 日期
- 每个新页面必须加入 `index.md` 对应分区(按字母序)
- 每个操作必须追加到 `log.md`
- **溯源标记:** 综合 3+ 来源的页面,在段落末尾追加 `^[raw/articles/xxx.md]`
- 物模型页面中的 TSL 片段(JSON)放入代码块,并注明来源设备型号/物模型版本
- 属性/测点/事件/服务列表优先用表格呈现(名称 | 标识符 | 数据类型 | 单位 | 说明)

## Frontmatter

```yaml
---
title: 页面标题(中文)
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [来自下方标签体系]
sources: [raw/articles/xxx.md]
# 可选质量信号:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

`confidence` 和 `contested` 在观点性强、快速变化或单一来源的主题上推荐使用。lint 会列出
`contested: true` 和 `confidence: low` 的页面供人工复核,防止弱证据悄悄固化为 wiki 事实。

### raw/ Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <正文的 sha256 摘要>
---
```

`sha256` 对 frontmatter 之后的正文字节计算,用于重摄取时检测源内容漂移。

## 标签体系 (Tag Taxonomy)

- 设备类型: `device`(设备), `sensor`(传感器), `actuator`(执行器), `gateway`(网关), `controller`(控制器)
- 物模型元素: `property`(属性), `measurepoint`(测点), `event`(事件), `service`(服务), `datatype`(数据类型)
- 通信: `protocol`(协议), `mqtt`, `modbus`, `opcua`
- 业务域: `power-distribution`(配电), `energy-storage`(储能), `charging`(充电), `photovoltaic`(光伏), `environmental-monitoring`(环境监测), `gateway-device`(网关设备)
- 元: `standard`(标准/规范), `comparison`(对比), `issue`(问题), `vendor`(供应商), `product-line`(产品线), `deprecated`(已弃用)

规则:页面上的每个标签必须来自本体系。需要新标签时,先在此处添加,再在页面上使用,防止标签泛滥。

## 页面阈值 (Page Thresholds)

- **创建页面**:设备型号/物模型在 2+ 来源出现,或是一个来源的核心对象
- **并入已有页面**:来源提到的内容已有页面覆盖时,更新原页面
- **不建页**:一句话带过的提及、次要细节、与物模型无关的内容
- **不拆分过细**:同一设备型号的属性/事件/服务归属该设备实体页;仅当某个元素本身是复杂结构
  (如 struct 数据类型、复杂的服务编排)时才单独建概念页
- **拆分页面**:超过 ~200 行时拆成子主题并互链
- **归档页面**:内容被完全取代时移入 `_archive/`,并从 index 移除

## 实体页 (Entity Pages)

每个设备型号、网关、供应商、产品线一个页面,包含:

- 设备概述:是什么、用在哪个业务场景/产线
- 物模型要点:关键属性、事件、服务(表格或 TSL 片段)
- 与其他页面的关系 `[[wikilinks]]`
- 来源引用

## 概念页 (Concept Pages)

物模型通用概念(属性/事件/服务的定义、数据类型约定、单位规范、协议)一个页面,包含:

- 定义 / 解释
- 当前状态:公司内现行标准、版本号
- 未决问题或争议
- 相关概念 `[[wikilinks]]`

## 对比页 (Comparison Pages)

同类型设备物模型对比(如 A/B 两款温度传感器)、新旧物模型版本对比、不同协议接入方案对比。包含:

- 对比什么、为什么
- 对比维度(表格优先)
- 结论 / 建议
- 来源

## 更新策略 (Update Policy)

新信息与已有内容冲突时:

1. 先看日期 —— 较新的来源一般取代较旧的
2. 真矛盾时:两个说法都记录,注明日期和来源
3. frontmatter 标记 `contradictions: [page-name]`
4. 在 lint 报告中标记供用户审阅
