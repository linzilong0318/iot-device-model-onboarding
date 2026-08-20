---
title: 门磁传感器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, power-distribution]
sources: [raw/papers/public_CabinetDoorSensor.md]
confidence: high
---
# 门磁传感器

## 概述

柜门磁传感器,用于配电柜/箱柜门开闭状态监测。物模型极简:4 个通用属性 + 1 个柜门状态测点(ENUM:关闭/开启),无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_CabinetDoorSensor` |
| 中文名 | 门磁传感器 |
| 英文名 | Magnetic Door Sensor |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_CabinetDoorSensor.md |

## 属性 (Attribute) — 4 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 1 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_Door` | 柜门状态 | ENUM | R |  |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[smoke-sensor]]
- [[water-sensor]]
- [[thing-model-structure]]
- [[sensor-family]]
