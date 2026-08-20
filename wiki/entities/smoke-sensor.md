---
title: 烟雾传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, power-distribution]
sources: [raw/papers/public_SmokeSensor.md]
confidence: high
---
# 烟雾传感器

## 概述

烟雾传感器,配电域。9 个测点:烟雾浓度/密度、报警状态与报警阈值/时间/恢复阈值/恢复时间;1 个事件 AlarmSmoke(烟雾告警);4 个服务:设置报警阈值/时间与恢复阈值/时间。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_SmokeSensor` |
| 中文名 | 烟雾传感器 |
| 英文名 | Smoke Sensor |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_SmokeSensor.md |

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
| `SmokeDensity` | 烟雾浓度（废弃） | FLOAT | R | ppm |
| `AlarmStatus` | 烟感报警状态（废弃） | ENUM | R |  |
| `Ala_Smoke` | 烟雾浓度告警状态 | ENUM | R |  |
| `AlarmRecTime` | 告警恢复时间 | INT | RW | s |
| `AlarmRecThr` | 告警恢复阈值 | FLOAT | RW | ppm |
| `AlarmTime` | 告警时间 | INT | RW | s |
| `AlarmThr` | 告警阈值 | FLOAT | RW | ppm |
| `SmokeConcentration` | 烟雾浓度 | FLOAT | R | ppm |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |

## 事件 (Event) — 1 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmSmoke` | 烟雾浓度异常告警 | ALARM |

## 服务 (Service) — 4 个

| 标识符 | 名称 |
| --- | --- |
| `SetAlarmRecThr` | 设置告警恢复阈值 |
| `SetAlarmRecTime` | 设置告警恢复时间 |
| `SetAlarmThr` | 设置告警阈值 |
| `SetAlarmTime` | 设置告警时间 |

## 关联

- [[water-sensor]]
- [[cabinet-door-sensor]]
- [[temp-rh-sensor]]
- [[thing-model-structure]]
- [[sensor-family]]
