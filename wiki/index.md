# Wiki Index

> 内容目录。每个 wiki 页面按类型列出,附一行摘要。
> 先读这里,再按需找页面。
> Last updated: 2026-08-07 | Total pages: 49

## Entities
<!-- 按字母序排列 -->

- [[acb-3p]] — (交流)框架断路器:配电主干保护,212 测点/61 事件/6 服务
- [[cabinet-door-sensor]] — 门磁传感器:柜门开闭状态,1 测点
- [[charging-pile-1p]] — 单相交流充电桩(单枪):充电计量 + 11 故障事件
- [[chint-sd-edge]] — Edge 系列边缘网关:网关自身运行资源监控,31 测点/4 服务
- [[chint-simulate-gate]] — 模拟网关:占位类型,四维度为空
- [[chint-soft-ware-edge]] — 软网关:占位类型,四维度为空
- [[electric-meter-1p]] — (交流)单相电表 V1.0.2:66 测点/6 事件/7 服务
- [[electric-meter-3p]] — 三相电表 V1.0.2:最全电能计量,184 测点/19 事件/7 服务
- [[environment-controller]] — 环境控制器:两路温湿度监测 + 上下限设置
- [[esmu]] — 电池簇管理单元:20 簇 × 37 测点 + 76 系统级测点(816)
- [[fire-detector]] — 火灾探测器:45 个三相电气参量测点(经确认文档无误)
- [[ghi-sensor]] — 太阳总辐射传感器:辐射量 + 日照时数
- [[ion-concentration-detector]] — 离子浓度检测仪:离子浓度/温度及偏差
- [[low-voltage-smart-connector]] — 低压智能接插件:三相电气量监测,1 故障记录事件
- [[mcb-1p]] — (交流)单相微型断路器:67 测点/18 事件/9 服务(含漏电检测)
- [[mcb-3p]] — (交流)三相微型断路器:96 测点/20 事件/9 服务
- [[mccb-3p]] — (交流)塑壳断路器:4 组测量回路,203 测点/54 事件/8 服务
- [[mix-inverter-1p]] — 单相混合逆变器:光储并离网,129 测点/26 事件/18 服务
- [[motor-protector]] — 马达保护器:电机电气量监测,属性最全(14)
- [[null-type]] — 空设备类型:纯占位,仅 3 个通用属性
- [[pcs]] — 储能变流器:175 测点/65 事件/41 服务(储能域最全)
- [[pdu-1p]] — 配电单元(1P):过压/欠压/过流/欠流报警 + 阈值设置
- [[pfc-panel]] — 无功补偿柜:补偿分组 + 负荷/补偿电气量
- [[pv-optimizer]] — 光伏优化器:组件级保护配置,14 服务
- [[pwzb]] — 微机保护装置:三相电气量监测,14 测点
- [[rain-sensor]] — 雨量传感器:降雨量/雨强统计
- [[smoke-sensor]] — 烟雾传感器:浓度报警 + 阈值设置(旧测点已废弃)
- [[string-inverter-3p]] — 三相组串逆变器:179 测点/65 事件(含 12 路 PV 电弧)
- [[temp-rh-sensor]] — 温湿度传感器 V1.0.2:温湿度报警 + 阈值设置
- [[vfd]] — 变频器:频率/转速/转矩等 10 测点
- [[water-sensor]] — 水浸传感器:水浸报警 + 阈值设置
- [[weather-station]] — 气象站:风速/温湿度/噪声/PM/CO2/气压/光照
- [[wind-direction-sensor]] — 风向传感器:1 测点(属性含疑似模板残留 `tt`)

## Measure Point References
<!-- 大设备测点全集参考页(>100 测点拆分) -->

- [[acb-3p-measure-points]] — 框架断路器测点全集(212,按前缀分组)
- [[electric-meter-3p-measure-points]] — 三相电表测点全集(184)
- [[esmu-measure-points]] — ESMU 测点全集(816:簇模板 × 20 + 系统级 76)
- [[mccb-3p-measure-points]] — 塑壳断路器测点全集(203)
- [[mix-inverter-1p-measure-points]] — 混合逆变器测点全集(129)
- [[pcs-measure-points]] — PCS 测点全集(175)
- [[string-inverter-3p-measure-points]] — 组串逆变器测点全集(179)

## Concepts

- [[thing-model-structure]] — 物模型四维度(属性/测点/事件/服务)结构与字段约定
- [[common-attributes]] — 跨设备公共属性(SN/版本/型号等,含"型号"三套命名并存)
- [[datatype-convention]] — 6 种数据类型与 DataDefine 结构、单位瑕疵记录
- [[device-category-and-domain]] — 设备大类(NORMAL/GATEWAY)与业务域划分、占位类型

## Comparisons

- [[circuit-breaker-family]] — 断路器家族:ACB/MCCB/MCB 1P/3P + 接插件 + 马达保护器
- [[electric-meter-family]] — 电表家族:单相 vs 三相 V1.0.2(服务集一致,测点规模差 3 倍)
- [[gateway-types]] — 网关类型:SDEdge(已整理)vs 模拟/软网关(占位)
- [[inverter-family]] — 逆变器家族:PCS/组串/混合/优化器(服务能力逐级递减)
- [[sensor-family]] — 传感器家族:智能报警型 vs 只读气象型

## Queries

<!-- 暂无归档查询 -->
