# public_TempRHSensor_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_TempRHSensor_V1_0_2 | 温湿度传感器 |  | Temperature and Humidity Sensor | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ManufacturerCode | 厂家工厂代码 |  | Manufacturer Factory Code | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 | 安装位置 | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RHAlarmRecThr | 湿度告警恢复阈值 |  | Humidity Alert Recovery Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | %RH |  |
| RHAlarmTime | 湿度告警时间 |  | Humidity Alert Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| RHAlarmRecTime | 湿度告警恢复时间 |  | Humidity Alert Recovery Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| RHAlarmThr | 湿度告警阈值 |  | Humidity Alert Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | %RH |  |
| RH | 湿度 |  | Humidity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| TempAlarmRecTime | 温度告警恢复时间 |  | Temperature Alert Recovery Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| TempAlarmRecThr | 温度告警恢复阈值 |  | Temperature Alert Recovery Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| TempAlarmTime | 温度告警时间 |  | Temperature Alert Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | s |  |
| TempAlarmThr | 温度告警阈值 |  | Temperature Alert Threshold | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| Temp | 温度 |  | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| DeviceTime | 设备时间 |  | Device Time | DATETIME |  | RW |  |  |
| Ala_Temp | 温度告警状态 |  | Temperature Alert Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RH | 湿度告警状态 |  | Humidity Alert Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmRH | 湿度告警 |  | Humidity Alert | ALARM | Ala_RH | Ala_RH = 1 |  |
| AlarmTemp | 温度告警 |  | Temperature Alert | ALARM | Ala_Temp | Ala_Temp = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| SetRHAlarmRecThr | 设置湿度告警恢复阈值 |  | Set Humidity Alert Recovery Threshold | RHAlarmRecThr |  |  |
| SetRHAlarmRecTime | 设置湿度告警恢复时间 |  | Set humidity alert recovery time | RHAlarmRecTime |  |  |
| SetRHAlarmThr | 设置湿度告警阈值 |  | Set humidity alert threshold | RHAlarmThr |  |  |
| SetRHAlarmTime | 设置湿度告警时间 |  | Set humidity alert time | RHAlarmTime |  |  |
| SetTempAlarmRecThr | 设置温度告警恢复阈值 |  | Set temperature alert recovery threshold | TempAlarmRecThr |  |  |
| SetTempAlarmRecTime | 设置温度告警恢复时间 |  | Set temperature alert recovery time | TempAlarmRecTime |  |  |
| SetTempAlarmThr | 设置温度告警阈值 |  | Set temperature alert threshold | TempAlarmThr |  |  |
| SetTempAlarmTime | 设置温度告警时间 |  | Set temperature alert time | TempAlarmTime |  |  |
