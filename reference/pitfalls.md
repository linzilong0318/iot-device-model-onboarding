# 踩坑记录 (Common Pitfalls)

> 本文件收录设备接入物模型工作流中积累的踩坑经验，按主题分组。
> SKILL.md 中的工作流规则大多源于这些实战教训，遇到疑虑时回查本文件。
> 新增踩坑时追加到对应主题分组末尾，并同步更新 SKILL.md 相关规则。

## 一、字段来源与 ID 前缀

1. **把用户文档的命名直接写进 Excel** —— 违反铁律，必须映射到知识库标准定义。
   引用点位的标识符、名称、数据类型、单位、枚举、必填等字段一律取自知识库类型页面
   （raw 文档）的标准定义；用户文档仅用于识别"需要哪些点"。

2. **ID 前缀写错** —— 生成物一律 `project_`，绝不 `public_`。
   `public_` 仅用于知识库公有类型，以及设备模型 `*DeviceType` 字段对公有类型的引用。

3. **私有类型擅自登记公有 wiki** —— 私有产物只产出 Excel，不回灌 `index.md`。
   知识库只收 `public_` 公有类型；私有类型/模型如需沉淀，另行与用户确认。

## 二、知识库检索与语义匹配

4. **只看实体页不看 measure-points 子页** —— 大设备测点全在子页，漏看会误判覆盖率。
   测点数 >100 的实体页只含前缀分组表，完整清单在 `wiki/entities/<slug>-measure-points.md`，
   必须读子页。

5. **语义匹配太松（名称沾边就算）或太严（要求标识符一致）** —— 用单位/类型/枚举交叉验证，
   悬空项必须查 wiki 或标未覆盖，不留模糊。判定依据综合：名称语义 > 单位 > 数据类型 > 枚举值；
   拿不准时用 `search_files` 在 wiki 里搜相关点位看其他设备页怎么命名。

6. **覆盖率定义无参考标准** —— 不算覆盖率百分比，改为直接呈现四维度覆盖明细
   （属性 覆盖 x 个/未覆盖 y 个），让用户自行判断是否合适。

6a. **匹配只记类型不记具体点位导致返工** —— S2 匹配子 agent 的 Attribute/MeasurePoint 段只返回
    `matched_type_id`（公有类型）而漏掉命中的具体公有点位 `matched_point` 时，merge 出的 match.json
    会有大量映射项缺 `matched_point`，S3 无法直接构造 select，必须再派补齐子 agent（403X 实测 6+53 项）。
    正确做法：每个 `matched_type_id` 条目同步给出 `matched_point`（公有类型原始定义里真实存在的标识符），
    一次匹配到位，杜绝补齐步骤。匹配子 agent 的 context 必须显式要求同时输出 matched_point。

## 三、说明书解析

7. **说明书属性/服务藏在正文就跳过** —— 属性与服务最容易漏，必须通读全文找全。
   - 属性常散落在"技术参数/规格"章节正文，不一定是表格（额定电压、SN、版本…）
   - 服务在"功能说明/操作说明/远程控制"章节，最不规整，需从功能描述中归纳
     （如分合闸、复位、阈值设置、参数下发）

8. **read_file 对含中文 md 可能误报 Binary** —— 用 `python3 io.open(encoding='utf-8')` 读。
   根因：工具以 head -c 1000 取样本经 shell errors=replace 解码，第 1000 字节截断多字节
   UTF-8 字符产生 U+FFFD，被判为二进制；实测随内容编辑漂移（改字即变）。

## 四、设备模型生成（分支 A）

9. **分析完不汇报直接生成** —— 必须先向用户呈现推荐类型、四维度覆盖明细与缺失清单，
   由用户选择生成路径（设备模型 / 设备类型 / 仅保留结论）；含点表路径时还要选通信协议。

10. **把 FromDeviceType 引用的点位重复写进四张子表** —— 四张子表只能写新增点位
    （FromDeviceType 中没有的）；引用点位只留在 FromDeviceType 清单，绝不重复。

10a. **设备类型中已有点位 ID 不得自定义同名点位** —— 平台铁律：`add`（子表新增）里任
    一 Attribute/MeasurePoint 的 ID 只要在公有类型对应维度存在，就不能再自定义同名点位，
    平台导入报错。即使设备方向/字段与类型不符（如类型 R 只读、设备寄存器 RW），也**不能**
    通过 add 私有重定义同名来改方向；必须从类型 `select` 引用（接受类型定义的方向/字段），
    需要下发能力时用**私有 Service**（Input=该测点）补齐。脚本 generate_model 已内置此检查，
    命中即抛错提示引用而非重定义。（HSM-WT11 SensitivitySetting 教训）

10b. **数值型新增点位必须带 DataDefine** —— 平台铁律：Attribute/MeasurePoint 的
    `*DataType` 为 INT/FLOAT 等数值类型时，必须提供 `DataDefine`（含 minValue/maxValue）；
    范围未知也要填 `{"minValue":"","maxValue":""}`，否则平台导入报错。生成脚本
    validate_point_groups 已内置此检查，缺失即报错。

10c. **ENUM 的 DataDefine 必须用平台 mappingItemList 格式** —— 平台导入要求
    `{"mappingItemList": [{"itemI18nValue":{"default":"正常","en_US":"Normal"}, "itemValue":"正常","itemKey":"0"}, ...], "enumKeyCode":"INT"}`，
    不是旧式 `{"enum":{"0":"正常"}}`（403X 实测旧式被平台侧视为格式错误）。生成器 `fill_sheet`
    现会对 ENUM 新增点位自动调用 `normalize_enum_datadefine` 把旧式转成平台格式再写入，因此
    交付物一定正确；旧式仅作兼容输入，校验器也兼容两者。写 spec 时仍建议直接用平台格式，
    英文未知时 `itemI18nValue.en_US` 可复用 `default`。

11. **引用服务/事件时漏掉其 Input/Output 依赖点位** —— 服务 `*Input`、事件 `*Output`
    （及 `*Condition` 等式左侧）引用的点位必须在模型点位全集中；缺失时平台导入会按
    引用自动补点（PD7777-3H 实测：平台自动补入 ClearE/FactoryReset 及 13 个 Ala_*
    告警测点），说明这些点位是平台校验对象。生成脚本 `ensure_refs_present` 会自动
    补入 FromDeviceType 引用，不必手改 SELECT；注意事件/服务 ID 与点位同名
    （如事件 Ala_RevP 的 Output 也是测点 Ala_RevP）时，检查须按测点/属性维度，
    不能因 ID 同名跳过。

12. **事件 *Condition 写成非等式（如"状态变化"/"计数增加"）** —— 平台事件触发条件
    仅支持等式"点位 = 值"（边沿触发），如 `Ala_RevU = 1`。说明书里的"变位/翻转"
    （SOE DI/DO）必须拆为接通/断开两个等式事件（如 DI1 = 1 / DI1 = 0）；
    "计数增加"类（如编程事件总次数）说明书无标志位则无法建事件，删除并说明，
    计数寄存器保留为统计测点即可。

13. **新增事件的 Output/Condition 引用了仅存在于 FromDeviceType 清单的类型点位
    （如 DI1/DO1）** —— 平台校验 Event 表时，Output/Condition 引用的点位必须在
    四张子表内可解析，否则报"设备数据类型不存在"。修复：把被引用点位（如 DI1-4/
    DO1-2）从 FromDeviceType 引用移入子表 MeasurePoint 新增（字段仍取类型标准定义）；
    服务 Input/Output 同理倾向子表点位（从类型引用服务、Input 引用类型点位有成功先例）。

14. **设备模型凭空新增事件** —— 经验铁律：设备模型一般不新增事件，基本从设备类型的
    事件集中引用【子集】（按设备功能筛选：设备没有的功能对应事件不引用，如烟感/
    测温/剩余电流）；新增事件仅在类型确无对应且设备确有明确事件定义时才考虑，
    且须满足等式条件（pitfall 12）与子表引用（pitfall 13）双重约束。

15. **测点能引用却不引用** —— 用户倾向"能通过设备类型引用的点位全部从类型引入"
    （从类型引用点位 = FromDeviceType 清单，字段由类型兜底，平台校验风险最低）；
    子表新增只放类型中确实没有的设备点位（如逐次谐波、细分不平衡度）。
    与 10a 呼应：类型里有的点位一律走引用，别想用 add 重命名/重定义绕开。

## 五、点表生成（分支 A2）

16. **点表点位名称/标识符与设备模型漂移** —— 平台按名称+标识符映射，点表的
    pointName/pointKey/unit 必须从生成的设备模型 Excel 读取，绝不从用户文档直抄。

17. **把平台模型数据类型直接当寄存器类型写入点表** —— 模型 FLOAT/INT/STRING 与寄存器
    u32/float32/str 是两层概念，dataType 以说明书寄存器定义为准；说明书未给时按
    映射表推断并在总结标注。

18. **寄存器地址进制错误或臆造** —— 模板要求十进制，说明书常为十六进制（0x…），必须转换；
    说明书查不到地址的点位不生成行（点表以说明书为准），但总结中必须告知用户
    哪些点位未找到地址，绝不臆造地址。

19. **点表混入属性/事件/服务** —— 点表只收录测点（MeasurePoint）维度点位；属性/事件/服务
    一律不入表（属性为静态配置、事件由测点状态触发、服务经平台下发，均不占采集行），
    无论说明书是否有对应寄存器。

20. **模板说明行/示例行未清理** —— 点表模板第 2 行字段说明、第 3 行示例必须删除，
    交付物只含表头 + 数据行。

## 六、模板与工具

21. **模板 WPS 加密还硬填** —— 先确认已拿到未加密版；没拿到就先输出结论并说明模板阻塞。

## 七、留痕

22. **分析报告写成 md 文件** —— 分析结论直接总结输出给用户（终端消息），不生成 md 报告文件；
    生成操作追加 `wiki/log.md`，私有类型/模型不登记 `index.md`。


## 八、寄存器解析与 Modbus 区间映射(QA 高频,两子技能并入)

> 本节固化自子技能 modbus-register-mapping 与 protocol-points-parsing,避免主流程再额外加载它们作补充。
> 语言无关,换任何协议/设备都会再犯。

### 8.1 有符号/无符号字符串判坑(最大坑)

`'int16' in "uint16"` 为 **True**——`uint16` = `u`+`int16` 是子串。用 `in` 会把无符号电压/发电量误判成有符号 i16,符号位解码全错。必须负向前瞻排除 `u`:

```python
def dtype_reg(ev):
    if re.search(r'uint32|\bu32\b', ev): return 'u32', 2
    if re.search(r'(?<!u)int32|\bi32\b', ev): return 'i32', 2
    if re.search(r'(?<!u)int16|\bi16\b', ev): return 'i16', 1
    return 'u16', 1          # uint16 / enum16
```

### 8.2 缩放系数正则坑(第二大坑)

source_evidence 同时含寄存器地址 `0x0016` 与缩放 `x0.1`。`r'x([0-9.]+)'` 会误匹配 `0x0016` 的 `x0016` → 系数=16(实为地址)。必须要求 `x` 前是词边界/空格:

```python
m = re.search(r'\bx([0-9.]+)\b', ev)   # 匹配 " x0.001"，不匹配 "0x0016"
```
`x1` → `coefficient=None`(无缩放)。排错:把生成的 coefficient 与 address 对照打印,若系数等于地址值,就是正则把地址吃进来了。

### 8.3 registerCount 宽度表

`u8/i8/u16/i16/bool/bits`=1;`u32/i32/float32/ieee754_f32`=2;`u64/i64/double64`=4。
`registerCount >= REGISTER_WIDTH[dataType]`,否则校验报错。点表 dataType 以说明书寄存器定义为准(pitfall 17),与平台模型 FLOAT/INT/STRING 是两层概念。

### 8.4 Modbus 寄存器区间 → 四维度映射

| 区间/功能码 | 维度 |
| --- | --- |
| 输入寄存器(功能码 0x04:0x0000、0x8000-0x8600) | MeasurePoint(电压/电流/功率/频率/温度/绝缘/漏电/发电量/运行状态) |
| 保持寄存器(0x03:0x2000-0x2C00)参数设定(电网保护/降额/无功/LVRT-HVRT/使能/校准) | Attribute |
| RW 写命令、遥控寄存器(0x2700 控制命令组、0x2B00 写命令) | Service |
| 故障/告警字(0x8400 区 + 位定义表 Bit_P) | Event,condition 等式 `FaultX.BitY=1`,`inferred:true`+`need_user_confirm:true` |
| 工厂测试区(0x8600 ADC、0x2A00)、柱状图/历史批段(0x2B46/0x2C00)、IV 曲线(0x8700) | 逐条只读/工厂级,一般不进点位 |

### 8.5 两类行结构(寄存器表 vs 位定义表)

- **寄存器表** ~16 列(`Start,End,Size,R/W,Name,寄存器名,Type,Scale Factor,Unit,...`);`Scale Factor`(10^k)+`Unit` → 实际值 = 原始值 × 10^(ScaleFactor),address 保留原始寄存器地址。`R/W` 含 RO/RW/WO(WO 多为控制命令)。
- **位定义表**(Bit_S/Bit_P/Bit_B)~7 列(`Register Address,Type,Bit Position,英/中文描述,Fault Code`);寄存器地址只在**首行**出现一次,其余行 Bit15..Bit0 且地址栏空白 → 按"地址列非空"分组展开每个 bit。Bit_P=故障/告警位、Bit_S=系统运行状态字、Bit_B=工厂引脚(一般不进点位)。
- 读取脚本模式(compact dump):
  ```python
  for r in t["rows"]:
      r = [str(c) if c is not None else "" for c in r]
      r = r + [""] * (16 - len(r))      # 短行(合并单元格/保留区)补列,避免 IndexError
      if r[0] and r[0] != "Start":       # 跳表头与空行
          print(r[0], "|", r[5], "|", r[6], r[7], r[8], "|", r[14][:70])
  ```

### 8.6 points.json 解析级要点

- 中文源字符串含 `{0X0004:uint16 x0.01}` 时**不要**用 `.format(Sheet)` → KeyError(`'{0X0004}'`);用常量拼接或转义 `{{ }}`。
- Bit_P 常 150+ 命名故障位:只选"有英文描述的命名保护"建**代表事件**,不需要一个不漏(合并了哪些要向用户说明)。
- 有的版本配置 sheet(如 0X2E00、0X2300 保留)可能空缺 — extraction 没有的 sheet 别硬凑,摘要说明即可。

### 8.7 点表构造(点表不足/未覆盖场景)

- **一个公有测点对应多个同值用户寄存器**(公共 0X0000 与专用 0X8100 各有 copy):点表一行一个点,显式维护 `MAIN={公有id:[首选用户id]}` 表,优先取专用区;按**公有 id** 查(误写成按首个用户 id 查永不命中,会把点误入"未生成")。
- **RW 控制点无用户测点引用**(开关机/重启/复位/扫描是写命令,match 无映射):单独硬编码(读03+写06 保持区),并从待生成清单剔除,别漏进"未生成"。
- **状态位点**(Err_/Ala_ 只存在于故障状态字位映射、无独立寄存器):不生成行、不臆造地址,归入"未生成清单"在摘要告知。
- **校验语义**:`verify_output.py --kind point` 只校验点表**已存在**的行(pointKey 唯一/在 model 测点/name/unit 一致/Modbus 语义),**不**要求覆盖全部 model 测点 —— 未生成点不影响 `passed`。
- **生成器默认落盘**:`gen_point_table.py` 未给显式输出路径时按 `HERMES_SESSION_ID` 派生目录,可能与所用工作目录不一致——务必传显式路径 `python gen_point_table.py <point_reg.json> /abs/path/<模型>_<协议>.xlsx`(主流程已由 workspace.py 收敛,子 agent 场景尤须注意)。
