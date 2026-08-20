---
title: 风向传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, environmental-monitoring]
sources: [raw/papers/public_WindDirectionSensor.md]
confidence: high
---
# 风向传感器

## 概述

风向传感器,公共域。1 个测点 WindDirection(风向);9 个属性中除通用 SN/厂家/分类/系列/型号/版本/位置外,含一个名为 "tt" 的 STRING 属性(疑为模板残留,待确认)。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_WindDirectionSensor` |
| 中文名 | 风向传感器 |
| 英文名 | Wind Direction Sensor |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_WindDirectionSensor.md |

## 属性 (Attribute) — 9 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `tt` | tt | STRING |  | False |
| `SN` | 设备SN | STRING |  | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WindDirection` | 风向 | ENUM | R |  |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[rain-sensor]]
- [[weather-station]]
- [[thing-model-structure]]
- [[sensor-family]]
