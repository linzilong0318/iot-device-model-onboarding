---
title: 气象站
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [sensor, environmental-monitoring]
sources: [raw/papers/public_WeatherStation.md]
confidence: high
---
# 气象站

## 概述

气象站,公共域。16 个测点:风速/风力/风向、温度/湿度、噪声、PM2.5/PM10、CO2、气压、光照(多种 Lux 阈值)等,集环境监测于一体。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_WeatherStation` |
| 中文名 | 气象站 |
| 英文名 | ​Weather Station |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_WeatherStation.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |

## 测点 (MeasurePoint) — 16 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WindSpeed` | 风速值 | FLOAT | R | m/s |
| `WindPower` | 风力 | FLOAT | R |  |
| `WindDirection` | 风向 | FLOAT | R | ° |
| `Humidity` | 湿度值 | FLOAT | R | %RH |
| `Temperature` | 温度值 | FLOAT | R | °C |
| `Noise` | 噪声值 | FLOAT | R | dB |
| `PM2_5` | PM2.5值 | FLOAT | R | μg/m³ |
| `PM10` | PM10值 | FLOAT | R | μg/m³ |
| `CO2` | CO2值 | FLOAT | R | ppm |
| `AtmosphericPressure` | 大气压值 | FLOAT | R | kPa |
| `HighLuxValueFor20W` | 20W的Lux值高16位值 | FLOAT | R | Lux |
| `LowLuxValueFor20W` | 20W的Lux值低16位值 | FLOAT | R | Lux |
| `IlluminationFor20W` | 20W的光照值 | FLOAT | R | Lux |
| `Rainfall` | 雨量值 | FLOAT | R | mm |
| `ElectronicCompassAngle` | 电子指南针角度 | FLOAT | R | ° |
| `TotalSolarRadiation` | 太阳总辐射值 | FLOAT | R | W/m² |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[rain-sensor]]
- [[ghi-sensor]]
- [[wind-direction-sensor]]
- [[ion-concentration-detector]]
- [[thing-model-structure]]
- [[sensor-family]]
