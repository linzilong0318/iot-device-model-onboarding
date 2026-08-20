---
title: 三相组串逆变器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, energy-storage, photovoltaic]
sources: [raw/papers/public_StringInverter_3P.md]
confidence: high
---
# 三相组串逆变器

## 概述

三相组串逆变器 (String Inverter - Three Phase),物模型无版本后缀,储能域。属性含 MPPT 路数、额定电压/频率/功率;179 个测点以故障/告警/MPPT/PV 组串状态为主;65 个事件含 12 路 PV 电弧(PV1Arc~PV12Arc)与 AFCI 相关、电网/母线/绝缘/GFCI/通信/温度等;8 个服务:电弧检测与复位、MPPT 扫描、强制重启、出厂复位、开关机。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_StringInverter_3P` |
| 中文名 | 三相组串逆变器 |
| 英文名 | String Inverter - Three Phase |
| 设备大类 | NORMAL |
| 业务域 | electricityStorage |
| 来源 | raw/papers/public_StringInverter_3P.md |

## 属性 (Attribute) — 12 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `MPPTNumber` | MPPT路数 | INT |  | False |
| `RatedU` | 额定电压 | FLOAT | V | False |
| `RatedFreq` | 额定频率 | FLOAT | Hz | False |
| `RatedP` | 额定有功功率 | FLOAT | V | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 179 个

测点数量超过 100,完整清单见 [[string-inverter-3p-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Err | 55 |
| MPPT | 16 |
| Sta | 14 |
| PV | 12 |
| Ala | 11 |
| SwitchOn | 1 |
| SwitchOff | 1 |
| FactoryReset | 1 |
| ForceReboot | 1 |
| MPPTScan | 1 |
| ARCCheck | 1 |
| ARCClearError | 1 |
| ARCCheckEn | 1 |
| PVInPt | 1 |
| DCIA | 1 |
| DCIB | 1 |
| DCIC | 1 |
| GFCI | 1 |
| UBusPst | 1 |
| UBusNgt | 1 |
| UBusPstNgt | 1 |
| CntDwPwrOn | 1 |
| GridUa | 1 |
| GridUb | 1 |
| GridUc | 1 |
| GridUab | 1 |
| GridUbc | 1 |
| GridUca | 1 |
| GridFreqa | 1 |
| GridFreqb | 1 |
| GridFreqc | 1 |
| GridFreq | 1 |
| GridTHDUa | 1 |
| GridTHDUb | 1 |
| GridTHDUc | 1 |
| GridTHDIa | 1 |
| GridTHDIb | 1 |
| GridTHDIc | 1 |
| GridUUnB | 1 |
| GridPhaSeq | 1 |
| GridNPEVoltage | 1 |
| InvertOutUa | 1 |
| InvertOutIa | 1 |
| InvertOutPa | 1 |
| InvertOutQa | 1 |
| InvertOutFreqa | 1 |
| InvertOutUb | 1 |
| InvertOutIb | 1 |
| InvertOutPb | 1 |
| InvertOutQb | 1 |
| InvertOutFreqb | 1 |
| InvertOutUc | 1 |
| InvertOutIc | 1 |
| InvertOutPc | 1 |
| InvertOutQc | 1 |
| InvertOutFreqc | 1 |
| InvertOutPFa | 1 |
| InvertOutPFb | 1 |
| InvertOutPFc | 1 |
| InvertOutPFt | 1 |
| InvertOutPt | 1 |
| InvertOutQt | 1 |
| InvertOutSt | 1 |
| DayInvertOutPPeak | 1 |
| DayPVE | 1 |
| TotalPVE | 1 |
| InvertEffi | 1 |
| ISO | 1 |
| InTemp | 1 |
| CaseTemp | 1 |
| HeatSinkTemp | 1 |
| RelayTemp | 1 |
| CommInductorTemp | 1 |
| InvertATemp | 1 |
| InvertBTemp | 1 |
| InvertCTemp | 1 |

## 事件 (Event) — 65 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmCTComm` | CT板通讯异常告警 | ALARM |
| `ErrorGridOverFreq` | 电网过频故障 | FAULT |
| `AlarmTempSensor` | 温度传感器告警 | ALARM |
| `AlarmInputSPD` | 输入SPD故障 | ALARM |
| `AlarmEeprom` | EEPROM读写故障 | ALARM |
| `AlarmInComm` | 内部通讯失败告警 | ALARM |
| `AlarmInFan` | 内部风扇告警 | ALARM |
| `ErrorGridUnderFreq` | 电网欠频故障 | FAULT |
| `AlarmPIDCtrlComm` | PID与控制板通讯异常告警 | ALARM |
| `AlarmOutFan` | 外部风扇告警 | ALARM |
| `AlarmSVGVoltStab` | SVG电压稳定性告警 | ALARM |
| `AlarmPIDVoltStab` | PID电压稳定性告警 | ALARM |
| `ErrorInvOutIOffset` | 逆变电流偏置异常故障 | FAULT |
| `ErrorOverTemp` | 温度越限故障 | FAULT |
| `ErrorRelay` | 并网继电器故障 | FAULT |
| `ErrorGridPhaseLoss` | 电网断相故障 | FAULT |
| `ErrorWholeBusFall` | 整母线跌路故障 | FAULT |
| `ErrorOverBoostCur` | Boost电路过流故障 | FAULT |
| `ErrorBusShortCir` | 母线短路故障 | FAULT |
| `ErrorResonance` | 谐振故障 | FAULT |
| `ErrorInvOutOverI` | 逆变输出过流故障 | FAULT |
| `ErrorIsland` | 孤岛故障 | FAULT |
| `ErrorOverBusUDiff` | 母线电压差过高故障 | FAULT |
| `ErrorGridInvUDiff` | 电网和逆变器电压差过压故障 | FAULT |
| `ErrorOverBusU` | 母线过压故障 | FAULT |
| `ErrorGFCISensor` | 漏电流传感器故障 | FAULT |
| `ErrorGridUUnB` | 电网电压不平衡故障 | FAULT |
| `ErrorMCU` | MCU故障 | FAULT |
| `ErrorDCSInducOverI` | 直流小电感过流故障 | FAULT |
| `ErrorGFCIDynamic` | 动态漏电流过流故障 | FAULT |
| `ErrorIsolation` | 绝缘阻抗过低故障 | FAULT |
| `ErrorDCIHigh` | 逆变电流直流分量越限故障 | FAULT |
| `ErrorDCIOffset` | 逆变电流直流分量偏置保护 | FAULT |
| `ErrorPVCrashVolt` | PV起机电压异常故障 | FAULT |
| `ErrorPVVoltSample` | PV电压采样故障 | FAULT |
| `ErrorVNPE` | VNPE相地过压故障 | FAULT |
| `Error12VPowerSource` | 12V电源故障 | FAULT |
| `ErrorCANComm` | CAN通讯故障 | FAULT |
| `ErrorARCBoard` | ARC板故障 | FAULT |
| `ErrorARCSelfCheck` | ARC板自检故障 | FAULT |
| `ErrorGridTHDU` | 电网电压谐波过高故障 | FAULT |
| `ErrorInSelfDiagn` | 内部自我诊断故障 | FAULT |
| `ErrorPassiveIsland` | 被动孤岛故障 | FAULT |
| `ErrorMPPTReverse` | MPPT反接故障 | FAULT |
| `ErrorMPPTOverU` | MPPT过压故障 | FAULT |
| `ErrorPVLink` | PV连接异常故障 | FAULT |
| `ErrorOperaOverU` | 操作过电压故障 | FAULT |
| `ErrorGridOverLineU` | 电网线电压过压故障 | FAULT |
| `ErrorGridOverPhaseU` | 电网相电压过压故障 | FAULT |
| `ErrorPVInvPDiff` | PV和逆变器功率差越限故障 | FAULT |
| `AlarmOutputSPD` | 输出SPD故障 | ALARM |
| `ErrorOpenLoopSelfChk` | 逆变开环自检异常故障 | FAULT |
| `ErrorGFCIStatic` | 静态漏电流过流故障 | FAULT |
| `ErrorPV1Arc` | 第1路PV拉弧保护 | FAULT |
| `ErrorPV2Arc` | 第2路PV拉弧保护 | FAULT |
| `ErrorPV3Arc` | 第3路PV拉弧保护 | FAULT |
| `ErrorPV4Arc` | 第4路PV拉弧保护 | FAULT |
| `ErrorPV5Arc` | 第5路PV拉弧保护 | FAULT |
| `ErrorPV6Arc` | 第6路PV拉弧保护 | FAULT |
| `ErrorPV7Arc` | 第7路PV拉弧保护 | FAULT |
| `ErrorPV8Arc` | 第8路PV拉弧保护 | FAULT |
| `ErrorPV9Arc` | 第9路PV拉弧保护 | FAULT |
| `ErrorPV10Arc` | 第10路PV拉弧保护 | FAULT |
| `ErrorPV11Arc` | 第11路PV拉弧保护 | FAULT |
| `ErrorPV12Arc` | 第12路PV拉弧保护 | FAULT |

## 服务 (Service) — 8 个

| 标识符 | 名称 |
| --- | --- |
| `ARCCheckCmd` | ARC检测 |
| `ARCCheckEnCmd` | ARC检测使能 |
| `ARCClearErrorCmd` | ARC故障清除 |
| `FactoryResetCmd` | 恢复出厂设置 |
| `ForceRebootCmd` | 强制重启 |
| `MPPTScanCmd` | MPPT扫描 |
| `SwitchOffCmd` | 关机 |
| `SwitchOnCmd` | 开机 |

## 关联

- [[mix-inverter-1p]]
- [[pcs]]
- [[pv-optimizer]]
- [[string-inverter-3p-measure-points]]
- [[thing-model-structure]]
- [[inverter-family]]
