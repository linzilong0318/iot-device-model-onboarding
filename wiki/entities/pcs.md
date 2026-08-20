---
title: 储能变流器(PCS)
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, energy-storage]
sources: [raw/papers/public_PCS.md]
confidence: high
---
# 储能变流器(PCS)

## 概述

储能变流器 (Energy Storage Converter, PCS),储能域。属性含电池类型、电池容量、额定功率、额定充/放电功率等;175 个测点以故障/告警/状态为主;65 个事件覆盖隔离、GFCI、直流分量、孤岛、母线、电网、电池、温度、继电器等;41 个服务为储能域最全:远程有功/无功/电压/电流设定(CS 与 VS 模式)、削峰填谷调度 (CPS*)、电池开关与预充、快速放电、复位等。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_PCS` |
| 中文名 | 储能变流器(PCS) |
| 英文名 | Energy Storage Converter |
| 设备大类 | NORMAL |
| 业务域 | electricityStorage |
| 来源 | raw/papers/public_PCS.md |

## 属性 (Attribute) — 12 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `BatteryType` | 电池类型 | STRING |  | False |
| `BatteryCapacity` | 电池容量 | FLOAT | kWh | False |
| `RatedFreq` | 额定频率 | FLOAT | Hz | False |
| `RatedVoltage` | 额定电压 | FLOAT | V | False |
| `RatedPower` | 额定功率 | FLOAT | kW | False |
| `RatedChargeP` | 额定充电功率 | FLOAT | kW | False |
| `RatedDischargeP` | 额定放电功率 | FLOAT | kW | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 175 个

测点数量超过 100,完整清单见 [[pcs-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Err | 57 |
| Sta | 13 |
| Ala | 9 |
| CPSEn | 1 |
| PCSSwitchOn | 1 |
| PCSSwitchOff | 1 |
| FactoryReset | 1 |
| ForceReboot | 1 |
| AutoTest | 1 |
| ManualClearError | 1 |
| PCSConnect | 1 |
| PCSDisconnect | 1 |
| RapidDischarge | 1 |
| SetMaxSOC | 1 |
| SetMinSOC | 1 |
| RemoteSwitchVS | 1 |
| RemoteVsEn | 1 |
| SetRemoVsFreq | 1 |
| SetRemoVSU | 1 |
| SetRemoVSP | 1 |
| SetRemoVSQ | 1 |
| RemoteSwitchCS | 1 |
| RemoteCSPCtrlEn | 1 |
| RemoteCSPCtrlMode | 1 |
| SetRemoCSP | 1 |
| SetRemoCSDCI | 1 |
| SetRemoCSQ | 1 |
| SetRemoCSPF | 1 |
| RemoteCSQCtrlEn | 1 |
| RemoteCSQCtrlMode | 1 |
| BattPreChargeEn | 1 |
| SetRemoCharULim | 1 |
| SetRemoDischarULim | 1 |
| SetRemoCharILim | 1 |
| SetRemoDischarILim | 1 |
| SetRemoFloatCharULim | 1 |
| SetRemoFloatCharILim | 1 |
| SetCPSStartTimeT | 1 |
| SetCPSDeadlineT | 1 |
| SetCPSPT | 1 |
| CPST | 1 |
| AntiRevFlowEn | 1 |
| SOC | 1 |
| SOH | 1 |
| BatteryU | 1 |
| BatteryI | 1 |
| BatteryP | 1 |
| BattCharCurLim | 1 |
| BattDischarCurLim | 1 |
| MaxBattStackU | 1 |
| MinBattStackU | 1 |
| MaxBattStackTemp | 1 |
| MinBattStackTemp | 1 |
| CharERemain | 1 |
| DischarERemain | 1 |
| TotalChargeCount | 1 |
| TotalDischargeCount | 1 |
| DayChargeCount | 1 |
| DayDischargeCount | 1 |
| DayCharE | 1 |
| TotalCharE | 1 |
| DayDischarE | 1 |
| TotalDischarE | 1 |
| DayCharTime | 1 |
| TotalCharTime | 1 |
| DayDischarTime | 1 |
| TotalDischarTime | 1 |
| Ia | 1 |
| Ib | 1 |
| Ic | 1 |
| GridFreq | 1 |
| Uab | 1 |
| Ubc | 1 |
| Uca | 1 |
| GridUUnB | 1 |
| GridPhaSeq | 1 |
| InvertModuleTemp | 1 |
| AmbientTemp | 1 |
| BoostTemp | 1 |
| OutBoardTemp | 1 |
| PowerBoardTemp | 1 |
| GFCIRms | 1 |
| GFCIAvg | 1 |
| ISO | 1 |
| UBusPst | 1 |
| UBusNgt | 1 |
| DCVoltage | 1 |
| DCCurrent | 1 |
| S | 1 |
| DCInP | 1 |
| InvertOutP | 1 |
| InvertOutQ | 1 |
| DCIA | 1 |
| DCIB | 1 |
| DCIC | 1 |
| Efficiency | 1 |
| PF | 1 |
| BattSwitchOn | 1 |
| BattSwitchOff | 1 |

## 事件 (Event) — 65 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorIsolation` | 绝缘阻抗过低故障 | FAULT |
| `ErrorGFCIDynamic` | 动态漏电流过流故障 | FAULT |
| `AlarmACSPD` | 交流避雷器异常 | ALARM |
| `ErrorDCIHigh` | 逆变电流直流分量越限故障 | FAULT |
| `ErrorDCIOffset` | 逆变电流直流分量偏置保护 | FAULT |
| `ErrorOpenLoopSelfChk` | 开环自检异常故障 | FAULT |
| `ErrorCANComm` | CAN通讯故障 | FAULT |
| `ErrorGFCIStatic` | 静态漏电流过流故障 | FAULT |
| `ErrorOverBoostCur` | Boost电路过流故障 | FAULT |
| `ErrorIsland` | 孤岛故障 | FAULT |
| `AlarmTempSensor` | 温度传感器告警 | ALARM |
| `AlarmSPD` | 避雷器异常 | ALARM |
| `AlarmEeprom` | EEPROM读写故障 | ALARM |
| `AlarmInComm` | 内部通讯失败告警 | ALARM |
| `AlarmInFan` | 内部风扇告警 | ALARM |
| `AlarmOutFan` | 外部风扇告警 | ALARM |
| `ErrorMCU` | MCU故障 | FAULT |
| `ErrorBattIOffset` | 电池电流偏置故障 | FAULT |
| `ErrorGridUUnB` | 电网电压不平衡故障 | FAULT |
| `ErrorGFCISensor` | 漏电流传感器故障 | FAULT |
| `ErrorOverBusU` | 母线过压故障 | FAULT |
| `ErrorPassiveIsland` | 被动孤岛故障 | FAULT |
| `ErrorGridTHDU` | 电网电压谐波过高故障 | FAULT |
| `ErrorGridPhaseU` | 电网相电压故障 | FAULT |
| `ErrorInvOutOverI` | 逆变输出过流故障 | FAULT |
| `ErrorGridOverFreq` | 电网过频故障 | FAULT |
| `ErrorGridUnderFreq` | 电网欠频故障 | FAULT |
| `ErrorGridPhaseLoss` | 电网断相故障 | FAULT |
| `ErrorRelay` | 并网继电器故障 | FAULT |
| `ErrorOverTemp` | 温度越限故障 | FAULT |
| `ErrorInvOutIOffset` | 逆变电流偏置异常故障 | FAULT |
| `ErrorGridLineU` | 电网线电压故障 | FAULT |
| `AlarmDCPWMShut` | 直流封锁 | ALARM |
| `ErrorROCOF` | ROCOF故障 | FAULT |
| `ErrorHalfBusUUnB` | 半母线电压不平衡 | FAULT |
| `ErrorOverHalfBusU` | 半母线电压高 | FAULT |
| `ErrorInvPWMShut` | 逆变封锁保护 | FAULT |
| `ErrorOverCapCur` | 滤波电容电流越限故障 | FAULT |
| `ErrorDCRelay` | 直流继电器故障 | FAULT |
| `ErrorBusBattUDiff` | 母线和电池电压差过大 | FAULT |
| `ErrorBattPara` | 电池参数设置错误 | FAULT |
| `ErrorTempSensor` | 温度传感器故障 | FAULT |
| `ErrorOnOffGridPara` | 并离网参数不匹配 | FAULT |
| `ErrorBattInputRevCon` | 电池输入反接故障 | FAULT |
| `ErrorInvHWOverI` | 逆变硬件过流故障 | FAULT |
| `ErrorGridInvUDiff` | 网侧逆变侧电压不一致故障 | FAULT |
| `ErrorNoBusU` | 母线无电压故障 | FAULT |
| `ErrorOverBattU` | 电池电压过高故障 | FAULT |
| `ErrorDCChargeCir` | 直流侧充电回路异常 | FAULT |
| `ErrorOverGridLineU` | 电网线电压瞬时值越限故障 | FAULT |
| `AlarmDCIUmB` | 直流电流不平衡 | ALARM |
| `ErrorUnderBattU` | 电池欠压故障 | FAULT |
| `ErrorOverDCI` | 直流侧过流故障 | FAULT |
| `ErrorGFCICurOffset` | 漏电流偏置故障 | FAULT |
| `ErrorLoadCur` | 负载电流偏置故障 | FAULT |
| `ErrorJETIsland` | JET孤岛频率异常 | FAULT |
| `ErrorCPLDOscil` | CPLD晶振失效故障 | FAULT |
| `ErrorOverGridUPeak` | 电网电压峰值越限故障 | FAULT |
| `ErrorEmergCloase` | 紧急按钮闭合 | FAULT |
| `ErrorVNPE` | NPE电压差越限故障 | FAULT |
| `ErrorInvRelay` | 逆变继电器故障 | FAULT |
| `ErrorDCVUOffset` | DCV电压偏置故障 | FAULT |
| `ErrorRapidDischarge` | 快速放电动作 | FAULT |
| `ErrorGridBreaker` | 电网外部断路器故障 | FAULT |
| `ErrorLoadPF` | 负载功率因数过低 | FAULT |

## 服务 (Service) — 41 个

| 标识符 | 名称 |
| --- | --- |
| `RemoteCSPCtrlModeCmd` | 远程CS有功控制模式 |
| `RemoCharULimSet` | 远程设置充电电压限值 |
| `RemoCSDCISet` | 远程设置CS直流电流 |
| `RemoCSPFSet` | 远程设置CS功率因数 |
| `RemoCSPSet` | 远程设置CS有功功率 |
| `RemoCSQSet` | 远程设置CS无功功率 |
| `RemoDischarILimSet` | 远程设置放电电流限值 |
| `RemoDischarULimSet` | 远程设置放电电压限值 |
| `RemoFloatCharILimSet` | 远程设置浮充电流限值 |
| `RemoFloatCharULimSet` | 远程设置浮充电压限值 |
| `RemoteCSPCtrlEnCmd` | 远程CS有功控制使能 |
| `RemoCharILimSet` | 远程设置充电电流限值 |
| `RemoteCSQCtrlEnCmd` | 远程CS无功控制使能 |
| `RemoteCSQCtrlModeCmd` | 远程CS无功控制模式 |
| `RemoteSwitchCSCmd` | 远程选择CS模式 |
| `RemoteSwitchVSCmd` | 远程选择VS模式 |
| `RemoteVsEnCmd` | 远程VS模式使能 |
| `RemoVsFreqSet` | 远程设置VS频率 |
| `RemoVSPSet` | 远程设置VS有功功率 |
| `RemoVSQSet` | 远程设置VS无功功率 |
| `RemoVSUSet` | 远程设置VS电压 |
| `FactoryResetCmd` | 恢复出厂设置 |
| `AutoTestCmd` | 自动测试 |
| `BattPreChargeEn` | 电池预充电使能 |
| `BattSwitchOffCmd` | 电池关机 |
| `BattSwitchOnCmd` | 电池开机 |
| `CPSDeadlineT1Set` | 设置削峰填谷时间段1截止时间 |
| `CPSEnCmd` | CPS使能 |
| `CPSPT1Set` | 削峰填谷时间段1功率值 |
| `CPSStartTimeT1Set` | 设置削峰填谷时间段1起始时间 |
| `CPST1EnCmd` | 削峰填谷时间段1使能状态 |
| `AntiRevFlowEnCmd` | 防逆流使能 |
| `ForceRebootCmd` | 强制重启 |
| `ManualClearErrorCmd` | 手动清除故障 |
| `MaxSOCSet` | 设置SOC上限 |
| `MinSOCSet` | 设置SOC下限 |
| `PCSConnectCmd` | PCS连接 |
| `PCSDisconnectCmd` | PCS断开 |
| `PCSSwitchOffCmd` | PCS关机 |
| `PCSSwitchOnCmd` | PCS开机 |
| `RapidDischargeCmd` | 快速放电 |

## 关联

- [[esmu]]
- [[mix-inverter-1p]]
- [[pcs-measure-points]]
- [[thing-model-structure]]
- [[inverter-family]]
