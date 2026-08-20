---
title: 雨量传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, environmental-monitoring]
sources: [raw/papers/public_RainSensor.md]
confidence: high
---
# 雨量传感器

## 概述

雨量传感器 (Rainfall Sensor),公共域。10 个测点:瞬时/小时/日/累计降雨量、昨日/上小时降雨量、最大/最小降雨时段与小时雨强。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_RainSensor` |
| 中文名 | 雨量传感器 |
| 英文名 | Rainfall Sensor |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_RainSensor.md |

## 属性 (Attribute) — 8 个

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

## 测点 (MeasurePoint) — 10 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `DayRainFall` | 当日降雨量 | FLOAT | R | mm |
| `TotalRainfall` | 总降雨量 | FLOAT | R | mm |
| `InstantRainFall` | 瞬时降雨量 | FLOAT | R | mm |
| `LastDayRainFall` | 昨日降雨量 | FLOAT | R | mm |
| `HourRainFall` | 小时降雨量 | FLOAT | R | mm |
| `LastHourRainfall` | 上小时降雨量 | FLOAT | R | mm |
| `MaxRainFallPeriod` | 最大降雨量时段 | FLOAT | R | h |
| `MinRainfallPeriod` | 最小降雨量时段 | FLOAT | R | h |
| `MaxHourRainFall` | 最大时段降雨量 | FLOAT | R | mm |
| `MinHourRainFall` | 最小时段降雨量 | FLOAT | R | mm |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[weather-station]]
- [[ghi-sensor]]
- [[wind-direction-sensor]]
- [[thing-model-structure]]
- [[sensor-family]]
