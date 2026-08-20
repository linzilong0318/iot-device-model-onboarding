---
title: 空设备类型
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device]
sources: [raw/papers/public_Null.md]
confidence: high
---
# 空设备类型

## 概述

空设备类型 (NullType),纯占位用途。仅有 SN/设备型号/安装位置 3 个通用属性,无测点、事件、服务。用于平台中尚未定义物模型时的占位绑定。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_Null` |
| 中文名 | 空设备类型 |
| 英文名 | NullType |
| 设备大类 | NORMAL |
| 业务域 | public |
| 来源 | raw/papers/public_Null.md |

## 属性 (Attribute) — 3 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `DeviceVersion` | 设备型号 | STRING |  | False |
| `SN` | 设备SN | STRING |  | False |

## 测点 (MeasurePoint) — 0 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[chint-simulate-gate]]
- [[thing-model-structure]]
