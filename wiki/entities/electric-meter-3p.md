---
title: 三相电表
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_ElectricMeter_3P_V1_0_2.md]
confidence: high
---
# 三相电表

## 概述

三相电表,物模型版本 V1.0.2,配电域。184 个测点为目前最完整的电能计量物模型:三相相/线电压电流、功率与电能(含分时费率表 EPET/EPIT/EQET/EQIT 等)、需量、谐波、序分量、不平衡度、4 路测温、DI/DO、预付费(剩余金额/电量)等;19 个事件覆盖过压/欠压/过流/过频/欠频/缺相/逆相序/反向功率/烟雾/过温等;7 个服务(清零/DO/复位)。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ElectricMeter_3P_V1_0_2` |
| 中文名 | 三相电表 |
| 英文名 | Three-phase Meter |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_ElectricMeter_3P_V1_0_2.md |

## 属性 (Attribute) — 6 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 184 个

测点数量超过 100,完整清单见 [[electric-meter-3p-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Q | 24 |
| Ala | 19 |
| DI | 8 |
| ComEPT | 5 |
| EPIT | 5 |
| EPET | 5 |
| FroMonEPIT | 5 |
| FroMonEPET | 5 |
| FroDEPIT | 5 |
| FroDEPET | 5 |
| EPI | 4 |
| EPE | 4 |
| EQI | 4 |
| EQE | 4 |
| TempCir | 4 |
| DO | 4 |
| SeqU | 3 |
| SeqI | 3 |
| EQt | 1 |
| DeviceTime | 1 |
| Ua | 1 |
| Ub | 1 |
| Uc | 1 |
| Un | 1 |
| Uab | 1 |
| Ubc | 1 |
| Uca | 1 |
| Ia | 1 |
| Ib | 1 |
| Ic | 1 |
| In | 1 |
| TempPhaseA | 1 |
| EPt | 1 |
| ComEP | 1 |
| ComEQ | 1 |
| Pt | 1 |
| Pa | 1 |
| Pb | 1 |
| Pc | 1 |
| Qt | 1 |
| Qa | 1 |
| Qb | 1 |
| Qc | 1 |
| St | 1 |
| Sa | 1 |
| Sb | 1 |
| Sc | 1 |
| PFt | 1 |
| PFa | 1 |
| PFb | 1 |
| PFc | 1 |
| THDUa | 1 |
| THDUb | 1 |
| THDUc | 1 |
| THDIa | 1 |
| THDIb | 1 |
| THDIc | 1 |
| FundamentalIa | 1 |
| HarmonicRmsIa | 1 |
| FundamentalIb | 1 |
| HarmonicRmsIb | 1 |
| FundamentalIc | 1 |
| HarmonicRmsIc | 1 |
| UUnB | 1 |
| TempPhaseB | 1 |
| TempPhaseC | 1 |
| TempN | 1 |
| Freq | 1 |
| MaxDmdEPI | 1 |
| MaxDmdEPE | 1 |
| EnergyRemain | 1 |
| CreditRemain | 1 |
| CreditTotal | 1 |
| VoltageRatio | 1 |
| CurrentRatio | 1 |
| ClearE | 1 |
| RemoteReset | 1 |
| FactoryReset | 1 |
| Sta | 1 |
| IUnB | 1 |
| FroMonEPI | 1 |
| FroMonEPE | 1 |
| FroDEPI | 1 |
| FroDEPE | 1 |
| CurrentDmdP | 1 |
| Ires | 1 |

## 事件 (Event) — 19 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmRevU` | 电压逆序告警 | ALARM |
| `AlarmOverVoltage` | 过压告警 | ALARM |
| `AlarmUnderVoltage` | 欠压告警 | ALARM |
| `AlarmOverCurrent` | 过载告警 | ALARM |
| `AlarmOverFreq` | 过频告警 | ALARM |
| `AlarmUnderFreq` | 欠频告警 | ALARM |
| `AlarmPhaseLoss` | 断相告警 | ALARM |
| `AlarmUUnB` | 电压不平衡告警 | ALARM |
| `AlarmIUnB` | 电流不平衡告警 | ALARM |
| `AlarmRevP_PhaseA` | A相有功功率反向告警 | ALARM |
| `AlarmSmoke` | 烟感告警 | ALARM |
| `AlarmRevP_PhaseB` | B相有功功率反向告警 | ALARM |
| `AlarmRevP_PhaseC` | C相有功功率反向告警 | ALARM |
| `Ala_RevP` | 总有功功率反向告警 | ALARM |
| `AlarmOverTempC1` | 第一路温度越限告警 | ALARM |
| `AlarmOverTempC2` | 第二路温度越限告警 | ALARM |
| `AlarmOverTempC3` | 第三路温度越限告警 | ALARM |
| `AlarmOverTempC4` | 第四路温度越限告警 | ALARM |
| `AlarmOverIres` | 剩余电流越限告警 | ALARM |

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

- [[electric-meter-1p]]
- [[acb-3p]]
- [[electric-meter-3p-measure-points]]
- [[thing-model-structure]]
- [[electric-meter-family]]
