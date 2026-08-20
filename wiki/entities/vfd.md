---
title: 变频器
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [actuator, power-distribution]
sources: [raw/papers/public_VFD.md]
confidence: high
---
# 变频器

## 概述

变频器 (Variable Frequency Drive),配电域。属性含类型(ENUM)、额定功率(W)、额定输入/输出电压、额定输出电流;10 个测点:控制字、变频器状态、运行/设定频率、母线电压、输出电压/电流、转速、输出功率、转矩。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_VFD` |
| 中文名 | 变频器 |
| 英文名 | Variable Frequency Drive |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_VFD.md |

## 属性 (Attribute) — 8 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `EquipmentType` | 设备型号 | STRING |  | True |
| `SN` | 设备SN | STRING |  | False |
| `Type` | 类型 | ENUM |  | False |
| `RatedPower` | 额定功率 | FLOAT | W | False |
| `RatedInputVoltage` | 额定输入电压 | FLOAT | V | False |
| `RatedOutputVoltage` | 额定输出电压 | FLOAT | V | False |
| `RatedOutputCurrent` | 额定输出电流 | FLOAT | A | False |

## 测点 (MeasurePoint) — 10 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Control` | 控制指令 | ENUM | W |  |
| `ConverterStatus` | 变频器状态 | ENUM | R |  |
| `RunningFrequency` | 运行频率 | FLOAT | R | Hz |
| `SetFrequency` | 设定频率 | FLOAT | R | Hz |
| `BusVoltage` | 母线电压 | FLOAT | R | V |
| `OutputVoltage` | 输出电压 | FLOAT | R | V |
| `OutputCurrent` | 输出电流 | FLOAT | R | A |
| `RunningSpeed` | 运行速度 | FLOAT | R | rpm |
| `OutputPower` | 输出功率 | FLOAT | R | W |
| `OutputTorque` | 输出转矩 | FLOAT | R | N·m |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[motor-protector]]
- [[environment-controller]]
- [[thing-model-structure]]
