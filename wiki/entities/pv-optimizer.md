---
title: 光伏优化器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, photovoltaic]
sources: [raw/papers/public_PVOptimizer.md]
confidence: high
---
# 光伏优化器

## 概述

光伏优化器 (Photovoltaic Optimizer),Solar 域。30 个测点:输入过压/过温/短路保护使能与阈值/恢复/动作时间等保护配置量;5 个事件:输入过压/欠压、输出过流/过功率/过温;14 个服务:各项保护阈值与时间设置、开关机。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_PVOptimizer` |
| 中文名 | 光伏优化器 |
| 英文名 | Photovoltaic Optimizer |
| 设备大类 | NORMAL |
| 业务域 | Solar |
| 来源 | raw/papers/public_PVOptimizer.md |

## 属性 (Attribute) — 6 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING | A | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 30 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `SetOverTempOpeTime` | 设置过温动作时间 | INT | RW |  |
| `SwitchOff` | 关机 | INT | W |  |
| `OverUEn` | 过压使能 | INT | RW |  |
| `SetOverUThr` | 设置过压阈值 | INT | RW |  |
| `SetOverURec` | 设置过压恢复阈值 | INT | RW |  |
| `SetOverUOpeTime` | 设置过压动作时间 | INT | RW |  |
| `InOverLoadEn` | 输入过载使能 | INT | RW |  |
| `ShoCirProtEn` | 短路保护使能 | INT | RW |  |
| `SetShoCirRecTime` | 设置短路恢复时间 | INT | RW |  |
| `SetShoCirContRecCoun` | 设置短路连续恢复次数 | INT | RW |  |
| `OverTempEn` | 过温使能 | INT | RW |  |
| `SetOverTempThr` | 设置过温阈值 | INT | RW |  |
| `SetOverTempRecThr` | 设置过温恢复阈值 | INT | RW |  |
| `InI` | 输入电流 | FLOAT | R | A |
| `Err_OutOverTemp` | 输出过温故障 | ENUM | R |  |
| `InP` | 输入功率 | FLOAT | R | W |
| `OutU` | 输出电压 | FLOAT | R | V |
| `OutI` | 输出电流 | FLOAT | R | A |
| `OutP` | 输出功率 | FLOAT | R | W |
| `InTemp` | 机内温度 | FLOAT | R | °C |
| `ErrorCount` | 故障记录条数 | INT | R |  |
| `Sta_OnOff` | 开关机状态 | ENUM | R |  |
| `Sta_Online` | 在线状态 | ENUM | R |  |
| `Err_InOverU` | 输入过压故障 | ENUM | R |  |
| `Err_InUnderU` | 输入欠压故障 | ENUM | R |  |
| `Err_OutOverCur` | 输出过流故障 | ENUM | R |  |
| `Err_OutOverP` | 输出过功率故障 | ENUM | R |  |
| `InU` | 输入电压 | FLOAT | R | V |
| `SwitchOn` | 开机 | INT | W |  |
| `DayE` | 当日发电量 | FLOAT | R | kWh |

## 事件 (Event) — 5 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `ErrorInOverU` | 输入过压故障 | FAULT |
| `ErrorInUnderU` | 输入欠压故障 | FAULT |
| `ErrorOutOverCur` | 输出过流故障 | FAULT |
| `ErrorOutOverP` | 输出过功率故障 | FAULT |
| `ErrorOutOverTemp` | 输出过温故障 | FAULT |

## 服务 (Service) — 14 个

| 标识符 | 名称 |
| --- | --- |
| `InOverLoadEnCmd` | 输入过载使能 |
| `OverTempEnCmd` | 过温使能 |
| `OverTempOpeTimeSet` | 设置过温动作时间 |
| `OverTempRecThrSet` | 设置过温恢复阈值 |
| `OverTempThrSet` | 设置过温阈值 |
| `OverUECmd` | 过压使能 |
| `OverUOpeTimeSet` | 设置过压动作时间 |
| `OverURecSet` | 设置过压恢复阈值 |
| `OverUThrSet` | 设置过压阈值 |
| `ShoCirContRecCounSet` | 设置短路连续恢复次数 |
| `ShoCirProtEnCmd` | 短路保护使能 |
| `ShoCirRecTimeSet` | 设置短路恢复时间 |
| `SwitchOffCmd` | 关机 |
| `SwitchOnCmd` | 开机 |

## 关联

- [[mix-inverter-1p]]
- [[string-inverter-3p]]
- [[ghi-sensor]]
- [[thing-model-structure]]
- [[inverter-family]]
