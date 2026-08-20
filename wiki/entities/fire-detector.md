---
title: 火灾探测器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, power-distribution]
sources: [raw/papers/public_FireDetector.md]
confidence: high
---
# 火灾探测器

## 概述

火灾探测器,配电域。属性仅 SN/设备型号/安装位置;45 个测点全部为三相电气参量(相电压/电流、功率因数、正反向有功/无功/视在电能、频率、电压/电流不平衡度、序分量、谐波等),与一般"火灾探测"语义不同——经确认文档无误,该物模型确含大量电参量测点。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_FireDetector` |
| 中文名 | 火灾探测器 |
| 英文名 | FireDetector |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_FireDetector.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `EquipmentType` | 设备型号 | STRING |  | False |
| `SN` | 设备SN | STRING |  | False |

## 测点 (MeasurePoint) — 45 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PowerFactorC` | C相功率因数 | FLOAT | R |  |
| `PowerFactorB` | B相功率因数 | FLOAT | R |  |
| `PowerFactorAll` | 总功率因数 | FLOAT | R |  |
| `PowerFactorA` | A相功率因数 | FLOAT | R |  |
| `UxZsUnbalFactor` | 电压零序不平衡度 | FLOAT | R |  |
| `ApparentEnergyAll` | 总视在电能 | FLOAT | R | VAh |
| `Frequency` | 电网频率 | FLOAT | R | Hz |
| `CurrentUnbalanceRate` | 电流不平衡率 | FLOAT | R |  |
| `PosActiveEnergy` | 正向有功电能 | FLOAT | R | kWh |
| `NegActiveEnergy` | 反向有功电能 | FLOAT | R | kWh |
| `PosReactiveEnergyAll` | 正向无功总电能 | FLOAT | R | kvarh |
| `NegReactiveEnergyAll` | 反向无功总电能 | FLOAT | R | kvarh |
| `PosActivePowerDemandAll` | 正向有功总需量 | FLOAT | R | kW |
| `NegActivePowerDemandAll` | 反向有功总需量 | FLOAT | R | kW |
| `StateFire4` | 状态信号4 | BITMAP | R |  |
| `Ia` | A相电流 | FLOAT | R | A |
| `Ib` | B相电流 | FLOAT | R | A |
| `Ic` | C相电流 | FLOAT | R | A |
| `Ua` | A相电压 | FLOAT | R | V |
| `Ub` | B相电压 | FLOAT | R | V |
| `Uc` | C相电压 | FLOAT | R | V |
| `Uac` | AC线电压 | FLOAT | R | V |
| `Uba` | BA线电压 | FLOAT | R | V |
| `Ucb` | CB线电压 | FLOAT | R | V |
| `ActivePowerAll` | 总有功功率 | FLOAT | R | W |
| `ApparentPowerC` | C相视在功率 | FLOAT | R | VA |
| `ActivePowerB` | B相有功功率 | FLOAT | R | W |
| `ActivePowerC` | C相有功功率 | FLOAT | R | W |
| `ReactivePowerAll` | 总无功功率 | FLOAT | R | var |
| `ReactivePowerA` | A相无功功率 | FLOAT | R | var |
| `ReactivePowerB` | B相无功功率 | FLOAT | R | var |
| `ReactivePowerC` | C相无功功率 | FLOAT | R | var |
| `ApparentPowerAll` | 总视在功率 | FLOAT | R | VA |
| `ApparentPowerA` | A相视在功率 | FLOAT | R | VA |
| `ApparentPowerB` | B相视在功率 | FLOAT | R | VA |
| `IxZsUnbalFactor` | 电流零序不平衡度 | FLOAT | R |  |
| `ActivePowerA` | A相有功功率 | FLOAT | R | W |
| `SysState1` | 状态信号1 | BITMAP | R |  |
| `SysState2` | 状态信号2 | BITMAP | R |  |
| `SysState3` | 状态信号3 | BITMAP | R |  |
| `SysState4` | 状态信号4 | BITMAP | R |  |
| `StateFire1` | 状态信号1 | BITMAP | R |  |
| `StateFire2` | 状态信号2 | BITMAP | R |  |
| `StateFire3` | 状态信号3 | BITMAP | R |  |
| `IR_Current` | 剩余电流 | FLOAT | R | A |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[electric-meter-3p]]
- [[low-voltage-smart-connector]]
- [[thing-model-structure]]
