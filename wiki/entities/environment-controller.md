---
title: 环境控制器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [controller, power-distribution]
sources: [raw/papers/public_EnvironmentController.md]
confidence: high
---
# 环境控制器

## 概述

环境控制器,配电域。监测两路温度与相对湿度(带各自上下限),服务用于设置两路温湿度上下限;无事件。用于配电环境(如柜内温湿度)的监测与控制。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_EnvironmentController` |
| 中文名 | 环境控制器 |
| 英文名 | Environment Controller |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_EnvironmentController.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `EquipmentType` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |

## 测点 (MeasurePoint) — 11 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RelativeHumidity1` | 环境湿度1 | FLOAT | R | %RH |
| `Temperature1` | 环境温度1 | FLOAT | R | °C |
| `Temperature2` | 环境温度2 | FLOAT | R | °C |
| `RelativeHumidity2` | 环境湿度2 | FLOAT | R | %RH |
| `RelativeHumidity1HighLimit` | 环境1湿度上限 | FLOAT | RW | %RH |
| `Temperature1HighLimit` | 环境1温度上限 | FLOAT | RW | °C |
| `Temperature1LowLimit` | 环境1温度下限 | FLOAT | RW | °C |
| `RelativeHumidity2HighLimit` | 环境2湿度上限 | FLOAT | RW | %RH |
| `Temperature2HighLimit` | 环境2温度上限 | FLOAT | RW | °C |
| `Temperature2LowLimit` | 环境2温度下限 | FLOAT | RW | °C |
| `States` | 状态 | BITMAP | R |  |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 6 个

| 标识符 | 名称 |
| --- | --- |
| `SetRelativeHumidity1HighLimit` | 设置环境1湿度上限 |
| `SetRelativeHumidity2HighLimit` | 设置环境2湿度上限 |
| `SetTemperature1HighLimit` | 设置环境1温度上限 |
| `SetTemperature1LowLimit` | 设置环境1温度下限 |
| `SetTemperature2HighLimit` | 设置环境2温度上限 |
| `SetTemperature2LowLimit` | 设置环境2温度下限 |

## 关联

- [[temp-rh-sensor]]
- [[vfd]]
- [[thing-model-structure]]
- [[sensor-family]]
