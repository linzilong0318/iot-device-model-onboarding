---
title: 储能变流器(PCS) — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, energy-storage]
sources: [raw/papers/public_PCS.md]
confidence: high
---
# 储能变流器(PCS) — 测点全集

> 实体页 [[pcs]] 的测点参考,共 175 个测点。按命名前缀分组。

## Ala* — 9 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_ACSPD` | 交流避雷器异常 | ENUM | R |  |
| `Ala_TempSensor` | 温度传感器告警 | ENUM | R |  |
| `Ala_SPD` | 避雷器异常 | ENUM | R |  |
| `Ala_Eeprom` | EEPROM读写故障 | ENUM | R |  |
| `Ala_InComm` | 内部通讯失败告警 | ENUM | R |  |
| `Ala_InFan` | 内部风扇告警 | ENUM | R |  |
| `Ala_OutFan` | 外部风扇告警 | ENUM | R |  |
| `Ala_DCPWMShut` | 直流封锁 | ENUM | R |  |
| `Ala_DCIUmB` | 直流电流不平衡 | ENUM | R |  |

## AmbientTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AmbientTemp` | 环境温度 | FLOAT | R | °C |

## AntiRevFlowEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AntiRevFlowEn` | 防逆流使能 | ENUM | RW |  |

## AutoTest* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AutoTest` | 自动测试 | INT | RW |  |

## BattCharCurLim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattCharCurLim` | 电池放电限流 | FLOAT | R | A |

## BattDischarCurLim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattDischarCurLim` | 电池充电限流 | FLOAT | R | A |

## BattPreChargeEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattPreChargeEn` | 电池预充电使能 | ENUM | RW |  |

## BattSwitchOff* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattSwitchOff` | 电池关机 | INT | RW |  |

## BattSwitchOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BattSwitchOn` | 电池开机 | INT | RW |  |

## BatteryI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryI` | 电池电流 | FLOAT | R | A |

## BatteryP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryP` | 电池功率 | FLOAT | R | kW |

## BatteryU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BatteryU` | 电池电压 | FLOAT | R | V |

## BoostTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `BoostTemp` | Boost模块温度 | FLOAT | R | °C |

## CPSEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CPSEn` | CPS使能 | ENUM | RW |  |

## CPST* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CPST1En` | 削峰填谷时间段1使能状态 | ENUM | RW |  |

## CharERemain* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CharERemain` | 电池充电剩余电量 | FLOAT | R | kWh |

## DCCurrent* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCCurrent` | 直流电流 | FLOAT | R | A |

## DCIA* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCIA` | A相直流分量 | FLOAT | R | mA |

## DCIB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCIB` | B相直流分量 | FLOAT | R | mA |

## DCIC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCIC` | C相直流分量 | FLOAT | R | mA |

## DCInP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCInP` | 直流输入功率 | FLOAT | R | kW |

## DCVoltage* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DCVoltage` | 直流电压 | FLOAT | R | V |

## DayCharE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayCharE` | 当日充电量 | FLOAT | R | kWh |

## DayCharTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayCharTime` | 日充电时长 | INT | R | min |

## DayChargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayChargeCount` | 日充电次数 | INT | R | x |

## DayDischarE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayDischarE` | 当日放电量 | FLOAT | R | kWh |

## DayDischarTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayDischarTime` | 日放电时长 | INT | R | min |

## DayDischargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayDischargeCount` | 日放电次数 | INT | R | x |

## DischarERemain* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DischarERemain` | 电池放电剩余电量 | FLOAT | R | kWh |

## Efficiency* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Efficiency` | 效率 | FLOAT | R | % |

## Err* — 57 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Err_Island` | 孤岛故障 | ENUM | R |  |
| `Err_PassiveIsland` | 被动孤岛故障 | ENUM | R |  |
| `Err_OverBusU` | 母线过压故障 | ENUM | R |  |
| `Err_GFCISensor` | 漏电流传感器故障 | ENUM | R |  |
| `Err_GridUUnB` | 电网电压不平衡故障 | ENUM | R |  |
| `Err_MCU` | MCU故障 | ENUM | R |  |
| `Err_GFCIDynamic` | 动态漏电流过流故障 | ENUM | R |  |
| `Err_Isolation` | 绝缘阻抗过低故障 | ENUM | R |  |
| `Err_DCIHigh` | 逆变电流直流分量越限故障 | ENUM | R |  |
| `Err_DCIOffset` | 逆变电流直流分量偏置保护 | ENUM | R |  |
| `Err_OpenLoopSelfChk` | 开环自检异常故障 | ENUM | R |  |
| `Err_GridTHDU` | 电网电压谐波过高故障 | ENUM | R |  |
| `Err_CANComm` | CAN通讯故障 | ENUM | R |  |
| `Err_GFCIStatic` | 静态漏电流过流故障 | ENUM | R |  |
| `Err_OverBoostCur` | Boost电路过流故障 | ENUM | R |  |
| `Err_DCChargeCir` | 直流侧充电回路异常 | ENUM | R |  |
| `Err_OverBattU` | 电池电压过高故障 | ENUM | R |  |
| `Err_NoBusU` | 母线无电压故障 | ENUM | R |  |
| `Err_GridInvUDiff` | 网侧逆变侧电压不一致故障 | ENUM | R |  |
| `Err_InvHWOverI` | 逆变硬件过流故障 | ENUM | R |  |
| `Err_BattInputRevCon` | 电池输入反接故障 | ENUM | R |  |
| `Err_OverGridLineU` | 电网线电压瞬时值越限故障 | ENUM | R |  |
| `Err_EmergCloase` | 紧急按钮闭合 | ENUM | R |  |
| `Err_ROCOF` | ROCOF故障 | ENUM | R |  |
| `Err_BusBattUDiff` | 母线和电池电压差过大 | ENUM | R |  |
| `Err_DCRelay` | 直流继电器故障 | ENUM | R |  |
| `Err_OverCapCur` | 滤波电容电流越限故障 | ENUM | R |  |
| `Err_InvPWMShut` | 逆变封锁保护 | ENUM | R |  |
| `Err_OverHalfBusU` | 半母线电压高 | ENUM | R |  |
| `Err_HalfBusUUnB` | 半母线电压不平衡 | ENUM | R |  |
| `Err_OnOffGridPara` | 并离网参数不匹配 | ENUM | R |  |
| `Err_TempSensor` | 温度传感器故障 | ENUM | R |  |
| `Err_OverDCI` | 直流侧过流故障 | ENUM | R |  |
| `Err_GFCICurOffset` | 漏电流偏置故障 | ENUM | R |  |
| `Err_LoadCur` | 负载电流偏置故障 | ENUM | R |  |
| `Err_JETIsland` | JET孤岛频率异常 | ENUM | R |  |
| `Err_CPLDOscil` | CPLD晶振失效故障 | ENUM | R |  |
| `Err_OverGridUPeak` | 电网电压峰值越限故障 | ENUM | R |  |
| `Err_BattPara` | 电池参数设置错误 | ENUM | R |  |
| `Err_UnderBattU` | 电池欠压故障 | ENUM | R |  |
| `Err_VNPE` | NPE电压差越限故障 | ENUM | R |  |
| `Err_InvRelay` | 逆变继电器故障 | ENUM | R |  |
| `Err_DCVUOffset` | DCV电压偏置故障 | ENUM | R |  |
| `Err_RapidDischarge` | 快速放电动作 | ENUM | R |  |
| `Err_GridBreaker` | 电网外部断路器故障 | ENUM | R |  |
| `Err_LoadPF` | 负载功率因数过低 | ENUM | R |  |
| `Err_BattIOffset` | 电池电流偏置故障 | ENUM | R |  |
| `Err_Time` | 近一次故障事件时间 | DATETIME | R |  |
| `Err_InvOutIOffset` | 逆变电流偏置异常故障 | ENUM | R |  |
| `Err_OverTemp` | 温度越限故障 | ENUM | R |  |
| `Err_Relay` | 并网继电器故障 | ENUM | R |  |
| `Err_GridPhaseLoss` | 电网断相故障 | ENUM | R |  |
| `Err_GridUnderFreq` | 电网欠频故障 | ENUM | R |  |
| `Err_GridOverFreq` | 电网过频故障 | ENUM | R |  |
| `Err_InvOutOverI` | 逆变输出过流故障 | ENUM | R |  |
| `Err_GridPhaseU` | 电网相电压故障 | ENUM | R |  |
| `Err_GridLineU` | 电网线电压故障 | ENUM | R |  |

## FactoryReset* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FactoryReset` | 恢复出厂设置 | INT | RW |  |

## ForceReboot* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ForceReboot` | 强制重启 | INT | RW |  |

## GFCIAvg* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GFCIAvg` | 漏电流侦测平均值 | FLOAT | R | mA |

## GFCIRms* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GFCIRms` | 漏电流侦测有效值 | FLOAT | R | mA |

## GridFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreq` | 电网频率 | FLOAT | R | Hz |

## GridPhaSeq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridPhaSeq` | 电网相序 | ENUM | R |  |

## GridUUnB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUUnB` | 电网电压不平衡度 | FLOAT | R | % |

## ISO* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ISO` | 绝缘阻抗侦测值 | FLOAT | R | kΩ |

## Ia* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ia` | 电网A相电流 | FLOAT | R | A |

## Ib* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ib` | 电网B相电流 | FLOAT | R | A |

## Ic* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ic` | 电网C相电流 | FLOAT | R | A |

## InvertModuleTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertModuleTemp` | 逆变模块温度 | FLOAT | R | °C |

## InvertOutP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutP` | 逆变输出有功功率 | FLOAT | R | kW |

## InvertOutQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQ` | 逆变输出无功功率 | FLOAT | R | kvar |

## ManualClearError* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ManualClearError` | 手动清除故障 | INT | RW |  |

## MaxBattStackTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MaxBattStackTemp` | 电池包最高温度 | FLOAT | R | °C |

## MaxBattStackU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MaxBattStackU` | 电池包最高电压 | FLOAT | R | V |

## MinBattStackTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MinBattStackTemp` | 电池包最低温度 | FLOAT | R | °C |

## MinBattStackU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MinBattStackU` | 电池包最低电压 | FLOAT | R | V |

## OutBoardTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `OutBoardTemp` | 输出板温度 | FLOAT | R | °C |

## PCSConnect* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PCSConnect` | PCS连接 | INT | RW |  |

## PCSDisconnect* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PCSDisconnect` | PCS断开 | INT | RW |  |

## PCSSwitchOff* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PCSSwitchOff` | PCS关机 | INT | RW |  |

## PCSSwitchOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PCSSwitchOn` | PCS开机 | INT | RW |  |

## PF* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PF` | 功率因数 | FLOAT | R |  |

## PowerBoardTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PowerBoardTemp` | 功率板温度 | FLOAT | R | °C |

## RapidDischarge* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RapidDischarge` | 快速放电 | INT | RW |  |

## RemoteCSPCtrlEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteCSPCtrlEn` | 远程CS有功控制使能 | ENUM | RW |  |

## RemoteCSPCtrlMode* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteCSPCtrlMode` | 远程CS有功控制模式 | ENUM | RW |  |

## RemoteCSQCtrlEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteCSQCtrlEn` | 远程CS无功控制使能 | ENUM | RW |  |

## RemoteCSQCtrlMode* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteCSQCtrlMode` | 远程CS无功控制模式 | ENUM | RW |  |

## RemoteSwitchCS* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteSwitchCS` | 远程选择CS模式 | INT | RW |  |

## RemoteSwitchVS* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteSwitchVS` | 远程选择VS模式 | INT | RW |  |

## RemoteVsEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteVsEn` | 远程VS模式使能 | ENUM | RW |  |

## S* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `S` | 视在功率 | FLOAT | R | kVA |

## SOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SOC` | 荷电状态 | FLOAT | R | % |

## SOH* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SOH` | 健康状态 | FLOAT | R | % |

## SetCPSDeadlineT* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetCPSDeadlineT1` | 设置削峰填谷时间段1截止时间 | DATETIME | RW |  |

## SetCPSPT* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetCPSPT1` | 削峰填谷时间段1功率值 | FLOAT | RW | % |

## SetCPSStartTimeT* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetCPSStartTimeT1` | 设置削峰填谷时间段1起始时间 | DATETIME | RW |  |

## SetMaxSOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetMaxSOC` | 设置SOC上限 | INT | RW | % |

## SetMinSOC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetMinSOC` | 设置SOC下限 | INT | RW | % |

## SetRemoCSDCI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCSDCI` | 远程设置CS直流电流 | FLOAT | RW | A |

## SetRemoCSP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCSP` | 远程设置CS有功功率 | FLOAT | RW | % |

## SetRemoCSPF* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCSPF` | 远程设置CS功率因数 | FLOAT | RW |  |

## SetRemoCSQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCSQ` | 远程设置CS无功功率 | FLOAT | RW | % |

## SetRemoCharILim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCharILim` | 远程设置充电电流限值 | FLOAT | RW | A |

## SetRemoCharULim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoCharULim` | 远程设置充电电压限值 | FLOAT | RW | V |

## SetRemoDischarILim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoDischarILim` | 远程设置放电电流限值 | FLOAT | RW | A |

## SetRemoDischarULim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoDischarULim` | 远程设置放电电压限值 | FLOAT | RW | V |

## SetRemoFloatCharILim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoFloatCharILim` | 远程设置浮充电流限值 | FLOAT | RW | A |

## SetRemoFloatCharULim* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoFloatCharULim` | 远程设置浮充电压限值 | FLOAT | RW | V |

## SetRemoVSP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoVSP` | 远程设置VS有功功率 | FLOAT | RW | % |

## SetRemoVSQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoVSQ` | 远程设置VS无功功率 | FLOAT | RW | % |

## SetRemoVSU* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoVSU` | 远程设置VS电压 | FLOAT | RW | V |

## SetRemoVsFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetRemoVsFreq` | 远程设置VS频率 | FLOAT | RW | Hz |

## Sta* — 13 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_BattStack` | 电池堆状态 | ENUM | R |  |
| `Sta_BattStackRu` | 电池堆工作状态 | ENUM | R |  |
| `Sta_BattRunMode` | 电池运行模式 | ENUM | R |  |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `Sta_RunMode` | 系统运行模式 | ENUM | R |  |
| `Sta_Grid` | 电网状态 | ENUM | R |  |
| `Sta_OnOffGrid` | 并离网状态 | ENUM | R |  |
| `Sta_UnderRatedP` | 降额运行 | ENUM | R |  |
| `Sta_15VPowerSource` | 系统15V控制电源 | ENUM | R |  |
| `Sta_InvertRun` | 并网发电 | ENUM | R |  |
| `Sta_StartMode` | 启动模式 | ENUM | R |  |
| `Sta_Debug` | 调试状态 | ENUM | R |  |
| `Sta_InvSelfChk` | 逆变自检模式 | ENUM | R |  |

## TotalCharE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalCharE` | 累计充电量 | FLOAT | R | kWh |

## TotalCharTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalCharTime` | 总充电时长 | INT | R | h |

## TotalChargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalChargeCount` | 总充电次数 | INT | R | x |

## TotalDischarE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalDischarE` | 累计放电量 | FLOAT | R | kWh |

## TotalDischarTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalDischarTime` | 总放电时长 | INT | R | h |

## TotalDischargeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalDischargeCount` | 总放电次数 | INT | R | x |

## UBusNgt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UBusNgt` | 负母线电压 | FLOAT | R | V |

## UBusPst* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UBusPst` | 正母线电压 | FLOAT | R | V |

## Uab* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Uab` | AB线电压 | FLOAT | R | V |

## Ubc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ubc` | BC线电压 | FLOAT | R | V |

## Uca* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Uca` | CA线电压 | FLOAT | R | V |

## 关联

- [[pcs]]
- [[thing-model-structure]]
