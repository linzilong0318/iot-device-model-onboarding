---
title: 公共属性约定
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [property, standard]
sources: [raw/papers/public_SmokeSensor.md, raw/papers/public_MCB_1P_V1_0_2.md]
confidence: high
---

# 公共属性约定

33 个现役物模型共有的属性命名与用途约定。属性多为 STRING 类型、非必填,表达设备身份/版本/分类/安装信息。

## 高频公共属性

| 属性 | 出现设备数/33 | 含义 | 说明 |
| --- | --- | --- | --- |
| `SN` | 31 | 设备序列号 | 事实上的必填项,个别文档标注 False |
| `InstallLocation` | 28 | 安装位置 | |
| `SoftwareVersion` / `HardwareVersion` | 20 | 软件/硬件版本号 | 网关类型标注为必填(True) |
| `ProductCategory` / `ProductSeries` | 19 | 产品分类 / 产品系列 | 成对出现 |
| `DeviceModel` | 14 | 设备型号 | 与 `DeviceVersion`、`EquipmentType` 语义重叠(见下) |
| `Manufacturer` | 12 | 生产厂家 | |

## "型号"三套命名并存(历史遗留)

同一语义存在三种命名,分布在不同的物模型中:

- `DeviceModel`(设备型号)— 14 个,多为版本化物模型(断路器、电表、逆变器)
- `DeviceVersion`(设备型号)— 6 个,老式物模型(马达保护器、气象站、离子浓度检测仪等)
- `EquipmentType`(设备型号)— 3 个,标注必填(环境控制器、变频器)

三者中文名均为"设备型号",属命名不统一,引用时以具体物模型为准。

## 额定参数类属性(功率设备)

- 电压:`RatedVoltage`(5)、`RatedU`(2,逆变器)
- 电流:`RatedCurrent`(6)、`RatedOutputCurrent`(VFD)、`MaxCurrent`(低压智能接插件)
- 频率:`RatedFrequency`(4)、`RatedFreq`(2,逆变器)
- 功率:`RatedPower`(3)、`RatedP`(组串逆变器)、`RatedChargeP`/`RatedDischargeP`(PCS)
- 壳架电流:`FrameCurrent`(2,ACB/MCCB 断路器)
- 寿命:`MechanicalLife`/`ElectricalLife`(4,断路器;MCB 文档单位记为 `x`,疑为"次")
- 电池容量:`BatteryCapacity`(3,ESMU/PCS/PDU)
- MPPT 路数:`MPPTNumber`(2,逆变器)

## 关联

- [[thing-model-structure]] — 四维度结构与字段约定
- [[datatype-convention]] — 数据类型
- [[device-category-and-domain]] — 设备分类
