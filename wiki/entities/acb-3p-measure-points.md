---
title: (交流)框架断路器 — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, power-distribution]
sources: [raw/papers/public_ACB_3P_V1_0_2.md]
confidence: high
---
# (交流)框架断路器 — 测点全集

> 实体页 [[acb-3p]] 的测点参考,共 212 个测点。按命名前缀分组。

## Ala* — 37 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_TempCopBus` | 铜排温度越限告警 | ENUM | R |  |
| `Ala_HarmonicVolt` | 电压谐波告警 | ENUM | R |  |
| `Ala_HarmonicCur` | 电流谐波告警 | ENUM | R |  |
| `Ala_LifeTime` | 寿命超时告警 | ENUM | R |  |
| `Ala_RunOverTime` | 运行超时告警 | ENUM | R |  |
| `Ala_OverCurrent` | 过载告警 | ENUM | R |  |
| `Ala_SelfDiag` | 自诊断保护告警 | ENUM | R |  |
| `Ala_AntiIsLand` | 防孤岛告警 | ENUM | R |  |
| `Ala_GraResiI` | 缓变剩余电流越限告警 | ENUM | R |  |
| `Ala_SudResiI` | 突变剩余电流越限告警 | ENUM | R |  |
| `Ala_TempCtrl` | 控制器温度越限告警 | ENUM | R |  |
| `Ala_RHCtrl` | 控制器湿度越限告警 | ENUM | R |  |
| `Ala_TermTemp` | 接线端子温度越限告警 | ENUM | R |  |
| `Ala_PhaSeq` | 相序告警 | ENUM | R |  |
| `Ala_Gnd` | 接地告警 | ENUM | R |  |
| `Ala_RevPower` | 逆功率告警 | ENUM | R |  |
| `Ala_PhaseNLoss` | 断零告警 | ENUM | R |  |
| `Ala_IUnB` | 电流不平衡告警 | ENUM | R |  |
| `Ala_UUnB` | 电压不平衡告警 | ENUM | R |  |
| `Ala_OveCurLonDel` | 过载长延时告警 | ENUM | R |  |
| `Ala_UnderFreq` | 欠频告警 | ENUM | R |  |
| `Ala_OverFreq` | 过频告警 | ENUM | R |  |
| `Ala_PhaseLoss` | 断相告警 | ENUM | R |  |
| `Ala_UnderVol` | 欠压告警 | ENUM | R |  |
| `Ala_OverVol` | 过压告警 | ENUM | R |  |
| `Ala_Time` | 告警事件发生/恢复时间 | DATETIME | R |  |
| `Ala_Phase` | 告警事件相位 | ENUM | R |  |
| `Ala_CurDirec` | 告警事件前三相电流方向 | ENUM | R |  |
| `Ala_Ua` | 告警事件前A相电压 | FLOAT | R | V |
| `Ala_Ub` | 告警事件前B相电压 | FLOAT | R | V |
| `Ala_Uc` | 告警事件前C相电压 | FLOAT | R | V |
| `Ala_Ia` | 告警事件前A相电流 | FLOAT | R | A |
| `Ala_Ib` | 告警事件前B相电流 | FLOAT | R | A |
| `Ala_Ic` | 告警事件前C相电流 | FLOAT | R | A |
| `Ala_Uab` | 告警事件前AB线电压 | FLOAT | R | V |
| `Ala_Ubc` | 告警事件前BC线电压 | FLOAT | R | V |
| `Ala_Uca` | 告警事件前CA线电压 | FLOAT | R | V |

## AlarmEventCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AlarmEventCount` | 告警事件记录总数 | INT | R | x |

## AlarmIndicator* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AlarmIndicator` | 告警标志 | ENUM | R |  |

## AtmosPressure* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AtmosPressure` | 当前气压 | INT | R | atm |

## ClearContWear* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ClearContWear` | 触头磨损清除 | INT | W |  |

## ClearEnergyData* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ClearEnergyData` | 电能清除 | INT | W |  |

## ClearError* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ClearError` | 故障清除 | INT | W |  |

## ClearRecord* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ClearRecord` | 记录清除 | INT | W |  |

## Close* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Close` | 合闸 | INT | W |  |

## ComEP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEP` | 组合有功电能 | FLOAT | R | kWh |

## ComEQ* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEQ_C` | C相组合无功电能 | FLOAT | R | kvarh |
| `ComEQ_B` | B相组合无功电能 | FLOAT | R | kvarh |
| `ComEQ_A` | A相组合无功电能 | FLOAT | R | kvarh |
| `ComEQ` | 组合无功电能 | FLOAT | R | kvarh |

## ContactElecLife* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ContactElecLife` | 触头电气寿命 | INT | R | % |

## ContactHealIndex* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ContactHealIndex` | 健康度 | INT | R | % |

## ContactWear* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ContactWear` | 触头磨损度 | INT | R | % |

## EPE* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPE_C` | C相反向有功电能 | FLOAT | R | kWh |
| `EPE_B` | B相反向有功电能 | FLOAT | R | kWh |
| `EPE_A` | A相反向有功电能 | FLOAT | R | kWh |
| `EPE` | 反向有功电能 | FLOAT | R | kWh |

## EPI* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPI_C` | C相正向有功电能 | FLOAT | R | kWh |
| `EPI_B` | B相正向有功电能 | FLOAT | R | kWh |
| `EPI_A` | A相正向有功电能 | FLOAT | R | kWh |
| `EPI` | 正向有功电能 | FLOAT | R | kWh |

## EPt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPt` | 总有功电能 | FLOAT | R | kWh |

## EQE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQE` | 反向无功电能 | FLOAT | R | kvarh |

## EQI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQI` | 正向无功电能 | FLOAT | R | kvarh |

## EQt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQt` | 总无功电能 | FLOAT | R | kvarh |

## ESE* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ESE_C` | C相反向视在电能 | FLOAT | R | kVAh |
| `ESE_B` | B相反向视在电能 | FLOAT | R | kVAh |
| `ESE_A` | A相反向视在电能 | FLOAT | R | kVAh |
| `ESE` | 反向视在电能 | FLOAT | R | kVAh |

## ESI* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ESI_C` | C相正向视在电能 | FLOAT | R | kVAh |
| `ESI_B` | B相正向视在电能 | FLOAT | R | kVAh |
| `ESI_A` | A相正向视在电能 | FLOAT | R | kVAh |
| `ESI` | 正向视在电能 | FLOAT | R | kVAh |

## Err* — 36 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Err_Time` | 保护事件时间 | DATETIME | R |  |
| `Err_Phase` | 保护事件相位 | ENUM | R |  |
| `Err_OveCurLonDelay` | 过载长延时故障 | ENUM | R |  |
| `Err_ShoCirShoDelay` | 短路短延时故障 | ENUM | R |  |
| `Err_ShortCircuit` | 短路瞬时故障 | ENUM | R |  |
| `Err_OverFreq` | 过频故障 | ENUM | R |  |
| `Err_UnderVoltage` | 欠压故障 | ENUM | R |  |
| `Err_PhaseLoss` | 断相故障 | ENUM | R |  |
| `Err_UnderFreq` | 欠频故障 | ENUM | R |  |
| `Err_TempCopBus` | 铜排温度越限故障 | ENUM | R |  |
| `Err_SelfDiagProt` | 自诊断保护故障 | ENUM | R |  |
| `Err_HarmonicVolt` | 电压谐波故障 | ENUM | R |  |
| `Err_UUnB` | 电压不平衡故障 | ENUM | R |  |
| `Err_PhaseNLoss` | 断零故障 | ENUM | R |  |
| `Err_IUnB` | 电流不平衡故障 | ENUM | R |  |
| `Err_RevPower` | 逆功率故障 | ENUM | R |  |
| `Err_RHCtrl` | 控制器湿度越限故障 | ENUM | R |  |
| `Err_TermTemp` | 接线端子温度越限故障 | ENUM | R |  |
| `Err_GraResiI` | 缓变剩余电流越限故障 | ENUM | R |  |
| `Err_TempCtrl` | 控制器温度越限故障 | ENUM | R |  |
| `Err_SudResiI` | 突变剩余电流越限故障 | ENUM | R |  |
| `Err_AntiIsLand` | 防孤岛故障 | ENUM | R |  |
| `Err_HarmonicCur` | 电流谐波故障 | ENUM | R |  |
| `Err_OverVoltage` | 过压故障 | ENUM | R |  |
| `Err_PhaSeq` | 相序故障 | ENUM | R |  |
| `Err_Gnd` | 接地故障 | ENUM | R |  |
| `Err_Ua` | 保护事件前A相电压 | FLOAT | R | V |
| `Err_Ub` | 保护事件前B相电压 | FLOAT | R | V |
| `Err_Uc` | 保护事件前C相电压 | FLOAT | R | V |
| `Err_Ia` | 保护事件前A相电流 | FLOAT | R | A |
| `Err_Ib` | 保护事件前B相电流 | FLOAT | R | A |
| `Err_Ic` | 保护事件前C相电流 | FLOAT | R | A |
| `Err_CurDirec` | 保护事件前三相电流方向 | ENUM | R |  |
| `Err_Uab` | 保护事件前AB线电压 | FLOAT | R | V |
| `Err_Ubc` | 保护事件前BC线电压 | FLOAT | R | V |
| `Err_Uca` | 保护事件前CA线电压 | FLOAT | R | V |

## Freq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Freq` | 电网频率 | FLOAT | R | Hz |

## FreqA* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FreqA` | A相频率 | FLOAT | R | Hz |

## FreqB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FreqB` | B相频率 | FLOAT | R | Hz |

## FreqC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FreqC` | C相频率 | FLOAT | R | Hz |

## FundamentalIa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FundamentalIa` | A相电流基波值 | FLOAT | R | A |

## FundamentalIb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FundamentalIb` | B相电流基波值 | FLOAT | R | A |

## FundamentalIc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FundamentalIc` | C相电流基波值 | FLOAT | R | A |

## HarmonicRmsIa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `HarmonicRmsIa` | A相电流谐波有效值 | FLOAT | R | A |

## HarmonicRmsIb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `HarmonicRmsIb` | B相电流谐波有效值 | FLOAT | R | A |

## HarmonicRmsIc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `HarmonicRmsIc` | C相电流谐波有效值 | FLOAT | R | A |

## IUnB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `IUnB` | 电流不平衡度 | FLOAT | R | % |

## Ia* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ia` | A相电流 | FLOAT | R | A |

## Ib* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ib` | B相电流 | FLOAT | R | A |

## Ic* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ic` | C相电流 | FLOAT | R | A |

## Ig* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ig` | 接地电流 | FLOAT | R | A |

## In* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `In` | 中性线电流 | FLOAT | R | A |

## Inf* — 11 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Inf_FeeOpen` | 费控分闸 | ENUM | R |  |
| `Inf_FeeClose` | 费控合闸 | ENUM | R |  |
| `Inf_BtnOpen` | 按键分闸 | ENUM | R |  |
| `Inf_BtnClose` | 按键合闸 | ENUM | R |  |
| `Inf_RemoteOpen` | 远程分闸 | ENUM | R |  |
| `Inf_RemoteClose` | 远程合闸 | ENUM | R |  |
| `Inf_ManualClose` | 手动合闸 | ENUM | R |  |
| `Inf_ReClose` | 重合闸 | ENUM | R |  |
| `Inf_UpdateSuc` | 升级成功 | ENUM | R |  |
| `Inf_ParaChange` | 参数变更 | ENUM | R |  |
| `Inf_Manualopen` | 手动分闸 | ENUM | R |  |

## Ires* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ires` | 剩余电流 | FLOAT | R | mA |

## LeakOpenCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `LeakOpenCount` | 漏电分闸次数 | INT | R | x |

## Lock* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Lock` | 锁定 | INT | W |  |

## Lockout* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Lockout` | 锁死 | INT | W |  |

## Open* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Open` | 分闸 | INT | W |  |

## OpenCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `OpenCount` | 分闸次数 | INT | R | x |

## PFa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PFa` | A相功率因数 | FLOAT | R |  |

## PFb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PFb` | B相功率因数 | FLOAT | R |  |

## PFc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PFc` | C相功率因数 | FLOAT | R |  |

## PFt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PFt` | 总功率因数 | FLOAT | R |  |

## Pa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pa` | A相有功功率 | FLOAT | R | kW |

## Pb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pb` | B相有功功率 | FLOAT | R | kW |

## Pc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pc` | C相有功功率 | FLOAT | R | kW |

## PosChangeCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PosChangeCount` | 闸位变化事件记录总数 | INT | R | x |

## ProtEventCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ProtEventCount` | 保护事件记录总数 | INT | R | x |

## Pt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pt` | 总有功功率 | FLOAT | R | kW |

## Q* — 16 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Q4EQ_C` | C相第四象限无功总电能 | FLOAT | R | kvarh |
| `Q3EQ_C` | C相第三象限无功总电能 | FLOAT | R | kvarh |
| `Q2EQ_C` | C相第二象限无功总电能 | FLOAT | R | kvarh |
| `Q1EQ_C` | C相第一象限无功总电能 | FLOAT | R | kvarh |
| `Q4EQ_B` | B相第四象限无功总电能 | FLOAT | R | kvarh |
| `Q3EQ_B` | B相第三象限无功总电能 | FLOAT | R | kvarh |
| `Q2EQ_B` | B相第二象限无功总电能 | FLOAT | R | kvarh |
| `Q1EQ_B` | B相第一象限无功总电能 | FLOAT | R | kvarh |
| `Q4EQ_A` | A相第四象限无功总电能 | FLOAT | R | kvarh |
| `Q3EQ_A` | A相第三象限无功总电能 | FLOAT | R | kvarh |
| `Q2EQ_A` | A相第二象限无功总电能 | FLOAT | R | kvarh |
| `Q1EQ_A` | A相第一象限无功总电能 | FLOAT | R | kvarh |
| `Q4EQ` | 第四象限无功总电能 | FLOAT | R | kvarh |
| `Q3EQ` | 第三象限无功总电能 | FLOAT | R | kvarh |
| `Q2EQ` | 第二象限无功总电能 | FLOAT | R | kvarh |
| `Q1EQ` | 第一象限无功总电能 | FLOAT | R | kvarh |

## Qa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Qa` | A相无功功率 | FLOAT | R | kvar |

## Qb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Qb` | B相无功功率 | FLOAT | R | kvar |

## Qc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Qc` | C相无功功率 | FLOAT | R | kvar |

## Qt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Qt` | 总无功功率 | FLOAT | R | kvar |

## RHCtrl* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RHCtrl` | 控制器内湿度 | FLOAT | R | %RH |

## RemoteReset* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteReset` | 远方复位 | INT | W |  |

## ResiSelfTestCount* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ResiSelfTestCount` | 剩余电流自检事件记录总数 | INT | R | x |

## Sa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sa` | A相视在功率 | FLOAT | R | kVA |

## Sb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sb` | B相视在功率 | FLOAT | R | kVA |

## Sc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sc` | C相视在功率 | FLOAT | R | kVA |

## SeqI* — 3 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SeqI0` | 电流零序分量 | FLOAT | R | A |
| `SeqI2` | 电流负序分量 | FLOAT | R | A |
| `SeqI1` | 电流正序分量 | FLOAT | R | A |

## SeqU* — 3 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SeqU0` | 电压零序分量 | FLOAT | R | V |
| `SeqU2` | 电压负序分量 | FLOAT | R | V |
| `SeqU1` | 电压正序分量 | FLOAT | R | V |

## St* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `St` | 总视在功率 | FLOAT | R | kVA |

## Sta* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_Device` | 设备状态 | ENUM | R |  |

## THDIa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDIa` | A相电流总谐波畸变率 | FLOAT | R | % |

## THDIb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDIb` | B相电流总谐波畸变率 | FLOAT | R | % |

## THDIc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDIc` | C相电流总谐波畸变率 | FLOAT | R | % |

## THDUa* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDUa` | A相电压总谐波畸变率 | FLOAT | R | % |

## THDUb* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDUb` | B相电压总谐波畸变率 | FLOAT | R | % |

## THDUc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `THDUc` | C相电压总谐波畸变率 | FLOAT | R | % |

## Temp* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Temp` | 断路器内温度 | FLOAT | R | °C |

## TempCtrl* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempCtrl` | 控制器内温度 | FLOAT | R | °C |

## TempInACopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempInACopBus` | 进线Ａ相铜排温度 | FLOAT | R | °C |

## TempInBCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempInBCopBus` | 进线Ｂ相铜排温度 | FLOAT | R | °C |

## TempInCCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempInCCopBus` | 进线Ｃ相铜排温度 | FLOAT | R | °C |

## TempInNCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempInNCopBus` | 中性线进线铜排温度 | FLOAT | R | °C |

## TempOutACopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempOutACopBus` | 出线Ａ相铜排温度 | FLOAT | R | °C |

## TempOutBCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempOutBCopBus` | 出线Ｂ相铜排温度 | FLOAT | R | °C |

## TempOutCCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempOutCCopBus` | 出线Ｃ相铜排温度 | FLOAT | R | °C |

## TempOutNCopBus* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempOutNCopBus` | 中性线出线铜排温度 | FLOAT | R | °C |

## TotalOpeTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalOpeTime` | 累计运行时间 | INT | R | min |

## UUnB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `UUnB` | 电压不平衡度 | FLOAT | R | % |

## Ua* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ua` | A相电压 | FLOAT | R | V |

## Uab* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Uab` | AB线电压 | FLOAT | R | V |

## Ub* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ub` | B相电压 | FLOAT | R | V |

## Ubc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ubc` | BC线电压 | FLOAT | R | V |

## Uc* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Uc` | C相电压 | FLOAT | R | V |

## Uca* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Uca` | CA线电压 | FLOAT | R | V |

## Unlock* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Unlock` | 解锁 | INT | W |  |

## WorkingSts* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WorkingSts` | 状态字 | BITMAP | R |  |

## 关联

- [[acb-3p]]
- [[thing-model-structure]]
