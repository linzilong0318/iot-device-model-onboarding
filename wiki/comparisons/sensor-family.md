---
title: 传感器家族对比
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [sensor, comparison, environmental-monitoring, power-distribution]
sources: [raw/papers/public_SmokeSensor.md, raw/papers/public_WaterSensor.md, raw/papers/public_TempRHSensor_V1_0_2.md, raw/papers/public_WeatherStation.md]
confidence: high
---

# 传感器家族对比

环境/状态监测类传感器物模型,按结构分两类:

## 一、智能传感器(带报警事件 + 阈值设置服务)

| 维度 | [[smoke-sensor]] | [[water-sensor]] | [[temp-rh-sensor]] |
| --- | --- | --- | --- |
| 物模型 | SmokeSensor | WaterSensor | TempRHSensor V1.0.2 |
| 测点 | 9 | 9 | 13 |
| 事件 | 1 (AlarmSmoke) | 1 (AlarmWater) | 2 (AlarmTemp/AlarmRH) |
| 服务 | 4 | 4 | 8 |

**共同模式**:每个被监测量配一组 4 个设置服务——`SetAlarmThr`(报警阈值)、`SetAlarmRecThr`(恢复阈值)、
`SetAlarmTime`(报警时间)、`SetAlarmRecTime`(恢复时间);对应测点含报警状态 ENUM(正常/异常)、
阈值/时间/恢复阈值/恢复时间及设备时间。

- 烟雾/水浸结构几乎相同(1 量 × 4 服务);温湿度是双通道版(温度 + 湿度各 4 服务 = 8)
- 烟雾传感器旧测点 `SmokeDensity`/`AlarmStatus` 在文档中标注"(废弃)",已被
  `SmokeConcentration`/`Ala_Smoke` 取代
- 环境控制器 [[environment-controller]] 是这类传感器的"控制版":加上了温湿度上下限设置服务

## 二、只读传感器(仅属性 + 测点,无事件无服务)

| 物模型 | 测点 | 监测内容 |
| --- | --- | --- |
| [[weather-station]] | 16 | 风速/风力/风向、温湿度、噪声、PM2.5/PM10、CO2、气压、光照 |
| [[rain-sensor]] | 10 | 瞬时/小时/日/累计降雨量、最大最小雨强 |
| [[ghi-sensor]] | 9 | 总/直接/散射辐射、日照时数 |
| [[ion-concentration-detector]] | 4 | 离子浓度、温度及偏差 |
| [[wind-direction-sensor]] | 1 | 风向(属性含疑似模板残留的 `tt`) |
| [[cabinet-door-sensor]] | 1 | 柜门开闭状态(ENUM) |
| [[fire-detector]] | 45 | 三相电气参量(经确认文档无误,见实体页) |

## 域分布

- **配电监测**(distribution):烟雾、水浸、温湿度、柜门、火灾探测器 — 用于配电房/柜环境与安全监测
- **环境气象**(public):气象站、雨量、辐射、风向、离子浓度 — 用于户外气象观测(光伏电站等)

## 结论

- 报警类传感器遵循统一的"阈值-时间-恢复"四件套模式,平台可抽象通用报警配置逻辑
- 只读传感器多为气象类,数据被动采集,无本地阈值判断
- 温湿度传感器存在两代物模型:旧版 public_TempHumiditySensor(2 测点,已弃用)与
  现行 TempRHSensor V1.0.2(13 测点,带报警能力)

## 相关

- [[common-attributes]] — 传感器公共属性(SN/位置/版本等)
- [[thing-model-structure]] — 物模型结构
- [[device-category-and-domain]] — 域划分
