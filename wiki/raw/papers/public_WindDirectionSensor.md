# public_WindDirectionSensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_WindDirectionSensor | 风向传感器 |  | Wind Direction Sensor | NORMAL | public |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tt | tt |  |  | STRING |  |  | False |  |
| SN | 设备SN |  | Device SN | STRING |  |  | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WindDirection | 风向 |  | Wind Direction | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正北"<br>			},<br>			"itemValue":"正北",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"东北"<br>			},<br>			"itemValue":"东北",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"正东"<br>			},<br>			"itemValue":"正东",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"东南"<br>			},<br>			"itemValue":"东南",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"正南"<br>			},<br>			"itemValue":"正南",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"西南"<br>			},<br>			"itemValue":"西南",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"正西"<br>			},<br>			"itemValue":"正西",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"西北"<br>			},<br>			"itemValue":"西北",<br>			"itemKey":"8"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
