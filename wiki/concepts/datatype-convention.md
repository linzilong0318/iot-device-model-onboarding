---
title: 数据类型与单位约定
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [datatype, standard]
sources: [raw/papers/public_CabinetDoorSensor.md, raw/papers/public_SmokeSensor.md]
confidence: high
---

# 数据类型与单位约定

全库 33 个物模型仅使用 6 种数据类型。DataDefine 字段为 JSON 结构,表达取值范围或枚举映射。

## 数据类型

| 类型 | 使用次数 | 用途 |
| --- | --- | --- |
| `FLOAT` | 1441 | 测量量:电压、电流、功率、温度、浓度等 |
| `INT` | 579 | 计数/时间:寿命、报警时间、DI/DO、状态码 |
| `ENUM` | 528 | 枚举状态:报警状态、运行模式、柜门状态、设备大类 |
| `STRING` | 210 | 身份/版本:SN、型号、安装位置、固件版本 |
| `DATETIME` | 23 | 设备时间、时间戳 |
| `BITMAP` | 18 | 位图状态字(如故障字) |

## DataDefine 结构

- 数值范围(FLOAT/INT):
  ```json
  { "minValue": "", "maxValue": "" }
  ```
  minValue/maxValue 多数为空字符串(未约束)。
- 枚举映射(ENUM),键值编码 `enumKeyCode: INT`:
  ```json
  {
    "mappingItemList": [
      { "itemKey": "0", "itemValue": "正常",
        "itemI18nValue": { "default": "正常", "en_US": "Normal", "zh_CN": "正常" } },
      { "itemKey": "1", "itemValue": "异常",
        "itemI18nValue": { "default": "异常", "en_US": "Alarm", "zh_CN": "异常" } }
    ],
    "enumKeyCode": "INT"
  }
  ```

## 单位使用情况

常用单位:`V`(电压)、`A`(电流)、`W`/`kW`(功率)、`kWh`(电能)、`Hz`(频率)、`℃`(温度)、
`%RH`(湿度)、`ppm`(浓度)、`s`(时间)、`m/s`(风速)、`Lux`(光照)、`°`(角度/风向)等。

**文档中的单位瑕疵**(照实收录,引用时注意):
- MCB 系列 `MechanicalLife`/`ElectricalLife` 单位记为 `x`(应为"次")
- StringInverter_3P `RatedP`(额定有功功率)单位记为 `V`(应为 W/kW)
- LowVoltageSmartConnector `RatedCurrent` 单位记为 `V`(应为 A)

## 关联

- [[thing-model-structure]] — 四维度结构与字段约定
- [[common-attributes]] — 公共属性
- [[device-category-and-domain]] — 设备分类
