---
title: (交流)框架断路器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_ACB_3P_V1_0_2.md]
confidence: high
---
# (交流)框架断路器

## 概述

三相交流框架断路器(ACB),用于配电系统主回路的分合与保护。物模型版本 V1.0.2。测点覆盖运行状态、母线/触头温度、三相电量与电能质量(序分量、谐波、漏电流等);事件包含过压/欠压/过流/短路/接地/防孤岛/谐波/温度等 61 项告警与故障;服务提供分闸、合闸、锁定/解锁、复位等远程控制。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ACB_3P_V1_0_2` |
| 中文名 | (交流)框架断路器 |
| 英文名 | AC ACB |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_ACB_3P_V1_0_2.md |

## 属性 (Attribute) — 13 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `FrameCurrent` | 壳架电流 | FLOAT | A | False |
| `RatedVoltage` | 额定电压 | FLOAT | V | False |
| `RatedCurrent` | 额定电流 | FLOAT | A | False |
| `RatedFrequency` | 工作频率 | FLOAT | Hz | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `MechanicalLife` | 机械寿命 | INT |  | False |
| `ElectricalLife` | 电气寿命 | INT |  | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceType` | 设备类型 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 212 个

测点数量超过 100,完整清单见 [[acb-3p-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Ala | 37 |
| Err | 36 |
| Q | 16 |
| Inf | 11 |
| ESE | 4 |
| ESI | 4 |
| ComEQ | 4 |
| EPE | 4 |
| EPI | 4 |
| SeqI | 3 |
| SeqU | 3 |
| WorkingSts | 1 |
| Temp | 1 |
| TempOutNCopBus | 1 |
| TempInNCopBus | 1 |
| TempOutCCopBus | 1 |
| TempInCCopBus | 1 |
| TempOutBCopBus | 1 |
| TempInBCopBus | 1 |
| TempOutACopBus | 1 |
| TempInACopBus | 1 |
| IUnB | 1 |
| UUnB | 1 |
| HarmonicRmsIc | 1 |
| FundamentalIc | 1 |
| HarmonicRmsIb | 1 |
| FundamentalIb | 1 |
| HarmonicRmsIa | 1 |
| FundamentalIa | 1 |
| EQE | 1 |
| EQI | 1 |
| ComEP | 1 |
| EPt | 1 |
| EQt | 1 |
| Ig | 1 |
| In | 1 |
| FreqC | 1 |
| FreqB | 1 |
| FreqA | 1 |
| Freq | 1 |
| St | 1 |
| Qt | 1 |
| Pt | 1 |
| PFt | 1 |
| Uca | 1 |
| Ubc | 1 |
| Uab | 1 |
| Unlock | 1 |
| AlarmIndicator | 1 |
| Sta | 1 |
| PosChangeCount | 1 |
| ResiSelfTestCount | 1 |
| AlarmEventCount | 1 |
| ProtEventCount | 1 |
| TotalOpeTime | 1 |
| LeakOpenCount | 1 |
| OpenCount | 1 |
| ContactHealIndex | 1 |
| ContactWear | 1 |
| ContactElecLife | 1 |
| AtmosPressure | 1 |
| TempCtrl | 1 |
| RHCtrl | 1 |
| THDIc | 1 |
| THDIb | 1 |
| THDIa | 1 |
| THDUc | 1 |
| THDUb | 1 |
| THDUa | 1 |
| Ires | 1 |
| Pc | 1 |
| Sc | 1 |
| Qc | 1 |
| PFc | 1 |
| Ic | 1 |
| Uc | 1 |
| Pb | 1 |
| Sa | 1 |
| Sb | 1 |
| Qa | 1 |
| Qb | 1 |
| PFb | 1 |
| Ib | 1 |
| Ub | 1 |
| Pa | 1 |
| PFa | 1 |
| Ia | 1 |
| Ua | 1 |
| ClearContWear | 1 |
| ClearError | 1 |
| ClearEnergyData | 1 |
| RemoteReset | 1 |
| ClearRecord | 1 |
| Open | 1 |
| Close | 1 |
| Lockout | 1 |
| Lock | 1 |

## 事件 (Event) — 61 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorIUnB` | 电流不平衡故障 | FAULT |
| `ErrorTempCopBus` | 铜排温度越限故障 | FAULT |
| `ErrorSelfDiagProt` | 自诊断保护故障 | FAULT |
| `ErrorAntiIsLand` | 防孤岛故障 | FAULT |
| `ErrorGraResiI` | 缓变剩余电流越限故障 | FAULT |
| `ErrorSudResiI` | 突变剩余电流越限故障 | FAULT |
| `AlarmLifeTime` | 寿命超时告警 | ALARM |
| `AlarmHarmonicVolt` | 电压谐波告警 | ALARM |
| `AlarmOverCurrent` | 过载告警 | ALARM |
| `AlarmSelfDiag` | 自诊断保护告警 | ALARM |
| `AlarmRunOverTime` | 运行超时告警 | ALARM |
| `AlarmGraResiI` | 缓变剩余电流越限告警 | ALARM |
| `InfoFeeOpen` | 费控分闸 | INFO |
| `AlarmUnderFreq` | 欠频告警 | ALARM |
| `AlarmOverFreq` | 过频告警 | ALARM |
| `AlarmPhaseLoss` | 断相告警 | ALARM |
| `AlarmGnd` | 接地告警 | ALARM |
| `AlarmUnderVol` | 欠压告警 | ALARM |
| `LowVolt` | 线电压欠压告警 | ALARM |
| `AlarmOveCurLonDel` | 过载长延时告警 | ALARM |
| `AlarmUUnB` | 电压不平衡告警 | ALARM |
| `AlarmIUnB` | 电流不平衡告警 | ALARM |
| `AlarmRevPower` | 逆功率告警 | ALARM |
| `AlarmTempCopBus` | 铜排温度越限告警 | ALARM |
| `AlarmSudResiI` | 突变剩余电流越限告警 | ALARM |
| `ErrorHarmonicVolt` | 电压谐波故障 | FAULT |
| `AlarmPhaSeq` | 相序告警 | ALARM |
| `AlarmOverVol` | 过压告警 | ALARM |
| `InfoBtnOpen` | 按键分闸 | INFO |
| `InfoFeeClose` | 费控合闸 | INFO |
| `ErrorRHCtrl` | 控制器湿度越限故障 | FAULT |
| `AlarmPhaseNLoss` | 断零告警 | ALARM |
| `AlarmTempCtrl` | 控制器温度越限告警 | ALARM |
| `AlarmRHCtrl` | 控制器湿度越限告警 | ALARM |
| `ErrorOverVoltage` | 过压故障 | FAULT |
| `InfoUpdateSuc` | 升级成功 | INFO |
| `InfoReClose` | 重合闸 | INFO |
| `InfoManualClose` | 手动合闸 | INFO |
| `InfoManualopen` | 手动分闸 | INFO |
| `InfoRemoteClose` | 远程合闸 | INFO |
| `InfoRemoteOpen` | 远程分闸 | INFO |
| `InfoBtnClose` | 按键合闸 | INFO |
| `ErrorPhaseNLoss` | 断零故障 | FAULT |
| `ErrorPhaSeq` | 相序故障 | FAULT |
| `ErrorRevPower` | 逆功率故障 | FAULT |
| `ErrorPhaseLoss` | 断相故障 | FAULT |
| `ErrorOveCurLonDelay` | 过载长延时故障 | FAULT |
| `ErrorUnderVoltage` | 欠压故障 | FAULT |
| `AlarmHarmonicCur` | 电流谐波告警 | ALARM |
| `ErrorOverFreq` | 过频故障 | FAULT |
| `ErrorShortCircuit` | 短路瞬时故障 | FAULT |
| `ErrorUnderFreq` | 欠频故障 | FAULT |
| `ErrorUUnB` | 电压不平衡故障 | FAULT |
| `ErrorShoCirShoDelay` | 短路短延时故障 | FAULT |
| `ErrorHarmonicCur` | 电流谐波故障 | FAULT |
| `ErrorGnd` | 接地故障 | FAULT |
| `ErrorTermTemp` | 接线端子温度越限故障 | FAULT |
| `ErrorTempCtrl` | 控制器温度越限故障 | FAULT |
| `InfoParaChange` | 参数变更 | INFO |
| `AlarmAntiIsLand` | 防孤岛告警 | ALARM |
| `AlarmTermTemp` | 接线端子温度越限告警 | ALARM |

## 服务 (Service) — 6 个

| 标识符 | 名称 |
| --- | --- |
| `CloseCmd` | 合闸 |
| `LockCmd` | 锁定 |
| `LockoutCmd` | 锁死 |
| `OpenCmd` | 分闸 |
| `RemoteResetCmd` | 远方复位 |
| `UnlockCmd` | 解锁 |

## 关联

- [[mccb-3p]]
- [[mcb-3p]]
- [[electric-meter-3p]]
- [[thing-model-structure]]
- [[circuit-breaker-family]]
