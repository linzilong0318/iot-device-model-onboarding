---
title: 水浸传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, power-distribution]
sources: [raw/papers/public_WaterSensor.md]
confidence: high
---
# 水浸传感器

## 概述

水浸传感器 (Water Flood Sensor),配电域。9 个测点:水浸报警状态、灵敏度设置、报警阈值/时间/恢复阈值/恢复时间、模拟量品质、设备时间;1 个事件 AlarmWater(水浸告警);4 个服务:设置报警阈值/时间与恢复阈值/时间。与 [[smoke-sensor]] 结构高度相似。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_WaterSensor` |
| 中文名 | 水浸传感器 |
| 英文名 | Water Flood Sensor |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_WaterSensor.md |

## 属性 (Attribute) — 6 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |

## 测点 (MeasurePoint) — 9 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `AlarmStatus` | 报警状态（废弃） | ENUM | R |  |
| `Ala_Water` | 告警状态 | ENUM | R |  |
| `SensitivitySetting` | 报警灵敏度设置 | INT | R |  |
| `AlarmRecThr` | 告警恢复阈值 | FLOAT | RW |  |
| `AlarmThr` | 告警阈值 | FLOAT | RW |  |
| `AnalogQua` | 水浸值 | FLOAT | R |  |
| `AlarmRecTime` | 告警恢复时间 | INT | RW | s |
| `AlarmTime` | 告警时间 | INT | RW | s |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |

## 事件 (Event) — 1 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmWater` | 水浸告警 | ALARM |

## 服务 (Service) — 4 个

| 标识符 | 名称 |
| --- | --- |
| `SetAlarmRecThr` | 设置告警恢复阈值 |
| `SetAlarmRecTime` | 设置告警恢复时间 |
| `SetAlarmThr` | 设置告警阈值 |
| `SetAlarmTime` | 设置告警时间 |

## 关联

- [[smoke-sensor]]
- [[temp-rh-sensor]]
- [[cabinet-door-sensor]]
- [[thing-model-structure]]
- [[sensor-family]]
