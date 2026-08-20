---
title: 马达保护器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_MotorProtector.md]
confidence: high
---
# 马达保护器

## 概述

马达保护器,公共域。属性最全的一类(14 个):额定电压/电流(含高速档)/频率/功率(含高速档)、电机类型、接线方式、CT 变比、保护选择等;40 个测点为三相电气量(电压/电流/功率/功率因数/不平衡度等),用于电机运行监测与保护。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_MotorProtector` |
| 中文名 | 马达保护器 |
| 英文名 | Motor Protector |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_MotorProtector.md |

## 属性 (Attribute) — 14 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |
| `RatedVoltage` | 额定电压 | FLOAT | V | False |
| `RatedCurrent` | 额定电流 | FLOAT | A | False |
| `RatedCurrentType` | 额定电流规格 | FLOAT |  | False |
| `RatedCurrentHigh` | 额定电流（高速） | FLOAT | A | False |
| `RatedFrequency` | 额定频率 | FLOAT | Hz | False |
| `RatedPower` | 额定功率 | FLOAT | kW | False |
| `RatedPowerHigh` | 额定功率（高速） | FLOAT | kW | False |
| `MotorType` | 电机类型 | STRING |  | False |
| `Connection` | 接线方式 | STRING |  | False |
| `CtScale` | CT变比 | STRING |  | False |
| `ProtectSelect` | 保护选择 | STRING |  | False |

## 测点 (MeasurePoint) — 40 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pc` | C相有功功率 | FLOAT | R | W |
| `PFb` | B相功率因数 | FLOAT | R |  |
| `Qa` | A相无功功率 | FLOAT | R | var |
| `Qb` | B相无功功率 | FLOAT | R | var |
| `Qc` | C相无功功率 | FLOAT | R | var |
| `Sa` | A相视在功率 | FLOAT | R | VA |
| `Sb` | B相视在功率 | FLOAT | R | VA |
| `Sc` | C相视在功率 | FLOAT | R | VA |
| `PFa` | A相功率因数 | FLOAT | R |  |
| `PFc` | C相功率因数 | FLOAT | R |  |
| `Pa` | A相有功功率 | FLOAT | R | W |
| `PhaseAngleA` | A相相位角 | FLOAT | R | ° |
| `PhaseAngleB` | B相相位角 | FLOAT | R | ° |
| `PhaseAngleC` | C相相位角 | FLOAT | R | ° |
| `FundamentalVa` | A相电压基波值 | FLOAT | R | V |
| `FundamentalVb` | B相电压基波值 | FLOAT | R | V |
| `FundamentalVc` | C相电压基波值 | FLOAT | R | V |
| `FundamentalIa` | A相电流基波值 | FLOAT | R | V |
| `FundamentalIb` | B相电流基波值 | FLOAT | R | V |
| `FundamentalIc` | C相电流基波值 | FLOAT | R | V |
| `LeakCurrent` | 漏电流 | FLOAT | R | A |
| `Uca` | CA线电压 | FLOAT | R | V |
| `Ua` | A相电压 | FLOAT | R | V |
| `Ub` | B相电压 | FLOAT | R | V |
| `Uc` | C相电压 | FLOAT | R | V |
| `Un` | 中性点对地电压 | FLOAT | R | V |
| `Ia` | A相电流 | FLOAT | R | A |
| `Ib` | B相电流 | FLOAT | R | A |
| `Ic` | C相电流 | FLOAT | R | A |
| `Uab` | AB线电压 | FLOAT | R | V |
| `Ubc` | BC线电压 | FLOAT | R | V |
| `GroundCurrent` | 接地电流 | FLOAT | R | A |
| `Temp` | 温度 | FLOAT | R | °C |
| `EP` | 总有功电能 | FLOAT | R | kWh |
| `EPI_PhaseA` | A相正向有功电能 | FLOAT | R | kWh |
| `EPI_PhaseB` | B相正向有功电能 | FLOAT | R | kWh |
| `EPI_PhaseC` | C相正向有功电能 | FLOAT | R | kWh |
| `EQI_PhaseA` | A相正向无功电能 | FLOAT | R | kvarh |
| `EQI_PhaseB` | B相正向无功电能 | FLOAT | R | kvarh |
| `EQI_PhaseC` | C相正向无功电能 | FLOAT | R | kvarh |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[low-voltage-smart-connector]]
- [[vfd]]
- [[pwzb]]
- [[thing-model-structure]]
