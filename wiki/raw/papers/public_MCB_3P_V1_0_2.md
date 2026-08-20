# public_MCB_3P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_MCB_3P_V1_0_2 | (交流)三相微型断路器 | (交流)三相微型断路器 | AC MCB | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| RatedCurrent | 额定电流 |  | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| MechanicalLife | 机械寿命 |  | Mechanical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| ElectricalLife | 电气寿命 |  | Electrical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WorkingSts | 状态字 |  |  | BITMAP |  | R |  |  |
| ComEQ | 组合无功电能 |  | Reactive Power Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQE | 反向无功电能 |  | Reverse Reactive Power Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI | 正向无功电能 |  | Forward Reactive Power Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Qc | C相无功功率 |  | Phase C Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Uca | CA线电压 |  | Line Voltage CA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PFc | C相功率因数 |  | Phase C Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pb | B相有功功率 |  | Phase B Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Sb | B相视在功率 |  | Phase B Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Qb | B相无功功率 |  | Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| PFb | B相功率因数 |  | Phase B Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pa | A相有功功率 |  | Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Sa | A相视在功率 |  | Phase A Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Qa | A相无功功率 |  | Phase A Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| PFa | A相功率因数 |  | Phase A Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| DeviceTime | 设备时间 |  | Equipment Time | DATETIME |  | RW |  |  |
| Ua | A相电压 |  | Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ia | A相电流 |  | Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ub | B相电压 |  | Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ib | B相电流 |  | Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uc | C相电压 |  | Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ic | C相电流 |  | Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| In | 中性线电流 |  | Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uab | AB线电压 |  | Line Voltage AB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 |  | Line Voltage BC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| EPE | 反向有功电能 |  | Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Err_Pb | 故障事件前B相有功功率 |  | Pre-fault Phase B Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Err_Time | 故障事件时间 |  | Fault Event Time | DATETIME |  | R |  |  |
| Err_Reason | 故障事件原因 |  | Fault Event Reason | BITMAP |  | R |  |  |
| Err_Sta | 故障事件时运行状态 |  | Operation Status During Fault Event | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Ua | 故障事件前A相电压 |  | Pre-fault Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ub | 故障事件前B相电压 |  | Pre-fault Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ia | 故障事件前A相电流 |  | Pre-fault Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ib | 故障事件前B相电流 |  | Pre-fault Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ic | 故障事件前C相电流 |  | Pre-fault Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_In | 故障事件前中性线电流 |  | Pre-fault Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Pt | 故障事件前总有功功率 |  | Pre-fault Total Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Err_Pa | 故障事件前A相有功功率 |  | Pre-fault Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Sc | C相视在功率 |  | Phase C Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Err_Pc | 故障事件前C相有功功率 |  | Pre-fault Phase C Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Err_Freq | 故障事件前频率 |  | Pre-fault Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Err_Ires | 故障事件前剩余电流 |  | Pre-fault Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| Err_TempOnChip | 故障事件前片上温度 |  | Pre-fault event chip temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Err_Uc | 故障事件前C相电压 |  | Pre-fault Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Sta_Device | 设备状态 |  | Equipment status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| St | 总视在功率 |  | Total apparent power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Qt | 总无功功率 |  | Total reactive power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Pt | 总有功功率 |  | Total active power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| PFt | 总功率因数 |  | Total power factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pc | C相有功功率 |  | Phase C active power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Ala_OverFreq | 过频告警 |  | Over frequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverFreq | 过频故障 |  | Over frequency fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderFreq | 欠频故障 |  | Under frequency fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ButtonTest | 按钮试跳故障 |  | Button test jump fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RemoteTest | 远程试跳故障 |  | Remote test jump fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PowerLimit | 功率越限故障 |  | Over Power Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVoltage | 过压告警 |  | Overvoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderVoltage | 欠压告警 |  | Undervoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Leakage | 漏电告警 |  | Leakage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 |  | Overload Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTemp | 温度越限告警 |  | Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseLoss | 断相告警 |  | Phase Failure Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaseLoss | 断相故障 |  | Phase failure fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderFreq | 欠频告警 |  | Under-frequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PowerLimit | 功率越限告警 |  | Power limit exceeded alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Unlock | 解锁 |  | Unlock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lock | 锁定 |  | Lock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lockout | 锁死 |  | Lock Dead | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Close | 合闸 |  | Close | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Open | 分闸 |  | Trip | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| LeakageTest | 漏电试跳 |  | Leakage Test Trip | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| LeakageCheck | 漏电自检 |  | Leakage Self-Test | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| TempOutN | 中性线出线温度 |  | Neutral Line Output Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| LEDBlink | LED灯闪烁 |  | LED light flashing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| ComEP | 组合有功电能 |  | Combined active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Ires | 剩余电流 |  | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| TempInA | A相进线温度 |  | Temperature of Phase A Inlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutA | A相出线温度 |  | Temperature of Phase A Outlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInB | B相进线温度 |  | Temperature of Phase B Inlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutB | B相出线温度 |  | Temperature of Phase B Outlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInC | C相进线温度 |  | Temperature of Phase C Inlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutC | C相出线温度 |  | Temperature of Phase C Outlet | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInN | 中性线进线温度 |  | Neutral Line Input Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| EPI | 正向有功电能 |  | Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| OpenCount | 分闸次数 |  | Trip Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| LeakOpenCount | 漏电分闸次数 |  | Leakage Trip Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| Sta_OveUndVolLock | 过欠压锁死 |  | Over/Undervoltage Lockout | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未过欠压锁死",<br>				"en_US":"No overvoltage"<br>			},<br>			"itemValue":"未过欠压锁死",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"过欠压锁死",<br>				"en_US":"Overvoltage"<br>			},<br>			"itemValue":"过欠压锁死",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_RemoConLock | 遥控锁死 |  | Remote Lockout | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未遥控锁死",<br>				"en_US":"No remote control lockout"<br>			},<br>			"itemValue":"未遥控锁死",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"遥控锁死",<br>				"en_US":"Remote control lockout"<br>			},<br>			"itemValue":"遥控锁死",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_ManualAuto | 手自动 |  | Manual/Automatic | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"自动",<br>				"en_US":"Automatic"<br>			},<br>			"itemValue":"自动",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"手动",<br>				"en_US":"Manual"<br>			},<br>			"itemValue":"手动",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverVoltage | 过压故障 |  | Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderVoltage | 欠压故障 |  | Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Leakage | 漏电故障 |  | Leakage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverCurrent | 过载故障 |  | Overload fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverTemp | 温度越限故障 |  | Temperature limit fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorRemoteTest | 远程试跳故障 |  | Remote test jump failure | FAULT | Err_RemoteTest,Err_Ires,Err_Sta,Err_Time | Err_RemoteTest = 1 |  |
| ErrorOverVoltage | 过压故障 |  | Overvoltage fault | FAULT | Err_OverVoltage,Err_Time,Err_Sta,Err_Ua,Err_Ub,Err_Uc | Err_OverVoltage = 1 |  |
| ErrorUnderVoltage | 欠压故障 |  | Undervoltage fault | FAULT | Err_UnderVoltage,Err_Time,Err_Sta,Err_Ua,Err_Ub,Err_Uc | Err_UnderVoltage = 1 |  |
| ErrorLeakage | 漏电故障 |  | Leakage fault | FAULT | Err_Leakage,Err_Ires,Err_Sta,Err_Time | Err_Leakage = 1 |  |
| ErrorOverCurrent | 过载故障 |  | Overload fault | FAULT | Err_OverCurrent,Err_Sta,Err_Time,Err_Ic,Err_Ia,Err_Ib | Err_OverCurrent = 1 |  |
| ErrorOverTemp | 温度越限故障 |  | Temperature limit fault | FAULT | Err_OverTemp,Err_Sta,Err_TempOnChip,Err_Time | Err_OverTemp = 1 |  |
| ErrorPhaseLoss | 断相故障 |  | Phase failure | FAULT | Err_PhaseLoss,Err_Sta,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_PhaseLoss = 1 |  |
| ErrorOverFreq | 过频故障 |  | Over Frequency Fault | FAULT | Err_OverFreq,Err_Time,Err_Sta,Err_Freq | Err_OverFreq = 1 |  |
| ErrorUnderFreq | 欠频故障 |  | Under Frequency Fault | FAULT | Err_UnderFreq,Err_Time,Err_Sta,Err_Freq | Err_UnderFreq = 1 |  |
| ErrorButtonTest | 按钮试跳故障 |  | Button test jump failure | FAULT | Err_ButtonTest,Err_Ires,Err_Sta,Err_Time | Err_ButtonTest = 1 |  |
| AlarmPowerLimit | 功率越限告警 |  | Power Limit Alarm | ALARM | Ala_PowerLimit | Ala_PowerLimit = 1 |  |
| ErrorPowerLimit | 功率越限故障 |  | Over Power Limit Fault | FAULT | Err_PowerLimit,Err_Pa,Err_Pb,Err_Pc,Err_Pt,Err_Sta,Err_Time | Err_PowerLimit = 1 |  |
| AlarmOverVoltage | 过压告警 |  | Overvoltage warning | ALARM | Ala_OverVoltage | Ala_OverVoltage = 1 |  |
| AlarmUnderVoltage | 欠压告警 |  | Undervoltage Alarm | ALARM | Ala_UnderVoltage | Ala_UnderVoltage = 1 |  |
| AlarmLeakage | 漏电告警 |  | Leakage Alarm | ALARM | Ala_Leakage | Ala_Leakage = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload Alarm | ALARM | Ala_OverCurrent | Ala_OverCurrent = 1 |  |
| AlarmOverTemp | 温度越限告警 |  | Temperature Limit Alarm | ALARM | Ala_OverTemp | Ala_OverTemp = 1 |  |
| AlarmPhaseLoss | 断相告警 |  | Phase Failure Alarm | ALARM | Ala_PhaseLoss | Ala_PhaseLoss = 1 |  |
| AlarmOverFreq | 过频告警 |  | Over Frequency Alarm | ALARM | Ala_OverFreq | Ala_OverFreq = 1 |  |
| AlarmUnderFreq | 欠频告警 |  | Under Frequency Alarm | ALARM | Ala_UnderFreq | Ala_UnderFreq = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| CloseCmd | 合闸 |  | Close the circuit | Unlock,Close | Sta_Device |  |
| LeakageCheckCmd | 漏电自检 |  | Leakage Self-Test | LeakageCheck |  |  |
| LeakageTestCmd | 漏电试跳 |  | Leakage Test Trip | LeakageTest |  |  |
| LEDBlinkCmd | LED灯闪烁 |  | LED Light Flashing | LEDBlink |  |  |
| LockCmd | 锁定 |  | Lock | Lock |  |  |
| LockoutCmd | 锁死 |  | Lockout | Lockout |  |  |
| OpenCmd | 分闸 |  | Trip Open | Unlock,Open | Sta_Device |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
| UnlockCmd | 解锁 |  | Unlock | Unlock |  |  |
