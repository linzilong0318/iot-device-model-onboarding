---
title: (交流)单相电表
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_ElectricMeter_1P_V1_0_2.md]
confidence: high
---
# (交流)单相电表

## 概述

(交流)单相电表,物模型版本 V1.0.2。66 个测点覆盖分时/总电量(正反向有功、无功)、谐波(THD/谐波电流 RMS)、基波、温度、DI/DO 状态、设备时间等;6 个事件为过压/欠压/过流/过频/欠频/烟雾告警;7 个服务为电量清零、4 路 DO 控制、远程复位、出厂复位。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ElectricMeter_1P_V1_0_2` |
| 中文名 | (交流)单相电表 |
| 英文名 | (AC) Single-Phase Meter |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_ElectricMeter_1P_V1_0_2.md |

## 属性 (Attribute) — 8 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 66 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEPT3` | 组合有功费率3电能 | FLOAT | R | kWh |
| `THDI` | 电压总谐波畸变率 | FLOAT | R | % |
| `THDU` | 电流总谐波畸变率 | FLOAT | R | % |
| `HarmonicRmsI` | 电流谐波有效值 | FLOAT | R | A |
| `FundamentalI` | 电流基波值 | FLOAT | R | A |
| `Ires` | 剩余电流 | FLOAT | R | mA |
| `ComEP` | 组合有功电能 | FLOAT | R | kWh |
| `ComEPT1` | 组合有功费率1电能 | FLOAT | R | kWh |
| `EPIT5` | 正向有功费率5电能 | FLOAT | R | kWh |
| `EPIT3` | 正向有功费率3电能 | FLOAT | R | kWh |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |
| `ComEPT5` | 组合有功费率5电能 | FLOAT | R | kWh |
| `EPI` | 正向有功电能 | FLOAT | R | kWh |
| `EPIT1` | 正向有功费率1电能 | FLOAT | R | kWh |
| `EPIT2` | 正向有功费率2电能 | FLOAT | R | kWh |
| `RemoteReset` | 远方复位 | INT | W |  |
| `EPIT4` | 正向有功费率4电能 | FLOAT | R | kWh |
| `ComEPT2` | 组合有功费率2电能 | FLOAT | R | kWh |
| `EPE` | 反向有功电能 | FLOAT | R | kWh |
| `EPET1` | 反向有功费率1电能 | FLOAT | R | kWh |
| `EPET2` | 反向有功费率2电能 | FLOAT | R | kWh |
| `EPET3` | 反向有功费率3电能 | FLOAT | R | kWh |
| `EPET4` | 反向有功费率4电能 | FLOAT | R | kWh |
| `DI1` | 开关量输入1 | ENUM | R |  |
| `DI2` | 开关量输入2 | ENUM | R |  |
| `DI3` | 开关量输入3 | ENUM | R |  |
| `DI4` | 开关量输入4 | ENUM | R |  |
| `DI5` | 开关量输入5 | ENUM | R |  |
| `DI6` | 开关量输入6 | ENUM | R |  |
| `DI7` | 开关量输入7 | ENUM | R |  |
| `I` | 电流 | FLOAT | R | A |
| `FactoryReset` | 恢复出厂设置 | INT | W |  |
| `ClearE` | 电能清零 | INT | W |  |
| `Freq` | 电网频率 | FLOAT | R | Hz |
| `EPET5` | 反向有功费率5电能 | FLOAT | R | kWh |
| `Q` | 无功功率 | FLOAT | R | kvar |
| `S` | 视在功率 | FLOAT | R | kVA |
| `PF` | 功率因数 | FLOAT | R |  |
| `EP` | 总有功电能 | FLOAT | R | kWh |
| `EQ` | 总无功电能 | FLOAT | R | kWh |
| `EQI` | 正向无功电能 | FLOAT | R | kvarh |
| `Ala_UnderFreq` | 欠频告警 | ENUM | R |  |
| `P` | 有功功率 | FLOAT | R | kW |
| `MaxDmdEPI` | 正向有功最大需量 | FLOAT | R | kW |
| `MaxDmdEPE` | 反向有功最大需量 | FLOAT | R | kW |
| `CreditRemain` | 剩余金额 | FLOAT | R |  |
| `Temp` | 温度 | FLOAT | R | °C |
| `U` | 电压 | FLOAT | R | V |
| `ComEPT4` | 组合有功费率4电能 | FLOAT | R | kWh |
| `Ala_Smoke` | 烟感告警 | ENUM | R |  |
| `EQE` | 反向无功电能 | FLOAT | R | kvarh |
| `Ala_OverFreq` | 过频告警 | ENUM | R |  |
| `Ala_OverCurrent` | 过载告警 | ENUM | R |  |
| `Ala_UnderVoltage` | 欠压告警 | ENUM | R |  |
| `Ala_OverVoltage` | 过压告警 | ENUM | R |  |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `CurrentRatio` | 电流变比 | INT | RW |  |
| `VoltageRatio` | 电压变比 | INT | RW |  |
| `CreditTotal` | 总购电金额 | FLOAT | R |  |
| `EnergyRemain` | 剩余电量 | FLOAT | R | kWh |
| `DI8` | 开关量输入8 | ENUM | R |  |
| `DO1` | 开关量输出1 | ENUM | W |  |
| `DO2` | 开关量输出2 | ENUM | W |  |
| `DO3` | 开关量输出3 | ENUM | W |  |
| `DO4` | 开关量输出4 | ENUM | W |  |
| `CurrentDmdP` | 当前有功需量 | FLOAT | R | kW |

## 事件 (Event) — 6 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmSmoke` | 烟感告警 | ALARM |
| `AlarmUnderFreq` | 欠频告警 | ALARM |
| `AlarmOverFreq` | 过频告警 | ALARM |
| `AlarmOverCurrent` | 过载告警 | ALARM |
| `AlarmUnderVoltage` | 欠压告警 | ALARM |
| `AlarmOverVoltage` | 过压告警 | ALARM |

## 服务 (Service) — 7 个

| 标识符 | 名称 |
| --- | --- |
| `ClearECmd` | 电能清零 |
| `DO1Cmd` | 开关量输出1控制 |
| `DO2Cmd` | 开关量输出2控制 |
| `DO3Cmd` | 开关量输出3控制 |
| `DO4Cmd` | 开关量输出4控制 |
| `FactoryResetCmd` | 恢复出厂设置 |
| `RemoteResetCmd` | 远方复位 |

## 关联

- [[electric-meter-3p]]
- [[mcb-1p]]
- [[charging-pile-1p]]
- [[thing-model-structure]]
- [[electric-meter-family]]
