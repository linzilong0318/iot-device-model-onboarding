---
title: Edge 系列边缘网关
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [gateway, gateway-device]
sources: [raw/papers/public_ChintSDEdge.md]
confidence: high
---
# Edge 系列边缘网关

## 概述

正泰 Edge 系列边缘网关(硬件网关),设备大类为网关类型 (GATEWAY)。属性含 Edge 系列枚举、SN、软硬件版本、子型号(均必填);31 个测点监控网关自身运行资源(CPU/内存/磁盘占用、进程 Top10、WiFi 规格与 SSID、网口 MAC/IP 等);服务提供 LED 控制、HTTP 客户端模式设置、日志设置、复位。描述字段原文为"111"。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 物模型 ID | `public_ChintSDEdge` |
| 中文名 | Edge 系列边缘网关 |
| 英文名 |  |
| 设备大类 | GATEWAY |
| 业务域 | public |
| 来源 | raw/papers/public_ChintSDEdge.md |

## 属性 (Attribute) — 6 个

| 标识符 | 名称 | 数据类型 | 单位 | 必填 |
| --- | --- | --- | --- | --- |
| `EdgeType` | Edge系列 | ENUM |  | True |
| `SN` | SN | STRING |  | False |
| `InstallLocation` | 安装地址 | STRING |  | False |
| `SoftwareVersion` | 软件版本号 | STRING |  | True |
| `HardwareVersion` | 硬件版本号 | STRING |  | True |
| `SubCode` | 子型号 | STRING |  | True |

## 测点 (MeasurePoint) — 31 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `WifiSpec` | WiFi硬件规格 | STRING | R |  |
| `WifiApSsid` | 网关热点名称 | STRING | RW |  |
| `CPUCores` | CPU核心数 | INT | R |  |
| `MemorySize` | 内存大小 | INT | R | MB |
| `DiskSize` | 磁盘大小 | INT | R | MB |
| `CPU` | CPU占用率 | INT | R | % |
| `Memory` | 内存占用率 | INT | R | % |
| `Disk` | 磁盘占用率 | INT | R | % |
| `CPUProcessTop10` | 前10进程CPU各自占比 | STRING | R |  |
| `EdgeIP` | 当前上网IP | STRING | R |  |
| `EthMac` | 当前上网MAC地址 | STRING | R |  |
| `DNS` | DNS服务器 | STRING | RW |  |
| `ServerMode` | ModbusTcp模式 | INT | R |  |
| `WifiApPwd` | 网关热点密码 | STRING | RW |  |
| `WifiStaSsid` | Station ssid | STRING | R |  |
| `Priority` | 上网方式优先级设置 | INT | RW |  |
| `WifiStaRssi` | 作为Station时信号强度 | INT | R |  |
| `CellularSpec` | 4G硬件规格 | STRING | R |  |
| `CellularRssi` | 4G信号强度 | INT | R |  |
| `CellularNumber` | 4G卡号 | STRING | R |  |
| `ServerCard` | ModbusTcp绑定网卡 | STRING | R |  |
| `ServerCardServerCard` | ModbusTcp端口 | INT | R |  |
| `Led` | led控制 | INT | W |  |
| `Reset` | 复位 | INT | W |  |
| `Log` | log开关 | INT | RW |  |
| `HttpClientMode` | http模式 | INT | RW |  |
| `Connection` | 当前上网方式 | INT | R |  |
| `CpuClockSpeed` | CPU主频 | INT | R | MHz |
| `Hardware` | 当前硬件版本 | STRING | R |  |
| `Firmware` | 当前固件版本 | STRING | R |  |
| `Software` | 当前软件版本 | STRING | R |  |

## 事件 (Event) — 0 个

_本物模型未定义事件。_

## 服务 (Service) — 4 个

| 标识符 | 名称 |
| --- | --- |
| `LedCmd` | LedCmd |
| `setHttpClientMode` | setHttpClientMode |
| `SetLog` | SetLog |
| `SetReset` | SetReset |

## 关联

- [[chint-simulate-gate]]
- [[chint-soft-ware-edge]]
- [[gateway-types]]
- [[thing-model-structure]]
