---
title: 三相电表 — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, power-distribution]
sources: [raw/papers/public_ElectricMeter_3P_V1_0_2.md]
confidence: high
---
# 三相电表 — 测点全集

> 实体页 [[electric-meter-3p]] 的测点参考,共 184 个测点。按命名前缀分组。

## Ala* — 19 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_Smoke` | 烟感告警 | ENUM | R |  |
| `Ala_OverVoltage` | 过压告警 | ENUM | R |  |
| `Ala_UnderVoltage` | 欠压告警 | ENUM | R |  |
| `Ala_OverCurrent` | 过载告警 | ENUM | R |  |
| `Ala_OverFreq` | 过频告警 | ENUM | R |  |
| `Ala_UnderFreq` | 欠频告警 | ENUM | R |  |
| `Ala_PhaseLoss` | 断相告警 | ENUM | R |  |
| `Ala_UUnB` | 电压不平衡告警 | ENUM | R |  |
| `Ala_IUnB` | 电流不平衡告警 | ENUM | R |  |
| `Ala_RevU` | 电压逆序告警 | ENUM | R |  |
| `Ala_RevP_PhaseA` | A相有功功率反向告警 | ENUM | R |  |
| `Ala_RevP_PhaseB` | B相有功功率反向告警 | ENUM | R |  |
| `Ala_RevP_PhaseC` | C相有功功率反向告警 | ENUM | R |  |
| `Ala_RevP` | 总有功功率反向告警 | ENUM | R |  |
| `Ala_OverTempC1` | 第一路温度越限告警 | ENUM | R |  |
| `Ala_OverTempC2` | 第二路温度越限告警 | ENUM | R |  |
| `Ala_OverTempC3` | 第三路温度越限告警 | ENUM | R |  |
| `Ala_OverTempC4` | 第四路温度越限告警 | ENUM | R |  |
| `Ala_OverIres` | 剩余电流越限告警 | ENUM | R |  |

## ClearE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ClearE` | 电能清零 | INT | W |  |

## ComEP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEP` | 组合有功总电能 | FLOAT | R | kWh |

## ComEPT* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEPT1` | 组合有功费率1电能 | FLOAT | R | kWh |
| `ComEPT2` | 组合有功费率2电能 | FLOAT | R | kWh |
| `ComEPT3` | 组合有功费率3电能 | FLOAT | R | kWh |
| `ComEPT4` | 组合有功费率4电能 | FLOAT | R | kWh |
| `ComEPT5` | 组合有功费率5电能 | FLOAT | R | kWh |

## ComEQ* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `ComEQ` | 组合无功总电能 | FLOAT | R | kWh |

## CreditRemain* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CreditRemain` | 剩余金额 | FLOAT | R |  |

## CreditTotal* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CreditTotal` | 总购电金额 | FLOAT | R |  |

## CurrentDmdP* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CurrentDmdP` | 当前有功需量 | FLOAT | R | kW |

## CurrentRatio* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `CurrentRatio` | 电流变比 | INT | RW |  |

## DI* — 8 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DI1` | 开关量输入1 | ENUM | R |  |
| `DI2` | 开关量输入2 | ENUM | R |  |
| `DI3` | 开关量输入3 | ENUM | R |  |
| `DI4` | 开关量输入4 | ENUM | R |  |
| `DI5` | 开关量输入5 | ENUM | R |  |
| `DI6` | 开关量输入6 | ENUM | R |  |
| `DI7` | 开关量输入7 | ENUM | R |  |
| `DI8` | 开关量输入8 | ENUM | R |  |

## DO* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DO1` | 开关量输出1 | ENUM | W |  |
| `DO2` | 开关量输出2 | ENUM | W |  |
| `DO3` | 开关量输出3 | ENUM | W |  |
| `DO4` | 开关量输出4 | ENUM | W |  |

## DeviceTime* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |

## EPE* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPE` | 反向有功电能 | FLOAT | R | kWh |
| `EPE_PhaseA` | A相反向有功电能 | FLOAT | R | kWh |
| `EPE_PhaseB` | B相反向有功电能 | FLOAT | R | kWh |
| `EPE_PhaseC` | C相反向有功电能 | FLOAT | R | kWh |

## EPET* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPET1` | 反向有功费率1电能 | FLOAT | R | kWh |
| `EPET2` | 反向有功费率2电能 | FLOAT | R | kWh |
| `EPET3` | 反向有功费率3电能 | FLOAT | R | kWh |
| `EPET4` | 反向有功费率4电能 | FLOAT | R | kWh |
| `EPET5` | 反向有功费率5电能 | FLOAT | R | kWh |

## EPI* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPI` | 正向有功电能 | FLOAT | R | kWh |
| `EPI_PhaseA` | A相正向有功电能 | FLOAT | R | kWh |
| `EPI_PhaseB` | B相正向有功电能 | FLOAT | R | kWh |
| `EPI_PhaseC` | C相正向有功电能 | FLOAT | R | kWh |

## EPIT* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPIT1` | 正向有功费率1电能 | FLOAT | R | kWh |
| `EPIT2` | 正向有功费率2电能 | FLOAT | R | kWh |
| `EPIT3` | 正向有功费率3电能 | FLOAT | R | kWh |
| `EPIT4` | 正向有功费率4电能 | FLOAT | R | kWh |
| `EPIT5` | 正向有功费率5电能 | FLOAT | R | kWh |

## EPt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EPt` | 总有功电能 | FLOAT | R | kWh |

## EQE* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQE` | 反向无功电能 | FLOAT | R | kvarh |
| `EQE_PhaseA` | A相反向无功电能 | FLOAT | R | kWh |
| `EQE_PhaseB` | B相反向无功电能 | FLOAT | R | kWh |
| `EQE_PhaseC` | C相反向无功电能 | FLOAT | R | kWh |

## EQI* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQI` | 正向无功电能 | FLOAT | R | kvarh |
| `EQI_PhaseA` | A相正向无功电能 | FLOAT | R | kWh |
| `EQI_PhaseB` | B相正向无功电能 | FLOAT | R | kWh |
| `EQI_PhaseC` | C相正向无功电能 | FLOAT | R | kWh |

## EQt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EQt` | 总无功电能 | FLOAT | R | kvarh |

## EnergyRemain* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `EnergyRemain` | 剩余电量 | FLOAT | R | kWh |

## FactoryReset* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FactoryReset` | 恢复出厂设置 | INT | W |  |

## Freq* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Freq` | 电网频率 | FLOAT | R | Hz |

## FroDEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroDEPE` | (冻结)日反向有功电能 | FLOAT | R | kWh |

## FroDEPET* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroDEPET1` | （冻结）日费率1反向有功电能 | FLOAT | R | kWh |
| `FroDEPET2` | （冻结）日费率2反向有功电能 | FLOAT | R | kWh |
| `FroDEPET3` | （冻结）日费率3反向有功电能 | FLOAT | R | kWh |
| `FroDEPET4` | （冻结）日费率4反向有功电能 | FLOAT | R | kWh |
| `FroDEPET5` | （冻结）日费率5反向有功电能 | FLOAT | R | kWh |

## FroDEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroDEPI` | (冻结)日正向有功电能 | FLOAT | R | kWh |

## FroDEPIT* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroDEPIT1` | （冻结）日费率1正向有功电能 | FLOAT | R | kWh |
| `FroDEPIT2` | （冻结）日费率2正向有功电能 | FLOAT | R | kWh |
| `FroDEPIT3` | （冻结）日费率3正向有功电能 | FLOAT | R | kWh |
| `FroDEPIT4` | （冻结）日费率4正向有功电能 | FLOAT | R | kWh |
| `FroDEPIT5` | （冻结）日费率5正向有功电能 | FLOAT | R | kWh |

## FroMonEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroMonEPE` | (冻结)月反向有功电能 | FLOAT | R | kWh |

## FroMonEPET* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroMonEPET1` | （冻结）月费率1反向有功电能 | FLOAT | R | kWh |
| `FroMonEPET2` | （冻结）月费率2反向有功电能 | FLOAT | R | kWh |
| `FroMonEPET3` | （冻结）月费率3反向有功电能 | FLOAT | R | kWh |
| `FroMonEPET4` | （冻结）月费率4反向有功电能 | FLOAT | R | kWh |
| `FroMonEPET5` | （冻结）月费率5反向有功电能 | FLOAT | R | kWh |

## FroMonEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroMonEPI` | (冻结)月正向有功电能 | FLOAT | R | kWh |

## FroMonEPIT* — 5 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `FroMonEPIT2` | （冻结）月费率2正向有功电能 | FLOAT | R | kWh |
| `FroMonEPIT3` | （冻结）月费率3正向有功电能 | FLOAT | R | kWh |
| `FroMonEPIT4` | （冻结）月费率4正向有功电能 | FLOAT | R | kWh |
| `FroMonEPIT5` | （冻结）月费率5正向有功电能 | FLOAT | R | kWh |
| `FroMonEPIT1` | （冻结）月费率1正向有功电能 | FLOAT | R | kWh |

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

## In* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `In` | 中性线电流 | FLOAT | R | A |

## Ires* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ires` | 剩余电流 | FLOAT | R | A |

## MaxDmdEPE* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MaxDmdEPE` | 反向有功最大需量 | FLOAT | R | kW |

## MaxDmdEPI* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `MaxDmdEPI` | 正向有功最大需量 | FLOAT | R | kW |

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

## Pt* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Pt` | 总有功功率 | FLOAT | R | kW |

## Q* — 24 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Q1EQ` | 第一象限无功总电能 | FLOAT | R | kvarh |
| `Q1EQT1` | 第一象限无功费率1电能 | FLOAT | R | kvarh |
| `Q1EQT2` | 第一象限无功费率2电能 | FLOAT | R | kvarh |
| `Q1EQT3` | 第一象限无功费率3电能 | FLOAT | R | kvarh |
| `Q1EQT4` | 第一象限无功费率4电能 | FLOAT | R | kvarh |
| `Q2EQ` | 第二象限无功总电能 | FLOAT | R | kvarh |
| `Q2EQT1` | 第二象限无功费率1电能 | FLOAT | R | kvarh |
| `Q2EQT2` | 第二象限无功费率2电能 | FLOAT | R | kvarh |
| `Q2EQT3` | 第二象限无功费率3电能 | FLOAT | R | kvarh |
| `Q2EQT4` | 第二象限无功费率4电能 | FLOAT | R | kvarh |
| `Q3EQ` | 第三象限无功总电能 | FLOAT | R | kvarh |
| `Q3EQT1` | 第三象限无功费率1电能 | FLOAT | R | kvarh |
| `Q3EQT2` | 第三象限无功费率2电能 | FLOAT | R | kvarh |
| `Q3EQT3` | 第三象限无功费率3电能 | FLOAT | R | kvarh |
| `Q3EQT4` | 第三象限无功费率4电能 | FLOAT | R | kvarh |
| `Q4EQ` | 第四象限无功总电能 | FLOAT | R | kvarh |
| `Q4EQT1` | 第四象限无功费率1电能 | FLOAT | R | kvarh |
| `Q4EQT2` | 第四象限无功费率2电能 | FLOAT | R | kvarh |
| `Q4EQT3` | 第四象限无功费率3电能 | FLOAT | R | kvarh |
| `Q4EQT4` | 第四象限无功费率4电能 | FLOAT | R | kvarh |
| `Q1EQT5` | 第一象限无功费率5电能 | FLOAT | R | kvarh |
| `Q2EQT5` | 第二象限无功费率5电能 | FLOAT | R | kvarh |
| `Q3EQT5` | 第三象限无功费率5电能 | FLOAT | R | kvarh |
| `Q4EQT5` | 第四象限无功费率5电能 | FLOAT | R | kvarh |

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

## RemoteReset* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RemoteReset` | 远方复位 | INT | W |  |

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
| `SeqI1` | 电流正序分量 | FLOAT | R | A |
| `SeqI2` | 电流负序分量 | FLOAT | R | A |
| `SeqI0` | 电流零序分量 | FLOAT | R | A |

## SeqU* — 3 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SeqU1` | 电压正序分量 | FLOAT | R | V |
| `SeqU2` | 电压负序分量 | FLOAT | R | V |
| `SeqU0` | 电压零序分量 | FLOAT | R | V |

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

## TempCir* — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempCir1` | 第一路温度 | FLOAT | R | °C |
| `TempCir2` | 第二路温度 | FLOAT | R | °C |
| `TempCir3` | 第三路温度 | FLOAT | R | °C |
| `TempCir4` | 第四路温度 | FLOAT | R | °C |

## TempN* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempN` | 中性线温度 | FLOAT | R | °C |

## TempPhaseA* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempPhaseA` | A相温度 | FLOAT | R | °C |

## TempPhaseB* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempPhaseB` | B相温度 | FLOAT | R | °C |

## TempPhaseC* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TempPhaseC` | C相温度 | FLOAT | R | °C |

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

## Un* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Un` | 中性点对地电压 | FLOAT | R | V |

## VoltageRatio* — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `VoltageRatio` | 电压变比 | INT | RW |  |

## 关联

- [[electric-meter-3p]]
- [[thing-model-structure]]
