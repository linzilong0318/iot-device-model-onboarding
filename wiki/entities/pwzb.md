---
title: 微机保护装置
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, power-distribution]
sources: [raw/papers/public_PWZB.md]
confidence: high
---
# 微机保护装置

## 概述

微机保护装置 (PWZB),配电域。属性仅 SN/型号/位置;14 个测点为三相电压/电流/功率/功率因数/频率等电气量。无事件、无服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_PWZB` |
| 中文名 | 微机保护装置 |
| 英文名 | PWZB |
| 设备大类 | NORMAL |
| 业务域 | distribution |
| 来源 | raw/papers/public_PWZB.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | True |

## 测点 (MeasurePoint) — 14 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `PowerFactor` | 功率因数 | FLOAT | R |  |
| `ApparentPower` | 视在功率 | FLOAT | R | VA |
| `ReactivePower` | B相无功功率 | FLOAT | R | var |
| `ActivePowe` | 有功功率 | FLOAT | R | W |
| `Ia` | A相电流 | FLOAT | R | A |
| `Ib` | B相电流 | FLOAT | R | A |
| `Ic` | C相电流 | FLOAT | R | A |
| `Ua` | A相电压 | FLOAT | R | V |
| `Ub` | B相电压 | FLOAT | R | V |
| `Uc` | C相电压 | FLOAT | R | V |
| `Uab` | A、B相线电压 | FLOAT | R | V |
| `Ubc` | B、C相线电压 | FLOAT | R | V |
| `Uca` | C、A相线电压 | FLOAT | R | V |
| `Frequency` | 频率 | FLOAT | R | Hz |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[motor-protector]]
- [[pfc-panel]]
- [[thing-model-structure]]
