# public_VFD

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_VFD | 变频器 | 变频器 | Variable Frequency Drive | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| EquipmentType | 设备型号 | 设备型号 | Device Model | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |
| Type | 类型 | 类型 | Device Type | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"恒定转矩",<br>				"en_US":"Constant Torque",<br>				"zh_CN":"恒定转矩"<br>			},<br>			"itemValue":"恒定转矩",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"可变转矩",<br>				"en_US":"Variable Torque",<br>				"zh_CN":"可变转矩"<br>			},<br>			"itemValue":"可变转矩",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"STRING"<br>} |  | False |  |
| RatedPower | 额定功率 | 额定功率 | Rated Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W | False |  |
| RatedInputVoltage | 额定输入电压 | 额定输入电压 | Rated Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedOutputVoltage | 额定输出电压 | 额定输出电压 | Rated Output Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedOutputCurrent | 额定输出电流 | 额定输出电流 | Rated Output Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Control | 控制指令 | 控制指令 | Control Command | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正向转动",<br>				"en_US":"Forward Run",<br>				"zh_CN":"正向转动"<br>			},<br>			"itemValue":"正向转动",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"反向转动",<br>				"en_US":"Reverse Run",<br>				"zh_CN":"反向转动"<br>			},<br>			"itemValue":"反向转动",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"停止",<br>				"en_US":"Stop",<br>				"zh_CN":"停止"<br>			},<br>			"itemValue":"停止",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"紧急停机",<br>				"en_US":"Emergency Shutdown",<br>				"zh_CN":"紧急停机"<br>			},<br>			"itemValue":"紧急停机",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障重置",<br>				"en_US":"Fault Reset",<br>				"zh_CN":"故障重置"<br>			},<br>			"itemValue":"故障重置",<br>			"itemKey":"5"<br>		}<br>	],<br>	"enumKeyCode":"STRING"<br>} | W |  |  |
| ConverterStatus | 变频器状态 | 变频器状态 | Converter Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正向转动中",<br>				"en_US":"Forward Running",<br>				"zh_CN":"正向转动中"<br>			},<br>			"itemValue":"正向转动中",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"反向转动中",<br>				"en_US":"Reverse Running",<br>				"zh_CN":"反向转动中"<br>			},<br>			"itemValue":"反向转动中",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"待机状态",<br>				"en_US":"Standby Status",<br>				"zh_CN":"待机状态"<br>			},<br>			"itemValue":"待机状态",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障状态",<br>				"en_US":"Fault Status",<br>				"zh_CN":"故障状态"<br>			},<br>			"itemValue":"故障状态",<br>			"itemKey":"4"<br>		}<br>	],<br>	"enumKeyCode":"STRING"<br>} | R |  |  |
| RunningFrequency | 运行频率 | 运行频率 | Running Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| SetFrequency | 设定频率 | 设定频率 | Set Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| BusVoltage | 母线电压 | 母线电压 | Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| OutputVoltage | 输出电压 | 输出电压 | Output Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| OutputCurrent | 输出电流 | 输出电流 | Output Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| RunningSpeed | 运行速度 | 运行速度 | Running Speed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | rpm |  |
| OutputPower | 输出功率 | 输出功率 | Output Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| OutputTorque | 输出转矩 | 输出转矩 | Output Torque | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | N·m |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
