---
title: 离子浓度检测仪
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, environmental-monitoring]
sources: [raw/papers/public_IonConcentrationDetector.md]
confidence: high
---
# 离子浓度检测仪

## 概述

离子浓度检测仪,公共域。4 个测点:离子浓度、温度及两者的偏差值。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_IonConcentrationDetector` |
| 中文名 | 离子浓度检测仪 |
| 英文名 | Ion Concentration Detector |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_IonConcentrationDetector.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |

## 测点 (MeasurePoint) — 4 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `IonConcentration` | 离子浓度值 | FLOAT | R | ppm |
| `Temperature` | 温度 | FLOAT | R | °C |
| `TemperatureDeviation` | 温度偏差值 | FLOAT | R | °C |
| `IonConcentrationDeviation` | 离子浓度偏差值 | FLOAT | R | ppm |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[weather-station]]
- [[thing-model-structure]]
- [[sensor-family]]
