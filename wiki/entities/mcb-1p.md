---
title: (交流)单相微型断路器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_MCB_1P_V1_0_2.md]
confidence: high
---
# (交流)单相微型断路器

## 概述

(交流)单相微型断路器 (MCB),物模型版本 V1.0.2。67 个测点含工作状态、分相/总量电量电能、漏电流、故障电流与电压等;18 个事件覆盖过压/欠压/过流/漏电/过温/过频/欠频/功率限制等(含告警与故障两级);9 个服务:分闸/合闸、漏电检测与测试、LED 闪烁、锁定/解锁、远程复位。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_MCB_1P_V1_0_2` |
| 中文名 | (交流)单相微型断路器 |
| 英文名 | （AC）MCB |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_MCB_1P_V1_0_2.md |

## 属性 (Attribute) — 11 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `RatedCurrent` | 额定电流 | FLOAT | A | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `MechanicalLife` | 机械寿命 | INT | x | False |
| `ElectricalLife` | 电气寿命 | INT | x | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 67 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WorkingStatus` | 状态字 | BITMAP | R |  |
| `EQE` | 反向无功电能 | FLOAT | R | kvarh |
| `EQI` | 正向无功电能 | FLOAT | R | kvarh |
| `EPE` | 反向有功电能 | FLOAT | R | kWh |
| `EPI` | 正向有功电能 | FLOAT | R | kWh |
| `Err_P` | 故障事件前有功功率 | FLOAT | R | kW |
| `Err_I` | 故障事件前电流 | FLOAT | R | A |
| `Err_UnderVoltage` | 欠压故障 | ENUM | R |  |
| `Err_U` | 故障事件前电压 | FLOAT | R | V |
| `Err_Ires` | 故障事件前剩余电流 | FLOAT | R | mA |
| `ComEQ` | 组合无功电能 | FLOAT | R | kvarh |
| `Err1th_Ires` | 故障事件前剩余电流 | FLOAT | R | mA |
| `Ires` | 剩余电流 | FLOAT | R | mA |
| `U` | 电压 | FLOAT | R | V |
| `S` | 视在功率 | FLOAT | R | VA |
| `Err_Sta` | 故障事件时运行状态 | ENUM | R |  |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `TempOut` | 出线温度 | FLOAT | R | °C |
| `TempIn` | 进线温度 | FLOAT | R | °C |
| `Q` | 无功功率 | FLOAT | R | var |
| `PF` | 功率因数 | FLOAT | R |  |
| `P` | 有功功率 | FLOAT | R | W |
| `I` | 电流 | FLOAT | R | A |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |
| `TempOnChip` | 片上温度 | FLOAT | R | °C |
| `Err_TempOnChip` | 故障事件前片上温度 | FLOAT | R | °C |
| `Err_Freq` | 故障事件前频率 | FLOAT | R | Hz |
| `Err_Time` | 故障事件时间 | DATETIME | R |  |
| `Err_OverFreq` | 过频故障 | ENUM | R |  |
| `Err_PowerLimit` | 功率越限故障 | ENUM | R |  |
| `Freq` | 电网频率 | FLOAT | R | Hz |
| `LeakageCheck` | 漏电自检 | INT | W |  |
| `LeakageTest` | 漏电试跳 | INT | W |  |
| `RemoteReset` | 远方复位 | INT | W |  |
| `Open` | 分闸 | INT | W |  |
| `Close` | 合闸 | INT | W |  |
| `Lockout` | 锁死 | INT | W |  |
| `Lock` | 锁定 | INT | W |  |
| `Unlock` | 解锁 | INT | W |  |
| `Ala_PowerLimit` | 功率限定告警 | ENUM | R |  |
| `Ala_UnderFreq` | 欠频告警 | ENUM | R |  |
| `Ala_OverFreq` | 过频告警 | ENUM | R |  |
| `Ala_OverTemp` | 温度越限告警 | ENUM | R |  |
| `Ala_OverCurrent` | 过载告警 | ENUM | R |  |
| `ComEP` | 组合有功电能 | FLOAT | R | kWh |
| `Err_OverTemp` | 温度越限故障 | ENUM | R |  |
| `Ala_OverVoltage` | 过压告警 | ENUM | R |  |
| `Ala_UnderVoltage` | 欠压告警 | ENUM | R |  |
| `Ala_Leakage` | 漏电告警 | ENUM | R |  |
| `OpenCount` | 分闸次数 | INT | R | x |
| `OperationCount` | 操作次数 | INT | R | x |
| `Sta_OveUndVolLock` | 过欠压锁死 | ENUM | R |  |
| `LEDBlink` | LED灯闪烁 | INT | W |  |
| `Sta_RemoConLock` | 遥控锁死 | ENUM | R |  |
| `Sta_ManualAuto` | 手自动 | ENUM | R |  |
| `Err_UnderFreq` | 欠频故障 | ENUM | R |  |
| `Err_OverVoltage` | 过压故障 | ENUM | R |  |
| `Err_Leakage` | 漏电故障 | ENUM | R |  |
| `Err_OverCurrent` | 过载故障 | ENUM | R |  |
| `Err1th_TempOnChip` | 故障事件前片上温度 | FLOAT | R | °C |
| `Err_Reason` | 故障事件原因 | BITMAP | R |  |
| `Err1th_P` | 故障事件前有功功率 | FLOAT | R | kW |
| `Err1th_Freq` | 故障事件前频率 | FLOAT | R | Hz |
| `Err1th_Time` | 故障事件时间 | DATETIME | R |  |
| `Err1th_Reason` | 故障事件原因 | BITMAP | R |  |
| `Err1th_U` | 故障事件前电压 | FLOAT | R | V |
| `Err1th_I` | 故障事件前电流 | FLOAT | R | A |

## 事件 (Event) — 18 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorRemoteTest` | 远程试跳故障 | FAULT |
| `ErrorOverVoltage` | 过压故障 | FAULT |
| `ErrorUnderVoltage` | 欠压故障 | FAULT |
| `ErrorLeakage` | 漏电故障 | FAULT |
| `ErrorOverCurrent` | 过载故障 | FAULT |
| `ErrorOverTemp` | 温度越限故障 | FAULT |
| `ErrorOverFreq` | 过频故障 | FAULT |
| `ErrorUnderFreq` | 欠频故障 | FAULT |
| `ErrorButtonTest` | 按钮试跳故障 | FAULT |
| `AlarmPowerLimit` | 功率越限告警 | ALARM |
| `ErrorPowerLimit` | 功率越限故障 | FAULT |
| `AlarmOverVoltage` | 过压告警 | ALARM |
| `AlarmUnderVoltage` | 欠压告警 | ALARM |
| `AlarmLeakage` | 漏电告警 | ALARM |
| `AlarmOverCurrent` | 过载告警 | ALARM |
| `AlarmOverTemp` | 温度越限告警 | ALARM |
| `AlarmOverFreq` | 过频告警 | ALARM |
| `AlarmUnderFreq` | 欠频告警 | ALARM |

## 服务 (Service) — 9 个

| 标识符 | 名称 |
| --- | --- |
| `CloseCmd` | 合闸 |
| `LeakageCheckCmd` | 漏电自检 |
| `LeakageTestCmd` | 漏电试跳 |
| `LEDBlinkCmd` | LED灯闪烁 |
| `LockCmd` | 锁定 |
| `LockoutCmd` | 锁死 |
| `OpenCmd` | 分闸 |
| `RemoteResetCmd` | 远方复位 |
| `UnlockCmd` | 解锁 |

## 关联

- [[mcb-3p]]
- [[mccb-3p]]
- [[acb-3p]]
- [[thing-model-structure]]
- [[circuit-breaker-family]]
