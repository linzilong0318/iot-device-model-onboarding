---
title: 温湿度传感器 V1.0.2
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, power-distribution]
sources: [raw/papers/public_TempRHSensor_V1_0_2.md]
confidence: high
---
# 温湿度传感器 V1.0.2

## 概述

温湿度传感器,物模型版本 V1.0.2,配电域。13 个测点:温度/湿度实时值 + 各自报警阈值/恢复阈值/报警时间/恢复时间 + 设备时间;2 个事件 AlarmTemp/AlarmRH(温/湿度告警);8 个服务:设置温度/湿度的报警阈值、恢复阈值、报警时间、恢复时间。已取代无版本后缀的旧版 public_TempHumiditySensor(已弃用)。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_TempRHSensor_V1_0_2` |
| 中文名 | 温湿度传感器 V1.0.2 |
| 英文名 | Temperature and Humidity Sensor |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_TempRHSensor_V1_0_2.md |

## 属性 (Attribute) — 7 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ManufacturerCode` | 厂家工厂代码 | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |

## 测点 (MeasurePoint) — 13 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `RHAlarmRecThr` | 湿度告警恢复阈值 | FLOAT | RW | %RH |
| `RHAlarmTime` | 湿度告警时间 | INT | RW | s |
| `RHAlarmRecTime` | 湿度告警恢复时间 | INT | RW | s |
| `RHAlarmThr` | 湿度告警阈值 | FLOAT | RW | %RH |
| `RH` | 湿度 | FLOAT | R | %RH |
| `TempAlarmRecTime` | 温度告警恢复时间 | INT | RW | s |
| `TempAlarmRecThr` | 温度告警恢复阈值 | FLOAT | RW | °C |
| `TempAlarmTime` | 温度告警时间 | INT | RW | s |
| `TempAlarmThr` | 温度告警阈值 | FLOAT | RW | °C |
| `Temp` | 温度 | FLOAT | R | °C |
| `DeviceTime` | 设备时间 | DATETIME | RW |  |
| `Ala_Temp` | 温度告警状态 | ENUM | R |  |
| `Ala_RH` | 湿度告警状态 | ENUM | R |  |

## 事件 (Event) — 2 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmRH` | 湿度告警 | ALARM |
| `AlarmTemp` | 温度告警 | ALARM |

## 服务 (Service) — 8 个

| 标识符 | 名称 |
| --- | --- |
| `SetRHAlarmRecThr` | 设置湿度告警恢复阈值 |
| `SetRHAlarmRecTime` | 设置湿度告警恢复时间 |
| `SetRHAlarmThr` | 设置湿度告警阈值 |
| `SetRHAlarmTime` | 设置湿度告警时间 |
| `SetTempAlarmRecThr` | 设置温度告警恢复阈值 |
| `SetTempAlarmRecTime` | 设置温度告警恢复时间 |
| `SetTempAlarmThr` | 设置温度告警阈值 |
| `SetTempAlarmTime` | 设置温度告警时间 |

## 关联

- [[smoke-sensor]]
- [[environment-controller]]
- [[water-sensor]]
- [[thing-model-structure]]
- [[sensor-family]]
