# public_MCB_1P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_MCB_1P_V1_0_2 | (交流)单相微型断路器 | (交流)单相微型断路器 | （AC）MCB | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device SN | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| RatedCurrent | 额定电流 |  | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 | 硬件版本号 | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| MechanicalLife | 机械寿命 |  | Mechanical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| ElectricalLife | 电气寿命 |  | Electrical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WorkingStatus | 状态字 |  |  | BITMAP |  | R |  |  |
| EQE | 反向无功电能 |  | Export Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI | 正向无功电能 |  | Import Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EPE | 反向有功电能 |  | Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI | 正向有功电能 |  | Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Err_P | 故障事件前有功功率 |  | Pre-fault Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Err_I | 故障事件前电流 |  | Pre-fault Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_UnderVoltage | 欠压故障 |  | Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_U | 故障事件前电压 |  | Pre-fault Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ires | 故障事件前剩余电流 |  | Pre-fault Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| ComEQ | 组合无功电能 |  | Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Err1th_Ires | 故障事件前剩余电流 |  | Pre-failure event residual current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| Ires | 剩余电流 |  | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| U | 电压 |  | Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| S | 视在功率 |  | Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Err_Sta | 故障事件时运行状态 |  | Operating Status at Fault Event | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| TempOut | 出线温度 |  | Outlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempIn | 进线温度 |  | Inlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Q | 无功功率 |  | Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| PF | 功率因数 |  | Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| P | 有功功率 |  | Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| I | 电流 |  | Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| DeviceTime | 设备时间 |  | Equipment Time | DATETIME |  | RW |  |  |
| TempOnChip | 片上温度 |  | On-chip Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Err_TempOnChip | 故障事件前片上温度 |  | Die Temperature Before Fault Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Err_Freq | 故障事件前频率 |  | Frequency Before Fault Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Err_Time | 故障事件时间 |  | Fault Event Time | DATETIME |  | R |  |  |
| Err_OverFreq | 过频故障 |  | Overfrequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PowerLimit | 功率越限故障 |  | Power Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| LeakageCheck | 漏电自检 |  | Leakage Self-Test | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| LeakageTest | 漏电试跳 |  | Leakage Test Trip | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Open | 分闸 |  | Tripped | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Close | 合闸 |  | Close Circuit | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lockout | 锁死 |  | Locked | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lock | 锁定 |  | Locked | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Unlock | 解锁 |  | Unlock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Ala_PowerLimit | 功率限定告警 |  | Power Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderFreq | 欠频告警 |  | Under Frequency Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverFreq | 过频告警 |  | Overfrequency Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTemp | 温度越限告警 |  | Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 |  | Overload Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| ComEP | 组合有功电能 |  | Combined Active Power Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Err_OverTemp | 温度越限故障 |  | Temperature Limit Exceeded Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVoltage | 过压告警 |  | Overvoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderVoltage | 欠压告警 |  | Undervoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Leakage | 漏电告警 |  | Leakage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| OpenCount | 分闸次数 |  | Trip Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| OperationCount | 操作次数 |  | Operation Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| Sta_OveUndVolLock | 过欠压锁死 |  | Over-Under Voltage Lockout | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未过欠压锁死",<br>				"en_US":"No overvoltage"<br>			},<br>			"itemValue":"未过欠压锁死",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"过欠压锁死",<br>				"en_US":"Overvoltage"<br>			},<br>			"itemValue":"过欠压锁死",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| LEDBlink | LED灯闪烁 |  | LED light blinking | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Sta_RemoConLock | 遥控锁死 |  | Remote Lockout | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未遥控锁死",<br>				"en_US":"No remote control lockout"<br>			},<br>			"itemValue":"未遥控锁死",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"遥控锁死",<br>				"en_US":"Remote control lockout"<br>			},<br>			"itemValue":"遥控锁死",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_ManualAuto | 手自动 |  | Manual/Automatic | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"自动",<br>				"en_US":"Automatic"<br>			},<br>			"itemValue":"自动",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"手动",<br>				"en_US":"Manual"<br>			},<br>			"itemValue":"手动",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderFreq | 欠频故障 |  | Underfrequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverVoltage | 过压故障 |  | Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Leakage | 漏电故障 |  | Leakage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverCurrent | 过载故障 |  | Overload Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err1th_TempOnChip | 故障事件前片上温度 |  | Pre-failure event chip temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Err_Reason | 故障事件原因 |  | Cause of Fault Event | BITMAP |  | R |  |  |
| Err1th_P | 故障事件前有功功率 |  | Pre-failure event active power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Err1th_Freq | 故障事件前频率 |  | Pre-failure event frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Err1th_Time | 故障事件时间 |  | Time of failure event | DATETIME |  | R |  |  |
| Err1th_Reason | 故障事件原因 |  | Cause of failure event | BITMAP |  | R |  |  |
| Err1th_U | 故障事件前电压 |  | Pre-failure event voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err1th_I | 故障事件前电流 |  | Current Before Fault Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorRemoteTest | 远程试跳故障 |  | Remote test trip fault | FAULT | Err_Leakage,Err_Ires,Err_Sta,Err_Time | Err_Leakage = 1 |  |
| ErrorOverVoltage | 过压故障 |  | Overvoltage fault | FAULT | Err_OverVoltage,Err_Time,Err_Sta,Err_U | Err_OverVoltage = 1 |  |
| ErrorUnderVoltage | 欠压故障 |  | Undervoltage fault | FAULT | Err_UnderVoltage,Err_U,Err_Sta,Err_Time | Err_UnderVoltage = 1 |  |
| ErrorLeakage | 漏电故障 |  | Leakage fault | FAULT | Err_Leakage,Err_Ires,Err_Sta,Err_Time | Err_Leakage = 1 |  |
| ErrorOverCurrent | 过载故障 |  | Overload failure | FAULT | Err_OverCurrent,Err_Sta,Err_Time,Err_I | Err_OverCurrent = 1 |  |
| ErrorOverTemp | 温度越限故障 |  | Temperature limit fault | FAULT | Err_OverTemp,Err_TempOnChip,Err_Sta,Err_Time | Err_OverTemp = 1 |  |
| ErrorOverFreq | 过频故障 |  | Overfrequency fault | FAULT | Err_OverFreq,Err_Freq,Err_Sta,Err_Time | Err_OverFreq = 1 |  |
| ErrorUnderFreq | 欠频故障 |  | Underfrequency fault | FAULT | Err_UnderFreq,Err_Freq,Err_Sta,Err_Time | Err_UnderFreq = 1 |  |
| ErrorButtonTest | 按钮试跳故障 |  | Button test trip fault | FAULT | Err_Leakage,Err_Ires,Err_Sta,Err_Time | Err_Leakage = 1 |  |
| AlarmPowerLimit | 功率越限告警 |  | Power limit alarm | ALARM | Ala_PowerLimit | Ala_PowerLimit = 1 |  |
| ErrorPowerLimit | 功率越限故障 |  | Power Out-of-Limit Fault | FAULT | Err_PowerLimit,Err_P,Err_Sta,Err_Time | Err_PowerLimit = 1 |  |
| AlarmOverVoltage | 过压告警 |  | Overvoltage Alarm | ALARM | Ala_OverVoltage | Ala_OverVoltage = 1 |  |
| AlarmUnderVoltage | 欠压告警 |  | Undervoltage alarm | ALARM | Ala_UnderVoltage | Ala_UnderVoltage = 1 |  |
| AlarmLeakage | 漏电告警 |  | Leakage Alarm | ALARM | Ala_Leakage | Ala_Leakage = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload Alarm | ALARM | Ala_OverCurrent | Ala_OverCurrent = 1 |  |
| AlarmOverTemp | 温度越限告警 |  | Temperature Out-of-Limit Alarm | ALARM | Ala_OverTemp | Ala_OverTemp = 1 |  |
| AlarmOverFreq | 过频告警 |  | Overfrequency Alarm | ALARM | Ala_OverFreq | Ala_OverFreq = 1 |  |
| AlarmUnderFreq | 欠频告警 |  | Underfrequency Alarm | ALARM | Ala_UnderFreq | Ala_UnderFreq = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| CloseCmd | 合闸 |  | Close the circuit | Unlock,Close | Sta_Device |  |
| LeakageCheckCmd | 漏电自检 |  | Leakage Self-Test | LeakageCheck |  |  |
| LeakageTestCmd | 漏电试跳 |  | Leakage Trip Test | LeakageTest |  |  |
| LEDBlinkCmd | LED灯闪烁 |  | LED Light Flashing | LEDBlink |  |  |
| LockCmd | 锁定 |  | Lock | Lock |  |  |
| LockoutCmd | 锁死 |  | Locked | Lockout |  |  |
| OpenCmd | 分闸 |  | Trip | Unlock,Open | Sta_Device |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
| UnlockCmd | 解锁 |  | Unlock | Unlock |  |  |
