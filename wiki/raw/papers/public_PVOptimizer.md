# public_PVOptimizer

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_PVOptimizer | 光伏优化器 |  | Photovoltaic Optimizer | NORMAL | Solar |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device SN | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  | A | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SetOverTempOpeTime | 设置过温动作时间 |  | Set overtemperature action time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SwitchOff | 关机 |  | Shutdown | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| OverUEn | 过压使能 |  | Overvoltage Enable | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverUThr | 设置过压阈值 |  | Set Overvoltage Threshold | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverURec | 设置过压恢复阈值 |  | Set Overvoltage Recovery Threshold | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverUOpeTime | 设置过压动作时间 |  | Set Overvoltage Trip Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| InOverLoadEn | 输入过载使能 |  | Enable input overload | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ShoCirProtEn | 短路保护使能 |  | Enable short circuit protection | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetShoCirRecTime | 设置短路恢复时间 |  | Set short circuit recovery time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetShoCirContRecCoun | 设置短路连续恢复次数 |  | Set consecutive short circuit recovery count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| OverTempEn | 过温使能 |  | Enable overtemperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverTempThr | 设置过温阈值 |  | Set overtemperature threshold | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverTempRecThr | 设置过温恢复阈值 |  | Set overtemperature recovery threshold | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| InI | 输入电流 |  | Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_OutOverTemp | 输出过温故障 |  | Output Overtemperature Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| InP | 输入功率 |  | Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| OutU | 输出电压 |  | Output Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| OutI | 输出电流 |  | Output Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| OutP | 输出功率 |  | Output Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| InTemp | 机内温度 |  | Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| ErrorCount | 故障记录条数 |  | Fault Record Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Sta_OnOff | 开关机状态 |  | Power On/Off Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"关机"<br>			},<br>			"itemValue":"关机",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"开机"<br>			},<br>			"itemValue":"开机",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Online | 在线状态 |  | Online Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"离线"<br>			},<br>			"itemValue":"离线",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"在线"<br>			},<br>			"itemValue":"在线",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InOverU | 输入过压故障 |  | Input Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InUnderU | 输入欠压故障 |  | Input Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OutOverCur | 输出过流故障 |  | Output Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OutOverP | 输出过功率故障 |  | Output Overpower Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| InU | 输入电压 |  | Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SwitchOn | 开机 |  | Turn on | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| DayE | 当日发电量 |  | Daily power generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorInOverU | 输入过压故障 |  | Input Overvoltage Fault | FAULT | Err_InOverU | Err_InOverU = 1 |  |
| ErrorInUnderU | 输入欠压故障 |  | Input Undervoltage Fault | FAULT | Err_InUnderU | Err_InUnderU = 1 |  |
| ErrorOutOverCur | 输出过流故障 |  | Output Overcurrent Fault | FAULT | Err_OutOverCur | Err_OutOverCur = 1 |  |
| ErrorOutOverP | 输出过功率故障 |  | Output Overpower Fault | FAULT | Err_OutOverP | Err_OutOverP = 1 |  |
| ErrorOutOverTemp | 输出过温故障 |  | Output Overtemperature Fault | FAULT | Err_OutOverTemp | Err_OutOverTemp = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| InOverLoadEnCmd | 输入过载使能 |  | Input Overload Protection Enabled | InOverLoadEn |  |  |
| OverTempEnCmd | 过温使能 |  | Overtemperature Protection Enabled | OverTempEn |  |  |
| OverTempOpeTimeSet | 设置过温动作时间 |  | Set Overtemperature Action Time | SetOverTempOpeTime |  |  |
| OverTempRecThrSet | 设置过温恢复阈值 |  | Set Overtemperature Recovery Threshold | SetOverTempRecThr |  |  |
| OverTempThrSet | 设置过温阈值 |  | Set Overtemperature Threshold | SetOverTempThr |  |  |
| OverUECmd | 过压使能 |  | Overvoltage Protection Enabled | OverUEn |  |  |
| OverUOpeTimeSet | 设置过压动作时间 |  | Set Overvoltage Trip Time | SetOverUOpeTime |  |  |
| OverURecSet | 设置过压恢复阈值 |  | Set the overvoltage recovery threshold | SetOverURec |  |  |
| OverUThrSet | 设置过压阈值 |  | Set Overvoltage Threshold | SetOverUThr |  |  |
| ShoCirContRecCounSet | 设置短路连续恢复次数 |  | Set Short Circuit Continuous Recovery Count | SetShoCirContRecCoun |  |  |
| ShoCirProtEnCmd | 短路保护使能 |  | Short Circuit Protection Enabled | ShoCirProtEn |  |  |
| ShoCirRecTimeSet | 设置短路恢复时间 |  | Set Short Circuit Recovery Time | SetShoCirRecTime |  |  |
| SwitchOffCmd | 关机 |  | Shutdown | SwitchOff |  |  |
| SwitchOnCmd | 开机 |  | Power On | SwitchOn |  |  |
