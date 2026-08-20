---
title: 单相混合逆变器 — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, energy-storage]
sources: [raw/papers/public_MixInverter_1P_V1_0_2.md]
confidence: high
---
# 单相混合逆变器 — 测点全集

> 实体页 [[mix-inverter-1p]] 的测点参考,共 129 个测点。按命名前缀分组。

## Ala* — 7 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_SecBattOffLine` | 从电池或者从组通信离线 | ENUM | R |  |
| `Ala_CharOverCur` | 充电过电流告警 | ENUM | R |  |
| `Ala_DischarOverCur` | 放电过电流告警 | ENUM | R |  |
| `Ala_UnderBattTemp` | 电池温度过低告警 | ENUM | R |  |
| `Ala_OverBattTemp` | 电池温度过高告警 | ENUM | R |  |
| `Ala_BattModuOverU` | 电池模块过压告警 | ENUM | R |  |
| `Ala_BattModuUnderU` | 电池模块欠压告警 | ENUM | R |  |

## AntiRevFlowEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AntiRevFlowEn` | 防逆流使能 | ENUM | RW |  |

## BattCharEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattCharEn` | 电池充电使能 | ENUM | RW |  |

## BattModTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattModTemp` | 电池模块温度 | FLOAT | R | °C |

## BattPToGridEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattPToGridEn` | 电池功率上网使能 | ENUM | RW |  |

## BattRecovEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattRecovEn` | 电池恢复使能 | ENUM | RW |  |

## BatteryI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryI` | 电池电流 | FLOAT | R | A |

## BatteryP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryP` | 电池功率 | FLOAT | R | kW |

## BatteryTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryTemp` | 电池温度 | FLOAT | R | °C |

## BatteryU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryU` | 电池电压 | FLOAT | R | V |

## ChargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ChargeCount` | 总充电次数 | INT | R | x |

## DCDCModTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCDCModTemp` | DCDC模块温度 | FLOAT | R | °C |

## DayCharE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayCharE` | 当日充电量 | FLOAT | R | kWh |

## DayCharTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayCharTime` | 日充电时长 | INT | R | min |

## DayDischarE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayDischarE` | 当日放电量 | FLOAT | R | kWh |

## DayDischarTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayDischarTime` | 日放电时长 | INT | R | min |

## DayEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayEPE` | 当日反向有功电能 | FLOAT | R | kWh |

## DayEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayEPI` | 当日正向有功电能 | FLOAT | R | kWh |

## DayGenE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayGenE` | 当日发电机发电量 | FLOAT | R | kWh |

## DayGenOpeTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayGenOpeTime` | 当日发电机工作时间 | FLOAT | R | min |

## DayLoadE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayLoadE` | 当日用电量 | FLOAT | R | kWh |

## DayLoadTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayLoadTime` | 负载日用电时长 | FLOAT | R | min |

## DayPVE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayPVE` | 当日PV发电量 | FLOAT | R | kWh |

## DayPVInPtPeak* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayPVInPtPeak` | 当日PV输入总功率峰值 | FLOAT | R |  |

## DayPVTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayPVTime` | 当日PV发电时间 | FLOAT | R | h |

## DeviceTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |

## DischargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DischargeCount` | 总放电次数 | INT | R | x |

## EnergyRemain* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EnergyRemain` | 剩余电量 | FLOAT | R | kWh |

## Err* — 19 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Err_UnderPVU` | PV电压过低故障 | ENUM | R |  |
| `Err_OverGridU` | 电网电压过高故障 | ENUM | R |  |
| `Err_UnderGridU` | 电网电压过低故障 | ENUM | R |  |
| `Err_NoGridPower` | 无市电故障 | ENUM | R |  |
| `Err_OverGridFreq` | 电网频率过高故障 | ENUM | R |  |
| `Err_UnderGridFreq` | 电网频率过低故障 | ENUM | R |  |
| `Err_OverPVU` | PV电压过高故障 | ENUM | R |  |
| `Err_OverBusU` | 母线电压过高故障 | ENUM | R |  |
| `Err_UnderBusU` | 母线电压过低故障 | ENUM | R |  |
| `Err_SoftStart` | 软起故障 | ENUM | R |  |
| `Err_UnderInvertTemp` | 逆变器温度越限故障 | ENUM | R |  |
| `Err_BMSComm` | BMS通讯故障 | ENUM | R |  |
| `Err_System` | 电池系统错误 | ENUM | R |  |
| `Err_CharOverCur` | 充电过电流故障 | ENUM | R |  |
| `Err_DischarOverCur` | 放电过电流故障 | ENUM | R |  |
| `Err_UnderBattTemp` | 电池温度过低故障 | ENUM | R |  |
| `Err_OverBattTemp` | 电池温度过高故障 | ENUM | R |  |
| `Err_BattModuOverU` | 电池模块过压故障 | ENUM | R |  |
| `Err_BattModuUnderU` | 电池模块欠压故障 | ENUM | R |  |

## GenCharEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenCharEn` | 发电机充电使能 | ENUM | RW |  |

## GenOutFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenOutFreq` | 发电机输出频率 | FLOAT | R | Hz |

## GenOutI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenOutI` | 发电机输出电流 | FLOAT | R | A |

## GenOutP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenOutP` | 发电机输出功率 | FLOAT | R | W |

## GenOutU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenOutU` | 发电机输出电压 | FLOAT | R | V |

## GenSwitchOff* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenSwitchOff` | 发电机关机 | INT | RW |  |

## GenSwitchOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GenSwitchOn` | 发电机开机 | INT | RW |  |

## GridCharEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridCharEn` | 电网充电使能 | ENUM | RW |  |

## GridCharEndTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridCharEndTime` | 电网充电结束时间 | DATETIME | RW |  |

## GridCharStartTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridCharStartTime` | 电网充电开始时间 | DATETIME | RW |  |

## GridFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreq` | 电网频率 | FLOAT | R | Hz |

## GridI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridI` | 电网电流 | FLOAT | R | A |

## GridP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridP` | 电网有功功率 | FLOAT | R | kW |

## GridPF* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridPF` | 电网功率因数 | FLOAT | R |  |

## GridQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridQ` | 电网无功功率 | FLOAT | R | kvar |

## GridS* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridS` | 电网视在功率 | FLOAT | R | kVA |

## GridU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridU` | 电网电压 | FLOAT | R | V |

## InTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InTemp` | 机内温度 | FLOAT | R | °C |

## InvModTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvModTemp` | 逆变模块温度 | FLOAT | R | °C |

## InvertEffi* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertEffi` | 逆变效率 | FLOAT | R |  |

## InvertOutDayE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutDayE` | 逆变输出日发电量 | FLOAT | R | kWh |

## InvertOutFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutFreq` | 逆变输出频率 | FLOAT | R | Hz |

## InvertOutI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutI` | 逆变输出电流 | FLOAT | R | A |

## InvertOutP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutP` | 逆变输出有功功率 | FLOAT | R | kW |

## InvertOutPF* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPF` | 逆变输出功率因数 | FLOAT | R |  |

## InvertOutQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQ` | 逆变输出无功功率 | FLOAT | R | kvar |

## InvertOutS* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutS` | 逆变输出视在功率 | FLOAT | R | kVA |

## InvertOutTotalE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutTotalE` | 逆变输出总发电量 | FLOAT | R | kWh |

## InvertOutU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutU` | 逆变输出电压 | FLOAT | R | V |

## LoadI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LoadI` | 负载电流 | FLOAT | R | A |

## LoadP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LoadP` | 负载有功功率 | FLOAT | R | W |

## LoadQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LoadQ` | 负载无功功率 | FLOAT | R | kvar |

## LoadS* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LoadS` | 负载视在功率 | FLOAT | R | kVA |

## LoadU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LoadU` | 负载电压 | FLOAT | R | V |

## MonGenE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MonGenE` | 当月发电机发电量 | FLOAT | R | kWh |

## MonLoadE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MonLoadE` | 当月用电量 | FLOAT | R | kWh |

## MontEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MontEPE` | 当月反向有功电能 | FLOAT | R | kWh |

## MontEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MontEPI` | 当月正向有功电能 | FLOAT | R | kWh |

## OnOffGridMode* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `OnOffGridMode` | 设置并离网模式 | ENUM | RW |  |

## PV* — 6 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PV2InU` | PV2输入电压 | FLOAT | R | V |
| `PV1InU` | PV1输入电压 | FLOAT | R | V |
| `PV2InP` | PV2输入功率 | FLOAT | R | W |
| `PV2InI` | PV2输入电流 | FLOAT | R | A |
| `PV1InP` | PV1输入功率 | FLOAT | R | W |
| `PV1InI` | PV1输入电流 | FLOAT | R | A |

## PVInPt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PVInPt` | PV输入总功率 | FLOAT | R | W |

## PVModTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PVModTemp` | PV模块温度 | FLOAT | R | °C |

## PurePVOffGridEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PurePVOffGridEn` | 纯PV离网运行使能 | ENUM | RW |  |

## RemoSysRunMode* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoSysRunMode` | 设置远程系统工作模式 | ENUM | RW |  |

## SOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SOC` | 荷电状态 | FLOAT | R | % |

## SOH* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SOH` | 健康状态 | FLOAT | R | % |

## SetGridCharPLim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetGridCharPLim` | 设置电网充电功率限值 | FLOAT | RW | kW |

## SetMaxCharSOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetMaxCharSOC` | 设置最大充电SOC | FLOAT | RW | % |

## SetMaxExGridP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetMaxExGridP` | 设置最大上网功率 | INT | RW | kW |

## SetMinDischarSOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetMinDischarSOC` | 设置最小放电SOC | FLOAT | RW | % |

## Sta* — 3 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `Sta_SysRunMode` | 系统运行模式 | ENUM | R |  |
| `Sta_Battery` | 电池状态 | ENUM | R |  |

## SwitchOff* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SwitchOff` | 关机 | INT | W |  |

## SwitchOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SwitchOn` | 开机 | INT | W |  |

## SysRunMode* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SysRunMode` | 系统工作模式 | ENUM | RW |  |

## TotalCharE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalCharE` | 累计充电量 | FLOAT | R | kWh |

## TotalCharTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalCharTime` | 总充电时长 | INT | R | h |

## TotalDischarE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalDischarE` | 累计放电量 | FLOAT | R | kWh |

## TotalDischarTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalDischarTime` | 总放电时长 | INT | R | h |

## TotalEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalEPE` | 总反向有功电能 | FLOAT | R | kWh |

## TotalEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalEPI` | 总正向有功电能 | FLOAT | R | kWh |

## TotalGenE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalGenE` | 累计发电机发电量 | FLOAT | R | kWh |

## TotalLoadE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalLoadE` | 总负载用能 | FLOAT | R | kWh |

## TotalLoadTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalLoadTime` | 负载总用电时长 | FLOAT | R | h |

## TotalPVE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalPVE` | 累计PV发电量 | FLOAT | R | kWh |

## TotalPVTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalPVTime` | 累计PV发电时间 | FLOAT | R | h |

## YearEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `YearEPE` | 当年反向有功电能 | FLOAT | R | kWh |

## YearEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `YearEPI` | 当年正向有功电能 | FLOAT | R | kWh |

## YearGenE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `YearGenE` | 当年发电机发电量 | FLOAT | R | kWh |

## YearLoadE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `YearLoadE` | 当年用电量 | FLOAT | R | kWh |

## 关联

- [[mix-inverter-1p]]
- [[thing-model-structure]]
