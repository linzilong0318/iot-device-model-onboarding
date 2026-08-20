---
title: 单相混合逆变器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, energy-storage]
sources: [raw/papers/public_MixInverter_1P_V1_0_2.md]
confidence: high
---
# 单相混合逆变器

## 概述

(单相)混合逆变器 (Hybrid Inverter),物模型版本 V1.0.2,储能域。属性含 MPPT 路数;129 个测点覆盖发电量(日/月/年/总)、设备状态与系统运行模式、电池与电网参数;26 个事件为电池过压/欠压/过温、充放电过流、电网过欠压/过欠频、母线、PV、BMS 通信等;18 个服务:并离网模式、电网充电(定时/功率限制/防逆流)、电池充放电使能、发电机启停等。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_MixInverter_1P_V1_0_2` |
| 中文名 | 单相混合逆变器 |
| 英文名 | (Single-phase) Hybrid Inverter |
| 设备大类 | NORMAL |
| 业务域 | electricityStorage |
| 来源 | raw/papers/public_MixInverter_1P_V1_0_2.md |

## 属性 (Attribute) — 9 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `MPPTNumber` | MPPT路数 | INT |  | False |

## 测点 (MeasurePoint) — 129 个

测点数量超过 100,完整清单见 [[mix-inverter-1p-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Err | 19 |
| Ala | 7 |
| PV | 6 |
| Sta | 3 |
| DayGenOpeTime | 1 |
| GenOutU | 1 |
| GenOutI | 1 |
| GenOutP | 1 |
| GenOutFreq | 1 |
| DayGenE | 1 |
| MonGenE | 1 |
| YearGenE | 1 |
| TotalGenE | 1 |
| SwitchOn | 1 |
| SwitchOff | 1 |
| GridCharEn | 1 |
| GenCharEn | 1 |
| PurePVOffGridEn | 1 |
| BattRecovEn | 1 |
| BattPToGridEn | 1 |
| AntiRevFlowEn | 1 |
| BattCharEn | 1 |
| GridCharStartTime | 1 |
| GridCharEndTime | 1 |
| TotalLoadTime | 1 |
| DayLoadTime | 1 |
| LoadS | 1 |
| LoadQ | 1 |
| LoadP | 1 |
| GridPF | 1 |
| GridS | 1 |
| GridQ | 1 |
| InvertOutTotalE | 1 |
| InvertOutDayE | 1 |
| InvertOutPF | 1 |
| InvertOutS | 1 |
| InvertOutQ | 1 |
| InvertOutP | 1 |
| InvertOutI | 1 |
| InvertOutU | 1 |
| DayPVInPtPeak | 1 |
| PVInPt | 1 |
| DCDCModTemp | 1 |
| GridP | 1 |
| InvertOutFreq | 1 |
| SetGridCharPLim | 1 |
| SetMinDischarSOC | 1 |
| SetMaxCharSOC | 1 |
| SysRunMode | 1 |
| RemoSysRunMode | 1 |
| GenSwitchOn | 1 |
| GenSwitchOff | 1 |
| OnOffGridMode | 1 |
| SetMaxExGridP | 1 |
| BattModTemp | 1 |
| PVModTemp | 1 |
| InvModTemp | 1 |
| InTemp | 1 |
| DeviceTime | 1 |
| LoadI | 1 |
| DayPVE | 1 |
| GridFreq | 1 |
| GridI | 1 |
| GridU | 1 |
| DayEPI | 1 |
| MontEPI | 1 |
| InvertEffi | 1 |
| TotalPVTime | 1 |
| DayPVTime | 1 |
| TotalPVE | 1 |
| TotalLoadE | 1 |
| YearLoadE | 1 |
| MonLoadE | 1 |
| DayLoadE | 1 |
| LoadU | 1 |
| TotalEPE | 1 |
| YearEPE | 1 |
| MontEPE | 1 |
| DayEPE | 1 |
| TotalEPI | 1 |
| YearEPI | 1 |
| ChargeCount | 1 |
| DischargeCount | 1 |
| EnergyRemain | 1 |
| SOC | 1 |
| SOH | 1 |
| BatteryTemp | 1 |
| BatteryU | 1 |
| BatteryI | 1 |
| BatteryP | 1 |
| DayCharTime | 1 |
| TotalCharTime | 1 |
| DayDischarTime | 1 |
| TotalDischarTime | 1 |
| DayCharE | 1 |
| TotalCharE | 1 |
| DayDischarE | 1 |
| TotalDischarE | 1 |

## 事件 (Event) — 26 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorSoftStart` | 软起故障 | FAULT |
| `AlarmBattModuUnderU` | 电池模块欠压告警 | ALARM |
| `AlarmBattModuOverU` | 电池模块过压告警 | ALARM |
| `AlarmOverBattTemp` | 电池温度过高告警 | ALARM |
| `AlarmUnderBattTemp` | 电池温度过低告警 | ALARM |
| `AlarmDischarOverCur` | 放电过电流告警 | ALARM |
| `AlarmCharOverCur` | 充电过电流告警 | ALARM |
| `AlarmSecBattOffLine` | 从电池或者从组通信离线 | ALARM |
| `ErrorBattModuUnderU` | 电池模块欠压故障 | FAULT |
| `ErrorBattModuOverU` | 电池模块过压故障 | FAULT |
| `ErrorOverBattTemp` | 电池温度过高故障 | FAULT |
| `ErrorUnderBattTemp` | 电池温度过低故障 | FAULT |
| `ErrorDischarOverCur` | 放电过电流故障 | FAULT |
| `ErrorSystem` | 电池系统错误 | FAULT |
| `ErrorOverGridU` | 电网电压过高故障 | FAULT |
| `ErrorUnderGridU` | 电网电压过低故障 | FAULT |
| `ErrorNoGridPower` | 无市电故障 | FAULT |
| `ErrorOverGridFreq` | 电网频率过高故障 | FAULT |
| `ErrorUnderGridFreq` | 电网频率过低故障 | FAULT |
| `ErrorBMSComm` | BMS通讯故障 | FAULT |
| `ErrorOverPVU` | PV电压过高故障 | FAULT |
| `ErrorUnderPVU` | PV电压过低故障 | FAULT |
| `ErrorOverBusU` | 母线电压过高故障 | FAULT |
| `ErrorUnderBusU` | 母线电压过低故障 | FAULT |
| `ErrorUnderInvertTemp` | 逆变器温度越限故障 | FAULT |
| `ErrorCharOverCur` | 充电过电流故障 | FAULT |

## 服务 (Service) — 18 个

| 标识符 | 名称 |
| --- | --- |
| `GridCharPLimSet` | 设置电网充电功率限值 |
| `SysRunModeCmd` | 设置系统工作模式 |
| `SwitchOnCmd` | 开机 |
| `SwitchOffCmd` | 关机 |
| `RemoSysRunModeCmd` | 设置远程系统工作模式 |
| `PurePVOffGridEnCmd` | 纯PV离网运行使能 |
| `OnOffGridModeCmd` | 设置并离网模式 |
| `MaxExGridPSet` | 设置最大上网功率 |
| `GridCharStartTimeSet` | 电网充电开始时间 |
| `AntiRevFlowEnCmd` | 防逆流使能 |
| `GridCharEndTimeSet` | 电网充电结束时间 |
| `GridCharEnCmd` | 电网充电使能 |
| `GenSwitchOnCmd` | 发电机开机 |
| `GenSwitchOffCmd` | 发电机关机 |
| `GenCharEnCmd` | 发电机充电使能 |
| `BattRecovEnCmd` | 电池恢复使能 |
| `BattPToGridEnCmd` | 电池功率上网使能 |
| `BattCharEnCmd` | 电池充电使能 |

## 关联

- [[string-inverter-3p]]
- [[pcs]]
- [[pv-optimizer]]
- [[thing-model-structure]]
- [[inverter-family]]
