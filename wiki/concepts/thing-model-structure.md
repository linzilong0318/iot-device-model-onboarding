---
title: 物模型四维度结构
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [property, measurepoint, event, service, datatype, standard]
sources: [raw/papers/public_SmokeSensor.md, raw/papers/public_MCB_1P_V1_0_2.md, raw/papers/public_ElectricMeter_1P_V1_0_2.md, raw/papers/public_MixInverter_1P_V1_0_2.md]
confidence: high
---

# 物模型四维度结构

公司物模型 (Thing Model / TSL) 由**属性 (Attribute)、测点 (MeasurePoint)、事件 (Event)、服务 (Service)** 四个维度组成。
每个设备类型文档(如 raw/papers/ 下的源文件)即一个物模型,包含 BasicInfo(基础信息)与四个维度表格。

## 四维度定义

| 维度 | 英文 | 内容 | 典型数据类型 |
| --- | --- | --- | --- |
| 属性 | Attribute | 设备静态/配置信息:SN、安装位置、软硬件版本、额定参数 | STRING、INT、ENUM |
| 测点 | MeasurePoint | 实时测量/状态量:温度、电压、功率、运行状态;含 R/W 方向 | FLOAT、ENUM、INT |
| 事件 | Event | 设备主动上报的告警/故障/信息,分 FAULT、ALARM、INFO | — |
| 服务 | Service | 平台下发的控制/设置指令:分合闸、阈值设置、复位 | — |

## 统计概览(33 个现役物模型)

- 属性总计约 250 个;测点总计 2546 个;事件 372 个;服务 188 个
- 事件类型分布:FAULT 223、ALARM 127、INFO 22
- 典型物模型结构规律:
  - **只读型**(14 个):只有属性+测点,无事件无服务(多数传感器、VFD、PWZB 等)
  - **可配置型**(15 个):属性+测点+事件+服务齐全(断路器、电表、逆变器、智能传感器)
  - 混合形态:充电桩有事件但无服务;SD 网关有服务但无事件

## 表格字段约定

各维度表格的列定义(与源文档一致):

- 属性:`*ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc`
- 测点:`*ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc`
- 事件:`*ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc`
- 服务:`*ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc`

R/W 取值:`R`(只读)、`RW`(可读写)。事件类型取值:`FAULT`(故障)、`ALARM`(告警)、`INFO`(信息)。
`*` 前缀字段为必填;DataDefine 为 JSON 结构,见 [[datatype-convention]]。

## 事件与测点的关联

事件与测点是平级的两个独立维度(均为四维度之一),事件不挂靠在某个测点之下,但通过 ID 引用与测点建立直接关联。
抽查断路器 (MCB 1P)、电表 (ElectricMeter 1P)、烟雾传感器、混合逆变器等设备文档,规律一致:

- **触发条件 (*Condition)**:测点 ID 表达式,如 `Err_OverVoltage = 1`、`Ala_Smoke = 1` —— 告警/故障标志测点
  (`Ala_*`/`Alarm*`、`Err_*`/`Error*`)置位时触发对应事件
- **输出 (*Output)**:事件上报时携带的测点快照列表,如 MCB 过压故障输出 `Err_OverVoltage,Err_Time,Err_Sta,Err_U`
  (故障标志、故障时间、故障时运行状态、故障时电压)
- **事件配套测点**:测点表中有专门为事件服务的测点,如 `Err_Time`(故障事件时间)、`Err_Sta`(故障事件时运行状态)、
  `Err_TempOnChip`(故障事件前片上温度)、`Err_U`/`Err_I`(故障事件前电压/电流)等,记录事件发生前后的设备状态
^[raw/papers/public_MCB_1P_V1_0_2.md]

注:测点表中没有指向事件的字段,关联方向为 事件 → 测点(ID 引用)。

## 命名规律

- 测点命名常用前缀表意:`Ala_*`/`Alarm*`(告警)、`Err_*`/`Error*`(故障)、`Inf_*`/`Info*`(信息)、`Sta_*`(状态)、`Sys*`(系统级)、`StrN*`(第 N 簇/组)
- 同一语义在新旧版本间有命名漂移(如烟雾浓度 SmokeDensity → SmokeConcentration),以文档名称为准

## 相关

- [[common-attributes]] — 跨设备公共属性
- [[datatype-convention]] — 数据类型与 DataDefine 结构
- [[device-category-and-domain]] — 设备大类与业务域
- [[thing-model-structure]] 为所有实体页的基础概念页
