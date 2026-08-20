---
title: 网关类型对比
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [gateway, comparison, gateway-device]
sources: [raw/papers/public_ChintSDEdge.md, raw/papers/public_ChintSimulateGate.md, raw/papers/public_ChintSoftWareEdge.md]
confidence: high
---

# 网关类型对比

三个网关类型物模型的对比。SDEdge 为已整理硬件网关;另两个为占位类型。

| 维度 | [[chint-sd-edge]] | [[chint-simulate-gate]] | [[chint-soft-ware-edge]] |
| --- | --- | --- | --- |
| 物模型 ID | public_ChintSDEdge | public_ChintSimulateGate | public_ChintSoftWareEdge |
| 业务域 | public | public | heatingSupply |
| 描述字段 | "111"(原文) | (空) | "软网关类型" |
| 属性 | 6(含必填 EdgeType/版本/子型号) | 0 | 0 |
| 测点 | 31(CPU/内存/磁盘/WiFi/网口) | 0 | 0 |
| 事件 | 0 | 0 | 0 |
| 服务 | 4(LedCmd/setHttpClientMode/SetLog/SetReset) | 0 | 0 |

## 结论

- 网关类型物模型目前只有 **SDEdge(Edge 系列边缘网关)** 有实际内容,监控对象是网关自身运行资源而非下挂设备
- 模拟网关、软网关为**占位类型**,待设备类型整理后再补充四维度内容(用户确认 2026-08-07)
- 网关与普通设备的差异:网关属性必填项更多,且通过服务(LED/HTTP 模式/日志/复位)管理网关自身

## 相关

- [[device-category-and-domain]] — 设备大类划分
- [[chint-sd-edge]] — Edge 系列边缘网关实体页
