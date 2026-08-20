# public_WaterSensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_WaterSensor | 水浸传感器 |  | Water Flood Sensor | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmStatus | 报警状态（废弃） |  | AlarmStatus | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal",<br>				"zh_CN":"正常"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal",<br>				"zh_CN":"异常"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Water | 告警状态 |  | Alarm Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SensitivitySetting | 报警灵敏度设置 | 报警灵敏度设置 | SensitivitySetting | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| AlarmRecThr | 告警恢复阈值 |  | Alarm Recovery Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| AlarmThr | 告警阈值 |  | Alarm Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| AnalogQua | 水浸值 |  | Water Level | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| AlarmRecTime | 告警恢复时间 |  | Alarm Recovery Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| AlarmTime | 告警时间 |  | Alarm Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| DeviceTime | 设备时间 |  | Device Time | DATETIME |  | RW |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmWater | 水浸告警 |  | Flood Warning | ALARM | Ala_Water,AnalogQua | Ala_Water = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| SetAlarmRecThr | 设置告警恢复阈值 |  | Set alarm recovery threshold | AlarmRecThr |  |  |
| SetAlarmRecTime | 设置告警恢复时间 |  | Set alert recovery time | AlarmRecTime |  |  |
| SetAlarmThr | 设置告警阈值 |  | Set alert threshold | AlarmThr |  |  |
| SetAlarmTime | 设置告警时间 |  | Set alert time | AlarmTime |  |  |
