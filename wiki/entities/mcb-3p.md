---
title: (交流)三相微型断路器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_MCB_3P_V1_0_2.md]
confidence: high
---
# (交流)三相微型断路器

## 概述

(交流)三相微型断路器 (MCB),物模型版本 V1.0.2。96 个测点:三相电压/电流/功率/功率因数/电量电能、漏电流、故障标志与工作状态等;20 个事件(较单相版多出缺相 AlarmPhaseLoss/ErrorPhaseLoss);9 个服务与单相版一致(分合闸/漏电检测测试/LED/锁定/复位)。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_MCB_3P_V1_0_2` |
| 中文名 | (交流)三相微型断路器 |
| 英文名 | AC MCB |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_MCB_3P_V1_0_2.md |

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

## 测点 (MeasurePoint) — 96 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WorkingSts` | 状态字 | BITMAP | R |  |
| `ComEQ` | 组合无功电能 | FLOAT | R | kvarh |
| `EQE` | 反向无功电能 | FLOAT | R | kvarh |
| `EQI` | 正向无功电能 | FLOAT | R | kvarh |
| `Qc` | C相无功功率 | FLOAT | R | var |
| `Uca` | CA线电压 | FLOAT | R | V |
| `PFc` | C相功率因数 | FLOAT | R |  |
| `Pb` | B相有功功率 | FLOAT | R | W |
| `Sb` | B相视在功率 | FLOAT | R | VA |
| `Qb` | B相无功功率 | FLOAT | R | var |
| `PFb` | B相功率因数 | FLOAT | R |  |
| `Pa` | A相有功功率 | FLOAT | R | W |
| `Sa` | A相视在功率 | FLOAT | R | VA |
| `Qa` | A相无功功率 | FLOAT | R | var |
| `PFa` | A相功率因数 | FLOAT | R |  |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |
| `Ua` | A相电压 | FLOAT | R | V |
| `Ia` | A相电流 | FLOAT | R | A |
| `Ub` | B相电压 | FLOAT | R | V |
| `Ib` | B相电流 | FLOAT | R | A |
| `Uc` | C相电压 | FLOAT | R | V |
| `Ic` | C相电流 | FLOAT | R | A |
| `In` | 中性线电流 | FLOAT | R | A |
| `Uab` | AB线电压 | FLOAT | R | V |
| `Ubc` | BC线电压 | FLOAT | R | V |
| `EPE` | 反向有功电能 | FLOAT | R | kWh |
| `Err_Pb` | 故障事件前B相有功功率 | FLOAT | R | W |
| `Err_Time` | 故障事件时间 | DATETIME | R |  |
| `Err_Reason` | 故障事件原因 | BITMAP | R |  |
| `Err_Sta` | 故障事件时运行状态 | ENUM | R |  |
| `Err_Ua` | 故障事件前A相电压 | FLOAT | R | V |
| `Err_Ub` | 故障事件前B相电压 | FLOAT | R | V |
| `Err_Ia` | 故障事件前A相电流 | FLOAT | R | A |
| `Err_Ib` | 故障事件前B相电流 | FLOAT | R | A |
| `Err_Ic` | 故障事件前C相电流 | FLOAT | R | A |
| `Err_In` | 故障事件前中性线电流 | FLOAT | R | A |
| `Err_Pt` | 故障事件前总有功功率 | FLOAT | R | W |
| `Err_Pa` | 故障事件前A相有功功率 | FLOAT | R | W |
| `Sc` | C相视在功率 | FLOAT | R | VA |
| `Err_Pc` | 故障事件前C相有功功率 | FLOAT | R | W |
| `Err_Freq` | 故障事件前频率 | FLOAT | R | Hz |
| `Err_Ires` | 故障事件前剩余电流 | FLOAT | R | mA |
| `Err_TempOnChip` | 故障事件前片上温度 | FLOAT | R | °C |
| `Err_Uc` | 故障事件前C相电压 | FLOAT | R | V |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `St` | 总视在功率 | FLOAT | R | VA |
| `Qt` | 总无功功率 | FLOAT | R | var |
| `Pt` | 总有功功率 | FLOAT | R | W |
| `PFt` | 总功率因数 | FLOAT | R |  |
| `Pc` | C相有功功率 | FLOAT | R | W |
| `Ala_OverFreq` | 过频告警 | ENUM | R |  |
| `Err_OverFreq` | 过频故障 | ENUM | R |  |
| `Err_UnderFreq` | 欠频故障 | ENUM | R |  |
| `Err_ButtonTest` | 按钮试跳故障 | ENUM | R |  |
| `Err_RemoteTest` | 远程试跳故障 | ENUM | R |  |
| `Err_PowerLimit` | 功率越限故障 | ENUM | R |  |
| `Ala_OverVoltage` | 过压告警 | ENUM | R |  |
| `Ala_UnderVoltage` | 欠压告警 | ENUM | R |  |
| `Ala_Leakage` | 漏电告警 | ENUM | R |  |
| `Ala_OverCurrent` | 过载告警 | ENUM | R |  |
| `Ala_OverTemp` | 温度越限告警 | ENUM | R |  |
| `Ala_PhaseLoss` | 断相告警 | ENUM | R |  |
| `Err_PhaseLoss` | 断相故障 | ENUM | R |  |
| `Ala_UnderFreq` | 欠频告警 | ENUM | R |  |
| `Ala_PowerLimit` | 功率越限告警 | ENUM | R |  |
| `Unlock` | 解锁 | INT | W |  |
| `Lock` | 锁定 | INT | W |  |
| `Lockout` | 锁死 | INT | W |  |
| `Close` | 合闸 | INT | W |  |
| `Open` | 分闸 | INT | W |  |
| `RemoteReset` | 远方复位 | INT | W |  |
| `LeakageTest` | 漏电试跳 | INT | W |  |
| `LeakageCheck` | 漏电自检 | INT | W |  |
| `TempOutN` | 中性线出线温度 | FLOAT | R | °C |
| `LEDBlink` | LED灯闪烁 | INT | W |  |
| `ComEP` | 组合有功电能 | FLOAT | R | kWh |
| `Freq` | 电网频率 | FLOAT | R | Hz |
| `Ires` | 剩余电流 | FLOAT | R | mA |
| `TempInA` | A相进线温度 | FLOAT | R | °C |
| `TempOutA` | A相出线温度 | FLOAT | R | °C |
| `TempInB` | B相进线温度 | FLOAT | R | °C |
| `TempOutB` | B相出线温度 | FLOAT | R | °C |
| `TempInC` | C相进线温度 | FLOAT | R | °C |
| `TempOutC` | C相出线温度 | FLOAT | R | °C |
| `TempInN` | 中性线进线温度 | FLOAT | R | °C |
| `EPI` | 正向有功电能 | FLOAT | R | kWh |
| `OpenCount` | 分闸次数 | INT | R | x |
| `LeakOpenCount` | 漏电分闸次数 | INT | R | x |
| `Sta_OveUndVolLock` | 过欠压锁死 | ENUM | R |  |
| `Sta_RemoConLock` | 遥控锁死 | ENUM | R |  |
| `Sta_ManualAuto` | 手自动 | ENUM | R |  |
| `Err_OverVoltage` | 过压故障 | ENUM | R |  |
| `Err_UnderVoltage` | 欠压故障 | ENUM | R |  |
| `Err_Leakage` | 漏电故障 | ENUM | R |  |
| `Err_OverCurrent` | 过载故障 | ENUM | R |  |
| `Err_OverTemp` | 温度越限故障 | ENUM | R |  |

## 事件 (Event) — 20 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorRemoteTest` | 远程试跳故障 | FAULT |
| `ErrorOverVoltage` | 过压故障 | FAULT |
| `ErrorUnderVoltage` | 欠压故障 | FAULT |
| `ErrorLeakage` | 漏电故障 | FAULT |
| `ErrorOverCurrent` | 过载故障 | FAULT |
| `ErrorOverTemp` | 温度越限故障 | FAULT |
| `ErrorPhaseLoss` | 断相故障 | FAULT |
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
| `AlarmPhaseLoss` | 断相告警 | ALARM |
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

- [[mcb-1p]]
- [[mccb-3p]]
- [[electric-meter-3p]]
- [[thing-model-structure]]
- [[circuit-breaker-family]]
