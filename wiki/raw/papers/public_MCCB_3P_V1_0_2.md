# public_MCCB_3P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_MCCB_3P_V1_0_2 | (交流) 塑壳断路器 | (交流) 塑壳断路器 | AC Molded Case Circuit Breaker | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN | 设备SN | Device SN | STRING |  |  | False |  |
| FrameCurrent | 壳架电流 | 壳架电流 | Frame current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedVoltage | 额定电压 | 额定电压 | Rated voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedCurrent | 额定电流 | 额定电流 | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedFrequency | 工作频率 | 工作频率 | Operating frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| SoftwareVersion | 软件版本号 | 软件版本号 | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 | 硬件版本号 | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 | 安装位置 | Installation Location | STRING |  |  | False |  |
| MechanicalLife | 机械寿命 | 机械寿命 | Mechanical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| ElectricalLife | 电气寿命 | 电气寿命 | Electrical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | x | False |  |
| Manufacturer | 生产厂家 | 生产厂家 | Manufacturer | STRING |  |  | False |  |
| DeviceType | 设备类型 | 设备类型 | Device Type | STRING |  |  | False |  |
| DeviceModel | 设备型号 | 设备型号 | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WorkingSts | 状态字 |  |  | BITMAP |  | R |  |  |
| Q1EQ_A | A相第一象限无功总电能 | A相第一象限无功总电能 | Phase A Quadrant I Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_A | A相第二象限无功总电能 | A相第二象限无功总电能 | Phase A Quadrant II Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_A | A相第三象限无功总电能 | A相第三象限无功总电能 | Phase A Quadrant III Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQ_A | A相第四象限无功总电能 | A相第四象限无功总电能 | Phase A Quadrant IV Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_B | B相第二象限无功总电能 | B相第二象限无功总电能 | Phase B Quadrant 2 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_B | BA相第三象限无功总电能 | BA相第三象限无功总电能 | Phase BA Quadrant 3 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ_C | C相第一象限无功总电能 | C相第一象限无功总电能 | Phase C Quadrant 1 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQ_B | B相第四象限无功总电能 | B相第四象限无功总电能 | Phase B Quadrant 4 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_C | C相第二象限无功总电能 | C相第二象限无功总电能 | Phase C Quadrant 2 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_C | C相第三象限无功总电能 | C相第三象限无功总电能 | Phase C Quadrant 3 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQ_C | C相第四象限无功总电能 | C相第四象限无功总电能 | Phase C Quadrant 4 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ_B | B相第一象限无功总电能 | B相第一象限无功总电能 | Phase B Quadrant 1 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_C | C相组合无功电能 | C相组合无功电能 | Phase C Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_A | A相组合无功电能 | A相组合无功电能 | Phase A Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQE | 反向无功电能 | 反向无功电能 | Reverse Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI | 正向无功电能 | 正向无功电能 | Forward reactive energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQt | 总无功电能 | 总无功电能 | Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_B | B相组合无功电能 | B相组合无功电能 | Phase B Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ | 组合无功电能 | 组合无功电能 | Combined reactive energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Ala_IUnB | 电流不平衡告警 |  | Current Imbalance Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UUnB | 电压不平衡告警 |  | Voltage Unbalance Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| RemoteReSetInf | 远程复位操作状态字 |  | Remote Reset Operation Status Word | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReStart | 远程程序重启 |  | Remote Program Restart | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| LeakageCheck | 漏电自检 |  | Earth Leakage Self-Test | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| LeakageTest | 漏电试跳 |  | Leakage Trip Test | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lockout | 锁死 |  | Locked Out | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Ala_UnderVol | 欠压告警 | 欠压告警 | Undervoltage Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseLoss | 断相告警 | 断相告警 | Phase Failure Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverFreq | 过频告警 | 过频告警 | Over-frequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderFreq | 欠频告警 | 欠频告警 | Under Frequency Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OveCurLonDel | 过载长延时告警 | 过载长延时告警 | Overload Long Delay Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseNLoss | 断零告警 | 断零告警 | Zero Sequence Disconnection Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevPower | 逆功率告警 | 逆功率告警 | Reverse Power Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaSeq | 相序告警 | 相序告警 | Phase Sequence Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Gnd | 接地故障告警 | 接地故障 | Ground Fault Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TermTemp | 接线端子温度告警 | 接线端子温度告警 | Terminal Temperature Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RHCtrl | 控制器湿度告警 | 控制器湿度告警 | Controller Humidity Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TempCtrl | 控制器温度告警 | 控制器温度告警 | Controller Temperature Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SudResiI | 突变剩余电流告警 | 突变剩余电流告警 | Sudden Residual Current Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_GraResiI | 缓变剩余电流告警 | 缓变剩余电流告警 | Slow Change Residual Current Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_AntiIsLand | 防孤岛告警 | 防孤岛告警 | Anti-Islanding Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SelfDiag | 自诊断保护告警 | 自诊断保护告警 | Self-diagnostic Protection Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 | 过载告警 | Overload Alert | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RunOverTime | 运行超时告警 | 运行超时告警 | Running Time Exceeded Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_LifeTime | 寿命超时告警 | 寿命超时告警 | Lifetime Overdue Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVol | 过压告警 | 过压告警 | Overvoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"告警恢复",<br>				"en_US":"Alarm triggered"<br>			},<br>			"itemValue":"告警恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警发生",<br>				"en_US":"Alarm resolved"<br>			},<br>			"itemValue":"告警发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_SelfDiagProt | 自诊断保护故障 | 自诊断保护故障 | Self-diagnosis Protection Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_AntiIsLand | 防孤岛故障 | 防孤岛故障 | Anti-Islanding Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GraResiI | 缓变剩余电流越限故障 | 缓变剩余电流越限故障 | Slowly Changing Residual Current Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_SudResiI | 突变剩余电流越限故障 | 突变剩余电流故障 | Mutation Residual Current Overlimit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RHCtrl | 控制器湿度越限故障 | 控制器湿度越限故障 | Controller Humidity Exceeding Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TempCtrl | 控制器温度越限故障 | 控制器温度越限故障 | Controller temperature limit fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Gnd | 接地故障 | 接地故障 | Ground Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverVoltage | 过压故障 | 过压故障 | Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderVoltage | 欠压故障 | 欠压故障 | Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ShortCircuit | 短路瞬时故障 | 短路瞬时故障 | Short Circuit Instantaneous Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaseLoss | 断相故障 | 断相故障 | Phase Failure Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverFreq | 过频故障 | 过频故障 | Over Frequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ShoCirShoDelay | 短路短延时故障 | 短路短延时故障 | Short Circuit Delay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OveCurLonDelay | 过载长延时故障 | 过载长延时故障 | Overload Long Delay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaseNLoss | 断零故障 | 断零故障 | Open Circuit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RevPower | 逆功率故障 | 逆功率故障 | Reverse Power Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaSeq | 相序故障 | 相序故障 | Phase Sequence Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TermTemp | 接线端子温度越限故障 | 接线端子温度越限故障 | Terminal Temperature Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_IUnB | 电流不平衡故障 |  | Current Imbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UUnB | 电压不平衡故障 |  | Voltage Unbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| IUnB | 电流不平衡度 |  | Current Imbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| PFt | 总功率因数 |  | Total Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| UUnB | 电压不平衡度 |  | Voltage Unbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SeqU0 | 电压零序分量 | 电压零序分量 | Voltage Zero Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU2 | 电压负序分量 | 电压负序分量 | Voltage Negative Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU1 | 电压正序分量 | 电压正序分量 | Voltage Positive Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| HarmonicRmsIc | C相电流谐波有效值 | C相电流谐波有效值 | Phase C Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIc | C相电流基波值 | C相电流基波值 | Phase C Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIb | B相电流谐波有效值 | B相电流谐波有效值 | Phase B Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIb | B相电流基波值 | B相电流基波值 | Phase B Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIa | A相电流谐波有效值 | A相电流谐波有效值 | Phase A Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIa | A相电流基波值 | A相电流基波值 | Phase A Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ESE_C | C相反向视在电能 | C相反向视在电能 | Phase C Negative Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_C | C相正向视在电能 | C相正向视在电能 | Phase C Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESE_B | B相反向视在电能 | B相反向视在电能 | Phase B Negative Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_B | B相正向视在电能 | B相正向视在电能 | Phase B Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESE_A | A相反向视在电能 | A相反向视在电能 | Phase A Reverse Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_A | A相正向视在电能 | A相正向视在电能 | Phase A Forward Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESE | 反向视在电能 | 反向视在电能 | Reverse Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI | 正向视在电能 | 正向视在电能 | Forward apparent energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| Q4EQ | 第四象限无功总电能 | 第四象限无功总电能 | Fourth Quadrant Reactive Power Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ | 第二象限无功总电能 | 第二象限无功总电能 | Second Quadrant Reactive Power Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ | 第三象限无功总电能 | 第三象限无功总电能 | Total Reactive Energy in Quadrant III | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ | 第一象限无功总电能 | 第一象限无功总电能 | Total Reactive Energy in Quadrant I | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEP | 组合有功电能 | 组合有功电能 | Combined Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPt | 总有功电能 | 总有功电能 | Total Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Ig | 接地电流 | 接地电流 | Earth Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| In | 中性线电流 | 中性线电流 | Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FreqC | C相频率 | C相频率 | Phase C Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Freq | 电网频率 | 电网频率 | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Uca | CA线电压 | CA线电压 | Line Voltage CA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 | BC线电压 | Line Voltage BC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uab | AB线电压 | AB线电压 | Line Voltage AB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| DeviceTime | 设备时间 | 设备时间 | Device Time | DATETIME |  | RW |  |  |
| Lock | 锁定 |  | Locked | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Unlock | 解锁 |  | Unlock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Close | 合闸 |  | Closing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Open | 分闸 |  | Trip | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Inf_FeeOpen | 费控分闸 | 费控分闸 | Billing Control Trip | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_FeeClose | 费控合闸 | 费控合闸 | Metering Control Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_BtnOpen | 按键分闸 | 按键分闸 | Button Open | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_BtnClose | 按键合闸 | 按键合闸 | Button Closing | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_RemoteOpen | 远程分闸 | 远程分闸 | Remote Open | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_RemoteClose | 远程合闸 | 远程合闸 | Remote Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_Manualopen | 手动分闸 | 手动分闸 | Manual Open | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ManualClose | 手动合闸 | 手动合闸 | Manual Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ReClose | 重合闸 | 重合闸 | Reclosure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_UpdateSuc | 升级成功 | 升级成功 | Upgrade Successful | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ParaChange | 参数变更 | 参数变更 | Parameter Change | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host issued a reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Executed successfully"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PosChangeCount | 闸位变化事件记录总数 | 闸位变化事件记录总数 | Total number of gate position change event records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| ResiSelfTestCount | 剩余电流自检事件记录总数 | 剩余电流自检事件记录总数 | Total Number of Residual Current Self-test Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| AlarmEventCount | 告警事件记录总数 | 告警事件记录总数 | Total Number of Alarm Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| ProtEventCount | 保护事件记录总数 | 保护事件记录总数 | Total Number of Protection Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| TotalOpeTime | 累计运行时间 | 累计运行时间 | Cumulative Operating Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| LeakOpenCount | 漏电分闸次数 | 漏电分闸次数 | Earth Leakage Trip Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| OpenCount | 分闸次数 | 分闸次数 | Trip Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| RHCtrl | 控制器内温度 | 控制器内温度 | Controller Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempCtrl | 控制器内湿度 | 控制器内湿度 | Controller Internal Humidity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| Temp | 断路器内温度 | 断路器内温度 | Circuit Breaker Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutN | 中性线出线温度 | 中性线出线温度 | Neutral Line Outlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInN | 中性线进线温度 | 中性线进线温度 | Neutral Line Inlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| SeqI0 | 电流零序分量 | 电流零序分量 | Current Zero Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI2 | 电流负序分量 | 电流负序分量 | Current Negative Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI1 | 电流正序分量 | 电流正序分量 | Current Positive Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_SeqNum | 保护事件记录序号 |  | Protection Event Record Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Err_Count | 保护事件记录总条数 |  | Total Number of Protection Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Err_Time | 保护事件时间 |  | Protection Event Time | DATETIME |  | R |  |  |
| Err_Phase | 保护事件相位 |  | Protection Event Phase | BITMAP |  | R |  |  |
| Ala_SeqNum | 告警事件记录序号 |  | Alarm Event Record Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ala_Count | 告警事件记录总条数 |  | Total Number of Alarm Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ala_Time | 告警事件时间 |  | Alarm Event Time | DATETIME |  | R |  |  |
| Ala_Phase | 告警事件相位 |  | Alarm Event Phase | BITMAP |  | R |  |  |
| Ala_Ic | 告警事件前C相电流 |  | Current Phase C Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_In | 告警事件前中性线电流 |  | Neutral Line Current Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| AlarmIndicator | 告警标志 |  | Alarm Flag | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"恢复"<br>			},<br>			"itemValue":"恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"发生"<br>			},<br>			"itemValue":"发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderFreq | 欠频故障 | 欠频故障 | Under Frequency Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸后恢复",<br>				"en_US":"Recovery after closing"<br>			},<br>			"itemValue":"合闸后恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"保护跳闸",<br>				"en_US":"Protection trip"<br>			},<br>			"itemValue":"保护跳闸",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Qt | 总无功功率 |  | Total Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Pt | 总有功功率 |  | Total Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pc | C相有功功率 |  | Phase C Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sc | C相视在功率 |  | Phase C Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qc | C相无功功率 | C相无功功率 | Phase C Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| PFc | C相功率因数 |  | Phase C Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pb | B相有功功率 |  | Phase B Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sb | B相视在功率 |  | Phase B Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qb | B相无功功率 |  | Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| PFb | B相功率因数 |  | Phase B Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pa | A相有功功率 |  | Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sa | A相视在功率 |  | Phase A Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qa | A相无功功率 |  | Phase A Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| PFa | A相功率因数 |  | Phase A Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| St | 总视在功率 |  | Total Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| THDIc | C相电流总谐波畸变率 | C相电流总谐波畸变率 | Phase C Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIb | B相电流总谐波畸变率 | B相电流总谐波畸变率 | Phase B Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIa | A相电流总谐波畸变率 | A相电流总谐波畸变率 | Phase A Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUc | C相电压总谐波畸变率 | C相电压总谐波畸变率 | Phase C Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUb | B相电压总谐波畸变率 | B相电压总谐波畸变率 | Phase B Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUa | A相电压总谐波畸变率 | A相电压总谐波畸变率 | Phase A Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| EPE_C | C相反向有功电能 | C相反向有功电能 | Phase C Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_C | C相正向有功电能 | C相正向有功电能 | Phase C Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_B | B相反向有功电能 | B相反向有功电能 | Phase B Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_B | B相正向有功电能 | B相正向有功电能 | Phase B Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_A | A相反向有功电能 | A相反向有功电能 | Phase A Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_A | A相正向有功电能 | A相正向有功电能 | Phase A Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE | 反向有功电能 | 反向有功电能 | Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI | 正向有功电能 | 正向有功电能 | Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Ires | 剩余电流 | 剩余电流 | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| FreqB | B相频率 | B相频率 | Phase B Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| FreqA | A相频率 | A相频率 | Phase A Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Ic | C相电流 | C相电流 | Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uc | C相电压 | C相电压 | Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ib | B相电流 | B相电流 | Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ub | B相电压 | B相电压 | Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ia | A相电流 | A相电流 | Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ua | A相电压 | A相电压 | Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| TempOutC | C相出线温度 | C相出线温度 | Phase C Outlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInC | C相进线温度 | C相进线温度 | Phase C Input Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutB | B相出线温度 | B相出线温度 | Phase B Outlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInB | B相进线温度 | B相进线温度 | Phase B Input Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutA | A相出线温度 | A相出线温度 | Phase A Outlet Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInA | A相进线温度 | A相进线温度 | Phase A Input Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Err_Ua | 保护事件前A相电压 |  | Pre-fault Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ub | 保护事件前B相电压 |  | Pre-fault Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Uc | 保护事件前C相电压 |  | Pre-fault Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ia | 保护事件前A相电流 |  | Pre-fault Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ib | 保护事件前B相电流 |  | Pre-fault Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ic | 保护事件前C相电流 |  | Pre-fault Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_In | 保护事件前中性线电流 |  | Pre-fault Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ires | 保护事件前剩余电流 |  | Residual Current before Protection Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| Ala_Ua | 告警事件前A相电压 |  | Voltage Phase A Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ub | 告警事件前B相电压 |  | Voltage Phase B Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Uc | 告警事件前C相电压 |  | Voltage Phase C Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ia | 告警事件前A相电流 |  | Current Phase A Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_Ib | 告警事件前B相电流 |  | Current Phase B Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_Ires | 告警事件前剩余电流 |  | Residual Current Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorUUnB | 电压不平衡故障 | 电压不平衡故障 | Voltage imbalance fault | FAULT | Err_UUnB,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_UUnB = 1 |  |
| AlarmRevPower | 逆功率告警 | 逆功率告警 | Reverse power alarm | ALARM | Ala_RevPower,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_RevPower = 1 |  |
| AlarmPhaseNLoss | 断零告警 | 断零告警 | Zero-break alarm | ALARM | Ala_PhaseNLoss,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_PhaseNLoss = 1 |  |
| AlarmOveCurLonDel | 过载长延时告警 | 过载长延时告警 | Overload long-time delay alarm | ALARM | Ala_OveCurLonDel,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_OveCurLonDel = 1 |  |
| ErrorAntiIsLand | 防孤岛故障 | 防孤岛故障 | Anti-islanding fault | FAULT | Err_AntiIsLand,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_AntiIsLand = 1 |  |
| ErrorIUnB | 电流不平衡故障 | 电流不平衡故障 | Current imbalance fault | FAULT | Err_IUnB,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_IUnB = 1 |  |
| AlarmUUnB | 电压不平衡告警 | 电压不平衡告警 | Voltage imbalance alarm | ALARM | Ala_UUnB,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_UUnB = 1 |  |
| AlarmIUnB | 电流不平衡告警 | 电流不平衡告警 | Current imbalance alarm | ALARM | Ala_IUnB,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_IUnB = 1 |  |
| ErrorGnd | 接地故障 | 接地故障 | Ground fault | FAULT | Err_Gnd,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_Gnd = 1 |  |
| AlarmPhaseLoss | 断相告警 | 断相告警 | Phase failure alarm | ALARM | Ala_PhaseLoss,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_PhaseLoss = 1 |  |
| AlarmUnderFreq | 欠频告警 | 欠频告警 | Underfrequency Alarm | ALARM | Ala_UnderFreq,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_UnderFreq = 1 |  |
| AlarmUnderVol | 欠压告警 | 欠压告警 | Under-voltage Alarm | ALARM | Ala_UnderVol,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_UnderVol = 1 |  |
| AlarmOverVol | 过压告警 | 过压告警 | Overvoltage Alarm | ALARM | Ala_OverVol,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_OverVol = 1 |  |
| ErrorSelfDiagProt | 自诊断保护故障 | 自诊断保护故障 | Self-diagnostic protection fault | FAULT | Err_SelfDiagProt,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_SelfDiagProt = 1 |  |
| AlarmGnd | 接地故障告警 | 接地故障告警 | Ground Fault Alarm | ALARM | Ala_Gnd,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_Gnd = 1 |  |
| ErrorGraResiI | 缓变剩余电流越限故障 | 缓变剩余电流越限故障 | Slowly changing residual current over-limit fault | FAULT | Err_GraResiI,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_GraResiI = 1 |  |
| ErrorSudResiI | 突变剩余电流越限故障 | 突变剩余电流越限故障 | Mutated Residual Current Overlimit Fault | FAULT | Err_SudResiI,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_SudResiI = 1 |  |
| ErrorTempCtrl | 控制器温度越限故障 | 控制器温度越限故障 | Controller temperature out-of-limit fault | FAULT | Err_TempCtrl,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_TempCtrl = 1 |  |
| ErrorRHCtrl | 控制器湿度越限故障 | 控制器湿度越限故障 | Controller humidity out-of-limit fault | FAULT | Err_RHCtrl,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_RHCtrl = 1 |  |
| ErrorTermTemp | 接线端子温度越限故障 | 接线端子温度越限故障 | Terminal temperature out-of-limit fault | FAULT | Err_TermTemp,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_TermTemp = 1 |  |
| ErrorPhaSeq | 相序故障 | 相序故障 | Phase sequence fault | FAULT | Err_PhaSeq,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_PhaSeq = 1 |  |
| ErrorRevPower | 逆功率故障 | 逆功率故障 | Reverse power fault | FAULT | Err_RevPower,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_RevPower = 1 |  |
| ErrorPhaseNLoss | 断零故障 | 断零故障 | Neutral open fault | FAULT | Err_PhaseNLoss,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_PhaseNLoss = 1 |  |
| ErrorOveCurLonDelay | 过载长延时故障 | 过载长延时故障 | Overload long-time delay fault | FAULT | Err_OveCurLonDelay,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_OveCurLonDelay = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload Alert | ALARM | Ala_OverCurrent,Ala_SeqNum,Ala_Count,Ala_Time,Ala_Phase,Ala_Ua,Ala_Ub,Ala_Uc,Ala_Ia,Ala_Ib,Ala_Ic,Ala_In,Ala_Ires,AlarmIndicator | Ala_OverCurrent = 1 |  |
| AlarmRunOverTime | 运行超时告警 |  | Operation Timeout Alert | ALARM | Ala_RunOverTime,Ala_SeqNum,Ala_Count,Ala_Time,Ala_Phase,Ala_Ua,Ala_Ub,Ala_Uc,Ala_Ia,Ala_Ib,Ala_Ic,Ala_In,Ala_Ires,AlarmIndicator | Ala_RunOverTime = 1 |  |
| AlarmLifeTime | 寿命超时告警 |  | Lifetime Overload Alert | ALARM | Ala_LifeTime,Ala_SeqNum,Ala_Count,Ala_Time,Ala_Phase,Ala_Ua,Ala_Ub,Ala_Uc,Ala_Ia,Ala_Ib,Ala_Ic,Ala_In,Ala_Ires,AlarmIndicator | Ala_LifeTime = 1 |  |
| ErrorOverFreq | 过频故障 | 过频故障 | Overfrequency fault | FAULT | Err_OverFreq,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_OverFreq = 1 |  |
| InfoUpdateSuc | 升级成功 |  | Upgrade successful | INFO | Inf_UpdateSuc | Inf_UpdateSuc = 1 |  |
| InfoReClose | 重合闸 |  | Reclosure | INFO | Inf_ReClose | Inf_ReClose = 1 |  |
| InfoManualClose | 手动合闸 |  | Manual Closure | INFO | Inf_ManualClose | Inf_ManualClose = 1 |  |
| InfoManualopen | 手动分闸 |  | Manual trip | INFO | Inf_Manualopen | Inf_Manualopen = 1 |  |
| InfoRemoteClose | 远程合闸 |  | Remote Closure | INFO | Inf_RemoteClose | Inf_RemoteClose = 1 |  |
| InfoRemoteOpen | 远程分闸 |  | Remote Trip | INFO | Inf_RemoteOpen | Inf_RemoteOpen = 1 |  |
| InfoBtnClose | 按键合闸 |  | Button Closure | INFO | Inf_BtnClose | Inf_BtnClose = 1 |  |
| InfoBtnOpen | 按键分闸 |  | Button trip | INFO | Inf_BtnOpen | Inf_BtnOpen = 1 |  |
| InfoFeeClose | 费控合闸 |  | Tariff Control Closure | INFO | Inf_FeeClose | Inf_FeeClose = 1 |  |
| InfoFeeOpen | 费控分闸 |  | Tariff Control Trip | INFO | Inf_FeeOpen | Inf_FeeOpen = 1 |  |
| AlarmGraResiI | 缓变剩余电流告警 | 缓变剩余电流告警 | Slowly Changing Residual Current Alarm | ALARM | Ala_GraResiI,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_GraResiI = 1 |  |
| ErrorShortCircuit | 短路瞬时故障 | 短路瞬时故障 | Short-circuit instantaneous fault | FAULT | Err_ShortCircuit,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_ShortCircuit = 1 |  |
| ErrorUnderFreq | 欠频故障 | 欠频故障 | Underfrequency fault | FAULT | Err_UnderFreq,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_UnderFreq = 1 |  |
| InfoParaChange | 参数变更 |  | Parameter change | INFO | Inf_ParaChange | Inf_ParaChange = 1 |  |
| ErrorPhaseLoss | 断相故障 | 断相故障 | Phase loss fault | FAULT | Err_PhaseLoss,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_PhaseLoss = 1 |  |
| ErrorUnderVoltage | 欠压故障 | 欠压故障 | Under-voltage fault | FAULT | Err_UnderVoltage,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_UnderVoltage = 1 |  |
| ErrorOverVoltage | 过压故障 | 过压故障 | Overvoltage fault | FAULT | Err_OverVoltage,Err_Ires,Err_In,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Phase,Err_Time | Err_OverVoltage = 1 |  |
| AlarmAntiIsLand | 防孤岛告警 | 防孤岛告警 | Anti-islanding Alarm | ALARM | Ala_AntiIsLand,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_AntiIsLand = 1 |  |
| AlarmSelfDiag | 自诊断保护告警 | 自诊断保护告警 | Self-diagnostic protection alarm | ALARM | Ala_SelfDiag,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_SelfDiag = 1 |  |
| AlarmOverFreq | 过频告警 | 过频告警 | Overfrequency Alarm | ALARM | Ala_OverFreq,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_OverFreq = 1 |  |
| ErrorShoCirShoDelay | 短路短延时故障 | 短路短延时故障 | Short-circuit short-delay fault | FAULT | Err_ShoCirShoDelay,Err_Ia,Err_Ib,Err_Ic,Err_In,Err_Ires,Err_Phase,Err_Time,Err_Ua,Err_Ub,Err_Uc | Err_ShoCirShoDelay = 1 |  |
| AlarmSudResiI | 突变剩余电流告警 | 突变剩余电流告警 | Mutated Residual Current Alarm | ALARM | Ala_SudResiI,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_SudResiI = 1 |  |
| AlarmTempCtrl | 控制器温度告警 | 控制器温度告警 | Controller temperature alarm | ALARM | Ala_TempCtrl,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_TempCtrl = 1 |  |
| AlarmRHCtrl | 控制器湿度告警 | 控制器湿度告警 | Controller humidity alarm | ALARM | Ala_RHCtrl,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_RHCtrl = 1 |  |
| AlarmTermTemp | 接线端子温度告警 | 接线端子温度告警 | Terminal temperature alarm | ALARM | Ala_TermTemp,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_TermTemp = 1 |  |
| AlarmPhaSeq | 相序告警 | 相序告警 | Phase sequence alarm | ALARM | Ala_PhaSeq,Ala_Ires,Ala_In,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Phase,Ala_Time,AlarmIndicator | Ala_PhaSeq = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| CloseCmd | 合闸 |  | Close Circuit | Unlock,Close | Sta_Device |  |
| LeakageCheckCmd | 漏电自检 |  | Leakage Self-Test | LeakageCheck |  |  |
| LockCmd | 锁定 |  | Lock | Lockout |  |  |
| LockoutCmd | 锁死 |  | Locked | Lockout |  |  |
| OpenCmd | 分闸 |  | Trip | Unlock,Open | Sta_Device |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
| RemoteReStartCmd | 远程程序重启 |  | Remote Program Restart | RemoteReStart |  |  |
| UnlockCmd | 解锁 |  | Unlock | Unlock |  |  |
