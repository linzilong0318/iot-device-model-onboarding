---
title: 单相交流充电桩
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [device, charging]
sources: [raw/papers/public_ChargingPile_1P.md]
confidence: high
---
# 单相交流充电桩

## 概述

单相交流充电桩(单枪),用于电动汽车交流充电。属性含 SIM 卡信息(ICCID/IMSI)、内置电表信息、桩号、充电枪数量等;33 个测点覆盖充电计量、费用与内部器件状态;11 个事件全部为故障类(急停、接触器、保险丝、风扇、电表/读卡器/绝缘/交直流通信等)。本物模型未定义服务。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ChargingPile_1P` |
| 中文名 | 单相交流充电桩 |
| 英文名 | Single-phase AC charging pile (single gun) |
| 设备大类 | NORMAL |
| 业务域 | charge |
| 来源 | raw/papers/public_ChargingPile_1P.md |

## 属性 (Attribute) — 15 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `SN` | 设备SN | STRING |  | False |
| `ProductCategory` | 产品分类 | STRING |  | False |
| `ProductSeries` | 产品系列 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | False |
| `HardwareVersion` | 硬件版本号 | STRING |  | False |
| `ChargeBoxSN` | 充电柜序列号 | STRING |  | False |
| `SIMIccid` | SIM卡ICCID（4G桩常用） | STRING |  | False |
| `SIMImsi` | SIM卡IMSI | STRING |  | False |
| `MeterType` | 电表类型 | STRING |  | False |
| `MeterSN` | 电表序列号 | STRING |  | False |
| `ChargingPileID` | 桩号 | STRING |  | False |
| `InstallLocation` | 安装位置 | STRING |  | False |
| `ConnectorNum` | 充电枪数量 | INT |  | False |
| `Manufacturer` | 生产厂家 | STRING |  | False |
| `DeviceModel` | 设备型号 | STRING |  | False |

## 测点 (MeasurePoint) — 33 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Err_AcSurgeProt` | 交流防雷故障 | ENUM | R |  |
| `Err_HVContactor` | 高压接触器故障 | ENUM | R |  |
| `ElecRateT1` | 尖电费费率 | FLOAT | R | CNY/kWh |
| `Err_DcFuse` | 直流熔断器故障 | ENUM | R |  |
| `Err_FanSpeedCtrl` | 风扇调速板故障 | ENUM | R |  |
| `Err_CardReaComm` | 读卡器通信中断故障 | ENUM | R |  |
| `Err_EMeterComm` | 电能表通信中断故障 | ENUM | R |  |
| `Err_InsulComm` | 绝缘检测模块通信中断故障 | ENUM | R |  |
| `Err_ACDCComm` | 交直流模块通信中断故障 | ENUM | R |  |
| `TotalMoney` | 当前订单累计总金额 | FLOAT | R | ￥ |
| `Err_OutletOverTemp` | 出风口温度过高故障 | ENUM | R |  |
| `Err_NoAvailRect` | 无可用整流模块故障 | ENUM | R |  |
| `Err_EmergencyStop` | 急停按钮动作故障 | ENUM | R |  |
| `Sta_ConnInserted` | 是否插枪 | ENUM | R |  |
| `Sta_ConnParked` | 枪是否归位 | ENUM | R |  |
| `Sta_Connector` | 枪状态 | ENUM | R |  |
| `RateModelID` | 计费模型编号 | STRING | R |  |
| `I` | 充电电流 | FLOAT | R | A |
| `ServiceMoney` | 当前订单累计服务费 | FLOAT | R | ￥ |
| `ElecMoney` | 当前订单累计电费 | FLOAT | R | ￥ |
| `TotalChargeE` | 累计充电量 | FLOAT | R | kWh |
| `OrderChargeE` | 当前订单充电量 | FLOAT | R | kWh |
| `ConnectorLineTemp` | 枪线温度 | FLOAT | R | °C |
| `P` | 充电功率 | FLOAT | R | kW |
| `ServRateT1` | 尖服务费费率 | FLOAT | R | CNY/kWh |
| `U` | 充电电压 | FLOAT | R | V |
| `Conn1TransID` | 枪1交易流水号 | STRING | R |  |
| `ServRateT4` | 谷服务费费率 | FLOAT | R | CNY/kWh |
| `ElecRateT4` | 谷电费费率 | FLOAT | R | CNY/kWh |
| `ServRateT3` | 平服务费费率 | FLOAT | R | CNY/kWh |
| `ElecRateT3` | 平电费费率 | FLOAT | R | CNY/kWh |
| `ServRateT2` | 峰服务费费率 | FLOAT | R | CNY/kWh |
| `ElecRateT2` | 峰电费费率 | FLOAT | R | CNY/kWh |

## 事件 (Event) — 11 个

| 标识符 | 名称 | 事件类型 |
| --- | --- | --- |
| `Err_EmergencyStop` | 急停按钮动作故障 | FAULT |
| `Err_NoAvailRect` | 无可用整流模块故障 | FAULT |
| `Err_OutletOverTemp` | 出风口温度过高故障 | FAULT |
| `Err_AcSurgeProt` | 交流防雷故障 | FAULT |
| `Err_ACDCComm` | 交直流模块通信中断故障 | FAULT |
| `Err_InsulComm` | 绝缘检测模块通信中断故障 | FAULT |
| `Err_EMeterComm` | 电能表通信中断故障 | FAULT |
| `Err_CardReaComm` | 读卡器通信中断故障 | FAULT |
| `Err_FanSpeedCtrl` | 风扇调速板故障 | FAULT |
| `Err_DcFuse` | 直流熔断器故障 | FAULT |
| `Err_HVContactor` | 高压接触器故障 | FAULT |

## 服务 (Service) — 0 个

_本物模型未定义服务。_

## 关联

- [[electric-meter-1p]]
- [[thing-model-structure]]
- [[pcs]]
