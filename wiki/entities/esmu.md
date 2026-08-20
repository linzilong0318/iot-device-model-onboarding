---
title: 电池簇管理单元(ESMU)
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, energy-storage]
sources: [raw/papers/public_ESMU.md]
confidence: high
---
# 电池簇管理单元(ESMU)

## 概述

电池管理系统中的电池簇管理单元 (Battery Stack Management Unit, ESMU),储能域。属性含电池容量等;测点共 816 个:20 个电池簇 (Str1~Str20) 每簇 37 个同构测点(簇电压/电流/温度/SOC/SOH/绝缘电阻/充放电电量与功率限值等) + 76 个系统级测点(簇运行状态、系统 SOC/SOH、充放电统计、接触器状态等);13 个事件为 PCS/EMS/ESBCM/ESBMM 通信、簇电压、接触器、采集等故障;24 个服务为 20 簇主控命令 + 系统功率/断路器/复位控制。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ESMU` |
| 中文名 | 电池簇管理单元(ESMU) |
| 英文名 | Battery Management System Battery Stack Management Unit |
| 设备大类 | NORMAL |
| 业务域 | electricityStorage |
| 来源 | raw/papers/public_ESMU.md |

## 属性 (Attribute) — 7 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `BatteryCapacity` | 电池容量 | FLOAT | kWh | False |

## 测点 (MeasurePoint) — 816 个

测点数量超过 100,完整清单见 [[esmu-measure-points]]。按命名前缀分组:

| 前缀 | 数量 |
| --- | --- |
| Str | 740 |
| Sta | 23 |
| Err | 12 |
| SysDayDischarCount | 1 |
| SysDayCharCount | 1 |
| SysDischarAvaiE | 1 |
| MinBattTemp | 1 |
| MINTempBattStrNo | 1 |
| MINTempPoINTNo | 1 |
| SysTotalCharE | 1 |
| SysTotalDischarE | 1 |
| SysCharESingle | 1 |
| SysDischarESingle | 1 |
| SysCharAvaiE | 1 |
| MaxTempPoINTNo | 1 |
| SysCharAvaiT | 1 |
| SysDischarAvaiT | 1 |
| SysDayDischarE | 1 |
| SysDayCharE | 1 |
| SysTemp | 1 |
| MaxBattU | 1 |
| SysMaxDischarILim | 1 |
| SysMaxCharPLim | 1 |
| SysMaxDischarPLim | 1 |
| SysU | 1 |
| SysI | 1 |
| SysSOC | 1 |
| SysSOH | 1 |
| SysMaxCharILim | 1 |
| MaxUBattStrNo | 1 |
| MaxUPoINTNo | 1 |
| MinBattU | 1 |
| MinUBattStrNo | 1 |
| MinUPoINTNo | 1 |
| MaxBattTemp | 1 |
| MaxTempBattStrNo | 1 |
| SysInsulationR | 1 |
| SysTotalCharT | 1 |
| SysTotalDischarT | 1 |
| Ala | 1 |
| StringNumber | 1 |
| SysFaultReset | 1 |
| SysCBCtrl | 1 |
| SysPowerCtrl | 1 |

## 事件 (Event) — 13 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorPCSandBMSComm` | PCS和BMS通信故障 | FAULT |
| `ErrorEMSandBMSComm` | EMS和BMS通信故障 | FAULT |
| `ErrorESBCMCommFault` | 堆内各主控失联汇总 | FAULT |
| `ErrorESBMMCommFault` | 堆内各从控失联汇总 | FAULT |
| `ErrorrStringsU` | 堆内各组电压异常 | FAULT |
| `ErrorContactorOpen` | 堆内接触器断开异常 | FAULT |
| `ErrorContactorClose` | 堆内接触器闭合异常 | FAULT |
| `ErrorNochar` | 充电禁止 | FAULT |
| `ErrorNoDischar` | 放电禁止 | FAULT |
| `AlaorBMSAlarmSum` | BMS系统告警汇总 | ALARM |
| `ErrorBMSFaultSum` | BMS系统故障汇总 | FAULT |
| `ErrorVoltAcquFault` | 电压采集失联 | FAULT |
| `ErrorTempAcquFault` | 温度采集失联 | FAULT |

## 服务 (Service) — 24 个

| 标识符 | 名称 |
| --- | --- |
| `Str2MainModeCtrlCmd` | 簇2维护模式控制 |
| `SysPowerCtrlCmd` | 系统上下电控制 |
| `SysFaultResetCmd` | 系统故障复位 |
| `SysCBCtrlCmd` | 电操控制 |
| `StringNumberCmd` | 电池簇数量 |
| `Str9MainModeCtrlCmd` | 簇9维护模式控制 |
| `Str8MainModeCtrlCmd` | 簇8维护模式控制 |
| `Str7MainModeCtrlCmd` | 簇7维护模式控制 |
| `Str6MainModeCtrlCmd` | 簇6维护模式控制 |
| `Str5MainModeCtrlCmd` | 簇5维护模式控制 |
| `Str4MainModeCtrlCmd` | 簇4维护模式控制 |
| `Str3MainModeCtrlCmd` | 簇3维护模式控制 |
| `Str10MainModeCtrlCmd` | 簇10维护模式控制 |
| `Str20MainModeCtrlCmd` | 簇20维护模式控制 |
| `Str1MainModeCtrlCmd` | 簇1维护模式控制 |
| `Str19MainModeCtrlCmd` | 簇19维护模式控制 |
| `Str18MainModeCtrlCmd` | 簇18维护模式控制 |
| `Str17MainModeCtrlCmd` | 簇17维护模式控制 |
| `Str16MainModeCtrlCmd` | 簇16维护模式控制 |
| `Str15MainModeCtrlCmd` | 簇15维护模式控制 |
| `Str14MainModeCtrlCmd` | 簇14维护模式控制 |
| `Str13MainModeCtrlCmd` | 簇13维护模式控制 |
| `Str12MainModeCtrlCmd` | 簇12维护模式控制 |
| `Str11MainModeCtrlCmd` | 簇11维护模式控制 |

## 关联

- [[pcs]]
- [[pdu-1p]]
- [[esmu-measure-points]]
- [[thing-model-structure]]
- [[inverter-family]]
