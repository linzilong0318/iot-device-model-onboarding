---
title: 设备分类与业务域
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [device, gateway, standard]
sources: [raw/papers/public_ChintSDEdge.md, raw/papers/public_Null.md]
confidence: high
---

# 设备分类与业务域

## 设备大类(Category)

物模型分两类,见 BasicInfo 的 `*Category` 字段:

| 大类 | 数量 | 物模型 |
| --- | --- | --- |
| `NORMAL`(普通类型) | 30 | 全部传感器、断路器、电表、逆变器、储能设备等 |
| `GATEWAY`(网关类型) | 3 | ChintSDEdge(Edge 系列边缘网关)、ChintSimulateGate(模拟网关)、ChintSoftWareEdge(软网关) |

### 网关类型说明

- **ChintSDEdge**:已整理的硬件边缘网关,31 个测点监控网关自身运行资源(CPU/内存/磁盘/WiFi/网口),4 个服务(LED/HTTP 模式/日志/复位)。见 [[chint-sd-edge]]
- **ChintSimulateGate / ChintSoftWareEdge**:**占位类型**——四个维度均为空,对应设备类型尚未整理,仅保留物模型 ID 供平台绑定
- 网关类型的属性标为必填的更多(EdgeType/SoftwareVersion/HardwareVersion/SubCode)

### 占位类型(Null)

`public_Null`(空设备类型)为**纯占位**:仅 SN/设备型号/安装位置 3 个通用属性,无测点/事件/服务,
用于平台中尚未定义物模型时的占位绑定。见 [[null-type]]。

## 业务域(Domain)

| 域 | 数量 | 物模型 |
| --- | --- | --- |
| `distribution`(配电) | 17 | ACB_3P、MCB_1P/3P、MCCB_3P、电表 1P/3P、FireDetector、VFD、PWZB、PFC_Panel、PDU_1P、EnvironmentController、LowVoltageSmartConnector、Smoke/Water/TempRH/CabinetDoor 传感器 |
| `public`(公共) | 9 | SDEdge、SimulateGate、GHI/Rain/WindDirection/WeatherStation/IonConcentration 传感器、MotorProtector、Null |
| `electricityStorage`(储能) | 4 | ESMU、PCS、StringInverter_3P、MixInverter_1P |
| `charge`(充电) | 1 | ChargingPile_1P |
| `Solar`(光伏) | 1 | PVOptimizer |
| `heatingSupply`(供热) | 1 | ChintSoftWareEdge |

**域命名不一致**(照实收录):
- PVOptimizer 的 domain 为 `Solar`(首字母大写),其余均为小写
- StringInverter_3P、MixInverter_1P 归入 `electricityStorage`,但分别为光伏并网逆变器与混合(光储)逆变器
- ChintSoftWareEdge 归入 `heatingSupply`,但属网关大类

## 关联

- [[thing-model-structure]] — 物模型结构
- [[gateway-types]] 相关实体:[[chint-sd-edge]]、[[chint-simulate-gate]]、[[chint-soft-ware-edge]]
- [[null-type]] — 空设备类型
