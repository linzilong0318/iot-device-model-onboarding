# public_SmokeSensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_SmokeSensor | 烟雾传感器 |  | Smoke Sensor | NORMAL | distribution |  |  |

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
| SmokeDensity | 烟雾浓度（废弃） |  | Smoke Concentration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ppm |  |
| AlarmStatus | 烟感报警状态（废弃） |  | Smoke Alarm Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal",<br>				"zh_CN":"正常"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal",<br>				"zh_CN":"异常"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Smoke | 烟雾浓度告警状态 |  | Smoke Alarm Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| AlarmRecTime | 告警恢复时间 |  | Alarm Recovery Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| AlarmRecThr | 告警恢复阈值 |  | Alarm Recovery Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | ppm |  |
| AlarmTime | 告警时间 |  | Alarm Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| AlarmThr | 告警阈值 |  | Alarm Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | ppm |  |
| SmokeConcentration | 烟雾浓度 |  | Smoke Concentration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ppm |  |
| DeviceTime | 设备时间 |  | Device Time | DATETIME |  | RW |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmSmoke | 烟雾浓度异常告警 |  | Abnormal smoke concentration alert | ALARM | Ala_Smoke,SmokeConcentration | Ala_Smoke = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| SetAlarmRecThr | 设置告警恢复阈值 |  | Set the alarm recovery threshold | AlarmRecThr |  |  |
| SetAlarmRecTime | 设置告警恢复时间 |  | Set alarm recovery time | AlarmRecTime |  |  |
| SetAlarmThr | 设置告警阈值 |  | Set alarm threshold | AlarmThr |  |  |
| SetAlarmTime | 设置告警时间 |  | Set the alarm time | AlarmTime |  |  |
