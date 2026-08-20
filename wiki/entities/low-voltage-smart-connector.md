---
title: 低压智能接插件
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_LowVoltageSmartConnector.md]
confidence: high
---
# 低压智能接插件

## 概述

低压智能接插件,配电域。属性含额定电压/电流/频率与最大电流;49 个测点为三相电气量(电压/电流/功率/电能/功率因数/漏电流与故障标志等);1 个事件 ErrorRecord(故障记录);无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_LowVoltageSmartConnector` |
| 中文名 | 低压智能接插件 |
| 英文名 | Low Voltage Smart Connector |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_LowVoltageSmartConnector.md |

## 属性 (Attribute) — 7 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |
| `RatedVoltage` | 额定电压 | FLOAT | V | False |
| `RatedCurrent` | 额定电流 | FLOAT | V | False |
| `RatedFrequency` | 额定频率 | FLOAT | Hz | False |
| `MaxCurrent` | 最大电流 | FLOAT | A | False |

## 测点 (MeasurePoint) — 49 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ErrorFlag` | 故障事件标志 | ENUM | R |  |
| `PowerFactorC` | C相功率因数 | FLOAT | R |  |
| `PowerFactorB` | B相功率因数 | FLOAT | R |  |
| `PowerFactorAll` | 总功率因数 | FLOAT | R |  |
| `PowerFactorA` | A相功率因数 | FLOAT | R |  |
| `Ic` | C相电流 | FLOAT | R | A |
| `ActivePowerAll` | 总有功功率 | FLOAT | R | W |
| `ActivePowerB` | B相有功功率 | FLOAT | R | W |
| `ActivePowerC` | C相有功功率 | FLOAT | R | W |
| `ApparentEnergyAll` | 总视在电能 | FLOAT | R | VAh |
| `ApparentPowerA` | A相视在功率 | FLOAT | R | VA |
| `ApparentPowerAll` | 总视在功率 | FLOAT | R | VA |
| `ApparentPowerB` | B相视在功率 | FLOAT | R | VA |
| `ApparentPowerC` | C相视在功率 | FLOAT | R | VA |
| `Ia` | A相电流 | FLOAT | R | A |
| `Ib` | B相电流 | FLOAT | R | A |
| `ErrorDataD` | 故障数据D | FLOAT | R |  |
| `ActivePowerA` | A相有功功率 | FLOAT | R | W |
| `ReactivePowerA` | A相无功功率 | FLOAT | R | var |
| `ReactivePowerAll` | 总无功功率 | FLOAT | R | var |
| `ReactivePowerB` | B相无功功率 | FLOAT | R | var |
| `ReactivePowerC` | C相无功功率 | FLOAT | R | var |
| `Ua` | A相电压 | FLOAT | R | V |
| `Ub` | B相电压 | FLOAT | R | V |
| `Uc` | C相电压 | FLOAT | R | V |
| `Uba` | BA线电压 | FLOAT | R | V |
| `TempInB` | B相进线端子温度 | FLOAT | R | °C |
| `ReactiveEnergyAll` | 无功总电能 | FLOAT | R | kvarh |
| `TempInC` | C相进线端子温度 | FLOAT | R | °C |
| `Uac` | AC线电压 | FLOAT | R | V |
| `ActiveEnergyAll` | 有功总电能 | FLOAT | R | kWh |
| `PosActiveEnergy` | 正向有功电能 | FLOAT | R | kWh |
| `NegActiveEnergy` | 反向有功电能 | FLOAT | R | kWh |
| `Frequency` | 电网频率 | FLOAT | R | Hz |
| `VoltageUnbalanceRate` | 电压不平衡率 | FLOAT | R |  |
| `CurrentUnbalanceRate` | 电流不平衡率 | FLOAT | R |  |
| `TempInA` | A相进线端子温度 | FLOAT | R | °C |
| `TempOutA` | A相出线端子温度 | FLOAT | R | °C |
| `ApparentPowerDemandAll` | 视在总需量 | FLOAT | R | kVA |
| `TempOutB` | B相出线端子温度 | FLOAT | R | °C |
| `Ucb` | CB线电压 | FLOAT | R | V |
| `TempOutC` | C相出线端子温度 | FLOAT | R | °C |
| `PosActivePowerDemandAll` | 正向有功总需量 | FLOAT | R | kW |
| `NegActivePowerDemandAll` | 反向有功总需量 | FLOAT | R | kW |
| `ErrorCode` | 故障代码 | INT | R |  |
| `ErrorTime` | 故障时间 | DATETIME | R |  |
| `ErrorDataA` | 故障数据A | FLOAT | R |  |
| `ErrorDataB` | 故障数据B | FLOAT | R |  |
| `ErrorDataC` | 故障数据C | FLOAT | R |  |

## 事件 (Event) — 1 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorRecord` | 故障事件 | ALARM |

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[motor-protector]]
- [[mccb-3p]]
- [[thing-model-structure]]
