# public_CabinetDoorSensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_CabinetDoorSensor | 门磁传感器 |  | Magnetic Door Sensor | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sta_Door | 柜门状态 |  | Cabinet door status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"关闭状态",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"关闭状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"开启状态",<br>				"en_US":"Open"<br>			},<br>			"itemValue":"开启状态",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
