---
title: (交流)塑壳断路器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_MCCB_3P_V1_0_2.md]
confidence: high
---
# (交流)塑壳断路器

## 概述

(交流)三相塑壳断路器 (MCCB),物模型版本 V1.0.2,配电域。203 个测点:4 组测量回路(Q1~Q4)各相电能、三相电气量、状态、温度、漏电流与序分量等;54 个事件为配电域最全(含 11 个 INFO 类:手动/远程/按钮分合、参数变更、费控等);8 个服务(分合闸、漏电检测、锁定/解锁、远程复位与重启)。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_MCCB_3P_V1_0_2` |
| 中文名 | (交流)塑壳断路器 |
| 英文名 | AC Molded Case Circuit Breaker |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_MCCB_3P_V1_0_2.md |

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
| `MechanicalLife` | 机械寿命 | INT | x | False |
| `ElectricalLife` | 电气寿命 | INT | x | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceType` | 设备类型 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 203 个

测点数量超过 100,完整清单见 [[mccb-3p-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Ala | 34 |
| Err | 33 |
| Q | 16 |
| Inf | 11 |
| ComEQ | 4 |
| ESE | 4 |
| ESI | 4 |
| EPE | 4 |
| EPI | 4 |
| SeqU | 3 |
| SeqI | 3 |
| WorkingSts | 1 |
| EQE | 1 |
| EQI | 1 |
| EQt | 1 |
| RemoteReSetInf | 1 |
| RemoteReStart | 1 |
| LeakageCheck | 1 |
| LeakageTest | 1 |
| RemoteReset | 1 |
| Lockout | 1 |
| Sta | 1 |
| IUnB | 1 |
| PFt | 1 |
| UUnB | 1 |
| HarmonicRmsIc | 1 |
| FundamentalIc | 1 |
| HarmonicRmsIb | 1 |
| FundamentalIb | 1 |
| HarmonicRmsIa | 1 |
| FundamentalIa | 1 |
| ComEP | 1 |
| EPt | 1 |
| Ig | 1 |
| In | 1 |
| FreqC | 1 |
| Freq | 1 |
| Uca | 1 |
| Ubc | 1 |
| Uab | 1 |
| DeviceTime | 1 |
| Lock | 1 |
| Unlock | 1 |
| Close | 1 |
| Open | 1 |
| PosChangeCount | 1 |
| ResiSelfTestCount | 1 |
| AlarmEventCount | 1 |
| ProtEventCount | 1 |
| TotalOpeTime | 1 |
| LeakOpenCount | 1 |
| OpenCount | 1 |
| RHCtrl | 1 |
| TempCtrl | 1 |
| Temp | 1 |
| TempOutN | 1 |
| TempInN | 1 |
| AlarmIndicator | 1 |
| Qt | 1 |
| Pt | 1 |
| Pc | 1 |
| Sc | 1 |
| Qc | 1 |
| PFc | 1 |
| Pb | 1 |
| Sb | 1 |
| Qb | 1 |
| PFb | 1 |
| Pa | 1 |
| Sa | 1 |
| Qa | 1 |
| PFa | 1 |
| St | 1 |
| THDIc | 1 |
| THDIb | 1 |
| THDIa | 1 |
| THDUc | 1 |
| THDUb | 1 |
| THDUa | 1 |
| Ires | 1 |
| FreqB | 1 |
| FreqA | 1 |
| Ic | 1 |
| Uc | 1 |
| Ib | 1 |
| Ub | 1 |
| Ia | 1 |
| Ua | 1 |
| TempOutC | 1 |
| TempInC | 1 |
| TempOutB | 1 |
| TempInB | 1 |
| TempOutA | 1 |
| TempInA | 1 |

## 事件 (Event) — 54 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorUUnB` | 电压不平衡故障 | FAULT |
| `AlarmRevPower` | 逆功率告警 | ALARM |
| `AlarmPhaseNLoss` | 断零告警 | ALARM |
| `AlarmOveCurLonDel` | 过载长延时告警 | ALARM |
| `ErrorAntiIsLand` | 防孤岛故障 | FAULT |
| `ErrorIUnB` | 电流不平衡故障 | FAULT |
| `AlarmUUnB` | 电压不平衡告警 | ALARM |
| `AlarmIUnB` | 电流不平衡告警 | ALARM |
| `ErrorGnd` | 接地故障 | FAULT |
| `AlarmPhaseLoss` | 断相告警 | ALARM |
| `AlarmUnderFreq` | 欠频告警 | ALARM |
| `AlarmUnderVol` | 欠压告警 | ALARM |
| `AlarmOverVol` | 过压告警 | ALARM |
| `ErrorSelfDiagProt` | 自诊断保护故障 | FAULT |
| `AlarmGnd` | 接地故障告警 | ALARM |
| `ErrorGraResiI` | 缓变剩余电流越限故障 | FAULT |
| `ErrorSudResiI` | 突变剩余电流越限故障 | FAULT |
| `ErrorTempCtrl` | 控制器温度越限故障 | FAULT |
| `ErrorRHCtrl` | 控制器湿度越限故障 | FAULT |
| `ErrorTermTemp` | 接线端子温度越限故障 | FAULT |
| `ErrorPhaSeq` | 相序故障 | FAULT |
| `ErrorRevPower` | 逆功率故障 | FAULT |
| `ErrorPhaseNLoss` | 断零故障 | FAULT |
| `ErrorOveCurLonDelay` | 过载长延时故障 | FAULT |
| `AlarmOverCurrent` | 过载告警 | ALARM |
| `AlarmRunOverTime` | 运行超时告警 | ALARM |
| `AlarmLifeTime` | 寿命超时告警 | ALARM |
| `ErrorOverFreq` | 过频故障 | FAULT |
| `InfoUpdateSuc` | 升级成功 | INFO |
| `InfoReClose` | 重合闸 | INFO |
| `InfoManualClose` | 手动合闸 | INFO |
| `InfoManualopen` | 手动分闸 | INFO |
| `InfoRemoteClose` | 远程合闸 | INFO |
| `InfoRemoteOpen` | 远程分闸 | INFO |
| `InfoBtnClose` | 按键合闸 | INFO |
| `InfoBtnOpen` | 按键分闸 | INFO |
| `InfoFeeClose` | 费控合闸 | INFO |
| `InfoFeeOpen` | 费控分闸 | INFO |
| `AlarmGraResiI` | 缓变剩余电流告警 | ALARM |
| `ErrorShortCircuit` | 短路瞬时故障 | FAULT |
| `ErrorUnderFreq` | 欠频故障 | FAULT |
| `InfoParaChange` | 参数变更 | INFO |
| `ErrorPhaseLoss` | 断相故障 | FAULT |
| `ErrorUnderVoltage` | 欠压故障 | FAULT |
| `ErrorOverVoltage` | 过压故障 | FAULT |
| `AlarmAntiIsLand` | 防孤岛告警 | ALARM |
| `AlarmSelfDiag` | 自诊断保护告警 | ALARM |
| `AlarmOverFreq` | 过频告警 | ALARM |
| `ErrorShoCirShoDelay` | 短路短延时故障 | FAULT |
| `AlarmSudResiI` | 突变剩余电流告警 | ALARM |
| `AlarmTempCtrl` | 控制器温度告警 | ALARM |
| `AlarmRHCtrl` | 控制器湿度告警 | ALARM |
| `AlarmTermTemp` | 接线端子温度告警 | ALARM |
| `AlarmPhaSeq` | 相序告警 | ALARM |

## 服务 (Service) — 8 个

| 标识符 | 名称 |
| --- | --- |
| `CloseCmd` | 合闸 |
| `LeakageCheckCmd` | 漏电自检 |
| `LockCmd` | 锁定 |
| `LockoutCmd` | 锁死 |
| `OpenCmd` | 分闸 |
| `RemoteResetCmd` | 远方复位 |
| `RemoteReStartCmd` | 远程程序重启 |
| `UnlockCmd` | 解锁 |

## 关联

- [[acb-3p]]
- [[mcb-3p]]
- [[low-voltage-smart-connector]]
- [[mccb-3p-measure-points]]
- [[thing-model-structure]]
- [[circuit-breaker-family]]
