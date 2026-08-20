---
title: 无功补偿柜
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_PFC_Panel.md]
confidence: high
---
# 无功补偿柜

## 概述

无功补偿柜 (Reactive Power Compensation Cabinet),配电域。58 个测点:补偿分组状态(Group1/Group2 等)、三相负荷与补偿侧电气量(无功/电流等);无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_PFC_Panel` |
| 中文名 | 无功补偿柜 |
| 英文名 | Reactive Power Compensation Cabinet |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_PFC_Panel.md |

## 属性 (Attribute) — 6 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 58 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Group1` | Group1 | STRING | R |  |
| `Group2` | Group2 | STRING | R |  |
| `Sa_Load` | 负载A相视在功率 | FLOAT | R | kVA |
| `Qa` | 源侧A相无功功率 | FLOAT | R | kvar |
| `Qb` | 源侧B相无功功率 | FLOAT | R | kvar |
| `Qc` | 源侧C相无功功率 | FLOAT | R | kvar |
| `Qa_Load` | 负载A相无功功率 | FLOAT | R | kvar |
| `Qb_Load` | 负载B相无功功率 | FLOAT | R | kvar |
| `Qc_Load` | 负载C相无功功率 | FLOAT | R | kvar |
| `Ia_Comp` | A相补偿电流 | FLOAT | R | A |
| `Ib_Comp` | B相补偿电流 | FLOAT | R | A |
| `Ic_Comp` | C相补偿电流 | FLOAT | R | A |
| `Temp4` | 温度4 | FLOAT | R | °C |
| `Temp5` | 温度5 | FLOAT | R | °C |
| `Temp6` | 温度6 | FLOAT | R | °C |
| `Temp2` | 温度2 | FLOAT | R | °C |
| `Sb_Load` | 负载B相视在功率 | FLOAT | R | kVA |
| `Sc_Load` | 负载C相视在功率 | FLOAT | R | kVA |
| `Pa_Load` | 负载A相有功功率 | FLOAT | R | kW |
| `Pb_Load` | 负载B相有功功率 | FLOAT | R | kW |
| `Pc_Load` | 负载C相有功功率 | FLOAT | R | kW |
| `Ua` | 源侧A相电压 | FLOAT | R | V |
| `Ub` | 源侧B相电压 | FLOAT | R | V |
| `Uc` | 源侧C相电压 | FLOAT | R | V |
| `Freq_A` | 源侧A相频率 | FLOAT | R | Hz |
| `Freq_B` | 源侧B相频率 | FLOAT | R | Hz |
| `Freq_C` | 源侧C相频率 | FLOAT | R | Hz |
| `THDUa` | 源侧A相THDU | FLOAT | R | % |
| `THDUb` | 源侧B相THDU | FLOAT | R | % |
| `THDUc` | 源侧C相THDU | FLOAT | R | % |
| `Pb` | 源侧B相有功功率 | FLOAT | R | kW |
| `Ia_Load` | 负载A相电流 | FLOAT | R | A |
| `Ib_Load` | 负载B相电流 | FLOAT | R | A |
| `Ic_Load` | 负载C相电流 | FLOAT | R | A |
| `THDIa_Load` | 负载A相THDI | FLOAT | R | % |
| `THDIb_Load` | 负载B相THDI | FLOAT | R | % |
| `THDIc_Load` | 负载C相THDI | FLOAT | R | % |
| `PFa_Load` | 负载A相功率因数 | FLOAT | R |  |
| `PFb_Load` | 负载B相功率因数 | FLOAT | R |  |
| `PFc_Load` | 负载C相功率因数 | FLOAT | R |  |
| `Sa` | 源侧A相视在功率 | FLOAT | R | kVA |
| `Sb` | 源侧B相视在功率 | FLOAT | R | kVA |
| `Sc` | 源侧C相视在功率 | FLOAT | R | kVA |
| `Pa` | 源侧A相有功功率 | FLOAT | R | kW |
| `Temp3` | 温度3 | FLOAT | R | °C |
| `Pc` | 源侧C相有功功率 | FLOAT | R | kW |
| `In` | 源侧N线电流 | FLOAT | R | A |
| `In_Load` | 负载N线电流 | FLOAT | R | A |
| `Ia` | 源侧A相电流 | FLOAT | R | A |
| `Ib` | 源侧B相电流 | FLOAT | R | A |
| `Ic` | 源侧C相电流 | FLOAT | R | A |
| `THDIa` | 源侧A相THDI | FLOAT | R | % |
| `THDIb` | 源侧B相THDI | FLOAT | R | % |
| `THDIc` | 源侧C相THDI | FLOAT | R | % |
| `PFa` | 源侧A相功率因数 | FLOAT | R |  |
| `PFb` | 源侧B相功率因数 | FLOAT | R |  |
| `PFc` | 源侧C相功率因数 | FLOAT | R |  |
| `Temp1` | 温度1 | FLOAT | R | °C |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[electric-meter-3p]]
- [[pwzb]]
- [[thing-model-structure]]
