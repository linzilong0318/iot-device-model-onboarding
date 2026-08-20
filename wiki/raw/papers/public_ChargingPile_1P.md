# public_ChargingPile_1P

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ChargingPile_1P | 单相交流充电桩（单枪） |  | Single-phase AC charging pile (single gun) | NORMAL | charge |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| ChargeBoxSN | 充电柜序列号 |  | Charging Cabinet Serial Number | STRING |  |  | False |  |
| SIMIccid | SIM卡ICCID（4G桩常用） |  | SIM Card ICCID (Commonly used for 4G piles) | STRING |  |  | False |  |
| SIMImsi | SIM卡IMSI |  | SIM Card IMSI | STRING |  |  | False |  |
| MeterType | 电表类型 |  | Meter Type | STRING |  |  | False |  |
| MeterSN | 电表序列号 |  | Meter Serial Number | STRING |  |  | False |  |
| ChargingPileID | 桩号 |  | Pile Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| ConnectorNum | 充电枪数量 |  | Number of Charging Guns | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Err_AcSurgeProt | 交流防雷故障 |  | Lightning Protection Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_HVContactor | 高压接触器故障 |  | High Voltage Contactor Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| ElecRateT1 | 尖电费费率 |  | Peak electricity rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| Err_DcFuse | 直流熔断器故障 |  | DC Fuse Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_FanSpeedCtrl | 风扇调速板故障 |  | Fan Speed Control Board Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_CardReaComm | 读卡器通信中断故障 |  | Card Reader Communication Interruption Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_EMeterComm | 电能表通信中断故障 |  | Power Meter Communication Interruption Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InsulComm | 绝缘检测模块通信中断故障 |  | Insulation Detection Module Communication Interruption Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ACDCComm | 交直流模块通信中断故障 |  | AC/DC Module Communication Interruption Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| TotalMoney | 当前订单累计总金额 |  | Current Order Cumulative Total Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ￥ |  |
| Err_OutletOverTemp | 出风口温度过高故障 |  | Exhaust Temperature Too High Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_NoAvailRect | 无可用整流模块故障 |  | No Available Rectifier Module Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_EmergencyStop | 急停按钮动作故障 |  | Emergency Stop Button Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_ConnInserted | 是否插枪 |  | Whether the Gun is Plugged | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"否"<br>			},<br>			"itemValue":"否",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"是"<br>			},<br>			"itemValue":"是",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"未知"<br>			},<br>			"itemValue":"未知",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_ConnParked | 枪是否归位 |  | Whether the Gun is in Place | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"否"<br>			},<br>			"itemValue":"否",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"是"<br>			},<br>			"itemValue":"是",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"未知"<br>			},<br>			"itemValue":"未知",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Connector | 枪状态 |  | Gun Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"离线"<br>			},<br>			"itemValue":"离线",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"空闲"<br>			},<br>			"itemValue":"空闲",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"3"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| RateModelID | 计费模型编号 |  | Charging Model Number | STRING |  | R |  |  |
| I | 充电电流 |  | Charging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ServiceMoney | 当前订单累计服务费 |  | Current Order Cumulative Service Fee | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ￥ |  |
| ElecMoney | 当前订单累计电费 |  | Current Order Cumulative Electricity Cost | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ￥ |  |
| TotalChargeE | 累计充电量 |  | Cumulative Charging Quantity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| OrderChargeE | 当前订单充电量 |  | Current Order Charge Quantity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ConnectorLineTemp | 枪线温度 |  | Cable Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| P | 充电功率 |  | Charging power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| ServRateT1 | 尖服务费费率 |  | Peak service fee rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| U | 充电电压 |  | Charging Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Conn1TransID | 枪1交易流水号 |  | Gun 1 transaction number | STRING |  | R |  |  |
| ServRateT4 | 谷服务费费率 |  | Off-peak service fee rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| ElecRateT4 | 谷电费费率 |  | Off-peak electricity rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| ServRateT3 | 平服务费费率 |  | Peak service fee rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| ElecRateT3 | 平电费费率 |  | Peak electricity rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| ServRateT2 | 峰服务费费率 |  | Peak service fee rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |
| ElecRateT2 | 峰电费费率 |  | Peak electricity rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | CNY/kWh |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Err_EmergencyStop | 急停按钮动作故障 |  | Emergency Stop Button Action Failure | FAULT | Err_EmergencyStop | Err_EmergencyStop = 1 |  |
| Err_NoAvailRect | 无可用整流模块故障 |  | No available rectifier module fault | FAULT | Err_NoAvailRect | Err_NoAvailRect = 1 |  |
| Err_OutletOverTemp | 出风口温度过高故障 |  | Exhaust temperature too high fault | FAULT | Err_OutletOverTemp | Err_OutletOverTemp = 1 |  |
| Err_AcSurgeProt | 交流防雷故障 |  | AC surge protection fault | FAULT | Err_AcSurgeProt | Err_AcSurgeProt = 1 |  |
| Err_ACDCComm | 交直流模块通信中断故障 |  | AC/DC module communication interruption fault | FAULT | Err_ACDCComm | Err_ACDCComm = 1 |  |
| Err_InsulComm | 绝缘检测模块通信中断故障 |  | Insulation detection module communication interruption fault | FAULT | Err_InsulComm | Err_InsulComm = 1 |  |
| Err_EMeterComm | 电能表通信中断故障 |  | Power meter communication interruption fault | FAULT | Err_EMeterComm | Err_EMeterComm = 1 |  |
| Err_CardReaComm | 读卡器通信中断故障 |  | Card reader communication interruption fault | FAULT | Err_CardReaComm | Err_CardReaComm = 1 |  |
| Err_FanSpeedCtrl | 风扇调速板故障 |  | Fan speed control board fault | FAULT | Err_FanSpeedCtrl | Err_FanSpeedCtrl = 1 |  |
| Err_DcFuse | 直流熔断器故障 |  | DC fuse fault | FAULT | Err_DcFuse | Err_DcFuse = 1 |  |
| Err_HVContactor | 高压接触器故障 |  | High voltage contactor fault | FAULT | Err_HVContactor | Err_HVContactor = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
