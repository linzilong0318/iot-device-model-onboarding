---
title: 配电单元(1P)
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_PDU_1P.md]
confidence: high
---
# 配电单元(1P)

## 概述

配电单元 (PDU, 1P),配电域。属性含电池容量,疑似用于储能系统簇级配电;26 个测点为过压/欠压/过流/欠流报警与阈值/继电器/蜂鸣设置量;4 个事件为过压/欠压/过流/欠流告警;11 个服务:报警声音、过流联动、各路阈值与延时设置、继电器状态控制。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_PDU_1P` |
| 中文名 | 配电单元(1P) |
| 英文名 |  |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_PDU_1P.md |

## 属性 (Attribute) — 7 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `BatteryCapacity` | 电池容量 | FLOAT | kWh | False |

## 测点 (MeasurePoint) — 26 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Ala_OverU` | 过压告警 | ENUM | R |  |
| `Ala_UnderU` | 欠压告警 | ENUM | R |  |
| `Ala_UnderI` | 空载告警 | ENUM | R |  |
| `SetAlarmSound` | 配置报警声音 | ENUM | RW |  |
| `Ala_OverI` | 过流告警 | ENUM | R |  |
| `SetRelayStatus` | 设置继电器状态 | ENUM | RW |  |
| `OverILinkEnable` | 过载联动使能开关 | ENUM | RW |  |
| `SetUnderITime` | 设置空载判断时间 | INT | RW |  |
| `SetOverITime` | 设置过载判断时间 | INT | RW |  |
| `SetUnderUTime` | 设置欠压判断时间 | INT | RW |  |
| `SetOverUTime` | 设置过压判断时间 | INT | RW |  |
| `SetUnderIThr` | 设置空载下限值 | INT | RW |  |
| `SetOverIThr` | 设置过载上限值 | INT | RW |  |
| `SetUnderUThr` | 设置欠压下限值 | INT | RW |  |
| `SetOverUThr` | 设置过压上限值 | INT | RW |  |
| `RH` | 湿度 | FLOAT | R | %RH |
| `Sta_Alarm` | 报警状态 | ENUM | R |  |
| `Freq` | 电网频率 | FLOAT | R | Hz |
| `EP` | 总有功电能 | FLOAT | R | kWh |
| `Temp` | 温度 | FLOAT | R | °C |
| `PF` | 功率因数 | FLOAT | R |  |
| `S` | 视在功率 | FLOAT | R | VA |
| `Q` | 无功功率 | FLOAT | R | var |
| `P` | 有功功率 | FLOAT | R | W |
| `I` | 电流 | FLOAT | R | A |
| `U` | 电压 | FLOAT | R | V |

## 事件 (Event) — 4 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `AlarmOverU` | 过压告警 | ALARM |
| `AlarmUnderU` | 欠压告警 | ALARM |
| `AlarmOverI` | 过流告警 | ALARM |
| `AlarmUnderI` | 空载告警 | ALARM |

## 服务 (Service) — 11 个

| 标识符 | 名称 |
| --- | --- |
| `AlarmSound` | 配置报警声音 |
| `OverILinkEnableCmd` | 过载联动使能开关 |
| `OverIThr` | 设置过载上限值 |
| `OverITime` | 设置过载判断时间 |
| `OverUThrSet` | 设置过压上限值 |
| `OverUTime` | 设置过压判断时间 |
| `RelayStatus` | 设置继电器状态 |
| `UnderIThr` | 设置空载下限值 |
| `UnderITime` | 设置空载判断时间 |
| `UnderUThr` | 设置欠压下限值 |
| `UnderUTime` | 设置欠压判断时间 |

## 关联

- [[esmu]]
- [[pcs]]
- [[thing-model-structure]]
