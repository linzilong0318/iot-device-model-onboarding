# public_ElectricMeter_1P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ElectricMeter_1P_V1_0_2 | (交流)单相电表 |  | (AC) Single-Phase Meter | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ComEPT3 | 组合有功费率3电能 |  | Combined Active Energy Rate 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| THDI | 电压总谐波畸变率 |  | Total Harmonic Distortion of Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDU | 电流总谐波畸变率 |  | Total Harmonic Distortion of Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| HarmonicRmsI | 电流谐波有效值 |  | Current Harmonic Root Mean Square | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalI | 电流基波值 |  | Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ires | 剩余电流 |  | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| ComEP | 组合有功电能 |  | Combined Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT1 | 组合有功费率1电能 |  | Combined Active Energy Rate 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT5 | 正向有功费率5电能 |  | Forward Active Energy for Rate 5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT3 | 正向有功费率3电能 |  | Forward Active Power Rate 3 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DeviceTime | 设备时间 |  | Device Time | DATETIME |  | RW |  |  |
| ComEPT5 | 组合有功费率5电能 |  | Active Energy for Combined Rate 5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI | 正向有功电能 |  | Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT1 | 正向有功费率1电能 |  | Forward Active Energy for Rate 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT2 | 正向有功费率2电能 |  | Forward Active Energy for Rate 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| EPIT4 | 正向有功费率4电能 |  | Forward Active Energy for Rate 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT2 | 组合有功费率2电能 |  | Combined Active Energy Rate 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE | 反向有功电能 |  | Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET1 | 反向有功费率1电能 |  | Reverse Active Energy for Rate 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET2 | 反向有功费率2电能 |  | Reverse Active Energy for Rate 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET3 | 反向有功费率3电能 |  | Reverse Active Power Rate 3 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET4 | 反向有功费率4电能 |  | Reverse Active Power Rate 4 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DI1 | 开关量输入1 |  | Digital Input 1 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI2 | 开关量输入2 |  | Digital Input 2 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI3 | 开关量输入3 |  | Digital Input 3 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI4 | 开关量输入4 |  | Digital Input 4 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI5 | 开关量输入5 |  | Digital Input 5 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI6 | 开关量输入6 |  | Digital Input 6 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI7 | 开关量输入7 |  | Digital Input 7 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| I | 电流 |  | Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FactoryReset | 恢复出厂设置 |  | Factory Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| ClearE | 电能清零 |  | Energy Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| EPET5 | 反向有功费率5电能 |  | Reverse Active Energy Rate 5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Q | 无功功率 |  | Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| S | 视在功率 |  | Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| PF | 功率因数 |  | Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| EP | 总有功电能 |  | Total Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQ | 总无功电能 |  | Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQI | 正向无功电能 |  | Forward Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Ala_UnderFreq | 欠频告警 |  | Under Frequency Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| P | 有功功率 |  | Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| MaxDmdEPI | 正向有功最大需量 |  | Forward Active Maximum Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| MaxDmdEPE | 反向有功最大需量 |  | Reverse Active Maximum Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| CreditRemain | 剩余金额 |  | Remaining Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Temp | 温度 |  | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| U | 电压 |  | Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| ComEPT4 | 组合有功费率4电能 |  | Composite Active Rate 4 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Ala_Smoke | 烟感告警 |  | Smoke Alarm Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| EQE | 反向无功电能 |  | Reverse Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Ala_OverFreq | 过频告警 |  | Over Frequency Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 |  | Overload Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderVoltage | 欠压告警 |  | Undervoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVoltage | 过压告警 |  | Overvoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| CurrentRatio | 电流变比 |  | Current Ratio | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| VoltageRatio | 电压变比 |  | Voltage Ratio | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| CreditTotal | 总购电金额 |  | Total Electricity Purchase Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| EnergyRemain | 剩余电量 |  | Remaining Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DI8 | 开关量输入8 |  | Digital Input 8 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DO1 | 开关量输出1 |  | Digital Output 1 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO2 | 开关量输出2 |  | Digital Output 2 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO3 | 开关量输出3 |  | Digital Output 3 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO4 | 开关量输出4 |  | Digital Output 4 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| CurrentDmdP | 当前有功需量 |  | Current Active Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmSmoke | 烟感告警 |  | Smoke Alarm Alert | ALARM | Ala_Smoke | Ala_Smoke = 1 |  |
| AlarmUnderFreq | 欠频告警 |  | Under-frequency alarm | ALARM | Ala_UnderFreq | Ala_UnderFreq = 1 |  |
| AlarmOverFreq | 过频告警 |  | Over-frequency alarm | ALARM | Ala_OverFreq | Ala_OverFreq = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload alarm | ALARM | Ala_OverCurrent | Ala_OverCurrent = 1 |  |
| AlarmUnderVoltage | 欠压告警 |  | Under-voltage alarm | ALARM | Ala_UnderVoltage | Ala_UnderVoltage = 1 |  |
| AlarmOverVoltage | 过压告警 |  | Over-voltage alarm | ALARM | Ala_OverVoltage | Ala_OverVoltage = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| ClearECmd | 电能清零 |  | Energy Reset | ClearE |  |  |
| DO1Cmd | 开关量输出1控制 |  | Switch Output 1 Control | DO1 |  |  |
| DO2Cmd | 开关量输出2控制 |  | Switch Output 2 Control | DO2 |  |  |
| DO3Cmd | 开关量输出3控制 |  | Switch Output 3 Control | DO3 |  |  |
| DO4Cmd | 开关量输出4控制 |  | Digital Output 4 Control | DO4 |  |  |
| FactoryResetCmd | 恢复出厂设置 |  | Factory Reset | FactoryReset |  |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
