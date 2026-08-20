---
title: 三相组串逆变器 — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, energy-storage]
sources: [raw/papers/public_StringInverter_3P.md]
confidence: high
---
# 三相组串逆变器 — 测点全集

> 实体页 [[string-inverter-3p]] 的测点参考,共 179 个测点。按命名前缀分组。

## ARCCheck* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ARCCheck` | ARC检测 | INT | RW |  |

## ARCCheckEn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ARCCheckEn` | ARC检测使能 | INT | RW |  |

## ARCClearError* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ARCClearError` | ARC故障清除 | INT | RW |  |

## Ala* — 11 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_OutputSPD` | 输出SPD故障 | ENUM | R |  |
| `Ala_TempSensor` | 温度传感器告警 | ENUM | R |  |
| `Ala_InputSPD` | 输入SPD故障 | ENUM | R |  |
| `Ala_Eeprom` | EEPROM读写故障 | ENUM | R |  |
| `Ala_InComm` | 内部通讯失败告警 | ENUM | R |  |
| `Ala_InFan` | 内部风扇告警 | ENUM | R |  |
| `Ala_OutFan` | 外部风扇告警 | ENUM | R |  |
| `Ala_PIDCtrlComm` | PID与控制板通讯异常告警 | ENUM | R |  |
| `Ala_CTComm` | CT板通讯异常告警 | ENUM | R |  |
| `Ala_SVGVoltStab` | SVG电压稳定性告警 | ENUM | R |  |
| `Ala_PIDVoltStab` | PID电压稳定性告警 | ENUM | R |  |

## CaseTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CaseTemp` | 机箱温度 | FLOAT | R | °C |

## CntDwPwrOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CntDwPwrOn` | 开机倒计时 | INT | R | s |

## CommInductorTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CommInductorTemp` | 共模电感温度 | FLOAT | R | °C |

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

## DayInvertOutPPeak* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayInvertOutPPeak` | 当日逆变输出最大功率 | FLOAT | R | kW |

## DayPVE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayPVE` | 当日PV发电量 | FLOAT | R | kWh |

## Err* — 55 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Err_PV1Arc` | 第1路PV拉弧保护 | ENUM | R |  |
| `Err_PV2Arc` | 第2路PV拉弧保护 | ENUM | R |  |
| `Err_PV3Arc` | 第3路PV拉弧保护 | ENUM | R |  |
| `Err_PV4Arc` | 第4路PV拉弧保护 | ENUM | R |  |
| `Err_PV5Arc` | 第5路PV拉弧保护 | ENUM | R |  |
| `Err_PV6Arc` | 第6路PV拉弧保护 | ENUM | R |  |
| `Err_PV7Arc` | 第7路PV拉弧保护 | ENUM | R |  |
| `Err_PV8Arc` | 第8路PV拉弧保护 | ENUM | R |  |
| `Err_PV9Arc` | 第9路PV拉弧保护 | ENUM | R |  |
| `Err_PV10Arc` | 第10路PV拉弧保护 | ENUM | R |  |
| `Err_PV11Arc` | 第11路PV拉弧保护 | ENUM | R |  |
| `Err_PV12Arc` | 第12路PV拉弧保护 | ENUM | R |  |
| `Err_OverBoostCur` | Boost电路过流故障 | ENUM | R |  |
| `Err_BusShortCir` | 母线短路故障 | ENUM | R |  |
| `Err_WholeBusFall` | 整母线跌路故障 | ENUM | R |  |
| `Err_PassiveIsland` | 被动孤岛故障 | ENUM | R |  |
| `Err_GridPhaseU` | 电网相电压故障 | ENUM | R |  |
| `Err_GridLineU` | 电网线电压故障 | ENUM | R |  |
| `Err_Time` | 近一次故障事件时间 | DATETIME | R |  |
| `Err_InvOutIOffset` | 逆变电流偏置异常故障 | ENUM | R |  |
| `Err_OverTemp` | 温度越限故障 | ENUM | R |  |
| `Err_Relay` | 并网继电器故障 | ENUM | R |  |
| `Err_GridPhaseLoss` | 电网断相故障 | ENUM | R |  |
| `Err_GridUnderFreq` | 电网欠频故障 | ENUM | R |  |
| `Err_GridOverFreq` | 电网过频故障 | ENUM | R |  |
| `Err_InvOutOverI` | 逆变输出过流故障 | ENUM | R |  |
| `Err_Island` | 孤岛故障 | ENUM | R |  |
| `Err_OverBusUDiff` | 母线电压差过高故障 | ENUM | R |  |
| `Err_GridInvUDiff` | 电网和逆变器电压差过压故障 | ENUM | R |  |
| `Err_OverBusU` | 母线过压故障 | ENUM | R |  |
| `Err_GFCISensor` | 漏电流传感器故障 | ENUM | R |  |
| `Err_GridUUnB` | 电网电压不平衡故障 | ENUM | R |  |
| `Err_MCU` | MCU故障 | ENUM | R |  |
| `Err_DCSInducOverI` | 直流小电感过流故障 | ENUM | R |  |
| `Err_GFCIDynamic` | 动态漏电流过流故障 | ENUM | R |  |
| `Err_Isolation` | 绝缘阻抗过低故障 | ENUM | R |  |
| `Err_DCIHigh` | 逆变电流直流分量越限故障 | ENUM | R |  |
| `Err_DCIOffset` | 逆变电流直流分量偏置保护 | ENUM | R |  |
| `Err_OperaOverU` | 操作过电压故障 | ENUM | R |  |
| `Err_Resonance` | 谐振故障 | ENUM | R |  |
| `Err_OpenLoopSelfChk` | 逆变开环自检异常故障 | ENUM | R |  |
| `Err_PVLink` | PV连接异常故障 | ENUM | R |  |
| `Err_MPPTOverU` | MPPT过压故障 | ENUM | R |  |
| `Err_MPPTReverse` | MPPT反接故障 | ENUM | R |  |
| `Err_PVInvPDiff` | PV和逆变器功率差越限故障 | ENUM | R |  |
| `Err_InSelfDiagn` | 内部自我诊断故障 | ENUM | R |  |
| `Err_GridTHDU` | 电网电压谐波过高故障 | ENUM | R |  |
| `Err_ARCSelfCheck` | ARC板自检故障 | ENUM | R |  |
| `Err_ARCBoard` | ARC板故障 | ENUM | R |  |
| `Err_CANComm` | CAN通讯故障 | ENUM | R |  |
| `Err_12VPowerSource` | 12V电源故障 | ENUM | R |  |
| `Err_VNPE` | VNPE相地过压故障 | ENUM | R |  |
| `Err_PVVoltSample` | PV电压采样故障 | ENUM | R |  |
| `Err_PVCrashVolt` | PV起机电压异常故障 | ENUM | R |  |
| `Err_GFCIStatic` | 静态漏电流过流故障 | ENUM | R |  |

## FactoryReset* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FactoryReset` | 恢复出厂设置 | INT | RW |  |

## ForceReboot* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ForceReboot` | 强制重启 | INT | RW |  |

## GFCI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GFCI` | 漏电流侦测值 | FLOAT | R | mA |

## GridFreq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreq` | 电网频率 | FLOAT | R | Hz |

## GridFreqa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreqa` | 电网A相频率 | FLOAT | R | Hz |

## GridFreqb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreqb` | 电网B相频率 | FLOAT | R | Hz |

## GridFreqc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridFreqc` | 电网C相频率 | FLOAT | R | Hz |

## GridNPEVoltage* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridNPEVoltage` | 电网N线与接地线之间的电压 | FLOAT | R | V |

## GridPhaSeq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridPhaSeq` | 电网相序 | ENUM | R |  |

## GridTHDIa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDIa` | 电网A相电流总谐波畸变率 | FLOAT | R | % |

## GridTHDIb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDIb` | 电网B相电流总谐波畸变率 | FLOAT | R | % |

## GridTHDIc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDIc` | 电网C相电流总谐波畸变率 | FLOAT | R | % |

## GridTHDUa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDUa` | 电网A相电压总谐波畸变率 | FLOAT | R | % |

## GridTHDUb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDUb` | 电网B相电压总谐波畸变率 | FLOAT | R | % |

## GridTHDUc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridTHDUc` | 电网C相电压总谐波畸变率 | FLOAT | R | % |

## GridUUnB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUUnB` | 电压不平衡度 | FLOAT | R | % |

## GridUa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUa` | 电网A相电压 | FLOAT | R | V |

## GridUab* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUab` | 电网AB线电压 | FLOAT | R | V |

## GridUb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUb` | 电网B相电压 | FLOAT | R | V |

## GridUbc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUbc` | 电网BC线电压 | FLOAT | R | V |

## GridUc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUc` | 电网C相电压 | FLOAT | R | V |

## GridUca* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `GridUca` | 电网CA线电压 | FLOAT | R | V |

## HeatSinkTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `HeatSinkTemp` | 散热器温度 | FLOAT | R | °C |

## ISO* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ISO` | 绝缘阻抗侦测值 | FLOAT | R | kΩ |

## InTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InTemp` | 机内温度 | FLOAT | R | °C |

## InvertATemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertATemp` | A相逆变模块温度 | FLOAT | R | °C |

## InvertBTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertBTemp` | B相逆变模块温度 | FLOAT | R | °C |

## InvertCTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertCTemp` | C相逆变模块温度 | FLOAT | R | °C |

## InvertEffi* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertEffi` | 逆变效率 | FLOAT | R | % |

## InvertOutFreqa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutFreqa` | 逆变输出A相频率 | FLOAT | R | Hz |

## InvertOutFreqb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutFreqb` | 逆变输出B相频率 | FLOAT | R | Hz |

## InvertOutFreqc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutFreqc` | 逆变输出C相频率 | FLOAT | R | Hz |

## InvertOutIa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutIa` | 逆变输出A相电流 | FLOAT | R | A |

## InvertOutIb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutIb` | 逆变输出B相电流 | FLOAT | R | A |

## InvertOutIc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutIc` | 逆变输出C相电流 | FLOAT | R | A |

## InvertOutPFa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPFa` | 逆变输出A相功率因数 | FLOAT | R |  |

## InvertOutPFb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPFb` | 逆变输出B相功率因数 | FLOAT | R |  |

## InvertOutPFc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPFc` | 逆变输出C相功率因数 | FLOAT | R |  |

## InvertOutPFt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPFt` | 逆变输出总功率因数 | FLOAT | R |  |

## InvertOutPa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPa` | 逆变输出A相有功功率 | FLOAT | R | kW |

## InvertOutPb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPb` | 逆变输出B相有功功率 | FLOAT | R | kW |

## InvertOutPc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPc` | 逆变输出C相有功功率 | FLOAT | R | kW |

## InvertOutPt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutPt` | 逆变输出总有功功率 | FLOAT | R | kW |

## InvertOutQa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQa` | 逆变输出A相无功功率 | FLOAT | R | kvar |

## InvertOutQb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQb` | 逆变输出B相无功功率 | FLOAT | R | kvar |

## InvertOutQc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQc` | 逆变输出C相无功功率 | FLOAT | R | kvar |

## InvertOutQt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutQt` | 逆变输出总无功功率 | FLOAT | R | kvar |

## InvertOutSt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutSt` | 逆变输出总视在功率 | FLOAT | R | kVA |

## InvertOutUa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutUa` | 逆变输出A相电压 | FLOAT | R | V |

## InvertOutUb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutUb` | 逆变输出B相电压 | FLOAT | R | V |

## InvertOutUc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `InvertOutUc` | 逆变输出C相电压 | FLOAT | R | V |

## MPPT* — 16 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MPPT1U` | MPPT1电压 | FLOAT | R | V |
| `MPPT2U` | MPPT2电压 | FLOAT | R | V |
| `MPPT3U` | MPPT3电压 | FLOAT | R | V |
| `MPPT4U` | MPPT4电压 | FLOAT | R | V |
| `MPPT5U` | MPPT5电压 | FLOAT | R | V |
| `MPPT6U` | MPPT6电压 | FLOAT | R | V |
| `MPPT7U` | MPPT7电压 | FLOAT | R | V |
| `MPPT8U` | MPPT8电压 | FLOAT | R | V |
| `MPPT1I` | MPPT1电流 | FLOAT | R | A |
| `MPPT2I` | MPPT2电流 | FLOAT | R | A |
| `MPPT3I` | MPPT3电流 | FLOAT | R | A |
| `MPPT4I` | MPPT4电流 | FLOAT | R | A |
| `MPPT5I` | MPPT5电流 | FLOAT | R | A |
| `MPPT6I` | MPPT6电流 | FLOAT | R | A |
| `MPPT7I` | MPPT7电流 | FLOAT | R | A |
| `MPPT8I` | MPPT8电流 | FLOAT | R | A |

## MPPTScan* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MPPTScan` | MPPT扫描 | INT | RW |  |

## PV* — 12 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PV1Temp` | PV1温度 | FLOAT | R | °C |
| `PV2Temp` | PV2温度 | FLOAT | R | °C |
| `PV3Temp` | PV3温度 | FLOAT | R | °C |
| `PV4Temp` | PV4温度 | FLOAT | R | °C |
| `PV1InU` | PV1输入电压 | FLOAT | R | V |
| `PV1InI` | PV1输入电流 | FLOAT | R | A |
| `PV2InU` | PV2输入电压 | FLOAT | R | V |
| `PV2InI` | PV2输入电流 | FLOAT | R | A |
| `PV3InU` | PV3输入电压 | FLOAT | R | V |
| `PV3InI` | PV3输入电流 | FLOAT | R | A |
| `PV4InU` | PV4输入电压 | FLOAT | R | V |
| `PV4InI` | PV4输入电流 | FLOAT | R | A |

## PVInPt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PVInPt` | PV输入总功率 | FLOAT | R | W |

## RelayTemp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RelayTemp` | 继电器温度 | FLOAT | R | °C |

## Sta* — 14 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_Device` | 设备状态 | ENUM | R |  |
| `Sta_Grid` | 电网状态 | ENUM | R |  |
| `Sta_SelfCheck` | 自检 | ENUM | R |  |
| `Sta_Standby` | 待机 | ENUM | R |  |
| `Sta_Run` | 运行 | ENUM | R |  |
| `Sta_SVGRun` | SVG运行模式 | ENUM | R |  |
| `Sta_PVPSelfCheck` | PV开机功率自检中 | ENUM | R |  |
| `Sta_PVUnderVoltage` | PV电压低不能开机 | ENUM | R |  |
| `Sta_GridNGnd` | 电网N线接地状态 | ENUM | R |  |
| `Sta_InvertRun` | 并网发电 | ENUM | R |  |
| `Sta_Error` | 故障 | ENUM | R |  |
| `Sta_PVOverVoltage` | PV电压高不能开机 | ENUM | R |  |
| `Sta_UnderTemp` | 温度低不能开机 | ENUM | R |  |
| `Sta_UnderRatedP` | 降额运行 | ENUM | R |  |

## SwitchOff* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SwitchOff` | 关机 | INT | RW |  |

## SwitchOn* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SwitchOn` | 开机 | INT | RW |  |

## TotalPVE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalPVE` | 累计PV发电量 | FLOAT | R | kWh |

## UBusNgt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UBusNgt` | 负母线电压 | FLOAT | R | V |

## UBusPst* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UBusPst` | 正母线电压 | FLOAT | R | V |

## UBusPstNgt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UBusPstNgt` | 正负母线电压 | FLOAT | R | V |

## 关联

- [[string-inverter-3p]]
- [[thing-model-structure]]
