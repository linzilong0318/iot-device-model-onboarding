# public_ACB_3P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ACB_3P_V1_0_2 | (交流)框架断路器 | (交流)框架断路器 | AC ACB | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| FrameCurrent | 壳架电流 |  | FrameCurrent | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedVoltage | 额定电压 |  | Rated Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedCurrent | 额定电流 |  | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedFrequency | 工作频率 |  | RatedFrequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Install Location | STRING |  |  | False |  |
| MechanicalLife | 机械寿命 |  | MechanicalLife | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |
| ElectricalLife | 电气寿命 |  | ElectricalLife | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |
| Manufacturer | 生产厂家 | 生产厂家 | Manufacturer | STRING |  |  | False |  |
| DeviceType | 设备类型 | 设备类型 | Device Type | STRING |  |  | False |  |
| DeviceModel | 设备型号 | 设备型号 | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WorkingSts | 状态字 |  |  | BITMAP |  | R |  |  |
| Temp | 断路器内温度 |  | Circuit Breaker Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutNCopBus | 中性线出线铜排温度 |  | Neutral Line Outlet Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInNCopBus | 中性线进线铜排温度 |  | Neutral Line Inlet Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutCCopBus | 出线Ｃ相铜排温度 |  | Outgoing C-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInCCopBus | 进线Ｃ相铜排温度 |  | Incoming C-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutBCopBus | 出线Ｂ相铜排温度 |  | Outgoing B-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInBCopBus | 进线Ｂ相铜排温度 |  | Incoming B-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutACopBus | 出线Ａ相铜排温度 |  | Outgoing A-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempInACopBus | 进线Ａ相铜排温度 |  | Incoming A-Phase Busbar Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| SeqI0 | 电流零序分量 |  | Zero Sequence Component of Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI2 | 电流负序分量 |  | Negative Sequence Component of Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI1 | 电流正序分量 |  | Positive Sequence Component of Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| IUnB | 电流不平衡度 |  | Current Unbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SeqU0 | 电压零序分量 |  | Zero Sequence Component of Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU2 | 电压负序分量 |  | Negative Sequence Component of Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU1 | 电压正序分量 |  | Positive Sequence Component of Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| UUnB | 电压不平衡度 |  | Voltage Unbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| HarmonicRmsIc | C相电流谐波有效值 |  | Phase C Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIc | C相电流基波值 |  | Phase C Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIb | B相电流谐波有效值 |  | Phase B Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIb | B相电流基波值 |  | Phase B Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIa | A相电流谐波有效值 |  | Phase A Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIa | A相电流基波值 |  | Phase A Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ESE_C | C相反向视在电能 |  | Phase C Negative Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_C | C相正向视在电能 |  | Phase C Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| Q4EQ_C | C相第四象限无功总电能 |  | Phase C Quadrant 4 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_C | C相第三象限无功总电能 |  | Phase C Quadrant 3 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_C | C相第二象限无功总电能 |  | Phase C Quadrant 2 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ_C | C相第一象限无功总电能 |  | Phase C Quadrant 1 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_C | C相组合无功电能 |  | Phase C Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ESE_B | B相反向视在电能 |  | Phase B Negative Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_B | B相正向视在电能 |  | Phase B Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| Q4EQ_B | B相第四象限无功总电能 |  | Phase B Quadrant 4 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_B | B相第三象限无功总电能 |  | Phase B Quadrant 3 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_B | B相第二象限无功总电能 |  | Phase B Quadrant 2 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ_B | B相第一象限无功总电能 |  | Phase B Quadrant 1 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_B | B相组合无功电能 |  | Phase B Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ESE_A | A相反向视在电能 |  | Phase A Negative Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI_A | A相正向视在电能 |  | Phase A Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| Q4EQ_A | A相第四象限无功总电能 |  | Phase A Quadrant 4 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ_A | A相第三象限无功总电能 |  | Phase A Quadrant 3 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ_A | A相第二象限无功总电能 |  | Phase A Quadrant 2 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ_A | A相第一象限无功总电能 |  | Phase A Quadrant 1 Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEQ_A | A相组合无功电能 |  | Phase A Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ESE | 反向视在电能 |  | Reverse Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ESI | 正向视在电能 |  | Positive Apparent Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVAh |  |
| ComEQ | 组合无功电能 |  | Combined Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQE | 反向无功电能 |  | Reverse Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI | 正向无功电能 |  | Positive Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQ | 第四象限无功总电能 |  | Fourth Quadrant Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ | 第三象限无功总电能 |  | Third Quadrant Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ | 第二象限无功总电能 |  | Second Quadrant Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQ | 第一象限无功总电能 |  | Total Reactive Energy in Quadrant I | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| ComEP | 组合有功电能 |  | Combined Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPt | 总有功电能 |  | Total Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQt | 总无功电能 |  | Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Ig | 接地电流 |  | Earth Leakage Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| In | 中性线电流 |  | Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FreqC | C相频率 |  | Phase C Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| FreqB | B相频率 |  | Phase B Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| FreqA | A相频率 |  | Phase A Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| St | 总视在功率 |  | Total Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qt | 总无功功率 |  | Total Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Pt | 总有功功率 |  | Total Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| PFt | 总功率因数 |  | Total Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Uca | CA线电压 |  | Line Voltage CA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 |  | Line Voltage BC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uab | AB线电压 |  | Line Voltage AB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Unlock | 解锁 |  | Unlock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Inf_FeeOpen | 费控分闸 |  | Charge Control Trip | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sent operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_FeeClose | 费控合闸 |  | Charge Control Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sent operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_BtnOpen | 按键分闸 |  | Manual Trip | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sent operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_BtnClose | 按键合闸 |  | Button Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_RemoteOpen | 远程分闸 |  | Remote Trip | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_RemoteClose | 远程合闸 |  | Remote Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ManualClose | 手动合闸 |  | Manual Closure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ReClose | 重合闸 |  | Reclosure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_UpdateSuc | 升级成功 |  | Upgrade Successful | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Inf_ParaChange | 参数变更 |  | Parameter Change | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sends operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TempCopBus | 铜排温度越限告警 |  | Busbar Temperature Overlimit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_HarmonicVolt | 电压谐波告警 |  | Voltage Harmonic Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_HarmonicCur | 电流谐波告警 |  | Current Harmonic Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_LifeTime | 寿命超时告警 |  | Lifetime Exceeded Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RunOverTime | 运行超时告警 |  | Operation Exceeded Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 |  | Overload Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SelfDiag | 自诊断保护告警 |  | Self-diagnostic Protection Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_AntiIsLand | 防孤岛告警 |  | Anti-islanding Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_GraResiI | 缓变剩余电流越限告警 |  | Gradual Change Residual Current Overlimit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SudResiI | 突变剩余电流越限告警 |  | Sudden Change Residual Current Overlimit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TempCtrl | 控制器温度越限告警 |  | Controller Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RHCtrl | 控制器湿度越限告警 |  | Controller Humidity Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TermTemp | 接线端子温度越限告警 |  | Terminal Block Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaSeq | 相序告警 |  | Phase Sequence Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Gnd | 接地告警 |  | Grounding Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevPower | 逆功率告警 |  | Reverse Power Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseNLoss | 断零告警 |  | Zero Sequence Break Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_IUnB | 电流不平衡告警 |  | Current Imbalance Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UUnB | 电压不平衡告警 |  | Voltage Imbalance Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OveCurLonDel | 过载长延时告警 |  | Overload Long Delay Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderFreq | 欠频告警 |  | Underfrequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverFreq | 过频告警 |  | Overfrequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseLoss | 断相告警 |  | Phase failure alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderVol | 欠压告警 |  | Undervoltage alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVol | 过压告警 |  | Overvoltage alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Time | 保护事件时间 |  | Protection event time | DATETIME |  | R |  |  |
| Err_Phase | 保护事件相位 |  | Protection event phase | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"A相"<br>			},<br>			"itemValue":"A相",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"B相"<br>			},<br>			"itemValue":"B相",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"C相"<br>			},<br>			"itemValue":"C相",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"中性线"<br>			},<br>			"itemValue":"中性线",<br>			"itemKey":"3"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Time | 告警事件发生/恢复时间 |  | Alarm Event Occurrence/Recovery Time | DATETIME |  | R |  |  |
| AlarmIndicator | 告警标志 |  | Alarm Flag | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"恢复"<br>			},<br>			"itemValue":"恢复",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"发生"<br>			},<br>			"itemValue":"发生",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Phase | 告警事件相位 |  | Phase of alarm event | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"A相"<br>			},<br>			"itemValue":"A相",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"B相"<br>			},<br>			"itemValue":"B相",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"C相"<br>			},<br>			"itemValue":"C相",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"中性线"<br>			},<br>			"itemValue":"中性线",<br>			"itemKey":"3"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_CurDirec | 告警事件前三相电流方向 |  | Direction of three-phase current before alarm event | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正向"<br>			},<br>			"itemValue":"正向",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"反向"<br>			},<br>			"itemValue":"反向",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OveCurLonDelay | 过载长延时故障 |  | Overload Long Delay Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ShoCirShoDelay | 短路短延时故障 |  | Short Circuit Delayed Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ShortCircuit | 短路瞬时故障 |  | Short Circuit Instantaneous Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverFreq | 过频故障 |  | Frequent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderVoltage | 欠压故障 |  | Undervoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaseLoss | 断相故障 |  | Phase Loss Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderFreq | 欠频故障 |  | Underspeed Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TempCopBus | 铜排温度越限故障 |  | Copper Busbar Overtemperature Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_SelfDiagProt | 自诊断保护故障 |  | Self-diagnostic Protection Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_HarmonicVolt | 电压谐波故障 |  | Voltage Harmonic Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UUnB | 电压不平衡故障 |  | Voltage Unbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaseNLoss | 断零故障 |  | Neutral Disconnection Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_IUnB | 电流不平衡故障 |  | Current Unbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RevPower | 逆功率故障 |  | Reverse Power Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_RHCtrl | 控制器湿度越限故障 |  | Controller Humidity Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TermTemp | 接线端子温度越限故障 |  | Terminal Temperature Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GraResiI | 缓变剩余电流越限故障 |  | Slow Change Residual Current Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TempCtrl | 控制器温度越限故障 |  | Controller Temperature Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_SudResiI | 突变剩余电流越限故障 |  | Sudden Change Residual Current Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_AntiIsLand | 防孤岛故障 |  | Anti-Islanding Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_HarmonicCur | 电流谐波故障 |  | Current Harmonic Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverVoltage | 过压故障 |  | Overvoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close Circuit"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PhaSeq | 相序故障 |  | Phase Sequence Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Gnd | 接地故障 |  | Earth Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PosChangeCount | 闸位变化事件记录总数 |  | Total Number of Gate Position Change Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| ResiSelfTestCount | 剩余电流自检事件记录总数 |  | Total Number of Leakage Current Self-Test Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| AlarmEventCount | 告警事件记录总数 |  | Total Number of Alarm Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| ProtEventCount | 保护事件记录总数 |  | Total Number of Protection Event Records | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| TotalOpeTime | 累计运行时间 |  | Total Running Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| LeakOpenCount | 漏电分闸次数 |  | Number of Leakage Trip Times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| OpenCount | 分闸次数 |  | Disconnection Times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| ContactHealIndex | 健康度 |  | Health Status | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| ContactWear | 触头磨损度 |  | Contact Wear Degree | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| ContactElecLife | 触头电气寿命 |  | Contact Electrical Life | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| AtmosPressure | 当前气压 |  | Current Air Pressure | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | atm |  |
| TempCtrl | 控制器内温度 |  | Controller Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| RHCtrl | 控制器内湿度 |  | Controller Internal Humidity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| THDIc | C相电流总谐波畸变率 |  | Phase C Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIb | B相电流总谐波畸变率 |  | Phase B Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIa | A相电流总谐波畸变率 |  | Phase A Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUc | C相电压总谐波畸变率 |  | Phase C Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUb | B相电压总谐波畸变率 |  | Phase B Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUa | A相电压总谐波畸变率 |  | Phase A Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| EPE_C | C相反向有功电能 |  | Phase C Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_C | C相正向有功电能 |  | Phase C Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_B | B相反向有功电能 |  | Phase B Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_B | B相正向有功电能 |  | Phase B Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_A | A相反向有功电能 |  | Phase A Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_A | A相正向有功电能 |  | Phase A Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE | 反向有功电能 |  | Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI | 正向有功电能 |  | Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Ires | 剩余电流 |  | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| Pc | C相有功功率 |  | Phase C Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sc | C相视在功率 |  | Phase C Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qc | C相无功功率 |  | Phase C Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| PFc | C相功率因数 |  | Phase C Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ic | C相电流 |  | Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uc | C相电压 |  | Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Pb | B相有功功率 |  | Phase B Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sa | A相视在功率 |  | Phase A Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sb | B相视在功率 |  | Phase B Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qa | A相无功功率 |  | Phase A Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qb | B相无功功率 |  | Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| PFb | B相功率因数 |  | Phase B Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ib | B相电流 |  | Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ub | B相电压 |  | Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Pa | A相有功功率 |  | Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| PFa | A相功率因数 |  | Phase A Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ia | A相电流 |  | Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ua | A相电压 |  | Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Inf_Manualopen | 手动分闸 |  | Manual trip | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"动作成功执行",<br>				"en_US":"Action successfully executed"<br>			},<br>			"itemValue":"动作成功执行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"主机发操作复位",<br>				"en_US":"Host sent operation reset"<br>			},<br>			"itemValue":"主机发操作复位",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| ClearContWear | 触头磨损清除 |  | Contact Wear Clearing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| ClearError | 故障清除 |  | Fault Clearing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| ClearEnergyData | 电能清除 |  | Energy Clearing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| ClearRecord | 记录清除 |  | Record Clearing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Open | 分闸 |  | Opening | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Close | 合闸 |  | Closing | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lockout | 锁死 |  | Lockout | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Lock | 锁定 |  | Lock | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Err_Ua | 保护事件前A相电压 |  | Pre-protection event phase A voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ub | 保护事件前B相电压 |  | Pre-protection event phase B voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Uc | 保护事件前C相电压 |  | Pre-protection event phase C voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ia | 保护事件前A相电流 |  | Pre-protection Event Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ib | 保护事件前B相电流 |  | Pre-protection Event Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_Ic | 保护事件前C相电流 |  | Pre-protection Event Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Err_CurDirec | 保护事件前三相电流方向 |  | Pre-protection Event Three-Phase Current Direction | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正向"<br>			},<br>			"itemValue":"正向",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"反向"<br>			},<br>			"itemValue":"反向",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Uab | 保护事件前AB线电压 |  | Pre-protection Event AB Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Ubc | 保护事件前BC线电压 |  | Pre-protection Event BC Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Err_Uca | 保护事件前CA线电压 |  | Pre-protection Event CA Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ua | 告警事件前A相电压 |  | Phase A Voltage Before Alarm Event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ub | 告警事件前B相电压 |  | Voltage on phase B before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Uc | 告警事件前C相电压 |  | Voltage on phase C before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ia | 告警事件前A相电流 |  | Current on phase A before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_Ib | 告警事件前B相电流 |  | Current on phase B before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_Ic | 告警事件前C相电流 |  | Current on phase C before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ala_Uab | 告警事件前AB线电压 |  | Voltage between AB lines before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Ubc | 告警事件前BC线电压 |  | Voltage between BC lines before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ala_Uca | 告警事件前CA线电压 |  | Voltage on CA line before alarm event | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorIUnB | 电流不平衡故障 |  | Current Unbalance Fault | FAULT | Err_IUnB,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_IUnB = 1 |  |
| ErrorTempCopBus | 铜排温度越限故障 |  | Busbar Temperature Limit Exceeded Fault | FAULT | Err_TempCopBus,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_TempCopBus = 1 |  |
| ErrorSelfDiagProt | 自诊断保护故障 |  | Self-diagnostic Protection Fault | FAULT | Err_SelfDiagProt,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_SelfDiagProt = 1 |  |
| ErrorAntiIsLand | 防孤岛故障 |  | Anti-islanding Fault | FAULT | Err_AntiIsLand,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_AntiIsLand = 1 |  |
| ErrorGraResiI | 缓变剩余电流越限故障 |  | Gradual Change Residual Current Limit Exceeded Fault | FAULT | Err_GraResiI,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_GraResiI = 1 |  |
| ErrorSudResiI | 突变剩余电流越限故障 |  | Sudden Change Residual Current Limit Exceeded Fault | FAULT | Err_SudResiI,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_SudResiI = 1 |  |
| AlarmLifeTime | 寿命超时告警 |  | Lifetime Exceeded Alert | ALARM | Ala_LifeTime,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_LifeTime = 1 |  |
| AlarmHarmonicVolt | 电压谐波告警 |  | Voltage Harmonic Alert | ALARM | Ala_HarmonicVolt,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_HarmonicVolt = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload Alert | ALARM | Ala_OverCurrent,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_OverCurrent = 1 |  |
| AlarmSelfDiag | 自诊断保护告警 |  | Self-Diagnosis Protection Alarm | ALARM | Ala_SelfDiag,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_SelfDiag = 1 |  |
| AlarmRunOverTime | 运行超时告警 |  | Operation Time-out Alarm | ALARM | Ala_RunOverTime,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_RunOverTime = 1 |  |
| AlarmGraResiI | 缓变剩余电流越限告警 |  | Slow Change Residual Current Limit Alarm | ALARM | Ala_GraResiI,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_GraResiI = 1 |  |
| InfoFeeOpen | 费控分闸 |  |  | INFO | Inf_FeeOpen | Inf_FeeOpen = 1 |  |
| AlarmUnderFreq | 欠频告警 |  | Undervoltage Alarm | ALARM | Ala_UnderFreq,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_UnderFreq = 1 |  |
| AlarmOverFreq | 过频告警 |  | Overfrequency Alarm | ALARM | Ala_OverFreq,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_OverFreq = 1 |  |
| AlarmPhaseLoss | 断相告警 |  | Phase Loss Alarm | ALARM | Ala_PhaseLoss,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_PhaseLoss = 1 |  |
| AlarmGnd | 接地告警 |  | Ground Fault Alarm | ALARM | Ala_Gnd,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_Gnd = 1 |  |
| AlarmUnderVol | 欠压告警 |  | Undervoltage Alarm | ALARM | Ala_UnderVol,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_UnderVol = 1 |  |
| LowVolt | 线电压欠压告警 |  |  | ALARM | Uab,Ubc,Uca | Uab < 360,Ubc < 360,Uca < 360 |  |
| AlarmOveCurLonDel | 过载长延时告警 |  | Overload Long Delay Alarm | ALARM | Ala_OveCurLonDel,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_OveCurLonDel = 1 |  |
| AlarmUUnB | 电压不平衡告警 |  | Voltage Unbalance Alarm | ALARM | Ala_UUnB,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_UUnB = 1 |  |
| AlarmIUnB | 电流不平衡告警 |  | Current Unbalance Alarm | ALARM | Ala_IUnB,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_IUnB = 1 |  |
| AlarmRevPower | 逆功率告警 |  | Reverse Power Alarm | ALARM | Ala_RevPower,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_RevPower = 1 |  |
| AlarmTempCopBus | 铜排温度越限告警 |  | Copper Bar Temperature Limit Alarm | ALARM | Ala_TempCopBus,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_TempCopBus = 1 |  |
| AlarmSudResiI | 突变剩余电流越限告警 |  | Sudden Change Residual Current Limit Alarm | ALARM | Ala_SudResiI,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_SudResiI = 1 |  |
| ErrorHarmonicVolt | 电压谐波故障 |  | Voltage Harmonic Fault | FAULT | Err_HarmonicVolt,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_HarmonicVolt = 1 |  |
| AlarmPhaSeq | 相序告警 |  | Phase Sequence Alarm | ALARM | Ala_PhaSeq,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_PhaSeq = 1 |  |
| AlarmOverVol | 过压告警 |  |  | ALARM | Ala_OverVol,Ala_Time,Ala_Phase,Ala_Ua,Ala_Ub,Ala_Uc,Ala_Ia,Ala_Ib,Ala_Ic,Ala_CurDirec,Ala_Uab,Ala_Ubc,Ala_Uca | Ala_OverVol = 1 |  |
| InfoBtnOpen | 按键分闸 |  |  | INFO | Inf_BtnOpen | Inf_BtnOpen = 1 |  |
| InfoFeeClose | 费控合闸 |  |  | INFO | Inf_FeeClose | Inf_FeeClose = 1 |  |
| ErrorRHCtrl | 控制器湿度越限故障 |  | Controller Humidity Limit Exceeded Fault | FAULT | Err_RHCtrl,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_RHCtrl = 1 |  |
| AlarmPhaseNLoss | 断零告警 |  | Break Zero Alarm | ALARM | Ala_PhaseNLoss,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_PhaseNLoss = 1 |  |
| AlarmTempCtrl | 控制器温度越限告警 |  | Controller Temperature Limit Exceeded Alert | ALARM | Ala_TempCtrl,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_TempCtrl = 1 |  |
| AlarmRHCtrl | 控制器湿度越限告警 |  | Controller Humidity Limit Exceeded Alert | ALARM | Ala_RHCtrl,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_RHCtrl = 1 |  |
| ErrorOverVoltage | 过压故障 |  | Overvoltage fault | FAULT | Err_OverVoltage,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_OverVoltage = 1 |  |
| InfoUpdateSuc | 升级成功 |  |  | INFO | Inf_UpdateSuc | Inf_UpdateSuc = 1 |  |
| InfoReClose | 重合闸 |  |  | INFO | Inf_ReClose | Inf_ReClose = 1 |  |
| InfoManualClose | 手动合闸 |  |  | INFO | Inf_ManualClose | Inf_ManualClose = 1 |  |
| InfoManualopen | 手动分闸 |  |  | INFO | Inf_Manualopen | Inf_Manualopen = 1 |  |
| InfoRemoteClose | 远程合闸 |  |  | INFO | Inf_RemoteClose | Inf_RemoteClose = 1 |  |
| InfoRemoteOpen | 远程分闸 |  |  | INFO | Inf_RemoteOpen | Inf_RemoteOpen = 1 |  |
| InfoBtnClose | 按键合闸 |  |  | INFO | Inf_BtnClose | Inf_BtnClose = 1 |  |
| ErrorPhaseNLoss | 断零故障 |  | Zero Dropout Fault | FAULT | Err_PhaseNLoss,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_PhaseNLoss = 1 |  |
| ErrorPhaSeq | 相序故障 |  | Phase sequence fault | FAULT | Err_PhaSeq,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_PhaSeq = 1 |  |
| ErrorRevPower | 逆功率故障 |  | Reverse power fault | FAULT | Err_RevPower,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_RevPower = 1 |  |
| ErrorPhaseLoss | 断相故障 |  | Phase loss fault | FAULT | Err_PhaseLoss,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_PhaseLoss = 1 |  |
| ErrorOveCurLonDelay | 过载长延时故障 |  | Overload long-time delay fault | FAULT | Err_OveCurLonDelay,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_OveCurLonDelay = 1 |  |
| ErrorUnderVoltage | 欠压故障 |  | Undervoltage fault | FAULT | Err_UnderVoltage,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_UnderVoltage = 1 |  |
| AlarmHarmonicCur | 电流谐波告警 |  | Current Harmonic Alarm | ALARM | Ala_HarmonicCur,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_HarmonicCur = 1 |  |
| ErrorOverFreq | 过频故障 |  | Overfrequency fault | FAULT | Err_OverFreq,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_OverFreq = 1 |  |
| ErrorShortCircuit | 短路瞬时故障 |  | Short circuit instantaneous fault | FAULT | Err_ShortCircuit,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_ShortCircuit = 1 |  |
| ErrorUnderFreq | 欠频故障 |  | Undervoltage fault | FAULT | Err_UnderFreq,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_UnderFreq = 1 |  |
| ErrorUUnB | 电压不平衡故障 |  | Voltage Imbalance Fault | FAULT | Err_UUnB,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_UUnB = 1 |  |
| ErrorShoCirShoDelay | 短路短延时故障 |  | Short Circuit Short Delay Fault | FAULT | Err_ShoCirShoDelay,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_ShoCirShoDelay = 1 |  |
| ErrorHarmonicCur | 电流谐波故障 |  | Current harmonic fault | FAULT | Err_HarmonicCur,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_HarmonicCur = 1 |  |
| ErrorGnd | 接地故障 |  | Ground Fault | FAULT | Err_Gnd,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_Gnd = 1 |  |
| ErrorTermTemp | 接线端子温度越限故障 |  | Terminal Temperature Limit Exceeded Fault | FAULT | Err_TermTemp,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_TermTemp = 1 |  |
| ErrorTempCtrl | 控制器温度越限故障 |  | Controller Temperature Limit Exceeded Fault | FAULT | Err_TempCtrl,Err_CurDirec,Err_Phase,Err_Uca,Err_Ubc,Err_Uab,Err_Ic,Err_Ib,Err_Ia,Err_Uc,Err_Ub,Err_Ua,Err_Time | Err_TempCtrl = 1 |  |
| InfoParaChange | 参数变更 |  |  | INFO | Inf_ParaChange | Inf_ParaChange = 1 |  |
| AlarmAntiIsLand | 防孤岛告警 |  | Anti-Islanding Alarm | ALARM | Ala_AntiIsLand,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_AntiIsLand = 1 |  |
| AlarmTermTemp | 接线端子温度越限告警 |  | Terminal Temperature Limit Alarm | ALARM | Ala_TermTemp,Ala_CurDirec,Ala_Phase,Ala_Uca,Ala_Ubc,Ala_Uab,Ala_Ic,Ala_Ib,Ala_Ia,Ala_Uc,Ala_Ub,Ala_Ua,Ala_Time,AlarmIndicator | Ala_TermTemp = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| CloseCmd | 合闸 |  | Close the circuit | Unlock,Close | Sta_Device |  |
| LockCmd | 锁定 |  | Lock | Lock |  |  |
| LockoutCmd | 锁死 |  | Locked | Lockout |  |  |
| OpenCmd | 分闸 |  | Trip | Unlock,Open | Sta_Device |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
| UnlockCmd | 解锁 |  | Unlock | Unlock |  |  |
