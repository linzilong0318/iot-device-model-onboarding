---
title: 断路器家族对比
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [device, comparison, power-distribution]
sources: [raw/papers/public_ACB_3P_V1_0_2.md, raw/papers/public_MCB_1P_V1_0_2.md, raw/papers/public_MCB_3P_V1_0_2.md, raw/papers/public_MCCB_3P_V1_0_2.md, raw/papers/public_LowVoltageSmartConnector.md, raw/papers/public_MotorProtector.md]
confidence: high
---

# 断路器家族对比

配电域断路器/保护电器家族:框架断路器 (ACB)、微型断路器 (MCB 1P/3P)、塑壳断路器 (MCCB),
以及关联保护电器:低压智能接插件、马达保护器。

## 规模对比

| 维度 | [[acb-3p]] | [[mccb-3p]] | [[mcb-3p]] | [[mcb-1p]] | [[low-voltage-smart-connector]] | [[motor-protector]] |
| --- | --- | --- | --- | --- | --- | --- |
| 物模型 | ACB_3P V1.0.2 | MCCB_3P V1.0.2 | MCB_3P V1.0.2 | MCB_1P V1.0.2 | 低压智能接插件 | 马达保护器 |
| 壳架电流 FrameCurrent | ✓ | ✓ | — | — | — | — |
| 属性 | 13 | 13 | 11 | 11 | 7 | 14 |
| 测点 | 212 | 203 | 96 | 67 | 49 | 40 |
| 事件 | 61 | 54 | 20 | 18 | 1 | 0 |
| 服务 | 6 | 8 | 9 | 9 | 0 | 0 |

## 服务差异(共同 6 服务)

共有服务:`CloseCmd`(合闸)、`OpenCmd`(分闸)、`LockCmd`/`LockoutCmd`(锁定/锁定保持)、
`RemoteResetCmd`(远程复位)、`UnlockCmd`(解锁)。

| 服务 | ACB | MCCB | MCB 1P/3P | 说明 |
| --- | --- | --- | --- | --- |
| LeakageCheckCmd / LeakageTestCmd | — | ✓(仅 Check) | ✓ | 漏电检测/测试,MCB 最全 |
| RemoteReStartCmd | — | ✓ | — | 远程重启,MCCB 独有 |
| LEDBlinkCmd | — | — | ✓ | LED 闪烁定位,MCB 独有 |

## 事件差异

- **ACB(61)最全**:独有防孤岛 (AntiIsLand)、谐波 (HarmonicVolt/Cur)、费控 (InfoFeeOpen/Close)、
  母线/触头温度 (TempCopBus/TempCtrl/TermTemp)、剩余电流 (GraResiI/SudResiI) 等
- **MCCB(54)**:同样含防孤岛、谐波、剩余电流、费控,且有 4 组测量回路 (Q1~Q4) 相关告警
- **MCB(18/20)**:以过压/欠压/过流/漏电/过温/过频/欠频/功率限制为主,3P 版多缺相告警
- **低压智能接插件**:仅 1 个事件 ErrorRecord(故障记录)
- **马达保护器**:无事件无服务,仅监测三相电气量

## 结论

- 断路器物模型复杂度与断路器等级正相关:ACB ≈ MCCB > MCB-3P > MCB-1P
- ACB/MCCB 定位配电主干保护(带防孤岛、谐波、费控等高级功能);MCB 定位末端支路(带漏电检测、LED 定位)
- 低压智能接插件、马达保护器属于简化的"监测型"保护电器,无远程控制服务

## 相关

- [[electric-meter-family]] — 同域计量设备
- [[thing-model-structure]] — 物模型结构
