---
title: 电表家族对比
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [device, comparison, power-distribution, deprecated]
sources: [raw/papers/public_ElectricMeter_1P_V1_0_2.md, raw/papers/public_ElectricMeter_3P_V1_0_2.md]
confidence: high
---

# 电表家族对比

现役电表物模型两个:单相电表 (V1.0.2) 与三相电表 (V1.0.2)。旧版 `public_ElectricMeter`(9 测点)已弃用,
其原始文档已从 raw/papers/ 删除,不建页。

## 规模对比

| 维度 | [[electric-meter-1p]] | [[electric-meter-3p]] |
| --- | --- | --- |
| 物模型 | ElectricMeter_1P V1.0.2 | ElectricMeter_3P V1.0.2 |
| 属性 | 8 | 6 |
| 测点 | 66 | 184 |
| 事件 | 6 | 19 |
| 服务 | 7 | 7 |

## 相同点

- **服务完全一致**(7 个):`ClearECmd`(电量清零)、`DO1Cmd`~`DO4Cmd`(4 路 DO 控制)、
  `FactoryResetCmd`、`RemoteResetCmd`
- 属性结构一致(SN/产品分类/系列/软硬件版本/安装位置;1P 版多 Manufacturer、DeviceModel)
- 均含 `AlarmSmoke` 事件(电表内置烟雾检测)与过压/欠压/过流/过频/欠频告警

## 差异点

| 维度 | 单相电表 | 三相电表 |
| --- | --- | --- |
| 电压/电流测点 | 单相(U/I/谐波 RMS) | 三相相/线电压 (Ua~Uca)、相电流 (Ia~Ic)、零序 (In)、漏电流 (Ires) |
| 分时费率 | ComEPT1~5 等(5 时段) | 完整费率表:EPET/EPIT/EQET/EQIT × T1~T5 及冻结值 (Fro*)、需量 (MaxDmd*) |
| 电能质量 | THDU/THDI、谐波 | 序分量 (SeqU/SeqI)、不平衡度 (UUnB/IUnB)、谐波/THD 三相 |
| 预付费 | — | CreditRemain/CreditTotal/EnergyRemain |
| 测温 | 有 | TempPhaseA/B/C + TempN + 4 路 TempCir1~4 |
| DI/DO | DO 测点 | DI1~8 + DO1~4 |
| 事件 | 6 | 19(多缺相/逆相序/反向功率/过温/过流谐波) |

## 结论

- 三相电表是公司最完整的电能计量物模型,覆盖分时计量、需量、谐波、预付费、温度监测;
  单相电表为精简版
- 两个物模型服务集完全一致,平台侧控制逻辑可复用
- 预付费字段 (Credit*/EnergyRemain) 仅三相版具备

## 相关

- [[circuit-breaker-family]] — 同域保护电器
- [[charging-pile-1p]] — 内置电表信息的充电桩
- [[thing-model-structure]] — 物模型结构
