# public_MixInverter_1P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_MixInverter_1P_V1_0_2 | (单相)混合逆变器 |  | (Single-phase) Hybrid Inverter | NORMAL | electricityStorage |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Equipment Model | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |
| MPPTNumber | MPPT路数 |  | MPPT Channels | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DayGenOpeTime | 当日发电机工作时间 |  | Daily Generator Operation Time | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| GenOutU | 发电机输出电压 |  | Generator Output Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GenOutI | 发电机输出电流 |  | Generator Output Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| GenOutP | 发电机输出功率 |  | Generator Output Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| GenOutFreq | 发电机输出频率 |  | Generator Output Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| DayGenE | 当日发电机发电量 |  | Daily Generator Power Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| MonGenE | 当月发电机发电量 |  | Generator Output for the Month | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| YearGenE | 当年发电机发电量 |  | Annual Generator Power Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalGenE | 累计发电机发电量 |  | Cumulative Generator Power Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Device | 设备状态 |  | Equipment Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"自检"<br>			},<br>			"itemValue":"自检",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"运行"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"初始化"<br>			},<br>			"itemValue":"初始化",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"关机"<br>			},<br>			"itemValue":"关机",<br>			"itemKey":"7"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_SysRunMode | 系统运行模式 |  | System Operating Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"纯PV"<br>			},<br>			"itemValue":"纯PV",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"自发自用"<br>			},<br>			"itemValue":"自发自用",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"全额上网"<br>			},<br>			"itemValue":"全额上网",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"应急备电"<br>			},<br>			"itemValue":"应急备电",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"强制离网"<br>			},<br>			"itemValue":"强制离网",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU纯PV"<br>			},<br>			"itemValue":"TOU纯PV",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU自发自用"<br>			},<br>			"itemValue":"TOU自发自用",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU全额上网"<br>			},<br>			"itemValue":"TOU全额上网",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU应急备电"<br>			},<br>			"itemValue":"TOU应急备电",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"离网模式"<br>			},<br>			"itemValue":"离网模式",<br>			"itemKey":"9"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SwitchOn | 开机 |  | Power On | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| SwitchOff | 关机 |  | Power Off | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| GridCharEn | 电网充电使能 |  | Grid Charge Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| GenCharEn | 发电机充电使能 |  | Generator Charge Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| PurePVOffGridEn | 纯PV离网运行使能 |  | Pure PV Off-Grid Operation Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| BattRecovEn | 电池恢复使能 |  | Battery Recovery Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| BattPToGridEn | 电池功率上网使能 |  | Battery Power Grid Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| AntiRevFlowEn | 防逆流使能 |  | Anti-Reverse Current Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| BattCharEn | 电池充电使能 |  | Battery Charging Enable | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止",<br>				"en_US":"Disable"<br>			},<br>			"itemValue":"禁止",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"使能",<br>				"en_US":"Enable"<br>			},<br>			"itemValue":"使能",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| GridCharStartTime | 电网充电开始时间 |  | Grid Charging Start Time | DATETIME |  | RW |  |  |
| GridCharEndTime | 电网充电结束时间 |  | Grid Charging End Time | DATETIME |  | RW |  |  |
| TotalLoadTime | 负载总用电时长 |  | Total Daily Electricity Usage of Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| DayLoadTime | 负载日用电时长 |  | Daily Electricity Usage of Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| LoadS | 负载视在功率 |  | Apparent Power Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| LoadQ | 负载无功功率 |  | Reactive Power of Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| LoadP | 负载有功功率 |  | Active Power of Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| GridPF | 电网功率因数 |  | Grid Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| GridS | 电网视在功率 |  | Grid Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| GridQ | 电网无功功率 |  | Grid Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutTotalE | 逆变输出总发电量 |  | Inverter Output Total Power Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| InvertOutDayE | 逆变输出日发电量 |  | Inverter Output Daily Power Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| InvertOutPF | 逆变输出功率因数 |  | Inverter Output Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| InvertOutS | 逆变输出视在功率 |  | Inverter Output Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| InvertOutQ | 逆变输出无功功率 |  | Inverter Output Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| InvertOutP | 逆变输出有功功率 |  | Inverter Output Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutI | 逆变输出电流 |  | Inverter Output Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| InvertOutU | 逆变输出电压 |  | Inverter Output Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| DayPVInPtPeak | 当日PV输入总功率峰值 |  | Daily Peak PV Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PVInPt | PV输入总功率 |  | Total PV Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| DCDCModTemp | DCDC模块温度 |  | DCDC Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| GridP | 电网有功功率 |  | Grid Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| InvertOutFreq | 逆变输出频率 |  | Inverter Output Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| SetGridCharPLim | 设置电网充电功率限值 |  | Set the power limit for grid charging | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | kW |  |
| SetMinDischarSOC | 设置最小放电SOC |  | Set Minimum Discharge SOC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SetMaxCharSOC | 设置最大充电SOC |  | Set Maximum Charge SOC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | % |  |
| SysRunMode | 系统工作模式 |  | System Operation Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"自发自用"<br>			},<br>			"itemValue":"自发自用",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"全额上网"<br>			},<br>			"itemValue":"全额上网",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"应急充电"<br>			},<br>			"itemValue":"应急充电",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"强制离网"<br>			},<br>			"itemValue":"强制离网",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU"<br>			},<br>			"itemValue":"TOU",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"纯光伏"<br>			},<br>			"itemValue":"纯光伏",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| RemoSysRunMode | 设置远程系统工作模式 |  | Set Remote System Operation Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU自发自用"<br>			},<br>			"itemValue":"TOU自发自用",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU全额上网"<br>			},<br>			"itemValue":"TOU全额上网",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU应急充电"<br>			},<br>			"itemValue":"TOU应急充电",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TOU纯光伏"<br>			},<br>			"itemValue":"TOU纯光伏",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| GenSwitchOn | 发电机开机 |  | Generator Start | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| GenSwitchOff | 发电机关机 |  | Generator Stop | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| OnOffGridMode | 设置并离网模式 |  | Set Grid-Connected and Off-Grid Mode | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"立即离网"<br>			},<br>			"itemValue":"立即离网",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"穿越离网"<br>			},<br>			"itemValue":"穿越离网",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁止离网"<br>			},<br>			"itemValue":"禁止离网",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SetMaxExGridP | 设置最大上网功率 |  | Set Maximum Grid Export Power | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | kW |  |
| BattModTemp | 电池模块温度 |  | Battery Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PVModTemp | PV模块温度 |  | PV Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| InvModTemp | 逆变模块温度 |  | Inverter Module Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| InTemp | 机内温度 |  | Internal Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| DeviceTime | 设备时间 |  | Device Time | DATETIME |  | RW |  |  |
| Err_UnderPVU | PV电压过低故障 |  | PV Voltage Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverGridU | 电网电压过高故障 |  | Grid Voltage High Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderGridU | 电网电压过低故障 |  | Grid Voltage Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_NoGridPower | 无市电故障 |  | No Utility Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverGridFreq | 电网频率过高故障 |  | Grid Frequency High Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderGridFreq | 电网频率过低故障 |  | Grid Frequency Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverPVU | PV电压过高故障 |  | PV Voltage High Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBusU | 母线电压过高故障 |  | Bus Voltage High Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderBusU | 母线电压过低故障 |  | Bus Voltage Low Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_SoftStart | 软起故障 |  | Soft Start Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderInvertTemp | 逆变器温度越限故障 |  | Inverter Temperature Limit Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BMSComm | BMS通讯故障 |  | BMS Communication Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PV2InU | PV2输入电压 |  | PV2 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| LoadI | 负载电流 |  | Load Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| DayPVE | 当日PV发电量 |  | Daily PV Generation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| GridFreq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| GridI | 电网电流 |  | Grid Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| GridU | 电网电压 |  | Grid Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| DayEPI | 当日正向有功电能 |  | Daily Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| PV1InU | PV1输入电压 |  | PV1 Input Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| PV2InP | PV2输入功率 |  | PV2 Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| PV2InI | PV2输入电流 |  | PV2 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MontEPI | 当月正向有功电能 |  | Monthly Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| PV1InP | PV1输入功率 |  | PV1 Input Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| InvertEffi | 逆变效率 |  | Inverter Efficiency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| TotalPVTime | 累计PV发电时间 |  | Cumulative PV Generation Time | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| DayPVTime | 当日PV发电时间 |  | Daily PV Generation Time | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| TotalPVE | 累计PV发电量 |  | Cumulative PV Generation Output | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalLoadE | 总负载用能 |  | Total Load Energy Consumption | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| PV1InI | PV1输入电流 |  | PV1 Input Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| YearLoadE | 当年用电量 |  | Annual Electricity Consumption | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| MonLoadE | 当月用电量 |  | Monthly Electricity Consumption | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DayLoadE | 当日用电量 |  | Daily electricity consumption | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| LoadU | 负载电压 |  | Load voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| TotalEPE | 总反向有功电能 |  | Total reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| YearEPE | 当年反向有功电能 |  | Annual reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| MontEPE | 当月反向有功电能 |  | Month reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DayEPE | 当日反向有功电能 |  | Daily reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalEPI | 总正向有功电能 |  | Total forward active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| YearEPI | 当年正向有功电能 |  | Annual forward active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ChargeCount | 总充电次数 |  | Total charging times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| DischargeCount | 总放电次数 |  | Total discharging times | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| EnergyRemain | 剩余电量 |  | Remaining Charge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SOC | 荷电状态 |  | State of Charge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SOH | 健康状态 |  | Health Status | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| BatteryTemp | 电池温度 |  | Battery Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| BatteryU | 电池电压 |  | Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| BatteryI | 电池电流 |  | Battery Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| BatteryP | 电池功率 |  | Battery Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| DayCharTime | 日充电时长 |  | Daily Charging Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalCharTime | 总充电时长 |  | Total Charging Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| DayDischarTime | 日放电时长 |  | Daily Discharge Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalDischarTime | 总放电时长 |  | Total Discharge Duration | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| DayCharE | 当日充电量 |  | Daily Charge Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalCharE | 累计充电量 |  | Accumulative Charge Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| DayDischarE | 当日放电量 |  | Daily Discharge Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| TotalDischarE | 累计放电量 |  | Accumulative Discharge Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Battery | 电池状态 |  | Battery Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"运行"<br>			},<br>			"itemValue":"运行",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"3"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_System | 电池系统错误 |  | Battery System Error | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_CharOverCur | 充电过电流故障 |  | Charge Over-current Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_DischarOverCur | 放电过电流故障 |  | Discharge Over-current Fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_UnderBattTemp | 电池温度过低故障 |  | Battery temperature too low fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_OverBattTemp | 电池温度过高故障 |  | Battery temperature too high fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BattModuOverU | 电池模块过压故障 |  | Battery module overvoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BattModuUnderU | 电池模块欠压故障 |  | Battery module undervoltage fault | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_SecBattOffLine | 从电池或者从组通信离线 |  | Communication offline from battery or group | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_CharOverCur | 充电过电流告警 |  | Charging overcurrent alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_DischarOverCur | 放电过电流告警 |  | Discharging overcurrent alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderBattTemp | 电池温度过低告警 |  | Battery temperature too low alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverBattTemp | 电池温度过高告警 |  | Battery temperature too high alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_BattModuOverU | 电池模块过压告警 |  | Battery module overvoltage alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_BattModuUnderU | 电池模块欠压告警 |  | Battery Module Undervoltage Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorSoftStart | 软起故障 |  | Soft Start Fault | FAULT | Err_SoftStart | Err_SoftStart = 1 |  |
| AlarmBattModuUnderU | 电池模块欠压告警 |  | Battery Module Undervoltage Alarm | ALARM | Ala_BattModuUnderU | Ala_BattModuUnderU = 1 |  |
| AlarmBattModuOverU | 电池模块过压告警 |  | Battery Module Overvoltage Alarm | ALARM | Ala_BattModuOverU | Ala_BattModuOverU = 1 |  |
| AlarmOverBattTemp | 电池温度过高告警 |  | Battery Temperature High Alarm | ALARM | Ala_OverBattTemp | Ala_OverBattTemp = 1 |  |
| AlarmUnderBattTemp | 电池温度过低告警 |  | Battery Temperature Low Alarm | ALARM | Ala_UnderBattTemp | Ala_UnderBattTemp = 1 |  |
| AlarmDischarOverCur | 放电过电流告警 |  | Discharge Overcurrent Alarm | ALARM | Ala_DischarOverCur | Ala_DischarOverCur = 1 |  |
| AlarmCharOverCur | 充电过电流告警 |  | Charging Overcurrent Alarm | ALARM | Ala_CharOverCur | Ala_CharOverCur = 1 |  |
| AlarmSecBattOffLine | 从电池或者从组通信离线 |  | Communication Offline from Battery or Group | ALARM | Ala_SecBattOffLine | Ala_SecBattOffLine = 1 |  |
| ErrorBattModuUnderU | 电池模块欠压故障 |  | Battery Module Undervoltage Fault | FAULT | Err_BattModuUnderU | Err_BattModuUnderU = 1 |  |
| ErrorBattModuOverU | 电池模块过压故障 |  | Battery Module Overvoltage Fault | FAULT | Err_BattModuOverU | Err_BattModuOverU = 1 |  |
| ErrorOverBattTemp | 电池温度过高故障 |  | Battery temperature too high fault | FAULT | Err_OverBattTemp | Err_OverBattTemp = 1 |  |
| ErrorUnderBattTemp | 电池温度过低故障 |  | Battery temperature too low fault | FAULT | Err_UnderBattTemp | Err_UnderBattTemp = 1 |  |
| ErrorDischarOverCur | 放电过电流故障 |  | Discharge Overcurrent Fault | FAULT | Err_DischarOverCur | Err_DischarOverCur = 1 |  |
| ErrorSystem | 电池系统错误 |  | Battery system error | FAULT | Err_System | Err_System = 1 |  |
| ErrorOverGridU | 电网电压过高故障 |  | Grid voltage too high fault | FAULT | Err_OverGridU | Err_OverGridU = 1 |  |
| ErrorUnderGridU | 电网电压过低故障 |  | Grid voltage too low fault | FAULT | Err_UnderGridU | Err_UnderGridU = 1 |  |
| ErrorNoGridPower | 无市电故障 |  | No mains power fault | FAULT | Err_NoGridPower | Err_NoGridPower = 1 |  |
| ErrorOverGridFreq | 电网频率过高故障 |  | Grid frequency too high fault | FAULT | Err_OverGridFreq | Err_OverGridFreq = 1 |  |
| ErrorUnderGridFreq | 电网频率过低故障 |  | Grid frequency too low fault | FAULT | Err_UnderGridFreq | Err_UnderGridFreq = 1 |  |
| ErrorBMSComm | BMS通讯故障 |  | BMS Communication Failure | FAULT | Err_BMSComm | Err_BMSComm = 1 |  |
| ErrorOverPVU | PV电压过高故障 |  | PV Voltage High Fault | FAULT | Err_OverPVU | Err_OverPVU = 1 |  |
| ErrorUnderPVU | PV电压过低故障 |  | PV Voltage Low Fault | FAULT | Err_UnderPVU | Err_UnderPVU = 1 |  |
| ErrorOverBusU | 母线电压过高故障 |  | Bus Voltage High Fault | FAULT | Err_OverBusU | Err_OverBusU = 1 |  |
| ErrorUnderBusU | 母线电压过低故障 |  | Bus Voltage Low Fault | FAULT | Err_UnderBusU | Err_UnderBusU = 1 |  |
| ErrorUnderInvertTemp | 逆变器温度越限故障 |  | Inverter temperature limit fault | FAULT | Err_UnderInvertTemp | Err_UnderInvertTemp = 1 |  |
| ErrorCharOverCur | 充电过电流故障 |  | Charging Overcurrent Fault | FAULT | Err_CharOverCur | Err_CharOverCur = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| GridCharPLimSet | 设置电网充电功率限值 |  | Set the power limit for grid charging | SetGridCharPLim |  |  |
| SysRunModeCmd | 设置系统工作模式 |  | Set System Working Mode | SysRunMode |  |  |
| SwitchOnCmd | 开机 |  | Power On | SwitchOn |  |  |
| SwitchOffCmd | 关机 |  | Shutdown | SwitchOff |  |  |
| RemoSysRunModeCmd | 设置远程系统工作模式 |  | Set Remote System Working Mode | RemoSysRunMode |  |  |
| PurePVOffGridEnCmd | 纯PV离网运行使能 |  | Enable Pure PV Off-grid Operation | PurePVOffGridEn |  |  |
| OnOffGridModeCmd | 设置并离网模式 |  | Grid-Offgrid Mode | OnOffGridMode |  |  |
| MaxExGridPSet | 设置最大上网功率 |  | Set Maximum Internet Power | SetMaxExGridP |  |  |
| GridCharStartTimeSet | 电网充电开始时间 |  | Grid Charging Start Time | GridCharStartTime |  |  |
| AntiRevFlowEnCmd | 防逆流使能 |  | Anti-Reverse Current Enable | AntiRevFlowEn |  |  |
| GridCharEndTimeSet | 电网充电结束时间 |  | Grid Charging End Time | GridCharEndTime |  |  |
| GridCharEnCmd | 电网充电使能 |  | Grid Charging Enable | GridCharEn |  |  |
| GenSwitchOnCmd | 发电机开机 |  | Generator Start | GenSwitchOn |  |  |
| GenSwitchOffCmd | 发电机关机 |  | Generator Stop | GenSwitchOff |  |  |
| GenCharEnCmd | 发电机充电使能 |  | Generator Charging Enable | GenCharEn |  |  |
| BattRecovEnCmd | 电池恢复使能 |  | Battery Recovery Enable | BattRecovEn |  |  |
| BattPToGridEnCmd | 电池功率上网使能 |  | Battery Power Grid Enable | BattPToGridEn |  |  |
| BattCharEnCmd | 电池充电使能 |  | Battery Charge Enable | BattCharEn |  |  |
