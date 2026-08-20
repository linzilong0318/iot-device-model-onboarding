---
title: 逆变器家族对比
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [device, comparison, energy-storage, photovoltaic]
sources: [raw/papers/public_PCS.md, raw/papers/public_StringInverter_3P.md, raw/papers/public_MixInverter_1P_V1_0_2.md, raw/papers/public_PVOptimizer.md]
confidence: high
---

# 逆变器家族对比

储能/光伏域功率变换设备:储能变流器 (PCS)、三相组串逆变器、单相混合逆变器、光伏优化器。

## 规模对比

| 维度 | [[pcs]] | [[string-inverter-3p]] | [[mix-inverter-1p]] | [[pv-optimizer]] |
| --- | --- | --- | --- | --- |
| 物模型 | PCS | StringInverter_3P | MixInverter_1P V1.0.2 | PVOptimizer |
| 定位 | 储能变流器(电池↔电网) | 光伏组串并网 | 光储混合(并离网) | 组件级功率优化 |
| 属性 | 12(电池类型/容量/额定充放电功率) | 12(MPPT 路数/额定参数) | 9(MPPT 路数) | 6 |
| 测点 | 175 | 179 | 129 | 30 |
| 事件 | 65 | 65 | 26 | 5 |
| 服务 | 41 | 8 | 18 | 14 |

## 功能特色

| 能力 | PCS | 组串逆变器 | 混合逆变器 | 光伏优化器 |
| --- | --- | --- | --- | --- |
| 并网发电 | ✓ | ✓ | ✓ | —(仅优化) |
| 电池充放电 | ✓ | — | ✓ | — |
| 并离网切换/离网 | ✓(VS 模式) | — | ✓(OnOffGridMode) | — |
| 削峰填谷调度 | ✓(CPS* 系列服务) | — | ✓(GridChar 定时充电) | — |
| 防逆流 | ✓(AntiRevFlowEn) | — | ✓(AntiRevFlowEn) | — |
| AFCI 电弧检测 | — | ✓(12 路 PV 电弧 + ARCCheck*) | — | — |
| MPPT 扫描 | — | ✓(MPPTScanCmd) | — | — |
| 保护阈值配置 | — | — | — | ✓(过压/过温/短路 14 服务) |

## 服务集差异

- **PCS(41 个)最全**:Remote* 系列(有功/无功/电压/电流设定,CS 与 VS 双模式)、
  Batt* 电池管理(开关/预充)、PCSSwitchOn/Off、RapidDischarge、AutoTest、SOC 限值
- **混合逆变器(18 个)**:GridChar*(电网充电使能/定时/功率限制)、SysRunMode、Gen*(发电机)、Batt*(电池)
- **组串逆变器(8 个)**:ARCCheck*/MPPTScan/ForceReboot/FactoryReset/SwitchOn/Off
- **光伏优化器(14 个)**:全部为保护阈值与动作时间设置 + 开关机

## 结论

- 三款逆变器按"储能变流器 > 混合逆变器 > 组串逆变器"递减服务能力;
  光伏优化器是纯保护配置型,不并网
- PCS 与 ESMU 配套构成储能系统(见 [[esmu]]);组串/混合逆变器服务命令风格与 PCS 的
  Remote*/SwitchOn/Off 命名体系一致,但无版本后缀
- 组串逆变器独有 AFCI 电弧检测(光伏安全),PCS/混合逆变器无

## 相关

- [[esmu]]、[[pdu-1p]] — 储能系统配套设备
- [[ghi-sensor]] — 光伏气象监测
- [[thing-model-structure]] — 物模型结构
