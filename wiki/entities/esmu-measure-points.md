---
title: 电池簇管理单元(ESMU) — 测点全集
created: 2026-08-07
updated: 2026-08-07
type: summary
tags: [measurepoint, energy-storage]
sources: [raw/papers/public_ESMU.md]
confidence: high
---
# 电池簇管理单元(ESMU) — 测点全集

> 实体页 [[esmu]] 的测点参考,共 816 个测点。按命名前缀分组。

### 电池簇测点模板(每簇 37 个)

20 个电池簇 Str1~Str20 测点完全同构,以下模板中 `StrN` 替换为簇编号即可。

| 标识符(模板) | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `StrNMaxCharILim` | 簇1允许最大充电电流 | FLOAT | R | A |
| `StrNMaxDischarILim` | 簇1允许最大放电电流 | FLOAT | R | A |
| `StrNMaxCharPLim` | 簇1允许最大充电功率 | FLOAT | R | kW |
| `StrNMaxDischarPLim` | 簇1允许最大放电功率 | FLOAT | R | kW |
| `StrNMaxCharULim` | 簇1允许最大充电电压 | FLOAT | R | V |
| `StrNMaxDischarULim` | 簇1允许最大放电电压 | FLOAT | R | V |
| `StrNU` | 簇1电压 | FLOAT | R | V |
| `StrNI` | 簇1电流 | FLOAT | R | A |
| `StrNSOC` | 簇1SOC | INT | R | % |
| `StrNSOH` | 簇1SOH | INT | R | % |
| `StrNESBCMTemp` | 簇1模块温度 | INT | R | °C |
| `StrNInsulationR` | 簇1绝缘电阻 | INT | R | kΩ |
| `StrNUAvg` | 簇1平均电池电压 | FLOAT | R | V |
| `StrNTempAvg` | 簇1平均电池温度 | INT | R | °C |
| `StrNMaxBattU` | 簇1最高电池电压 | FLOAT | R | V |
| `StrNMaxUPoINTNo` | 簇1最高电压电池对应点号 | INT | R |  |
| `StrNMinBattU` | 簇1最低电池电压 | FLOAT | R | V |
| `StrNMinUPoINTNo` | 簇1最低电压电池对应点号 | INT | R |  |
| `StrNMaxBattTemp` | 簇1最高电池温度 | INT | R | °C |
| `StrNMaxTempPoINTNo` | 簇1最高温度电池对应点号 | INT | R |  |
| `StrNMinBattTemp` | 簇1最低电池温度 | INT | R | °C |
| `StrNMINTempPoINTNo` | 簇1最低温度电池对应点号 | INT | R |  |
| `StrNMaxBattSOC` | 簇1最高电池SOC | INT | R | % |
| `StrNMaxSOCPoINTNo` | 簇1最高电池SOC对应点号 | INT | R |  |
| `StrNMinBattSOC` | 簇1最低电池SOC | INT | R | % |
| `StrNMinSOCPoINTNo` | 簇1最低电池SOC对应点号 | INT | R |  |
| `StrNMaxBattSOH` | 簇1最高电池SOH | INT | R | % |
| `StrNMaxSOHPoINTNo` | 簇1最高电池SOH对应点号 | INT | R |  |
| `StrNMinBattSOH` | 簇1最低电池SOH | INT | R | % |
| `StrNMinSOHPoINTNo` | 簇1最低电池SOH对应点号 | INT | R |  |
| `StrNTotalCharE` | 簇1累计充电电量 | FLOAT | R | kWh |
| `StrNTotalDischarE` | 簇1累计放电电量 | FLOAT | R | kWh |
| `StrNCharESingle` | 簇1单次累计充电电量 | FLOAT | R | kWh |
| `StrNDischarESingle` | 簇1单次累计放电电量 | FLOAT | R | kWh |
| `StrNCharAvaiE` | 簇1可充电量 | FLOAT | R | kWh |
| `StrNDischarAvaiE` | 簇1可放电量 | FLOAT | R | kWh |
| `StrNMainModeCtrl` | 簇1维护模式控制 | ENUM | RW |  |

簇编号: Str1, Str2, Str3, Str4, Str5, Str6, Str7, Str8, Str9, Str10, Str11, Str12, Str13, Str14, Str15, Str16, Str17, Str18, Str19, Str20

### 系统级测点 — 76 个

| 标识符 | 名称 | 数据类型 | 读写 | 单位 |
| --- | --- | --- | --- | --- |
| `Sta_Str10Run` | 簇10运行状态 | ENUM | R |  |
| `Sta_Str11Run` | 簇11运行状态 | ENUM | R |  |
| `Sta_Str16Run` | 簇16运行状态 | ENUM | R |  |
| `Sta_Str17Run` | 簇17运行状态 | ENUM | R |  |
| `Sta_Str18Run` | 簇18运行状态 | ENUM | R |  |
| `Sta_Str19Run` | 簇19运行状态 | ENUM | R |  |
| `Sta_Str5Run` | 簇5运行状态 | ENUM | R |  |
| `Sta_Str6Run` | 簇6运行状态 | ENUM | R |  |
| `Sta_Str12Run` | 簇12运行状态 | ENUM | R |  |
| `Sta_Str13Run` | 簇13运行状态 | ENUM | R |  |
| `Sta_Str14Run` | 簇14运行状态 | ENUM | R |  |
| `Sta_Str15Run` | 簇15运行状态 | ENUM | R |  |
| `SysDayDischarCount` | 当天放电次数 | INT | R | x |
| `SysDayCharCount` | 当天充电次数 | INT | R | x |
| `SysDischarAvaiE` | 堆可放电量 | FLOAT | R | kWh |
| `MinBattTemp` | 最低电池温度 | INT | R | °C |
| `MINTempBattStrNo` | 最低温度电池组号 | INT | R |  |
| `MINTempPoINTNo` | 最低温度电池所在组中点号 | INT | R |  |
| `SysTotalCharE` | 堆累计充电电量 | FLOAT | R | kWh |
| `SysTotalDischarE` | 堆累计放电电量 | FLOAT | R | kWh |
| `SysCharESingle` | 堆单次累计充电电量 | FLOAT | R | kWh |
| `SysDischarESingle` | 堆单次累计放电电量 | FLOAT | R | kWh |
| `SysCharAvaiE` | 堆可充电量 | FLOAT | R | kWh |
| `MaxTempPoINTNo` | 最高温度电池所在组中点号 | INT | R |  |
| `SysCharAvaiT` | 可用充电时间 | INT | R | min |
| `SysDischarAvaiT` | 可用放电时间 | INT | R | min |
| `SysDayDischarE` | 当天放电电量 | FLOAT | R | kWh |
| `SysDayCharE` | 当天充电电量 | FLOAT | R | kWh |
| `SysTemp` | 电池堆运行温度 | INT | R | °C |
| `MaxBattU` | 最高电池电压 | FLOAT | R | V |
| `SysMaxDischarILim` | 电池堆允许最大放电电流 | FLOAT | R | A |
| `SysMaxCharPLim` | 电池堆允许最大充电功率 | FLOAT | R | kW |
| `SysMaxDischarPLim` | 电池堆允许最大放电功率 | FLOAT | R | kW |
| `Sta_SysCB` | 电池堆电操状态 | ENUM | R |  |
| `SysU` | 电池堆电压 | FLOAT | R | V |
| `SysI` | 电池堆电流 | FLOAT | R | A |
| `SysSOC` | 电池堆SOC | INT | R | % |
| `SysSOH` | 电池堆SOH | INT | R | % |
| `SysMaxCharILim` | 电池堆允许最大充电电流 | FLOAT | R | A |
| `MaxUBattStrNo` | 最高电压电池组号 | INT | R |  |
| `MaxUPoINTNo` | 最高电压电池所在组中的点号 | INT | R |  |
| `MinBattU` | 最低电池电压 | FLOAT | R | V |
| `MinUBattStrNo` | 最低电压电池组号 | INT | R |  |
| `MinUPoINTNo` | 最低电压电池所在组中的点号 | INT | R |  |
| `MaxBattTemp` | 最高电池温度 | INT | R | °C |
| `MaxTempBattStrNo` | 最高温度电池组号 | INT | R |  |
| `Sta_SysRun` | 堆运行状态 | ENUM | R |  |
| `Sta_CharDischar` | 充放电状态 | ENUM | R |  |
| `SysInsulationR` | 电池堆绝缘电阻 | INT | R | kΩ |
| `SysTotalCharT` | 堆累计充电时间 | INT | R | s |
| `SysTotalDischarT` | 堆累计放电时间 | INT | R | s |
| `Err_PCSandBMSComm` | PCS和BMS通信故障 | ENUM | R |  |
| `Err_EMSandBMSComm` | EMS和BMS通信故障 | ENUM | R |  |
| `Err_ESBCMCommFault` | 堆内各主控失联汇总 | ENUM | R |  |
| `Err_ESBMMCommFault` | 堆内各从控失联汇总 | ENUM | R |  |
| `Err_StringsU` | 堆内各组电压异常 | ENUM | R |  |
| `Err_ContactorOpen` | 堆内接触器断开异常 | ENUM | R |  |
| `Err_ContactorClose` | 堆内接触器闭合异常 | ENUM | R |  |
| `Err_Nochar` | 充电禁止 | ENUM | R |  |
| `Err_NoDischar` | 放电禁止 | ENUM | R |  |
| `Ala_BMSAlarmSum` | BMS系统告警汇总 | ENUM | R |  |
| `Err_BMSFaultSum` | BMS系统故障汇总 | ENUM | R |  |
| `Err_VoltAcquFault` | 电压采集失联 | ENUM | R |  |
| `Err_TempAcquFault` | 温度采集失联 | ENUM | R |  |
| `Sta_Str1Run` | 簇1运行状态 | ENUM | R |  |
| `Sta_Str2Run` | 簇2运行状态 | ENUM | R |  |
| `Sta_Str3Run` | 簇3运行状态 | ENUM | R |  |
| `Sta_Str4Run` | 簇4运行状态 | ENUM | R |  |
| `Sta_Str20Run` | 簇20运行状态 | ENUM | R |  |
| `StringNumber` | 电池簇数量 | INT | RW |  |
| `SysFaultReset` | 系统故障复位 | ENUM | RW |  |
| `SysCBCtrl` | 电操控制 | ENUM | RW |  |
| `SysPowerCtrl` | 系统上下电控制 | ENUM | RW |  |
| `Sta_Str7Run` | 簇7运行状态 | ENUM | R |  |
| `Sta_Str8Run` | 簇8运行状态 | ENUM | R |  |
| `Sta_Str9Run` | 簇9运行状态 | ENUM | R |  |

## 关联

- [[esmu]]
- [[thing-model-structure]]
