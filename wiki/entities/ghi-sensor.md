---
title: 太阳总辐射传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, environmental-monitoring, photovoltaic]
sources: [raw/papers/public_GHISensor.md]
confidence: high
---
# 太阳总辐射传感器

## 概述

太阳总辐射传感器 (Solar Total Radiation Sensor),公共域。9 个测点:总辐射、直接辐射、散射辐射(日/总/平均)、日照时数(日/总/平均峰值日照)。用于光伏电站气象监测。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_GHISensor` |
| 中文名 | 太阳总辐射传感器 |
| 英文名 | Solar Total Radiation Sensor |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_GHISensor.md |

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

## 测点 (MeasurePoint) — 9 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `TotalRad` | 总辐射瞬时值 | FLOAT | R | W/m² |
| `DirectRad` | 直接辐射瞬时值 | FLOAT | R | W/m² |
| `DiffuseRad` | 散射辐射瞬时值 | FLOAT | R | W/m² |
| `DaySunTime` | 当日日照时长 | FLOAT | R | min |
| `TotalSunTime` | 总日照时长 | FLOAT | R | min |
| `AvgSunTime` | 平均日照时长 | FLOAT | R | min |
| `DayPeakSunTime` | 当日日照峰值时长 | FLOAT | R | min |
| `TotalPeakSunTime` | 总日照峰值时长 | FLOAT | R | min |
| `AvgPeakSunTime` | 平均日照峰值时长 | FLOAT | R | min |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[weather-station]]
- [[rain-sensor]]
- [[pv-optimizer]]
- [[thing-model-structure]]
- [[sensor-family]]
