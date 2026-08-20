# public_PDU_1P

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_PDU_1P | 单相交流PDU |  |  | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| BatteryCapacity | 电池容量 |  | Battery Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kWh | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ala_OverU | 过压告警 |  | Overvoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"过压告警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"过压告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderU | 欠压告警 |  | Undervoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"过压告警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"过压告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderI | 空载告警 |  | No-load Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"空载告警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"空载告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SetAlarmSound | 配置报警声音 |  | Configure Alarm Sound | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"打开报警声音",<br>				"en_US":"Open"<br>			},<br>			"itemValue":"打开报警声音",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"关闭报警声音",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"关闭报警声音",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Ala_OverI | 过流告警 |  | Overcurrent Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"过流告警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"过流告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SetRelayStatus | 设置继电器状态 |  | Set Relay Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Open"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close",<br>				"zh_CN":"合闸"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| OverILinkEnable | 过载联动使能开关 |  | Overload Linkage Enable Switch | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"关闭联动",<br>				"en_US":"Open"<br>			},<br>			"itemValue":"关闭联动",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"开启联动",<br>				"en_US":"Open"<br>			},<br>			"itemValue":"开启联动",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SetUnderITime | 设置空载判断时间 |  | Set No-load Judgment Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverITime | 设置过载判断时间 |  | Set Overload Judgment Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetUnderUTime | 设置欠压判断时间 |  | Set Undervoltage Judgment Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverUTime | 设置过压判断时间 |  | Set Overvoltage Judgment Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetUnderIThr | 设置空载下限值 |  | Set No-load Lower Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverIThr | 设置过载上限值 |  | Set Overload Upper Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetUnderUThr | 设置欠压下限值 |  | Set Undervoltage Lower Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetOverUThr | 设置过压上限值 |  | Set Overvoltage Upper Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| RH | 湿度 |  | Humidity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| Sta_Alarm | 报警状态 |  | Alarm Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"不报警",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"不报警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"报警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"报警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| EP | 总有功电能 |  | Total Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Temp | 温度 |  | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PF | 功率因数 |  | Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| S | 视在功率 |  | Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Q | 无功功率 |  | Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| P | 有功功率 |  | Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| I | 电流 |  | Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| U | 电压 |  | Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmOverU | 过压告警 |  | Overvoltage Alarm | ALARM | Ala_OverU | Ala_OverU = 1 |  |
| AlarmUnderU | 欠压告警 |  | Undervoltage Alarm | ALARM | Ala_UnderU | Ala_UnderU = 1 |  |
| AlarmOverI | 过流告警 |  | Overcurrent Alarm | ALARM | Ala_OverI | Ala_OverI = 1 |  |
| AlarmUnderI | 空载告警 |  | No-load Alarm | ALARM | Ala_UnderI | Ala_UnderI = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| AlarmSound | 配置报警声音 | 配置报警声音 | Configure Alarm Sound | SetAlarmSound |  |  |
| OverILinkEnableCmd | 过载联动使能开关 | 过载联动使能开关 | Overload Linkage Enable Switch | OverILinkEnable |  |  |
| OverIThr | 设置过载上限值 | 设置过载上限值 | Set Overload Upper Limit | SetOverIThr |  |  |
| OverITime | 设置过载判断时间 | 设置过载判断时间 | Set Overload Judgment Time | SetOverITime |  |  |
| OverUThrSet | 设置过压上限值 | 设置过压上限值 | Set Overvoltage Upper Limit | SetOverUThr |  |  |
| OverUTime | 设置过压判断时间 | 设置过压判断时间 | Set Overvoltage Judgment Time | SetOverUTime |  |  |
| RelayStatus | 设置继电器状态 | 设置继电器状态 | Set Relay Status | SetRelayStatus |  |  |
| UnderIThr | 设置空载下限值 | 设置空载下限值 | Set No-load Lower Limit | SetUnderIThr |  |  |
| UnderITime | 设置空载判断时间 | 设置空载判断时间 | Set No-load Judgment Time | SetUnderITime |  |  |
| UnderUThr | 设置欠压下限值 | 设置欠压下限值 | Set Undervoltage Lower Limit | SetUnderUThr |  |  |
| UnderUTime | 设置欠压判断时间 | 设置欠压判断时间 | Set Undervoltage Judgment Time | SetUnderUTime |  |  |
