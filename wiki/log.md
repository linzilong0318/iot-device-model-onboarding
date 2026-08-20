# Wiki Log

> 所有 wiki 操作的时序记录。只追加。
> 格式:`## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> 超过 500 条时轮转:重命名为 `log-YYYY.md`,重新开始。

## [2026-08-07] create | Wiki initialized
- 领域: 公司内部 IoT 设备的物模型 (Thing Model / TSL)
- 路径: /opt/data/wiki
- 结构: SCHEMA.md, index.md, log.md + raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/

## [2026-08-07] ingest | 批量摄取 33 个物模型文档(35 文件,2 个弃用)
- 来源: raw/papers/ 下 33 个物模型 md 文档(原 35 个,删除弃用的 public_ElectricMeter.md、public_TempHumiditySensor.md)
- 用户确认: ① FireDetector 含大量电参量属正常;② 无版本后缀的两个物模型为弃用旧版,删除并跳过;
  ③ 设备分 NORMAL/GATEWAY 两类,模拟网关/软网关为空占位,Null 为纯占位
- SCHEMA.md 更新: 物模型三要素 → 四维度(属性/测点/事件/服务);新增业务域标签
- 创建 33 个实体页: acb-3p, cabinet-door-sensor, charging-pile-1p, chint-sd-edge,
  chint-simulate-gate, chint-soft-ware-edge, electric-meter-1p, electric-meter-3p,
  environment-controller, esmu, fire-detector, ghi-sensor, ion-concentration-detector,
  low-voltage-smart-connector, mcb-1p, mcb-3p, mccb-3p, mix-inverter-1p, motor-protector,
  null-type, pcs, pdu-1p, pfc-panel, pv-optimizer, pwzb, rain-sensor, smoke-sensor,
  string-inverter-3p, temp-rh-sensor, vfd, water-sensor, weather-station, wind-direction-sensor
- 创建 7 个测点参考页(>100 测点拆分): acb-3p-measure-points, electric-meter-3p-measure-points,
  esmu-measure-points(簇模板×20+系统级), mccb-3p-measure-points, mix-inverter-1p-measure-points,
  pcs-measure-points, string-inverter-3p-measure-points
- 创建 4 个概念页: thing-model-structure, common-attributes, datatype-convention, device-category-and-domain
- 创建 5 个对比页: circuit-breaker-family, electric-meter-family, gateway-types,
  inverter-family, sensor-family
- 更新 index.md(49 页)、SCHEMA.md

## [2026-08-07] lint | 0 issues (全库审计)
- 49 页:孤儿页 0、断链 0、索引完整(filesystem vs index 双向一致)、frontmatter 全部合法、
  标签全部来自 SCHEMA taxonomy、每页出链 ≥2
- 大设备实体页(acb-3p 232 行 / mccb-3p 225 / pcs 272 / string-inverter-3p 217 / mix-inverter-1p 206)
  略超 200 行阈值:测点已拆至参考子页,超限由事件/服务表(61~65 事件)所致,判定可接受,不再拆分
- 测点参考子页(576~714 行)为数据页性质,全量清单按前缀分组,保留
- 已知文档瑕疵(照实收录,见 datatype-convention):MCB 寿命单位 'x';StringInverter RatedP 单位 'V';
  LowVoltageSmartConnector RatedCurrent 单位 'V';WindDirectionSensor 属性 'tt' 疑为模板残留

## [2026-08-07] query | 物模型的事件(Event)是什么
- 用户提问事件维度的定义,回答基于 thing-model-structure + 各实体页事件表
- 要点:事件=设备主动上报(FAULT 223/ALARM 127/INFO 22),与测点(被动读取)相对;
  命名前缀 Error*/Alarm*/Info* 对应三类;概念已覆盖,未归档新页面

## [2026-08-07] update | 概念页补充"事件与测点的关联"
- 用户提问"事件和设备的点位有关联吗",经断路器/电表/烟雾传感器/混合逆变器多源抽查确认规律
- thing-model-structure.md 新增小节"事件与测点的关联":*Condition 触发条件与 *Output 输出均引用
  测点 ID;事件为平级独立维度,关联方向 事件→测点;附溯源标记
- sources 增加 public_ElectricMeter_1P_V1_0_2.md、public_MixInverter_1P_V1_0_2.md 两个验证源

## [2026-08-07] lint | 0 issues + read_file 编码误判根因调查
- 全库 lint 复查:49 页孤儿 0、断链 0、索引双向一致、frontmatter/标签/出链全合规;
  11 页 >200 行(测点数据页 + 大设备事件/服务表)与上次判定一致,维持可接受
- 编码扫描:全部 md 为合法 UTF-8,无 NUL/控制字符;raw/papers 34 个源文档为 CRLF(Windows 导出),
  wiki 页面为 LF
- read_file "Binary file" 误报根因:工具以 head -c 1000 取样本经 shell errors=replace 解码,
  第 1000 字节截断多字节 UTF-8 字符产生 U+FFFD,被 _is_likely_binary 判为二进制;
  实测当前 15/85 md 处于误判态,且随内容编辑漂移(改字即变)
- 规避:读取误判文件用 python3/sed 直接读字节

## [2026-08-07] query+deliver | PD7777 三相电能表接入分析(设备模型工作流首跑)
- 输入:三相电能表_PD7777-系列多功能数显表使用说明书.pdf(20页,正泰物联)
- 语义匹配知识库 → 推荐类型 public_ElectricMeter_3P_V1_0_2(三相电表),覆盖率 98/98 = 100%
- 生成设备模型 Excel:output/PD7777_设备模型_20260807.xlsx(模板 public_EN32_G2401FCI 结构,
  属性3/测点87/事件5/服务3,字段按 raw 文档标准定义;FromDeviceType 记录筛选清单)
- 分析报告:output/PD7777_分析报告_20260807.md
- 说明书本地配置参数(通讯/背光/轮显/密码/接线方式等)非物模型点位,未纳入
- 生成脚本:/opt/data/scripts/gen_device_model.py

## [2026-08-10] deliver | 为 PD7777 重新生成私有设备模型 project_PD7777
- 输入:【三相电能表】PD7777-系列多功能数显表使用说明书.pdf(正泰物联,20 页,重发;08-07 产物丢失)
- 语义匹配知识库 → 推荐类型 public_ElectricMeter_3P_V1_0_2(三相电表),覆盖率 98/98 = 100%
  (属性 3/3、测点 87/87、事件 5/5、服务 3/3,无未覆盖点位)
- 生成设备模型 Excel:output/PD7777_设备模型_20260810.xlsx(模板 public_EN32_G2401FCI 结构,
  属性3/测点87/事件5/服务3,字段按 raw 文档标准定义;FromDeviceType 记录筛选清单)
- 私有 ID:project_PD7777;私有产物不登记 index.md

## [2026-08-10] deliver | PD7777 三相电能表接入分析(重做,产物重建)
- 输入:三相电能表_PD7777-系列多功能数显表使用说明书.pdf(20页,正泰物联;用户重发,与 20260807 版本 MD5 一致 ca8ee331)
- 语义匹配知识库 → 推荐类型 public_ElectricMeter_3P_V1_0_2(三相电表),覆盖率 98/98 = 100%(属性3/测点87/事件5/服务3)
- 生成设备模型 Excel:output/PD7777_设备模型_20260810.xlsx(模板 public_EN32_G2401FCI 结构,ID=project_PD7777)
- 修正:上次脚本 MODEL_ID 误用 public_PD7777,本次改为 project_PD7777(铁律:生成物一律 project_)
- 说明:上次产物 output/ 已清空丢失,本次重建;点位清单 output/PD7777_点位清单.md
- 生成脚本:/opt/data/scripts/gen_device_model.py(已更新 OUTPUT/MODEL_ID)

## [2026-08-10] fix | PD7777 设备模型平台校验错误:Ires 不存在
- 平台校验反馈:FromDeviceType MeasurePoint 列含不存在标识符 Ires → 平台侧 public_ElectricMeter_3P_V1_0_2 类型无此测点
- 知识库 raw 文档 L207 及 wiki 实体页/子页/对比页均记录有 Ires(剩余电流 FLOAT R A)—— 知识库与平台不一致,raw 为平台旧版本导出
- 处置:从生成 Excel 移除 Ires(测点 87→86,FromDeviceType+MeasurePoint 两处),重新生成 output/PD7777_设备模型_20260810.xlsx;点位清单同步标注
- PD7777 剩余电流功能(表1,96×96 可选)标记为公有类型未覆盖
- 待办建议:核对平台侧最新类型,同步修正 raw 文档(未擅自改,等用户确认)

## [2026-08-10] fix | PD7777 Ires 校验误报更正
- 用户确认:知识库无错,Ires 在平台侧 public_ElectricMeter_3P_V1_0_2 类型中实际存在,此前"平台校验 Ires 不存在"系误报
- 撤销上一轮基于误报的修改:Excel 恢复含 Ires(测点 87,FromDeviceType+MeasurePoint),脚本 MP_SELECT 恢复 'In','Ires',点位清单恢复
- 知识库(raw 文档/wiki 页面)未做任何更改

## [2026-08-10] fix | 生成脚本迁移至 skill 目录
- gen_device_model.py 统一存放于 skill scripts/ 目录(/opt/data/skills/iot/iot-device-model-onboarding/scripts/),删除 /opt/data/scripts/ 工作副本,消除双副本漂移
- 同步修正规则:设备模型 Excel 四张子表(Attribute/MeasurePoint/Event/Service)只能写 FromDeviceType 未引用的新增点位,从类型引用点位仅留 FromDeviceType 清单
- PD7777 交付物(20260810)按旧逻辑生成,未重新生成(用户自行处理)


## [2026-08-10] deliver | PD7777-3H-E 数显谐波多功能表(以太网版)接入分析 + 设备模型生成
- 输入:【三相电能表】_PD7777-3H型数显谐波多功能表使用说明书.pdf(36页,正泰物联 2023-10,ModBus-TCP 以太网,带谐波 2-31 次/SOE/4DI/2DO)——与此前 PD7777-系列(RS485)为不同型号
- 语义匹配 → 推荐类型 public_ElectricMeter_3P_V1_0_2(三相电表);用户点位 80 个(属性10/测点62/事件4/服务4),覆盖 54,覆盖率 67.5%(属性0/10、测点50/62、事件0/4、服务4/4)
- 未覆盖 26 项均为平台类型缺失能力:通信/时钟/DO报警配置属性、四象限无功、逐次谐波(6组×30)、负序不平衡度、SOE 事件、通用 DO 报警机制
- 用户选择生成设备模型:output/PD7777-3H_设备模型_20260810.xlsx(ID=project_PD7777_3H,类型=public_ElectricMeter_3P_V1_0_2)
- FromDeviceType 引用:属性0/测点50/事件0/服务4(ClearECmd/DO1Cmd/DO2Cmd/FactoryResetCmd)
- 四张子表新增:属性26(通信/时钟/DO报警配置,原子粒度)、测点187(四象限4+负序不平衡2+SOE编程计数1+逐次谐波180)、事件5(SOE DI/DO/编程+2路DO报警,Output/Condition 推断标注)、服务0
- 关键决策:谐波含有率数组(6×30寄存器)经用户确认全拆 180 个逐次谐波测点(HRUa2~HRIc31)
- 推断项:RealTimeSet 合并 DATETIME、事件 Output/Condition、Language 枚举取值——均已在 Desc 标注
- 点位清单:output/PD7777-3H_点位清单.md;脚本 skill scripts/gen_device_model.py 已更新(支持 GEN_OUTPUT 覆盖 dry-run)


## [2026-08-10] fix | PD7777-3H 设备模型事件条件等式化(平台仅支持等式触发)
- 平台反馈:事件子表 *Condition 仅支持等式(点位 = 值,边沿触发),原 5 个事件中 SOE_DIChange/DOChange 条件为"状态变化"、SOE_Program 为"计数增加",非等式
- 按说明书(4.6 SOE/表3)分析:DI/DO 变位 = 状态翻转(0<->1),等式无法表达"翻转" → DI 变位拆 4路×接通(DIx=1)/断开(DIx=0)8 个事件;DO 报警与 DO 变位条件重叠,合并为 2路×有效(DOx=1,ALARM)/释放(DOx=0,INFO)4 个事件
- 编程事件:说明书仅累计计数/时间戳/类型/寄存器地址,无"编程发生"标志位,无法等式化 → 删除(SOEProgTotalNum 统计测点保留)
- 事件 5→12,全部等式条件(校验通过);Excel 重新生成 output/PD7777-3H_设备模型_20260810.xlsx,其余不变(引用50测点/4服务,新增属性26/测点187)


## [2026-08-10] fix | PD7777-3H 设备模型事件 Output 引用点位移入子表(平台报"Event 表设备数据类型不存在")
- 平台反馈:Event 表报"设备数据类型不存在";排查:模板成品案例(EN32_G2401FCI)Event 子表 168 个事件 Output 全部指向子表 MeasurePoint 点位,而本项目 12 个新增事件 Output=DI1/DO1 仅存在于 FromDeviceType 引用清单 → 平台 Event 校验(Output/Condition 引用解析范围为四张子表)解析不到数据类型
- 修复:DI1-DI4/DO1-DO2 从 FromDeviceType 引用(50→44 测点)移入子表 MeasurePoint 新增(193 测点,字段仍取类型标准定义 ENUM 0/1,DI R/DO W);事件 Output/Condition、服务 DO1Cmd/DO2Cmd Input 引用随之全部落在子表内(校验通过)
- 经验:设备模型 Excel 中,事件 Output/Condition 引用的点位必须在四张子表内可解析(新增事件不能引用仅 FromDeviceType 清单中的点位);服务 Input/Output 同理倾向子表点位(从类型引用服务 Input 引用类型点位有先例,可走类型解析)


## [2026-08-10] fix | PD7777-3H 设备模型重构:最大化类型引用,事件不新增
- 用户指示:事件不新增,从设备类型事件集引用子集;所有可通过类型引用的测点全部从类型引入
- 重构后 FromDeviceType 引用:属性 6(SN/ProductCategory/ProductSeries/SoftwareVersion/HardwareVersion/InstallLocation)、测点 54(原 44 + DI1-4/DO1-2 移回 + Q1EQ-Q4EQ 四象限无功改引用)、事件 13(按 3H 功能筛选,排除 AlarmSmoke/AlarmOverTempC1-4/AlarmOverIres 6 个设备无此功能事件)、服务 4
- 子表新增仅剩类型没有的:属性 26(通信/时钟/DO报警配置)、测点 183(负序不平衡度 2 + SOE 编程计数 1 + 逐次谐波 180)、事件 0、服务 0
- 关键修正:Qu1-4EnergyQ(四象限无功)此前误判未覆盖,实为类型 Q1EQ-Q4EQ 同义,改从类型引用
- 经验沉淀(用户):设备模型一般不新增事件,基本从设备类型事件集引用子集
- Excel 重新生成 output/PD7777-3H_设备模型_20260810.xlsx;技能 pitfalls 14/15 已补充


## [2026-08-17] action | PD7777-3H 生成点表(分支 A2:设备模型 + 说明书寄存器表)
- 输入:output/PD7777-3H_设备模型_20260810.xlsx + _PD7777-3H_raw.txt(说明书表2/表3 寄存器表、表4/表5 转换公式)
- 输出:output/PD7777-3H_点表_20260817.xlsx(272 行 = 属性 32 / 测点 237 / 服务 3;事件 0)
- 地址:266 个取自说明书十六进制寄存器表并转十进制(0x0000-0x02AE);dataType 全部说明书给出(int→i16、Uint→u16、float→float32、ulong→u32),0 推断
- 系数(表4):电压序分量×0.01、电流序分量×0.001、THD/逐次谐波/不平衡度×0.0001;电压/电流/功率按表5 为二次值不设系数(变比由 VoltageRatio/CurrentRatio 点位配置)
- 待补地址 6:SN/ProductCategory/ProductSeries/SoftwareVersion/HardwareVersion/InstallLocation(铭牌信息,说明书无寄存器)
- 不入表 14:事件 13(由测点状态触发,无独立寄存器)+ FactoryResetCmd(菜单功能无寄存器);ClearECmd/DO1Cmd/DO2Cmd 有控制寄存器已入表(DO1Cmd/DO2Cmd 与 DO1/DO2 测点共用寄存器)
- 脚本 skill scripts/gen_point_table.py 的 POINT_REG 已按 PD7777-3H 说明书配置(谐波 6 组×30 循环生成)


## [2026-08-17] fix | 点表规则更新:仅测点维度(属性/事件/服务不入表)+ PD7777-3H 点表重生成
- 用户指示:点表文件只关注四要素中的测点,属性/事件/服务不进入点表
- skill 更新:SKILL.md 6 处(Overview 点表定位/分支 A2 点位全集/模板结构/Pitfall 19 反转/Checklist/第 7 步总结)+ scripts/gen_point_table.py 6 处(build_rows 仅 MeasurePoint、merge_reg 去 no_reg、main 输出简化)
- PD7777-3H 点表重生成:output/PD7777-3H_点表_20260817.xlsx 覆盖,237 行全为测点(引用 54 + 新增 183),地址全有(待补 0),dataType 0 推断

## [2026-08-17] fix | 技能 1.3.0:引用服务/事件自动补 Input/Output 依赖点位 + PD7777-3H 模型重生成
- 用户反馈:PD7777-3H 模型导入平台成功,但平台按 Input/Output 引用自动补入缺失测点(ClearE/FactoryReset 等),说明这些点位是平台校验对象
- 技能更新:SKILL.md(分支 A 引用完整性规则 + Pitfall 21 + Checklist + 脚本说明,版本 1.2.0→1.3.0)+ scripts/gen_device_model.py 新增 ensure_refs_present(自动补服务 *Input / 事件 *Output 及 *Condition 等式左侧点位到 FromDeviceType 引用;修正事件/服务 ID 与点位同名误判,如事件 Ala_RevP 的 Output 也是测点 Ala_RevP)
- PD7777-3H 模型重生成:output/PD7777-3H_设备模型_20260817.xlsx,引用测点 54→69(+ClearE/FactoryReset + 13 个 Ala_* 告警测点);四张子表不变(属性 26/测点 183/事件 0/服务 0)

## [2026-08-17] action | PD7777-3H 点表同步(模型引用测点 54→69 后重生成)
- 输入:output/PD7777-3H_设备模型_20260817.xlsx(引用测点 69 = 54 + 服务 Input 2 + 事件 Output 13)
- 输出:output/PD7777-3H_点表_20260817.xlsx 覆盖,252 行 = 引用 69 + 新增 183,全部为测点
- ClearE 测点入表:地址 0x000D(CLRE 清零寄存器,十进制 13,[03,06],u16);原 ClearECmd/DO1Cmd/DO2Cmd 服务键从 POINT_REG 移除(服务不入表,DO1/DO2 测点行已覆盖遥控寄存器)
- 待补地址 14:FactoryReset(菜单功能无寄存器)+ 13 个 Ala_* 告警标志测点(说明书仅有 DO 报警机制,无独立状态字寄存器);均保留行、address 留空
- dataType 推断 0;地址进制转换 238(0x 十六进制→十进制)

## [2026-08-17] fix | 技能 1.4.0:点表无地址点位不生成行(以说明书为准)+ PD7777-3H 点表重生成
- 用户指示:点表以设备说明书为准,说明书查不到点位/地址时点表文件不保留空行,但须告知用户哪些点位未找到地址
- 技能更新:SKILL.md 6 处(分支 A2 点位全集/无寄存器点位/脚本说明/第 7 步总结/Pitfall 18/Checklist)+ scripts/gen_point_table.py(merge_reg 无地址点位不再保留行,todo 语义改为"未找到地址、不生成行"清单)
- PD7777-3H 点表重生成:output/PD7777-3H_点表_20260817.xlsx 覆盖,252→238 行(移除 FactoryReset + 13 个 Ala_* 空行);未找到地址 14 个已在总结告知用户

## [2026-08-17] action | PD7777 系列生成设备模型(分支 A:类型引用 + 私有新增)
- 输入:【三相电能表】PD7777-系列多功能数显表使用说明书(PD7777-□S3-EL,表4 ModBus 寄存器表完整,20页)
- 输出:output/PD7777_设备模型_20260817.xlsx(模板 public_EN32_G2401FCI.xlsx)
- 引用 FromDeviceType:属性 6(通用全引用)+ 测点 74(电压/电流/功率/视在/PF/频率/总谐波 THDU+THDI/正反有功+四象限无功电能含费率1-4/变比/DI1-8/DeviceTime/ClearE)+ 事件 0 + 服务 1(ClearECmd)
- 新增子表:属性 11(Password/Net/PulseOutput/DisplayTime/BackLightTime/232协议波特率地址/485协议波特率地址)+ 测点 3(AlarmStatus 综合故障字/DO1Status/DO2Status 只读状态);事件/服务 0
- 关键决策:DO1/DO2 类型为 W 控制方向,本设备寄存器只读状态 → 不引用,私有新增 DO1Status/DO2Status(ENUM R);事件因无独立标志位(仅综合 Alarm 字)不引用;不平衡度/最大需量/零线/剩余电流表1声称但表4无地址不建模;复费率时区表(6000H+)配置只读不入模型
- 引用完整性:ClearECmd.Input=ClearE 已在引用清单,无自动补;脚本 /opt/data/scripts/gen_pd7777_model.py

## [2026-08-17] action | PD7777 系列生成点表(分支 A2:设备模型 + 说明书表4 寄存器表)
- 输入:output/PD7777_设备模型_20260817.xlsx + PD7777-□S3-EL 说明书表4 ModBus 地址表
- 输出:output/PD7777_点表_20260817.xlsx(77 行,全为测点:引用 74 + 新增 3;事件/属性/服务不入表)
- 地址:77 个全取说明书十六进制寄存器表并转十进制(0x0002-0x2044),未找到地址 0 个
- dataType:全部说明书给出(float32/单精度浮点 2word、u16/16 位有符号 1word),0 推断
- 系数:电压×0.1/电流×0.001/功率×0.1/PF×0.001/频率×0.01 按表5 转换公式;谐波为直接百分数
  (float32,无倍率,不设系数);电能为二次值(变比由 VoltageRatio/CurrentRatio 配置,不设系数)
- 盘点位 DI1-8 共用 0x0028(mask bit0-7)、DO1Status/DO2Status 共用 0x002A(mask bit0/1,map 0=断开/1=接通);
  DeviceTime 为 0x002F-0x0034 六个时钟寄存器合并(同 3H RealTimeSet 风格)
- 属性(引用 6 + 新增 11)/事件 0/服务 ClearECmd 均不入表;脚本 /opt/data/scripts/gen_pd7777_point_table.py


## [2026-08-20] action | NJBK8 马达保护器生成设备模型 + 点表(分支 A + A2)
- 输入:input/【马达保护器】NJBK8数据定义.xlsx(3 sheet:数据定义 381 变量 / Modbus对象字典 / Sheet1)
- 推荐类型:public_MotorProtector(配电域,14 属性/40 测点/0 事件/0 服务)
- 四维度覆盖:属性 覆盖10/未覆盖203;测点 覆盖39/未覆盖36;事件 覆盖0/未覆盖4;服务 覆盖0/未覆盖10
- 用户选择:设备模型 + 点表(协议 ModbusRTU_Vega_ARM64_V1.1.0);按用户提示适当筛选
- 输出1:output/NJBK8/NJBK8_设备模型_20260820.xlsx(project_NJBK8)
  - FromDeviceType 引用:属性10(额定参数)+ 测点39(电气量)
  - 新增子表:属性32(核心保护配置)+ 测点17(运行统计7+DI/DO状态10)+ 事件4(跳闸/告警/操作/状态变化)+ 服务10(控制命令)
  - 校验:verify_output.py --kind model passed(0 errors)
- 输出2:output/NJBK8/NJBK8_点表_20260820.xlsx(ModbusRTU)
  - 56 行(全部测点:引用39+新增17);address 十六进制十进制转换 56;dataType 推断 0;未找到地址 0
  - 校验:verify_output.py --kind point passed(0 errors)
- 筛选说明:筛除谐波(9)/电流相位角(3)/总功率(4)等非核心测点;筛除厂内参数(21)/细分通讯配置等非核心属性
