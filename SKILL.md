---
name: iot-device-model-onboarding
description: Use when 用户给设备说明书(PDF/DOCX/Excel)要匹配物模型设备类型或生成物模型 Excel。
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [iot, thing-model, tsl, device, excel, wiki]
    category: iot
    related_skills: [llm-wiki, xlsx, pdf, docx, ocr-and-documents]
---

# 设备接入物模型辅助工作流(泰无界平台)

## Overview

用户拿到一台设备的说明书(PDF/DOCX),目标是把它接入泰无界平台(平台要求按物模型接入)。
本工作流:解析文档四维度点位 → 在知识库(/opt/data/wiki,33 个公有设备类型)中语义匹配最合适的
设备类型 → 把分析结果(推荐类型、覆盖率、未覆盖点位)汇报给用户 → 由用户交互式选择
生成【私有设备模型】或【私有设备类型】Excel。

层级关系:设备类型(抽象、点位全集)→ 设备模型(从类型筛选部分点位)→ 点表(模型每个点位的取数定义)。
例:类型=三相电表,模型=三相电表-国家电网专用。
点表:设备模型是抽象描述(有哪些点位),点表定义如何从设备获取这些点位信息(每个点位一行的
寄存器地址/数量/功能码/数据类型/系数等);平台按"点位名称 + 点位标识符"把点表映射到设备模型,
故点表的点位名称与标识符必须与设备模型保持一致。
**点表只收录测点(MeasurePoint)维度点位**,属性/事件/服务不进入点表
(属性为静态配置、事件由测点状态触发、服务经平台下发)。

**ID 前缀铁律**:知识库存放的是公有设备类型,ID 前缀一律 `public_`;
给用户生成的设备模型或设备类型均为用户私有,ID 前缀一律 `project_`
(如 `project_PD7777`)。私有产物不登记公有知识库。

**交互式决策**:分析完成后不直接生成,先把推荐结论与缺失情况告诉用户,由用户选择
生成新设备类型(私有)还是直接生成设备模型(私有);最终分析结论直接总结输出给用户,
不写 md 分析报告文件。

## When to Use

- 用户提供设备说明书 PDF/DOCX,要求接入平台、匹配设备类型、生成物模型
- 用户问"我的设备该选哪个设备类型/怎么生成物模型 Excel"
- 需要从知识库选类型并产出 Excel 交付物时

不使用:仅知识库问答(用 llm-wiki)、仅生成 Excel(用 xlsx)、仅解析 PDF(用 pdf/ocr-and-documents)、
仅解析 Excel 输入(用 xlsx)。

## 前置资源

- 知识库:`/opt/data/wiki`(entities/ 33 个公有设备类型页;大设备完整测点在 `*-measure-points` 子页)
- 模板(已解密校准,统一存放于 `templates/` 目录,结构见第 6 步"模板结构"节):
  - 设备模型模板(成品案例):`templates/model_template.xlsx`(原 public_EN32_G2401FCI.xlsx)
  - 设备类型模板(空白导出):`templates/type_template.xlsx`(原 public_Null.xlsx)
  - 点表模板(按通信协议分文件,与上述模板同目录,文件名即协议名):
    `ModbusTCP_Vega_ARM64_V1.1.0.xlsx` / `ModbusRTU_Vega_ARM64_V1.1.0.xlsx` /
    `ModbusRTU_SG_V1.0.0.xlsx` / `ModbusRTU_SMG_RTOS_V1.0.0.xlsx` /
    `DL_T_645_Vega_ARM64_V1.1.0.xlsx` / `DL_T_698_Vega_ARM32_V1.1.0.xlsx` /
    `MQTT_Vega_ARM64_V1.0.0.xlsx` / `IEC_104_Vega_ARM64_V1.0.0.xlsx` /
    `OPC UA_Vega_ARM64_V1.0.0.xlsx` / `Gateway_Vega_ARM64_V1.0.0.xlsx`
    各协议列定义不同(Modbus 系列有 address/registerCount/functionCode,MQTT 有 topic/jsonpath,
    OPC UA 有 tag 等),生成时按用户选择的协议选模板,按表头列名映射填充
  - 注:模板文件名带 public_ 仅表示模板源自公有类型导出;用它生成的内容 ID 仍必须用 project_
- 输出目录:`/opt/data/output/`(不存在则创建)
- Python 环境(使用全局 python 解释器):
  ```bash
  uv pip install --python $(python -c "import sys;print(sys.executable)") -r requirements.txt
  ```
  后续读写 Excel / 解析输入 Excel 统一用全局 `python` 解释器(openpyxl 已在 requirements.txt 声明)。
- 踩坑记录:`reference/pitfalls.md`(按主题分组的实战教训,遇疑回查)

## 工作流

### 0. 会话定向(llm-wiki 约定)

若本会话尚未读过,先读 `wiki/SCHEMA.md` + `wiki/index.md` + `wiki/log.md` 尾部(最后 30 行),
了解标签体系、页面清单与近期活动。
完成标准:已确认知识库当前页面数、候选类型清单来源(index.md Entities 节)。

### 1. 解析文档 → 四维度点位清单

用 pdf / docx / ocr-and-documents / xlsx 技能提取文本(说明书可能含扫描页,必要时 OCR;
表格优先用表格解析,不要只按纯文本流读)。

**输入格式分支**:
- PDF / DOCX:按下述"说明书形态提示"通读全文提取四维度点位
- Excel(.xlsx/.xls):用户提供的 Excel 可能是以下形态之一,**先识别表头结构再决定提取策略**:
  - **寄存器点表形态**(最常见):表头含 address / 寄存器地址 / 功能码 / 数据类型 / 系数 等
    通讯列 → 提取为测点的寄存器信息(供生成点表),点位名称列映射为测点名;此类 Excel
    通常只覆盖测点维度,属性/事件/服务仍需从其他来源(或追问用户)补充
  - **物模型点位清单形态**:表头含 *ID / *DataType / *R/W / *EventType / *Input 等物模型
    标准列,或按属性/测点/事件/服务分 sheet → 直接按四维度提取点位(相当于替代说明书角色)
  - **混合形态**:同一文件含多个 sheet(如"点位清单"+"寄存器表"),分别按上述策略提取后合并,
    以点位名称/标识符为关联键
  - 识别方法:读首个 sheet 表头,匹配通讯列关键词(address/寄存器/功能码)→ 寄存器点表;
    匹配物模型列关键词(*ID/*DataType/*EventType)→ 物模型清单;两者都不匹配时遍历所有
    sheet 再判;仍无法识别时向用户确认 Excel 用途
  - 多 sheet 时逐 sheet 解析,合并去重(以标识符/名称为键);Excel 单元格公式/合并单元格
    需展开(用 openpyxl data_only=True 取值,合并区域取左上角值填充)

说明书形态提示(与物模型文档不同,需主动找):
- 属性(Attribute):常散落在"技术参数/规格"章节正文,不一定是表格(额定电压、SN、版本…)
- 测点(MeasurePoint):通常有规整的"点位表/通讯点表/数据点表",最可靠
- 事件(Event):在"告警/故障/事件说明"章节,常为表格(故障码、告警码)
- 服务(Service):在"功能说明/操作说明/远程控制"章节,最不规整,需从功能描述中归纳
  (如分合闸、复位、阈值设置、参数下发)

产出:用户设备点位清单,按四维度分组,每个点位记录尽可能多的字段:
`标识符(如有) | 中文名/描述 | 数据类型 | 单位 | 读写方向 | 枚举/取值范围 | 来源章节`,
测点/属性另尽量收集寄存器信息(供生成点表):`寄存器地址(注意进制,说明书常为
十六进制 0x…,记录原始写法,生成点表时统一转十进制) | 寄存器数量 | 功能码(读/写) |
系数/基值 | 字节序 | 位索引`;说明书无寄存器表时标注"无寄存器信息"。
**结构化产物**:`/opt/data/output/<设备名>/points.json`(四维度点位清单,JSON 格式,
含 DataDefine 完整结构;推断项打 `inferred: true` 标记;寄存器信息保留原始进制写法)。
该文件是后续匹配、生成、点表对齐的唯一数据源,会话中断可断点续跑。
完成标准:四维度点位逐条列入 points.json,标注哪些字段是文档明确给出、哪些是推断。

### 2-3. 候选检索 + 语义匹配(合并,产出 match.json)

- 读 `wiki/index.md` Entities 节,按业务域(配电/储能/充电/光伏/环境监测…)、设备大类
  (NORMAL/GATEWAY)、设备功能关键词(电表/断路器/逆变器/传感器…)圈定候选类型 2~6 个
- 每个候选读其实体页:`wiki/entities/<slug>.md`
  - 测点数 >100 的实体页只含前缀分组表,完整清单在 `wiki/entities/<slug>-measure-points.md`,必须读子页
- **语义匹配,不是标识符精确匹配**:用户文档名称(可能"电压A相")与知识库标识符
  (如 `MeterVoltageA`)只要语义同指即算覆盖;允许别名/中英差异/缩写
- 判定依据综合:名称语义 > 单位 > 数据类型 > 枚举值;拿不准时用 `search_files`
  在 wiki 里搜相关点位看其他设备页怎么命名
- 一个用户点位匹配多个类型点位时取语义最贴近者;同一类型点位不可重复计
- **结构化产物**:`/opt/data/output/<设备名>/match.json`,每个用户点位 → 命中的类型
  标识符(或 `uncovered: true`)+ 匹配依据(`basis`);争议项标 `need_user_confirm: true`
- **不算覆盖率、不打置信度**(覆盖率定义无参考标准,改为直接呈现四维度覆盖明细让用户判断)

完成标准:用户全部点位在 match.json 中都有明确结论(覆盖某标识符 / 未覆盖),无悬空项;
争议项已标 need_user_confirm。

### 4. 交互式决策(核心步骤)

分析完成后**不直接生成文件**,先向用户完整汇报,再由用户选择生成路径:

汇报内容:
- 推荐类型(名称、业务域、四维度点数),或"知识库无合适类型"
- **四维度覆盖明细**(不算覆盖率百分比):属性 覆盖 x 个[...] / 未覆盖 y 个[...];
  测点/事件/服务同理
- 未覆盖点位清单(点位名、所属维度、缺失原因/影响说明)
- need_user_confirm 争议项(先批量问用户确认,再进入路径选择)
- 匹配明细摘要(用户追问时给出完整明细表)

用 clarify 工具呈现选项(单选;问题里放上述汇报摘要):
- 有合适类型时:
  ① 生成【设备模型】(私有,从推荐类型筛选匹配点位)
  ② 生成【设备模型 + 点表】(私有,模型生成后基于模型生成点表,见第 6 步分支 A2)
  ③ 生成【设备类型】(私有,基于说明书点位新建)
  ④ 仅保留分析结论,不生成 Excel
- 无合适类型(语义明显不符)时:
  ① 生成【设备类型】(私有,基于说明书点位新建)
  ② 仅保留分析结论,不生成 Excel

用户选择"仅保留结论"→ 直接进入第 6 步总结输出(仍可留痕),不生成 Excel。
完成标准:用户已看到推荐类型、四维度覆盖明细与缺失清单,并明确选择了生成路径。

**协议选择(仅路径含点表时)**:用户选择"设备模型+点表"后,用 clarify 工具列出
`templates/` 目录下的协议文件名(ModbusTCP_Vega_ARM64_V1.1.0 / ModbusRTU_... /
DL_T_645_... / MQTT_... / IEC_104_... / OPC UA_... 等),让用户选通信协议。
协议名即模板文件名(去 .xlsx);各协议列定义不同,脚本按所选协议模板表头列名映射填充。

### 5. 生成 Excel(spec 驱动 + 校验闸门)

**铁律 1(字段来源)**:生成文件的一切点位字段(标识符、名称、数据类型、单位、枚举、必填等)
一律取自知识库类型页面的标准定义;用户文档仅用于识别"需要哪些点"。
绝不用用户文档的原始命名/字段直接进 Excel(分支 B 新建私有类型时除外,见下)。

**铁律 2(ID 前缀)**:生成物的 ID 一律 `project_` 前缀(如 `project_PD7777`),
绝不使用 `public_`;`public_` 仅用于引用知识库公有类型(如设备模型的 *DeviceType 字段)。

- 分支 A(用户选择生成设备模型)→ 生成【设备模型】Excel:
  - **spec 驱动**:生成 `model_spec.json`(raw_doc + model{id,name,device_type} +
    select{四维度引用清单} + add{四维度新增点位}),调 `gen_device_model.py model_spec.json`;
    select 清单从 match.json 的命中标识符取(确定性查表),add 从 points.json 取未覆盖项
  - 模板:`templates/model_template.xlsx`(成品案例,结构见"模板结构"节)
  - FromDeviceType 子表:从类型引用(筛选)的点位标识符清单,即用户设备匹配上的类型点位
  - **引用完整性(强制)**:引用服务时,其 `*Input` 引用的点位;引用事件时,其 `*Output`
    (及 `*Condition` 等式左侧)引用的点位,必须一并加入 FromDeviceType 引用。
    教训(PD7777-3H 实测):平台导入按 Input/Output 引用校验并**自动补点**——原模型
    漏了 ClearE/FactoryReset(服务 Input)和 13 个 Ala_* 告警测点(事件 Output),
    平台全部自动补入,说明这些点位是平台校验对象;主动补上由类型兜底,校验风险最低。
    脚本 `ensure_refs_present` 自动补充,无需手改 SELECT 清单;注意事件/服务 ID 与
    点位同名(如事件 Ala_RevP 的 Output 也是测点 Ala_RevP)时按测点/属性维度检查,
    不能因 ID 同名跳过
  - 四张子表(Attribute/MeasurePoint/Event/Service):**只能写 FromDeviceType 中
    未引用的【新增点位】**——设备类型中没有、本模型私有新增的点位(用户设备特有、
    类型未覆盖、用户确认纳入模型的点位);从类型引用的点位绝不重复写入四张子表
  - 新增点位字段定义:类型中不存在该点位 → 知识库无标准定义,取自用户文档
    (标识符按语义规范化,参考知识库同域命名风格,ID 用 project_ 前缀);
    引用点位字段仍取自知识库标准定义(铁律 1)
  - 若用户设备点位全部被类型覆盖(无新增),四张子表只保留表头
  - ID:`project_<设备名>`(BasicInfo 的 *ID);*DeviceType 填引用的公有类型 ID(public_ 前缀)
  - 命名:`/opt/data/output/<设备名>_设备模型_yyyyMMdd.xlsx`
- 分支 A2(生成设备模型后,用户选择"模型+点表",或独立要求)→ 生成【点表】Excel:
  - 点表定位:设备模型是抽象描述(有哪些点位),点表定义如何从设备获取这些点位信息
    (每个点位一行:寄存器地址/数量/功能码/数据类型/系数/基值/超时/字节序/位索引/映射);
    平台按"点位名称 + 点位标识符"把点表映射到设备模型 → 点表的点位名称与标识符
    必须与设备模型保持一致
  - **模板按通信协议选择**:`templates/<协议名>.xlsx`(协议由用户在第 4 步选择);
    各协议列定义不同(Modbus 系列有 address/registerCount/functionCode,MQTT 有 topic/jsonpath,
    OPC UA 有 tag 等),脚本按目标模板表头列名映射填充,不硬编码列号;清空模板自带数据行
  - **spec 驱动**:生成 `point_reg.json`(protocol + model_xlsx + rows{pointKey -> 寄存器信息}),
    调 `gen_point_table.py point_reg.json`;rows 的 key 是模型 pointKey(与设备模型一致)
  - 点位全集 = 设备模型测点:FromDeviceType 引用测点 + 子表 MeasurePoint 新增测点;
    属性/事件/服务不进入点表(点表只定义测点的采集取数),总结中说明;
    以说明书为准:说明书查不到寄存器/地址的测点不生成行,总结中告知用户
    (哪些点位未找到地址),绝不臆造
  - 字段来源:pointName/pointKey/unit 一律从生成的设备模型 Excel 读取
    (pointKey = 模型点位 *ID,与模型一致,绝不从用户文档直抄);
    address/registerCount/functionCode/dataType/coefficient 等取说明书寄存器表
  - 寄存器地址进制:模板要求十进制;说明书常为十六进制(0x…)或其他进制,
    points.json 记录原始写法,生成时统一转十进制(脚本支持 0x 自动转换),总结标注转换项
  - dataType(寄存器数据类型)以说明书寄存器定义为准;说明书未给时按平台模型
    数据类型推断(FLOAT→float32 或整数+系数、INT→i32、ENUM→u16+map、STRING→str、
    BOOL→bool、DATETIME→str),推断项在总结中标注
  - 无寄存器信息的点位(说明书无寄存器表/查不到):点表不保留行(无地址即无
    采集定义,点表以说明书为准),但总结中必须告知用户哪些点位未找到地址,
    绝不臆造地址
  - 命名:`/opt/data/output/<设备名>_点表_yyyyMMdd.xlsx`
  - 独立入口:已有设备模型 Excel + 说明书寄存器信息时,可直接单独生成点表
    (输入 = point_reg.json,不经过第 4 步交互)
- 分支 B(用户选择生成设备类型)→ 生成【设备类型】Excel:
  - **spec 驱动**:生成 `type_spec.json`(template + type{id,name,category,domain,...} +
    points{四维度点位全集}),调 `gen_device_type.py type_spec.json`;
    内容全部来自 points.json(用户文档点位),不经过 match.json(新建类型不引用公有类型)
  - 模板:`templates/type_template.xlsx`(空白导出,结构见"模板结构"节)
  - 内容:由用户文档四维度点位生成;标识符规范化:优先用文档已有英文 ID,
    否则按语义译成英文 CamelCase(参考知识库同域命名风格,如 MeterVoltageA / AlarmOverCurrent)
  - ID:`project_<设备名>`(BasicInfo 的 *ID)
  - 命名:`/opt/data/output/<设备名>_设备类型_yyyyMMdd.xlsx`
  - 私有类型不回灌公有知识库(知识库只收 public_ 公有类型);如需沉淀,另行与用户确认

**校验闸门(强制)**:每个 Excel 生成后立即调 `verify_output.py` 校验,失败即 fail-fast
(退出码 1),不得交付;校验 agent 据此决定回退重生成或继续。三类校验:
  - `--kind model`:ID 前缀 project_、*DeviceType 前缀 public_、FromDeviceType 与子表互斥、
    DataDefine 合法 JSON、服务/事件 Input/Output 依赖点位在模型全集
  - `--kind type`:ID 前缀 project_、无 FromDeviceType sheet、DataDefine 合法 JSON
  - `--kind point --model <模型xlsx>`:pointKey 与模型测点全集一致、address 为十进制 int、
    无模板说明行/示例行、只含测点维度

模板结构(已校准 2026-08-07,基于解密后的真实模板):

- 设备模型模板 `templates/model_template.xlsx`(成品案例)6 个 sheet,列头(注意列序与类型模板不同):
  - BasicInfo: *ID | *Name_default | Name_zh_CN | Name_en_US | *DeviceType
  - FromDeviceType: Attribute | MeasurePoint | Event | Service(逗号分隔的从类型筛选点位标识符清单)
  - 关键规则:FromDeviceType 引用清单与四张子表内容互斥——四张子表只写 FromDeviceType
    中未出现的新增点位;从类型引用的点位只进 FromDeviceType 清单,不重复写入子表
  - Attribute: *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | Unit | *IsRequired | DataDefine | Desc
  - MeasurePoint: *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | *R/W | Unit | DataDefine | Desc
  - Event: *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc
  - Service: *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc
- 设备类型模板 `templates/type_template.xlsx`(空白导出,5 sheet,无 FromDeviceType):
  - BasicInfo: *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType
  - Attribute: *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc
  - MeasurePoint: *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc
  - Event / Service 同模型模板
- 点表模板 `templates/<协议名>.xlsx`(按通信协议分文件,与模型/类型模板同目录,各协议列定义不同;生成时按
    用户所选协议的模板表头列名映射填充,清空模板自带数据行;只填测点行,属性/事件/服务不生成行):
  - 共有列(多数协议):pointName | pointKey | unit | dataType | coefficient | wait | map
  - Modbus 系列(ModbusTCP/ModbusRTU/SG/SMG)特有:address(十进制 int,十六进制须转换)|
    registerCount | functionCode([读,写]如 [03,00])| order | mask | basicValue | parentKey
    (注:ModbusRTU_SMG 模板的 coefficient 列名拼写为 `efficient`,按实际表头填)
  - MQTT 特有:topic | jsonpath;OPC UA 特有:tag;IEC 104 特有:pointNum | pointType;
    DL/T 645 特有:dataFormat | dataEncoding | frontCode | dataTag | dataLength | ctrlCode | frameInterval;
    DL/T 698 特有:OAD | operationCode;Gateway 特有:southSample | precision
  - dataType(寄存器数据类型:u64/u32/u16/u8、i64/i32/i16/i8、float32、double64、
    ieee754_f32/f64、str、hex_str、mac_str、ver_str、ip_str、time_nb2、bits、bool;
    以说明书寄存器定义为准)
  - mask(位索引,非必填,如 [6,7])| map(映射关系 json,非必填)| basicValue(基值,非必填)
- 注意:两模板列序不同(模型模板 R/W 在前、类型模板 DataDefine 在前),填充一律按目标模板表头列名映射,不硬编码列号
- 点位全字段(含 DataDefine/英文名/Output/Condition)在 `wiki/raw/papers/<源文档>.md` 里,
  wiki 实体页是精简表,生成 Excel 时以 raw 文档为字段源
- 脚本(spec 驱动,数据与逻辑分离;新设备只改 spec 不改脚本):
  - `scripts/gen_device_model.py <model_spec.json>`(分支 A):读 spec 的 select/add +
    raw 文档,按模板填充;自动按引用服务/事件的 Input/Output 补全依赖点位引用
    (`ensure_refs_present`),select 清单无需手动补
  - `scripts/gen_device_type.py <type_spec.json>`(分支 B):读 spec 的 points 四维度,
    按 type_template.xlsx 模板填充
  - `scripts/gen_point_table.py <point_reg.json>`(分支 A2):读 spec 的 rows{pointKey ->
    寄存器信息} + 设备模型 Excel(pointName/pointKey/unit 来源),按所选协议模板填充;
    address 支持 0x 十六进制自动转十进制;说明书无寄存器信息的点位不生成行,输出"未找到地址"清单
  - `scripts/verify_output.py --kind {model|type|point} --xlsx <xlsx> [--model <模型xlsx>]`
    (校验闸门):对生成的 Excel 做机器可检校验,失败 exit 1;JSON 报告含 passed/errors/warnings

### 6. 总结输出(不再写 md 报告)

分析结论直接总结输出给用户(终端消息,不生成 md 文件),内容:
- 设备基本信息(来自文档)
- 用户选择的生成路径与结果:生成的 Excel 文件路径、所用模板、各维度点位数量
  (或"未生成 Excel,仅保留分析结论")
- 推荐类型(或"无合适类型"),业务域、四维度点数
- 四维度覆盖明细(覆盖/未覆盖点位清单)及影响
- 生成的私有 ID(project_ 前缀)列表;悬空/推断项说明(诚实标注,不得臆造)
- 若生成了点表:点表文件路径、行数(测点)、所用协议、未找到地址的点位清单
  (点表不保留空行,须告知用户)、dataType 推断项、寄存器地址进制转换项

### 7. 留痕

- 生成操作追加 `wiki/log.md`(格式:`## [YYYY-MM-DD] action | 主题`),记录产出
  (如"为 PD7777 生成私有设备模型 project_PD7777 + 点表 N 行")
- 私有类型/模型不登记 `wiki/index.md`(公有知识库只收 public_ 类型)
- 若发现知识库公有类型页有缺漏/错误,提出修正建议,不擅自改

## Common Pitfalls

踩坑记录已抽离至 [reference/pitfalls.md](reference/pitfalls.md),按主题分组(字段来源与 ID 前缀 /
知识库检索与语义匹配 / 说明书解析 / 设备模型生成 / 点表生成 / 模板与工具 / 留痕),共 22 条。
工作流中的规则大多源于这些实战教训,遇疑回查该文件。关键铁律摘要:

- 引用点位字段取自知识库标准定义,绝不用用户文档原始命名
- 生成物 ID 一律 `project_`,`public_` 仅用于引用公有类型
- FromDeviceType 引用与四张子表互斥;引用服务/事件的 Input/Output 依赖点位由脚本自动补
- 事件 *Condition 仅支持等式;设备模型一般不新增事件,从类型事件集引用子集
- 点表只收录测点;pointName/pointKey/unit 从设备模型读取;address 十进制;无地址不生成行

## Verification Checklist

- [ ] points.json 四维度齐全,推断项已标注(inferred: true)
- [ ] 每个候选类型读过实体页(大设备含子页)
- [ ] match.json 无悬空项(每个用户点位有 matched_type_id 或 uncovered);争议项已标 need_user_confirm 并经用户确认
- [ ] 已向用户汇报推荐类型、四维度覆盖明细、未覆盖清单,用户已选择生成路径
- [ ] 含点表路径时,用户已选择通信协议(templates/ 目录下的协议文件名)
- [ ] Excel 由 spec 驱动脚本生成(model_spec.json / type_spec.json / point_reg.json),能重新打开校验
- [ ] 每个 Excel 生成后 verify_output.py 校验通过(passed: true);失败已回退重生成
- [ ] Excel 点位字段全部来自知识库标准定义(抽查 3 条对照实体页)
- [ ] 生成文件内 ID 均为 project_ 前缀(抽查 BasicInfo 的 *ID)
- [ ] FromDeviceType 引用点位未重复出现在四张子表;四张子表内容均为新增点位
- [ ] 引用服务/事件的 Input/Output 依赖点位已全部在 FromDeviceType 引用中
      (脚本 ensure_refs_present 自动保证;抽查 ClearE/FactoryReset/Ala_* 等)
- [ ] 分析结论已直接总结输出给用户(无 md 报告文件)
- [ ] wiki log.md 已追加;私有类型/模型未登记 index.md
- [ ] 点表 pointName/pointKey/unit 与设备模型一致(抽查 3 条对照模型 Excel)
- [ ] 点表 dataType 以说明书寄存器定义为准;推断项已在总结标注
- [ ] 点表 address 均为十进制(十六进制已转换);说明书无地址点位未生成行,
      已在总结中告知用户清单,无臆造
- [ ] 点表仅含测点维度(属性/事件/服务均未入表)
- [ ] 点表按所选协议模板生成,列名映射正确(非 Modbus 协议的特有列如 topic/tag 等已填)