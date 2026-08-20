# public_PCS

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_PCS | 储能变流器 |  | Energy Storage Converter | NORMAL | electricityStorage |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| BatteryType | 电池类型 |  | Battery Type | STRING |  |  | False |  |
| BatteryCapacity | 电池容量 |  | Battery Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kWh | False |  |
| RatedFreq | 额定频率 |  | Rated Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| RatedVoltage | 额定电压 |  | Rated Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedPower | 额定功率 |  | Rated Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kW | False |  |
| RatedChargeP | 额定充电功率 |  | Rated Charging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kW | False |  |
| RatedDischargeP | 额定放电功率 |  | Rated Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kW | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Err_Island | 孤岛故障 |  | Islanding Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PassiveIsland | 被动孤岛故障 |  | Passive Islanding Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBusU | 母线过压故障 |  | Bus Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCISensor | 漏电流传感器故障 |  | Leakage Current Sensor Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridUUnB | 电网电压不平衡故障 |  | Grid Voltage Imbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_MCU | MCU故障 |  | MCU Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCIDynamic | 动态漏电流过流故障 |  | Dynamic Leakage Current Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Isolation | 绝缘阻抗过低故障 |  | Insulation Impedance Too Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCIHigh | 逆变电流直流分量越限故障 |  | Inverter Current DC Component Overlimit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCIOffset | 逆变电流直流分量偏置保护 |  | Inverter Current DC Component Bias Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OpenLoopSelfChk | 开环自检异常故障 |  | Open-loop Self-test Abnormal Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridTHDU | 电网电压谐波过高故障 |  | Grid Voltage Harmonic Excessive Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_CANComm | CAN通讯故障 |  | CAN Communication Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCIStatic | 静态漏电流过流故障 |  | Static Leakage Current Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBoostCur | Boost电路过流故障 |  | Boost Circuit Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCChargeCir | 直流侧充电回路异常 |  | DC side charging circuit abnormality | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBattU | 电池电压过高故障 |  | Battery voltage too high fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_NoBusU | 母线无电压故障 |  | Bus undervoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridInvUDiff | 网侧逆变侧电压不一致故障 |  | Grid-side inverter-side voltage inconsistency fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvHWOverI | 逆变硬件过流故障 |  | Inverter hardware overcurrent fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BattInputRevCon | 电池输入反接故障 |  | Battery input reverse polarity fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverGridLineU | 电网线电压瞬时值越限故障 |  | Grid line voltage transient value exceeds limit fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_EmergCloase | 紧急按钮闭合 |  | Emergency Button Closed | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ROCOF | ROCOF故障 |  | ROCOF Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BusBattUDiff | 母线和电池电压差过大 |  | Bus and Battery Voltage Difference Excessive | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCRelay | 直流继电器故障 |  | DC Relay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverCapCur | 滤波电容电流越限故障 |  | Filter Capacitor Current Limit Exceeded Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvPWMShut | 逆变封锁保护 |  | Inverter Blocking Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverHalfBusU | 半母线电压高 |  | Half Bus Voltage High | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| CPSEn | CPS使能 |  | CPS Enabled | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未使能",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"未使能",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"削峰填谷功能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"削峰填谷功能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Sta_BattStack | 电池堆状态 |  | Battery Stack Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始化",<br>				"en_US":"Initialization"<br>			},<br>			"itemValue":"初始化",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充满",<br>				"en_US":"Fully Charged"<br>			},<br>			"itemValue":"充满",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放空",<br>				"en_US":"Empty"<br>			},<br>			"itemValue":"放空",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警",<br>				"en_US":"Alarm"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障",<br>				"en_US":"Fault"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"5"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_BattStackRu | 电池堆工作状态 |  | Battery Stack Run Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"停止",<br>				"en_US":"Stopped"<br>			},<br>			"itemValue":"停止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"运行",<br>				"en_US":"Running"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_BattRunMode | 电池运行模式 |  | Battery Run Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"充电状态",<br>				"en_US":"Charging"<br>			},<br>			"itemValue":"充电状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电状态",<br>				"en_US":"Discharging"<br>			},<br>			"itemValue":"放电状态",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_HalfBusUUnB | 半母线电压不平衡 |  | Half Bus Voltage Imbalance | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OnOffGridPara | 并离网参数不匹配 |  | Grid-Off Parameters Mismatch | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TempSensor | 温度传感器故障 |  | Temperature Sensor Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverDCI | 直流侧过流故障 |  | DC Side Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCICurOffset | 漏电流偏置故障 |  | Leakage Current Bias Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_LoadCur | 负载电流偏置故障 |  | Load Current Bias Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_JETIsland | JET孤岛频率异常 |  | JET Island Frequency Anomaly | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_CPLDOscil | CPLD晶振失效故障 |  | CPLD Oscillator Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverGridUPeak | 电网电压峰值越限故障 |  | Grid Voltage Peak Overlimit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BattPara | 电池参数设置错误 |  | Battery Parameter Setting Error | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderBattU | 电池欠压故障 |  | Battery Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_VNPE | NPE电压差越限故障 |  | NPE Voltage Difference Overlimit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvRelay | 逆变继电器故障 |  | Inverter Relay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCVUOffset | DCV电压偏置故障 |  | DCV Voltage Bias Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RapidDischarge | 快速放电动作 |  | Rapid Discharge Action | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridBreaker | 电网外部断路器故障 |  | External Circuit Breaker Fault in Power Grid | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_LoadPF | 负载功率因数过低 |  | Low Load Power Factor | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BattIOffset | 电池电流偏置故障 |  | Battery Current Bias Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PCSSwitchOn | PCS开机 |  | PCS Power On | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| PCSSwitchOff | PCS关机 |  | PCS shutdown | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| FactoryReset | 恢复出厂设置 |  | Factory Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ForceReboot | 强制重启 |  | Forced Restart | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| AutoTest | 自动测试 |  | Automatic Test | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ManualClearError | 手动清除故障 |  | Manual Fault Clear | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| PCSConnect | PCS连接 |  | PCS Connection | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| PCSDisconnect | PCS断开 |  | PCS Disconnected | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| RapidDischarge | 快速放电 |  | Quick Discharge | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SetMaxSOC | 设置SOC上限 |  | Set SOC Upper Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SetMinSOC | 设置SOC下限 |  | Set SOC Lower Limit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| RemoteSwitchVS | 远程选择VS模式 |  | Remote Select VS Mode | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| RemoteVsEn | 远程VS模式使能 |  | Remote VS Mode Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SetRemoVsFreq | 远程设置VS频率 |  | Remote setting of VS frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | Hz |  |
| SetRemoVSU | 远程设置VS电压 |  | Remote setting of VS voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | V |  |
| SetRemoVSP | 远程设置VS有功功率 |  | Remote setting of VS active power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SetRemoVSQ | 远程设置VS无功功率 |  | Remote setting of VS reactive power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| RemoteSwitchCS | 远程选择CS模式 |  | Remote selection of CS mode | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| RemoteCSPCtrlEn | 远程CS有功控制使能 |  | Remote CS active control enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| RemoteCSPCtrlMode | 远程CS有功控制模式 |  | Remote CS active control mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"有功功率模式"<br>			},<br>			"itemValue":"有功功率模式",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"直流电流模式"<br>			},<br>			"itemValue":"直流电流模式",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SetRemoCSP | 远程设置CS有功功率 |  | Remote setting of CS active power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SetRemoCSDCI | 远程设置CS直流电流 |  | Remote setting of CS DC current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | A |  |
| SetRemoCSQ | 远程设置CS无功功率 |  | Remote setting of CS reactive power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SetRemoCSPF | 远程设置CS功率因数 |  | Remote Set CS Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| RemoteCSQCtrlEn | 远程CS无功控制使能 |  | Remote CS Reactive Power Control Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| RemoteCSQCtrlMode | 远程CS无功控制模式 |  | Remote CS Reactive Power Control Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"功率因素模式"<br>			},<br>			"itemValue":"功率因素模式",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"无功功率模式"<br>			},<br>			"itemValue":"无功功率模式",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"QU曲线"<br>			},<br>			"itemValue":"QU曲线",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"QP曲线"<br>			},<br>			"itemValue":"QP曲线",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"全部禁止"<br>			},<br>			"itemValue":"全部禁止",<br>			"itemKey":"4"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| BattPreChargeEn | 电池预充电使能 |  | Battery Precharge Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SetRemoCharULim | 远程设置充电电压限值 |  | Remote Set Charge Voltage Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | V |  |
| SetRemoDischarULim | 远程设置放电电压限值 |  | Remote Set Discharge Voltage Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | V |  |
| SetRemoCharILim | 远程设置充电电流限值 |  | Remote Set Charge Current Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | A |  |
| SetRemoDischarILim | 远程设置放电电流限值 |  | Remote Set Discharge Current Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | A |  |
| SetRemoFloatCharULim | 远程设置浮充电压限值 |  | Remote Set Float Voltage Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | V |  |
| SetRemoFloatCharILim | 远程设置浮充电流限值 |  | Remote Set Float Current Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | A |  |
| SetCPSStartTimeT1 | 设置削峰填谷时间段1起始时间 |  | Set Peak Shaving and Valley Filling Period 1 Start Time | DATETIME |  | RW |  |  |
| SetCPSDeadlineT1 | 设置削峰填谷时间段1截止时间 |  | Set Peak Shaving and Valley Filling Period 1 End Time | DATETIME |  | RW |  |  |
| SetCPSPT1 | 削峰填谷时间段1功率值 |  | Peak Shaving and Valley Filling Period 1 Power Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| CPST1En | 削峰填谷时间段1使能状态 |  | Peak Shaving and Valley Filling Period 1 Enable Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| AntiRevFlowEn | 防逆流使能 |  | Anti-Reverse Current Enabled | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SOC | 荷电状态 |  | State of Charge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SOH | 健康状态 |  | Health Status | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| BatteryU | 电池电压 |  | Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| BatteryI | 电池电流 |  | Battery Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| BatteryP | 电池功率 |  | Battery Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| BattCharCurLim | 电池放电限流 |  | Battery Discharge Current Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| BattDischarCurLim | 电池充电限流 |  | Battery Charge Current Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MaxBattStackU | 电池包最高电压 |  | Battery Pack Maximum Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MinBattStackU | 电池包最低电压 |  | Battery Pack Minimum Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MaxBattStackTemp | 电池包最高温度 |  | Battery Pack Maximum Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| MinBattStackTemp | 电池包最低温度 |  | Battery Pack Minimum Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| CharERemain | 电池充电剩余电量 |  | Battery Charge Remaining Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DischarERemain | 电池放电剩余电量 |  | Battery Discharge Remaining Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalChargeCount | 总充电次数 |  | Total Charging Cycles | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| TotalDischargeCount | 总放电次数 |  | Total Discharging Times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| DayChargeCount | 日充电次数 |  | Daily Charging Times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| DayDischargeCount | 日放电次数 |  | Daily Discharging Times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| DayCharE | 当日充电量 |  | Daily Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalCharE | 累计充电量 |  | Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DayDischarE | 当日放电量 |  | Daily Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalDischarE | 累计放电量 |  | Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DayCharTime | 日充电时长 |  | Daily Charging Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalCharTime | 总充电时长 |  | Total Charging Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| DayDischarTime | 日放电时长 |  | Daily Discharged Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalDischarTime | 总放电时长 |  | Total Discharge Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| Ia | 电网A相电流 |  | Grid Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | 电网B相电流 |  | Grid Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | 电网C相电流 |  | Grid Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| GridFreq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Uab | AB线电压 |  | AB Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 |  | BC Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uca | CA线电压 |  | Line voltage CA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUUnB | 电网电压不平衡度 |  | Grid voltage unbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridPhaSeq | 电网相序 |  | Grid phase sequence | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正序"<br>			},<br>			"itemValue":"正序",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"负序"<br>			},<br>			"itemValue":"负序",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| InvertModuleTemp | 逆变模块温度 |  | Inverter module temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| AmbientTemp | 环境温度 |  | Ambient temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| BoostTemp | Boost模块温度 |  | Boost module temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| OutBoardTemp | 输出板温度 |  | Output board temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PowerBoardTemp | 功率板温度 |  | Power Board Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| GFCIRms | 漏电流侦测有效值 |  | Leakage Current Detection RMS | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| GFCIAvg | 漏电流侦测平均值 |  | Leakage Current Detection Average | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| ISO | 绝缘阻抗侦测值 |  | Insulation Impedance Detection Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| UBusPst | 正母线电压 |  | Positive Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| UBusNgt | 负母线电压 |  | Negative Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| DCVoltage | 直流电压 |  | DC Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| DCCurrent | 直流电流 |  | DC Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| S | 视在功率 |  | Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| DCInP | 直流输入功率 |  | DC Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutP | 逆变输出有功功率 |  | Inverter Output Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutQ | 逆变输出无功功率 |  | Inverter Output Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| DCIA | A相直流分量 |  | DC Component of Phase A | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| DCIB | B相直流分量 |  | DC Component of Phase B | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| DCIC | C相直流分量 |  | DC Component of Phase C | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| Efficiency | 效率 |  | Efficiency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| PF | 功率因数 |  | Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"自检"<br>			},<br>			"itemValue":"自检",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"运行"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"热备份"<br>			},<br>			"itemValue":"热备份",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"5"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_RunMode | 系统运行模式 |  | System Operation Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"AI"<br>			},<br>			"itemValue":"AI",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"PFP"<br>			},<br>			"itemValue":"PFP",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"QU"<br>			},<br>			"itemValue":"QU",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"VW"<br>			},<br>			"itemValue":"VW",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"FW"<br>			},<br>			"itemValue":"FW",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"HVRT"<br>			},<br>			"itemValue":"HVRT",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"LVRT"<br>			},<br>			"itemValue":"LVRT",<br>			"itemKey":"6"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Grid | 电网状态 |  | Grid Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"电网状态正常",<br>				"en_US":"Grid status normal"<br>			},<br>			"itemValue":"电网状态正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"电网状态异常",<br>				"en_US":"Grid status abnormal"<br>			},<br>			"itemValue":"电网状态异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_OnOffGrid | 并离网状态 |  | Grid-Connected/Off-Grid Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"并网",<br>				"en_US":"On-grid"<br>			},<br>			"itemValue":"并网",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"离网",<br>				"en_US":"Off-grid"<br>			},<br>			"itemValue":"离网",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_UnderRatedP | 降额运行 |  | Degraded Operation | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"没有降额运行",<br>				"en_US":"No derated operation"<br>			},<br>			"itemValue":"没有降额运行",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"降额运行",<br>				"en_US":"Derated operation"<br>			},<br>			"itemValue":"降额运行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_15VPowerSource | 系统15V控制电源 |  | System 15V Control Power | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"系统电源未工作",<br>				"en_US":"System power supply is not operational"<br>			},<br>			"itemValue":"系统电源未工作",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"系统电源工作",<br>				"en_US":"System power supply is operational"<br>			},<br>			"itemValue":"系统电源工作",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_InvertRun | 并网发电 |  | Grid-Connected Power Generation | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"并网发电正常",<br>				"en_US":"Normal grid-connected power generation"<br>			},<br>			"itemValue":"并网发电正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"并网发电异常",<br>				"en_US":"Abnormal grid-connected power generation"<br>			},<br>			"itemValue":"并网发电异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_StartMode | 启动模式 |  | Start Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常模式",<br>				"en_US":"Normal mode"<br>			},<br>			"itemValue":"正常模式",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"黑启动模式",<br>				"en_US":"Black start mode"<br>			},<br>			"itemValue":"黑启动模式",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Debug | 调试状态 |  | Debugging Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未调试",<br>				"en_US":"Not debugged"<br>			},<br>			"itemValue":"未调试",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"已调试",<br>				"en_US":"Debugged"<br>			},<br>			"itemValue":"已调试",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_InvSelfChk | 逆变自检模式 |  | Inverter Self-Test Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未自检",<br>				"en_US":"Not self-checked"<br>			},<br>			"itemValue":"未自检",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"已自检",<br>				"en_US":"Self-checked"<br>			},<br>			"itemValue":"已自检",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| BattSwitchOn | 电池开机 |  | Battery Power On | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| BattSwitchOff | 电池关机 |  | Battery Power Off | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| Err_Time | 近一次故障事件时间 |  | Last Fault Event Time | DATETIME |  | R |  |  |
| Ala_ACSPD | 交流避雷器异常 |  | Abnormality in Surge Arrester | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TempSensor | 温度传感器告警 |  | Temperature Sensor Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SPD | 避雷器异常 |  | Abnormality in Arrester | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Eeprom | EEPROM读写故障 |  | EEPROM Read/Write Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_InComm | 内部通讯失败告警 |  | Internal Communication Failure Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_InFan | 内部风扇告警 |  | Internal Fan Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OutFan | 外部风扇告警 |  | External Fan Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_DCPWMShut | 直流封锁 |  | DC Block | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_DCIUmB | 直流电流不平衡 |  | DC Current Imbalance | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvOutIOffset | 逆变电流偏置异常故障 |  | Inverter Current Bias Abnormal Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverTemp | 温度越限故障 |  | Temperature Limit Exceeded Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Relay | 并网继电器故障 |  | Grid Relay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridPhaseLoss | 电网断相故障 |  | Grid Phase Loss Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridUnderFreq | 电网欠频故障 |  | Grid Underfrequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridOverFreq | 电网过频故障 |  | Grid Overfrequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvOutOverI | 逆变输出过流故障 |  | Inverter Output Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridPhaseU | 电网相电压故障 |  | Grid Phase Voltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridLineU | 电网线电压故障 |  | Grid Line Voltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorIsolation | 绝缘阻抗过低故障 |  | Insulation Impedance Too Low Fault | FAULT | Err_Isolation | Err_Isolation = 1 |  |
| ErrorGFCIDynamic | 动态漏电流过流故障 |  | Dynamic Leakage Current Overcurrent Fault | FAULT | Err_GFCIDynamic | Err_GFCIDynamic = 1 |  |
| AlarmACSPD | 交流避雷器异常 |  | AC Surge Arrester Anomaly | ALARM | Ala_ACSPD | Ala_ACSPD = 1 |  |
| ErrorDCIHigh | 逆变电流直流分量越限故障 |  | Inverter Current DC Component Overlimit Fault | FAULT | Err_DCIHigh | Err_DCIHigh = 1 |  |
| ErrorDCIOffset | 逆变电流直流分量偏置保护 |  | Inverter Current DC Component Bias Protection | FAULT | Err_DCIOffset | Err_DCIOffset = 1 |  |
| ErrorOpenLoopSelfChk | 开环自检异常故障 |  | Open-loop Self-test Abnormal Fault | FAULT | Err_OpenLoopSelfChk | Err_OpenLoopSelfChk = 1 |  |
| ErrorCANComm | CAN通讯故障 |  | CAN Communication Fault | FAULT | Err_CANComm | Err_CANComm = 1 |  |
| ErrorGFCIStatic | 静态漏电流过流故障 |  | Static Leakage Current Overcurrent Fault | FAULT | Err_GFCIStatic | Err_GFCIStatic = 1 |  |
| ErrorOverBoostCur | Boost电路过流故障 |  | Boost Circuit Overcurrent Fault | FAULT | Err_OverBoostCur | Err_OverBoostCur = 1 |  |
| ErrorIsland | 孤岛故障 |  | Islanding Fault | FAULT | Err_Island | Err_Island = 1 |  |
| AlarmTempSensor | 温度传感器告警 |  | Temperature Sensor Alarm | ALARM | Ala_TempSensor | Ala_TempSensor = 1 |  |
| AlarmSPD | 避雷器异常 |  | Surge Arrester Anomaly | ALARM | Ala_SPD | Ala_SPD = 1 |  |
| AlarmEeprom | EEPROM读写故障 |  | EEPROM Read/Write Failure | ALARM | Ala_Eeprom | Ala_Eeprom = 1 |  |
| AlarmInComm | 内部通讯失败告警 |  | Internal Communication Failure Alarm | ALARM | Ala_InComm | Ala_InComm = 1 |  |
| AlarmInFan | 内部风扇告警 |  | Internal Fan Alarm | ALARM | Ala_InFan | Ala_InFan = 1 |  |
| AlarmOutFan | 外部风扇告警 |  | External Fan Alarm | ALARM | Ala_OutFan | Ala_OutFan = 1 |  |
| ErrorMCU | MCU故障 |  | MCU Failure | FAULT | Err_MCU | Err_MCU = 1 |  |
| ErrorBattIOffset | 电池电流偏置故障 |  | Battery current bias fault | FAULT | Err_BattIOffset | Err_BattIOffset = 1 |  |
| ErrorGridUUnB | 电网电压不平衡故障 |  | Grid Voltage Unbalance Fault | FAULT | Err_GridUUnB | Err_GridUUnB = 1 |  |
| ErrorGFCISensor | 漏电流传感器故障 |  | Leak Current Sensor Failure | FAULT | Err_GFCISensor | Err_GFCISensor = 1 |  |
| ErrorOverBusU | 母线过压故障 |  | Bus Overvoltage Fault | FAULT | Err_OverBusU | Err_OverBusU = 1 |  |
| ErrorPassiveIsland | 被动孤岛故障 |  | Passive Islanding Fault | FAULT | Err_PassiveIsland | Err_PassiveIsland = 1 |  |
| ErrorGridTHDU | 电网电压谐波过高故障 |  | Power Grid Voltage Harmonic Excessive Fault | FAULT | Err_GridTHDU | Err_GridTHDU = 1 |  |
| ErrorGridPhaseU | 电网相电压故障 |  | Grid phase voltage fault | FAULT | Err_GridPhaseU | Err_GridPhaseU = 1 |  |
| ErrorInvOutOverI | 逆变输出过流故障 |  | Inverter output overcurrent fault | FAULT | Err_InvOutOverI | Err_InvOutOverI = 1 |  |
| ErrorGridOverFreq | 电网过频故障 |  | Grid over-frequency fault | FAULT | Err_GridOverFreq | Err_GridOverFreq = 1 |  |
| ErrorGridUnderFreq | 电网欠频故障 |  | Grid under-frequency fault | FAULT | Err_GridUnderFreq | Err_GridUnderFreq = 1 |  |
| ErrorGridPhaseLoss | 电网断相故障 |  | Grid phase failure | FAULT | Err_GridPhaseLoss | Err_GridPhaseLoss = 1 |  |
| ErrorRelay | 并网继电器故障 |  | Grid relay fault | FAULT | Err_Relay | Err_Relay = 1 |  |
| ErrorOverTemp | 温度越限故障 |  | Temperature Limit Exceeded Fault | FAULT | Err_OverTemp | Err_OverTemp = 1 |  |
| ErrorInvOutIOffset | 逆变电流偏置异常故障 |  | Inverter Current Bias Abnormality Fault | FAULT | Err_InvOutIOffset | Err_InvOutIOffset = 1 |  |
| ErrorGridLineU | 电网线电压故障 |  | Grid Line Voltage Fault | FAULT | Err_GridLineU | Err_GridLineU = 1 |  |
| AlarmDCPWMShut | 直流封锁 |  | DC Blocking | ALARM | Ala_DCPWMShut | Ala_DCPWMShut = 1 |  |
| ErrorROCOF | ROCOF故障 |  | Rate of Change of Frequency (ROCOF) Fault | FAULT | Err_ROCOF | Err_ROCOF = 1 |  |
| ErrorHalfBusUUnB | 半母线电压不平衡 |  | Half Bus Voltage Imbalance | FAULT | Err_HalfBusUUnB | Err_HalfBusUUnB = 1 |  |
| ErrorOverHalfBusU | 半母线电压高 |  | Half Bus Voltage High | FAULT | Err_OverHalfBusU | Err_OverHalfBusU = 1 |  |
| ErrorInvPWMShut | 逆变封锁保护 |  | Inverter Block Protection | FAULT | Err_InvPWMShut | Err_InvPWMShut = 1 |  |
| ErrorOverCapCur | 滤波电容电流越限故障 |  | Filter Capacitor Current Over-limit Failure | FAULT | Err_OverCapCur | Err_OverCapCur = 1 |  |
| ErrorDCRelay | 直流继电器故障 |  | DC Relay Fault | FAULT | Err_DCRelay | Err_DCRelay = 1 |  |
| ErrorBusBattUDiff | 母线和电池电压差过大 |  | Bus and Battery Voltage Difference Excessive | FAULT | Err_BusBattUDiff | Err_BusBattUDiff = 1 |  |
| ErrorBattPara | 电池参数设置错误 |  | Battery parameter setting error | FAULT | Err_BattPara | Err_BattPara = 1 |  |
| ErrorTempSensor | 温度传感器故障 |  | Temperature Sensor Fault | FAULT | Err_TempSensor | Err_TempSensor = 1 |  |
| ErrorOnOffGridPara | 并离网参数不匹配 |  | Grid-Island Parameter Mismatch | FAULT | Err_OnOffGridPara | Err_OnOffGridPara = 1 |  |
| ErrorBattInputRevCon | 电池输入反接故障 |  | Battery input reversed polarity fault | FAULT | Err_BattInputRevCon | Err_BattInputRevCon = 1 |  |
| ErrorInvHWOverI | 逆变硬件过流故障 |  | Inverter hardware overcurrent fault | FAULT | Err_InvHWOverI | Err_InvHWOverI = 1 |  |
| ErrorGridInvUDiff | 网侧逆变侧电压不一致故障 |  | Grid-side inverter-side voltage inconsistency fault | FAULT | Err_GridInvUDiff | Err_GridInvUDiff = 1 |  |
| ErrorNoBusU | 母线无电压故障 |  | Busbar no voltage fault | FAULT | Err_NoBusU | Err_NoBusU = 1 |  |
| ErrorOverBattU | 电池电压过高故障 |  | Battery voltage too high fault | FAULT | Err_OverBattU | Err_OverBattU = 1 |  |
| ErrorDCChargeCir | 直流侧充电回路异常 |  | DC side charging circuit abnormal | FAULT | Err_DCChargeCir | Err_DCChargeCir = 1 |  |
| ErrorOverGridLineU | 电网线电压瞬时值越限故障 |  | Grid Line Voltage Transient Over-limit Fault | FAULT | Err_OverGridLineU | Err_OverGridLineU = 1 |  |
| AlarmDCIUmB | 直流电流不平衡 |  | DC current imbalance | ALARM | Ala_DCIUmB | Ala_DCIUmB = 1 |  |
| ErrorUnderBattU | 电池欠压故障 |  | Battery Under Voltage Fault | FAULT | Err_UnderBattU | Err_UnderBattU = 1 |  |
| ErrorOverDCI | 直流侧过流故障 |  | DC side overcurrent fault | FAULT | Err_OverDCI | Err_OverDCI = 1 |  |
| ErrorGFCICurOffset | 漏电流偏置故障 |  | Leakage current bias fault | FAULT | Err_GFCICurOffset | Err_GFCICurOffset = 1 |  |
| ErrorLoadCur | 负载电流偏置故障 |  | Load Current Bias Fault | FAULT | Err_LoadCur | Err_LoadCur = 1 |  |
| ErrorJETIsland | JET孤岛频率异常 |  | JET Islanding Frequency Anomaly | FAULT | Err_JETIsland | Err_JETIsland = 1 |  |
| ErrorCPLDOscil | CPLD晶振失效故障 |  | CPLD Oscillator Failure Fault | FAULT | Err_CPLDOscil | Err_CPLDOscil = 1 |  |
| ErrorOverGridUPeak | 电网电压峰值越限故障 |  | Grid Voltage Peak Over Limit Fault | FAULT | Err_OverGridUPeak | Err_OverGridUPeak = 1 |  |
| ErrorEmergCloase | 紧急按钮闭合 |  | Emergency button closed | FAULT | Err_EmergCloase | Err_EmergCloase = 1 |  |
| ErrorVNPE | NPE电压差越限故障 |  | NPE Voltage Difference Over Limit Fault | FAULT | Err_VNPE | Err_VNPE = 1 |  |
| ErrorInvRelay | 逆变继电器故障 |  | Inverter Relay Fault | FAULT | Err_InvRelay | Err_InvRelay = 1 |  |
| ErrorDCVUOffset | DCV电压偏置故障 |  | DCV Voltage Bias Fault | FAULT | Err_DCVUOffset | Err_DCVUOffset = 1 |  |
| ErrorRapidDischarge | 快速放电动作 |  | Rapid Discharge Action | FAULT | Err_RapidDischarge | Err_RapidDischarge = 1 |  |
| ErrorGridBreaker | 电网外部断路器故障 |  | Grid external circuit breaker fault | FAULT | Err_GridBreaker | Err_GridBreaker = 1 |  |
| ErrorLoadPF | 负载功率因数过低 |  | Load power factor too low | FAULT | Err_LoadPF | Err_LoadPF = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| RemoteCSPCtrlModeCmd | 远程CS有功控制模式 |  | Remote CS Active Power Control Mode | RemoteCSPCtrlMode |  |  |
| RemoCharULimSet | 远程设置充电电压限值 |  | Remote Setting of Charge Voltage Limit | SetRemoCharULim |  |  |
| RemoCSDCISet | 远程设置CS直流电流 |  | Remote Setting of CS DC Current | SetRemoCSDCI |  |  |
| RemoCSPFSet | 远程设置CS功率因数 |  | Remote Setting of CS Power Factor | SetRemoCSPF |  |  |
| RemoCSPSet | 远程设置CS有功功率 |  | Remote Setting of CS Active Power | SetRemoCSP |  |  |
| RemoCSQSet | 远程设置CS无功功率 |  | Remote Setting of CS Reactive Power | SetRemoCSQ |  |  |
| RemoDischarILimSet | 远程设置放电电流限值 |  | Remote Setting of Discharge Current Limit | SetRemoDischarILim |  |  |
| RemoDischarULimSet | 远程设置放电电压限值 |  | Remote Setting of Discharge Voltage Limit | SetRemoDischarULim |  |  |
| RemoFloatCharILimSet | 远程设置浮充电流限值 |  | Remote Setting of Float Current Limit | SetRemoFloatCharILim |  |  |
| RemoFloatCharULimSet | 远程设置浮充电压限值 |  | Remote Setting of Float Voltage Limit | SetRemoFloatCharULim |  |  |
| RemoteCSPCtrlEnCmd | 远程CS有功控制使能 |  | Remote CS Active Control Enable | RemoteCSPCtrlEn |  |  |
| RemoCharILimSet | 远程设置充电电流限值 |  | Remote Set Charging Current Limit | SetRemoCharILim |  |  |
| RemoteCSQCtrlEnCmd | 远程CS无功控制使能 |  | Remote CS Reactive Power Control Enabled | RemoteCSQCtrlEn |  |  |
| RemoteCSQCtrlModeCmd | 远程CS无功控制模式 |  | Remote CS Reactive Power Control Mode | RemoteCSQCtrlMode |  |  |
| RemoteSwitchCSCmd | 远程选择CS模式 |  | Remote Select CS Mode | RemoteSwitchCS |  |  |
| RemoteSwitchVSCmd | 远程选择VS模式 |  | Remote Select VS Mode | RemoteSwitchVS |  |  |
| RemoteVsEnCmd | 远程VS模式使能 |  | Remote VS Mode Enable | RemoteVsEn |  |  |
| RemoVsFreqSet | 远程设置VS频率 |  | Remote Set VS Frequency | SetRemoVsFreq |  |  |
| RemoVSPSet | 远程设置VS有功功率 |  | Remote Set VS Active Power | SetRemoVSP |  |  |
| RemoVSQSet | 远程设置VS无功功率 |  | Remote Set VS Reactive Power | SetRemoVSQ |  |  |
| RemoVSUSet | 远程设置VS电压 |  | Remote Set VS Voltage | SetRemoVSU |  |  |
| FactoryResetCmd | 恢复出厂设置 |  | Factory Reset | FactoryReset |  |  |
| AutoTestCmd | 自动测试 |  | Auto Test | AutoTest |  |  |
| BattPreChargeEn | 电池预充电使能 |  | Battery Pre-Charging Enable | BattPreChargeEn |  |  |
| BattSwitchOffCmd | 电池关机 |  | Battery Shutdown | BattSwitchOff |  |  |
| BattSwitchOnCmd | 电池开机 |  | Battery Startup | BattSwitchOn |  |  |
| CPSDeadlineT1Set | 设置削峰填谷时间段1截止时间 |  | Set Valley Fill Time Period 1 End Time | SetCPSDeadlineT1 |  |  |
| CPSEnCmd | CPS使能 |  | CPS Enable | CPSEn |  |  |
| CPSPT1Set | 削峰填谷时间段1功率值 |  | Valley Fill Time Period 1 Power Value | SetCPSPT1 |  |  |
| CPSStartTimeT1Set | 设置削峰填谷时间段1起始时间 |  | Set Valley Fill Time Period 1 Start Time | SetCPSStartTimeT1 |  |  |
| CPST1EnCmd | 削峰填谷时间段1使能状态 |  | Valley Fill Time Period 1 Enable Status | CPST1En |  |  |
| AntiRevFlowEnCmd | 防逆流使能 |  | Anti-Reverse Flow Enabled | AntiRevFlowEn |  |  |
| ForceRebootCmd | 强制重启 |  | Forced Reboot | ForceReboot |  |  |
| ManualClearErrorCmd | 手动清除故障 |  | Manual Clear Fault | ManualClearError |  |  |
| MaxSOCSet | 设置SOC上限 |  | Set SOC Upper Limit | SetMaxSOC |  |  |
| MinSOCSet | 设置SOC下限 |  | Set SOC Lower Limit | SetMinSOC |  |  |
| PCSConnectCmd | PCS连接 |  | PCS Connected | PCSConnect |  |  |
| PCSDisconnectCmd | PCS断开 |  | PCS Disconnected | PCSDisconnect |  |  |
| PCSSwitchOffCmd | PCS关机 |  | PCS Shutdown | PCSSwitchOff |  |  |
| PCSSwitchOnCmd | PCS开机 |  | PCS Power On | PCSSwitchOn |  |  |
| RapidDischargeCmd | 快速放电 |  | Rapid Discharge | RapidDischarge |  |  |
