# public_StringInverter_3P

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_StringInverter_3P | 组串逆变器-三相 |  | String Inverter - Three Phase | NORMAL | electricityStorage |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| MPPTNumber | MPPT路数 |  | MPPT Channels | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |
| RatedU | 额定电压 |  | Rated Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedFreq | 额定频率 |  | Rated Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| RatedP | 额定有功功率 |  | rated voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Err_PV1Arc | 第1路PV拉弧保护 |  | Arc Protection for Channel 1 PV | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV2Arc | 第2路PV拉弧保护 |  | 2nd PV arc protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV3Arc | 第3路PV拉弧保护 |  | Arc Protection for 3rd PV Channel | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV4Arc | 第4路PV拉弧保护 |  | 4th PV Arcing Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV5Arc | 第5路PV拉弧保护 |  | 5th PV Arcing Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV6Arc | 第6路PV拉弧保护 |  | 6th PV Arcing Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV7Arc | 第7路PV拉弧保护 |  | 7th PV arc protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV8Arc | 第8路PV拉弧保护 |  | 8th Channel PV Arcing Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV9Arc | 第9路PV拉弧保护 |  | Arc Protection for 9th PV Channel | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV10Arc | 第10路PV拉弧保护 |  | 10th PV arc protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV11Arc | 第11路PV拉弧保护 |  | 11th PV Arcing Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PV12Arc | 第12路PV拉弧保护 |  | Arc Protection for 12th PV Channel | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBoostCur | Boost电路过流故障 |  | Boost Circuit Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BusShortCir | 母线短路故障 |  | Bus Short Circuit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_WholeBusFall | 整母线跌路故障 |  | Entire Busbar Drop Path Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SwitchOn | 开机 |  | Power On | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SwitchOff | 关机 |  | Shutdown | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| FactoryReset | 恢复出厂设置 |  | Restore Factory Settings | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ForceReboot | 强制重启 |  | Forced restart | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| MPPTScan | MPPT扫描 |  | MPPT Scan | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ARCCheck | ARC检测 |  | ARC Detection | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ARCClearError | ARC故障清除 |  | ARC Fault Clear | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ARCCheckEn | ARC检测使能 |  | ARC Detection Enabled | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| PVInPt | PV输入总功率 |  | Total Input Power PV | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"自检"<br>			},<br>			"itemValue":"自检",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"运行"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"降额"<br>			},<br>			"itemValue":"降额",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"5"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Grid | 电网状态 |  | Grid Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"电网异常",<br>				"en_US":"Grid anomaly"<br>			},<br>			"itemValue":"电网异常",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"电网正常",<br>				"en_US":"Grid normal"<br>			},<br>			"itemValue":"电网正常",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_SelfCheck | 自检 |  | Self-Test | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"自检",<br>				"en_US":"Self-test"<br>			},<br>			"itemValue":"自检",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有自检",<br>				"en_US":"No self-test"<br>			},<br>			"itemValue":"没有自检",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Standby | 待机 |  | Standby | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机",<br>				"en_US":"Standby"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有待机",<br>				"en_US":"No standby"<br>			},<br>			"itemValue":"没有待机",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Run | 运行 |  | Running | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"运行",<br>				"en_US":"Operation"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有运行",<br>				"en_US":"Not running"<br>			},<br>			"itemValue":"没有运行",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_SVGRun | SVG运行模式 |  | SVG Operating Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"SVG运行模式",<br>				"en_US":"SVG operation mode"<br>			},<br>			"itemValue":"SVG运行模式",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"退出SVG运行模式",<br>				"en_US":"Exit SVG running mode"<br>			},<br>			"itemValue":"退出SVG运行模式",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_PVPSelfCheck | PV开机功率自检中 |  | PV Powering On, Self-Checking | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"PV开机功率自检中",<br>				"en_US":"PV startup power self-test"<br>			},<br>			"itemValue":"PV开机功率自检中",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有PV开机功率自检中",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"没有PV开机功率自检中",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_PVUnderVoltage | PV电压低不能开机 |  | Low PV Voltage, Cannot Power On | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"PV电压低不能开机",<br>				"en_US":"Low PV voltage, unable to start"<br>			},<br>			"itemValue":"PV电压低不能开机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有PV电压低不能开机",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"没有PV电压低不能开机",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PV1Temp | PV1温度 |  | PV1 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PV2Temp | PV2温度 |  | PV2 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PV3Temp | PV3温度 |  | PV3 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PV4Temp | PV4温度 |  | PV4 temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| DCIA | A相直流分量 |  | A Phase DC Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| DCIB | B相直流分量 |  | B Phase DC Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| DCIC | C相直流分量 |  | Phase C DC Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| GFCI | 漏电流侦测值 |  | Leakage Current Detection Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mA |  |
| UBusPst | 正母线电压 |  | Positive Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| UBusNgt | 负母线电压 |  | Negative Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| UBusPstNgt | 正负母线电压 |  | DC Bus Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| CntDwPwrOn | 开机倒计时 |  | Startup Countdown | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | s |  |
| GridUa | 电网A相电压 |  | Grid A Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUb | 电网B相电压 |  | Grid Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUc | 电网C相电压 |  | Grid C Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUab | 电网AB线电压 |  | Grid AB Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUbc | 电网BC线电压 |  | Grid BC Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridUca | 电网CA线电压 |  | Grid CA Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GridFreqa | 电网A相频率 |  | Grid A Phase Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| GridFreqb | 电网B相频率 |  | Grid B Phase Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| GridFreqc | 电网C相频率 |  | Grid C Phase Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| GridFreq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| GridTHDUa | 电网A相电压总谐波畸变率 |  | Grid A Phase Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridTHDUb | 电网B相电压总谐波畸变率 |  | Grid B Phase Voltage Total Harmonic Distortion Rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridTHDUc | 电网C相电压总谐波畸变率 |  | Grid C Phase Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridTHDIa | 电网A相电流总谐波畸变率 |  | Grid Phase A Current Total Harmonic Distortion Rate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridTHDIb | 电网B相电流总谐波畸变率 |  | Grid Phase B Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridTHDIc | 电网C相电流总谐波畸变率 |  | C Phase Current Total Harmonic Distortion Rate of Grid | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridUUnB | 电压不平衡度 |  | Voltage Unbalance Degree | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| GridPhaSeq | 电网相序 |  | Grid Phase Sequence | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正序"<br>			},<br>			"itemValue":"正序",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"负序"<br>			},<br>			"itemValue":"负序",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| GridNPEVoltage | 电网N线与接地线之间的电压 |  | Voltage Between Grid N Line and Ground Line | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Sta_GridNGnd | 电网N线接地状态 |  | Neutral Line Earth Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"未检测"<br>			},<br>			"itemValue":"未检测",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"N线接地"<br>			},<br>			"itemValue":"N线接地",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"N线不接地"<br>			},<br>			"itemValue":"N线不接地",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"检测无效"<br>			},<br>			"itemValue":"检测无效",<br>			"itemKey":"3"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| InvertOutUa | 逆变输出A相电压 |  | Inverter Output A Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| InvertOutIa | 逆变输出A相电流 |  | Inverter Output A Phase Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| InvertOutPa | 逆变输出A相有功功率 |  | Inverter Output A Phase Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutQa | 逆变输出A相无功功率 |  | Inverter Output A Phase Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutFreqa | 逆变输出A相频率 |  | Inverter Output Phase A Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| InvertOutUb | 逆变输出B相电压 |  | Inverter Output B Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| InvertOutIb | 逆变输出B相电流 |  | Inverter Output B Phase Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| InvertOutPb | 逆变输出B相有功功率 |  | Inverter Output B Phase Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutQb | 逆变输出B相无功功率 |  | Inverter Output Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutFreqb | 逆变输出B相频率 |  | Inverter Output B Phase Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| InvertOutUc | 逆变输出C相电压 |  | Inverter Output Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| InvertOutIc | 逆变输出C相电流 |  | Inverter Output Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| InvertOutPc | 逆变输出C相有功功率 |  | Inverter Output C Phase Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutQc | 逆变输出C相无功功率 |  | Inverter Output C Phase Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutFreqc | 逆变输出C相频率 |  | Inverter Output Phase C Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| InvertOutPFa | 逆变输出A相功率因数 |  | Inverter Output Phase A Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| InvertOutPFb | 逆变输出B相功率因数 |  | Inverter Output B Phase Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| InvertOutPFc | 逆变输出C相功率因数 |  | Inverter Output C Phase Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| InvertOutPFt | 逆变输出总功率因数 |  | Inverter Output Total Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| InvertOutPt | 逆变输出总有功功率 |  | Total Active Power Output of Inverter | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutQt | 逆变输出总无功功率 |  | Inverter Output Total Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutSt | 逆变输出总视在功率 |  | Inverter Output Total Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| DayInvertOutPPeak | 当日逆变输出最大功率 |  | Maximum Inverter Output Today | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| DayPVE | 当日PV发电量 |  | Daily PV Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalPVE | 累计PV发电量 |  | Cumulative PV Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| InvertEffi | 逆变效率 |  | Inverter Efficiency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| MPPT1U | MPPT1电压 |  | MPPT1 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT2U | MPPT2电压 |  | MPPT2 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT3U | MPPT3电压 |  | MPPT3 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT4U | MPPT4电压 |  | MPPT4 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT5U | MPPT5电压 |  | MPPT5 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT6U | MPPT6电压 |  | MPPT6 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT7U | MPPT7电压 |  | MPPT7 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT8U | MPPT8电压 |  | MPPT8 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MPPT1I | MPPT1电流 |  | MPPT1 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT2I | MPPT2电流 |  | MPPT2 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT3I | MPPT3电流 |  | MPPT3 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT4I | MPPT4电流 |  | MPPT4 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT5I | MPPT5电流 |  | MPPT5 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT6I | MPPT6电流 |  | MPPT6 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT7I | MPPT7电流 |  | MPPT7 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MPPT8I | MPPT8电流 |  | MPPT8 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| PV1InU | PV1输入电压 |  | PV1 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PV1InI | PV1输入电流 |  | PV1 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| PV2InU | PV2输入电压 |  | PV2 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PV2InI | PV2输入电流 |  | PV2 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| PV3InU | PV3输入电压 |  | PV3 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PV3InI | PV3输入电流 |  | PV3 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| PV4InU | PV4输入电压 |  | PV4 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PV4InI | PV4输入电流 |  | PV4 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ISO | 绝缘阻抗侦测值 |  | Insulation impedance detection value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Err_PassiveIsland | 被动孤岛故障 |  | Passive Islanding Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridPhaseU | 电网相电压故障 |  | Grid Phase Voltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridLineU | 电网线电压故障 |  | Grid Line Voltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_InvertRun | 并网发电 |  | Grid-connected power generation | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"并网发电",<br>				"en_US":"Grid connection"<br>			},<br>			"itemValue":"并网发电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有并网发电",<br>				"en_US":"No grid connection"<br>			},<br>			"itemValue":"没有并网发电",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Error | 故障 |  | Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"故障",<br>				"en_US":"Failure"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有故障",<br>				"en_US":"No failure"<br>			},<br>			"itemValue":"没有故障",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| InTemp | 机内温度 |  | Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| CaseTemp | 机箱温度 |  | Chassis Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| HeatSinkTemp | 散热器温度 |  | Radiator Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| RelayTemp | 继电器温度 |  | Relay temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| CommInductorTemp | 共模电感温度 |  | Common Mode Inductor Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| InvertATemp | A相逆变模块温度 |  | A-phase inverter module temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| InvertBTemp | B相逆变模块温度 |  | B Phase Inverter Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| InvertCTemp | C相逆变模块温度 |  | C Phase Inverter Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Sta_PVOverVoltage | PV电压高不能开机 |  | High PV Voltage, Cannot Power On | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"PV电压高不能开机",<br>				"en_US":"High PV voltage, unable to turn on"<br>			},<br>			"itemValue":"PV电压高不能开机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有PV电压高不能开机",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"没有PV电压高不能开机",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_UnderTemp | 温度低不能开机 |  | Low Temperature, Cannot Power On | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"温度低不能开机",<br>				"en_US":"Cannot turn on due to low temperature"<br>			},<br>			"itemValue":"温度低不能开机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有温度低不能开机",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"没有温度低不能开机",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_UnderRatedP | 降额运行 |  | Derated Operation | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"降额运行",<br>				"en_US":"Reduced Capacity Operation"<br>			},<br>			"itemValue":"降额运行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"没有降额运行",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"没有降额运行",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Time | 近一次故障事件时间 |  | Last Fault Event Time | DATETIME |  | R |  |  |
| Ala_OutputSPD | 输出SPD故障 |  | Output SPD Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_TempSensor | 温度传感器告警 |  | Temperature Sensor Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_InputSPD | 输入SPD故障 |  | Input SPD Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Eeprom | EEPROM读写故障 |  | EEPROM Read/Write Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_InComm | 内部通讯失败告警 |  | Internal Communication Failure Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_InFan | 内部风扇告警 |  | Internal Fan Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OutFan | 外部风扇告警 |  | External Fan Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PIDCtrlComm | PID与控制板通讯异常告警 |  | PID Communication Abnormal Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_CTComm | CT板通讯异常告警 |  | CT Board Communication Abnormal Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SVGVoltStab | SVG电压稳定性告警 |  | SVG Voltage Stability Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PIDVoltStab | PID电压稳定性告警 |  | PID Voltage Stability Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvOutIOffset | 逆变电流偏置异常故障 |  | Inverter Current Bias Abnormal Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverTemp | 温度越限故障 |  | Temperature limit fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Relay | 并网继电器故障 |  | Grid relay fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridPhaseLoss | 电网断相故障 |  | Grid phase failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridUnderFreq | 电网欠频故障 |  | Grid underfrequency fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridOverFreq | 电网过频故障 |  | Grid overfrequency fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InvOutOverI | 逆变输出过流故障 |  | Inverter output overcurrent fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Island | 孤岛故障 |  | Island fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBusUDiff | 母线电压差过高故障 |  | Bus voltage difference过高 fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridInvUDiff | 电网和逆变器电压差过压故障 |  | Overvoltage fault between grid and inverter voltage | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBusU | 母线过压故障 |  | Bus overvoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCISensor | 漏电流传感器故障 |  | Leakage Current Sensor Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridUUnB | 电网电压不平衡故障 |  | Grid Voltage Imbalance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_MCU | MCU故障 |  | MCU Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCSInducOverI | 直流小电感过流故障 |  | DC Small Inductance Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCIDynamic | 动态漏电流过流故障 |  | Dynamic Leakage Current Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Isolation | 绝缘阻抗过低故障 |  | Insulation Impedance Too Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCIHigh | 逆变电流直流分量越限故障 |  | Inverter Current DC Component Out-of-Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DCIOffset | 逆变电流直流分量偏置保护 |  | Inverter Current DC Component Bias Protection | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OperaOverU | 操作过电压故障 |  | Operating Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Resonance | 谐振故障 |  | Resonance Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OpenLoopSelfChk | 逆变开环自检异常故障 |  | Inverter Open Loop Self-Test Abnormal Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PVLink | PV连接异常故障 |  | PV Connection Abnormal Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_MPPTOverU | MPPT过压故障 |  | MPPT Overvoltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_MPPTReverse | MPPT反接故障 |  | MPPT Reverse Connection Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PVInvPDiff | PV和逆变器功率差越限故障 |  | PV and Inverter Power Difference Exceeds Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_InSelfDiagn | 内部自我诊断故障 |  | Internal Self-Diagnostic Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GridTHDU | 电网电压谐波过高故障 |  | Grid Voltage Harmonic Excessive Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ARCSelfCheck | ARC板自检故障 |  | ARC Board Self-Test Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ARCBoard | ARC板故障 |  | ARC Board Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_CANComm | CAN通讯故障 |  | CAN Communication Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_12VPowerSource | 12V电源故障 |  | 12V Power Supply Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_VNPE | VNPE相地过压故障 |  | VNPE phase-to-ground overvoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PVVoltSample | PV电压采样故障 |  | PV Voltage Sampling Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_PVCrashVolt | PV起机电压异常故障 |  | Abnormal PV Starting Voltage Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_GFCIStatic | 静态漏电流过流故障 |  | Static Leakage Current Overcurrent Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmCTComm | CT板通讯异常告警 |  | CT Board Communication Anomaly Alert | ALARM | Ala_CTComm | Ala_CTComm = 1 |  |
| ErrorGridOverFreq | 电网过频故障 |  | Grid Overfrequency Fault | FAULT | Err_GridOverFreq | Err_GridOverFreq = 1 |  |
| AlarmTempSensor | 温度传感器告警 |  | Temperature Sensor Alarm | ALARM | Ala_TempSensor | Ala_TempSensor = 1 |  |
| AlarmInputSPD | 输入SPD故障 |  | Input SPD fault | ALARM | Ala_InputSPD | Ala_InputSPD = 1 |  |
| AlarmEeprom | EEPROM读写故障 |  | EEPROM read/write fault | ALARM | Ala_Eeprom | Ala_Eeprom = 1 |  |
| AlarmInComm | 内部通讯失败告警 |  | Internal communication failure alarm | ALARM | Ala_InComm | Ala_InComm = 1 |  |
| AlarmInFan | 内部风扇告警 |  | Internal Fan Alarm | ALARM | Ala_InFan | Ala_InFan = 1 |  |
| ErrorGridUnderFreq | 电网欠频故障 |  | Grid underfrequency fault | FAULT | Err_GridUnderFreq | Err_GridUnderFreq = 1 |  |
| AlarmPIDCtrlComm | PID与控制板通讯异常告警 |  | PID and Control Board Communication Anomaly Alert | ALARM | Ala_PIDCtrlComm | Ala_PIDCtrlComm = 1 |  |
| AlarmOutFan | 外部风扇告警 |  | External Fan Alert | ALARM | Ala_OutFan | Ala_OutFan = 1 |  |
| AlarmSVGVoltStab | SVG电压稳定性告警 |  | SVG Voltage Stability Alert | ALARM | Ala_SVGVoltStab | Ala_SVGVoltStab = 1 |  |
| AlarmPIDVoltStab | PID电压稳定性告警 |  | PID Voltage Stability Alert | ALARM | Ala_PIDVoltStab | Ala_PIDVoltStab = 1 |  |
| ErrorInvOutIOffset | 逆变电流偏置异常故障 |  | Inverter Current Bias Abnormal Fault | FAULT | Err_InvOutIOffset | Err_InvOutIOffset = 1 |  |
| ErrorOverTemp | 温度越限故障 |  | Temperature Limit Exceeded Fault | FAULT | Err_OverTemp | Err_OverTemp = 1 |  |
| ErrorRelay | 并网继电器故障 |  | Grid Relay Fault | FAULT | Err_Relay | Err_Relay = 1 |  |
| ErrorGridPhaseLoss | 电网断相故障 |  | Phase Loss Fault of Grid | FAULT | Err_GridPhaseLoss | Err_GridPhaseLoss = 1 |  |
| ErrorWholeBusFall | 整母线跌路故障 |  | Entire bus drop fault | FAULT | Err_WholeBusFall | Err_WholeBusFall = 1 |  |
| ErrorOverBoostCur | Boost电路过流故障 |  | Boost Circuit Overcurrent Fault | FAULT | Err_OverBoostCur | Err_OverBoostCur = 1 |  |
| ErrorBusShortCir | 母线短路故障 |  | Bus short circuit fault | FAULT | Err_BusShortCir | Err_BusShortCir = 1 |  |
| ErrorResonance | 谐振故障 |  | Resonance fault | FAULT | Err_Resonance | Err_Resonance = 1 |  |
| ErrorInvOutOverI | 逆变输出过流故障 |  | Inverter output overcurrent fault | FAULT | Err_InvOutOverI | Err_InvOutOverI = 1 |  |
| ErrorIsland | 孤岛故障 |  | Island fault | FAULT | Err_Island | Err_Island = 1 |  |
| ErrorOverBusUDiff | 母线电压差过高故障 |  | Bus voltage difference too high fault | FAULT | Err_OverBusUDiff | Err_OverBusUDiff = 1 |  |
| ErrorGridInvUDiff | 电网和逆变器电压差过压故障 |  | Grid and inverter voltage difference overvoltage fault | FAULT | Err_GridInvUDiff | Err_GridInvUDiff = 1 |  |
| ErrorOverBusU | 母线过压故障 |  | Bus overvoltage fault | FAULT | Err_OverBusU | Err_OverBusU = 1 |  |
| ErrorGFCISensor | 漏电流传感器故障 |  | Leakage current sensor fault | FAULT | Err_GFCISensor | Err_GFCISensor = 1 |  |
| ErrorGridUUnB | 电网电压不平衡故障 |  | Grid voltage unbalance fault | FAULT | Err_GridUUnB | Err_GridUUnB = 1 |  |
| ErrorMCU | MCU故障 |  | MCU fault | FAULT | Err_MCU | Err_MCU = 1 |  |
| ErrorDCSInducOverI | 直流小电感过流故障 |  | DC inductor overcurrent fault | FAULT | Err_DCSInducOverI | Err_DCSInducOverI = 1 |  |
| ErrorGFCIDynamic | 动态漏电流过流故障 |  | Dynamic leakage current overcurrent fault | FAULT | Err_GFCIDynamic | Err_GFCIDynamic = 1 |  |
| ErrorIsolation | 绝缘阻抗过低故障 |  | Insulation impedance too low fault | FAULT | Err_Isolation | Err_Isolation = 1 |  |
| ErrorDCIHigh | 逆变电流直流分量越限故障 |  | Inverter current DC component overlimit fault | FAULT | Err_DCIHigh | Err_DCIHigh = 1 |  |
| ErrorDCIOffset | 逆变电流直流分量偏置保护 |  | Inverter current DC component bias protection | FAULT | Err_DCIOffset | Err_DCIOffset = 1 |  |
| ErrorPVCrashVolt | PV起机电压异常故障 |  | PV Starting Voltage Anomaly Fault | FAULT | Err_PVCrashVolt | Err_PVCrashVolt = 1 |  |
| ErrorPVVoltSample | PV电压采样故障 |  | PV Voltage Sampling Fault | FAULT | Err_PVVoltSample | Err_PVVoltSample = 1 |  |
| ErrorVNPE | VNPE相地过压故障 |  | VNPE Phase-to-Ground Overvoltage Fault | FAULT | Err_VNPE | Err_VNPE = 1 |  |
| Error12VPowerSource | 12V电源故障 |  | 12V Power Supply Fault | FAULT | Err_12VPowerSource | Err_12VPowerSource = 1 |  |
| ErrorCANComm | CAN通讯故障 |  | CAN Communication Fault | FAULT | Err_CANComm | Err_CANComm = 1 |  |
| ErrorARCBoard | ARC板故障 |  | ARC Board Fault | FAULT | Err_ARCBoard | Err_ARCBoard = 1 |  |
| ErrorARCSelfCheck | ARC板自检故障 |  | ARC Board Self-Check Fault | FAULT | Err_ARCSelfCheck | Err_ARCSelfCheck = 1 |  |
| ErrorGridTHDU | 电网电压谐波过高故障 |  | Grid Voltage Harmonic Excessive Fault | FAULT | Err_GridTHDU | Err_GridTHDU = 1 |  |
| ErrorInSelfDiagn | 内部自我诊断故障 |  | Internal Self-Diagnostic Fault | FAULT | Err_InSelfDiagn | Err_InSelfDiagn = 1 |  |
| ErrorPassiveIsland | 被动孤岛故障 |  | Passive Islanding Fault | FAULT | Err_PassiveIsland | Err_PassiveIsland = 1 |  |
| ErrorMPPTReverse | MPPT反接故障 |  | MPPT Reverse Polarity Fault | FAULT | Err_MPPTReverse | Err_MPPTReverse = 1 |  |
| ErrorMPPTOverU | MPPT过压故障 |  | MPPT Overvoltage Fault | FAULT | Err_MPPTOverU | Err_MPPTOverU = 1 |  |
| ErrorPVLink | PV连接异常故障 |  | PV connection abnormality fault | FAULT | Err_PVLink | Err_PVLink = 1 |  |
| ErrorOperaOverU | 操作过电压故障 |  | Operational overvoltage fault | FAULT | Err_OperaOverU | Err_OperaOverU = 1 |  |
| ErrorGridOverLineU | 电网线电压过压故障 |  | Overvoltage Fault of Grid Line Voltage | FAULT | Err_GridLineU | Err_GridLineU = 1 |  |
| ErrorGridOverPhaseU | 电网相电压过压故障 |  | Grid phase voltage overvoltage fault | FAULT | Err_GridPhaseU | Err_GridPhaseU = 1 |  |
| ErrorPVInvPDiff | PV和逆变器功率差越限故障 |  | PV and Inverter Power Difference Exceeds Limit Fault | FAULT | Err_PVInvPDiff | Err_PVInvPDiff = 1 |  |
| AlarmOutputSPD | 输出SPD故障 |  | Output SPD fault | ALARM | Ala_OutputSPD | Ala_OutputSPD = 1 |  |
| ErrorOpenLoopSelfChk | 逆变开环自检异常故障 |  | Inverter Open-loop Self-test Abnormal Fault | FAULT | Err_OpenLoopSelfChk | Err_OpenLoopSelfChk = 1 |  |
| ErrorGFCIStatic | 静态漏电流过流故障 |  | Overcurrent Fault of Static Leakage Current | FAULT | Err_GFCIStatic | Err_GFCIStatic = 1 |  |
| ErrorPV1Arc | 第1路PV拉弧保护 |  | Arc Protection of the 1st PV Path | FAULT | Err_PV1Arc | Err_PV1Arc = 1 |  |
| ErrorPV2Arc | 第2路PV拉弧保护 |  | Arc Protection of the 2nd PV Path | FAULT | Err_PV2Arc | Err_PV2Arc = 1 |  |
| ErrorPV3Arc | 第3路PV拉弧保护 |  | Arc Protection of the 3rd PV Path | FAULT | Err_PV3Arc | Err_PV3Arc = 1 |  |
| ErrorPV4Arc | 第4路PV拉弧保护 |  | Arc Protection of the 4th PV Path | FAULT | Err_PV4Arc | Err_PV4Arc = 1 |  |
| ErrorPV5Arc | 第5路PV拉弧保护 |  | Arc Protection of the 5th PV Path | FAULT | Err_PV5Arc | Err_PV5Arc = 1 |  |
| ErrorPV6Arc | 第6路PV拉弧保护 |  | Arcing Protection Failure on Line 6 | FAULT | Err_PV6Arc | Err_PV6Arc = 1 |  |
| ErrorPV7Arc | 第7路PV拉弧保护 |  | Arcing Protection Failure on Line 7 | FAULT | Err_PV7Arc | Err_PV7Arc = 1 |  |
| ErrorPV8Arc | 第8路PV拉弧保护 |  | Arcing Protection Failure on Line 8 | FAULT | Err_PV8Arc | Err_PV8Arc = 1 |  |
| ErrorPV9Arc | 第9路PV拉弧保护 |  | Arcing Protection Failure on Line 9 | FAULT | Err_PV9Arc | Err_PV9Arc = 1 |  |
| ErrorPV10Arc | 第10路PV拉弧保护 |  | Arcing Protection Failure on Line 10 | FAULT | Err_PV10Arc | Err_PV10Arc = 1 |  |
| ErrorPV11Arc | 第11路PV拉弧保护 |  | Arcing Protection Failure on Line 11 | FAULT | Err_PV11Arc | Err_PV11Arc = 1 |  |
| ErrorPV12Arc | 第12路PV拉弧保护 |  | Arcing Protection Failure on Line 12 | FAULT | Err_PV12Arc | Err_PV12Arc = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| ARCCheckCmd | ARC检测 |  | ARC Detection | MPPTScan |  |  |
| ARCCheckEnCmd | ARC检测使能 |  | ARC Detection Enable | ARCCheckEn |  |  |
| ARCClearErrorCmd | ARC故障清除 |  | ARC Fault Clear | ARCClearError |  |  |
| FactoryResetCmd | 恢复出厂设置 |  | Factory Reset | FactoryReset |  |  |
| ForceRebootCmd | 强制重启 |  | Force Reboot | ForceReboot |  |  |
| MPPTScanCmd | MPPT扫描 |  | MPPT Scan | MPPTScan |  |  |
| SwitchOffCmd | 关机 |  | Shutdown | SwitchOff |  |  |
| SwitchOnCmd | 开机 |  | Power On | SwitchOn |  |  |
