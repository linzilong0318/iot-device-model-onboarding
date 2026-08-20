# public_ESMU

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ESMU | 电池管理系统电池堆管理单元 |  | Battery Management System Battery Stack Management Unit | NORMAL | electricityStorage |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| BatteryCapacity | 电池容量 |  | Battery Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kWh | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Str9MinUPoINTNo | 簇9最低电压电池对应点号 |  | Cluster 9 Lowest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MaxBattTemp | 簇9最高电池温度 |  | Cluster 9 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str9MaxTempPoINTNo | 簇9最高温度电池对应点号 |  | Cluster 9 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MinBattTemp | 簇9最低电池温度 |  | Cluster 9 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str9MINTempPoINTNo | 簇9最低温度电池对应点号 |  | Cluster 9 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MaxBattSOC | 簇9最高电池SOC |  | Cluster 9 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9MaxSOCPoINTNo | 簇9最高电池SOC对应点号 |  | Cluster 9 Highest Battery SOC Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MinBattSOC | 簇9最低电池SOC |  | Cluster 9 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9MinSOCPoINTNo | 簇9最低电池SOC对应点号 |  | Cluster 9 Lowest Battery SOC Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MaxBattSOH | 簇9最高电池SOH |  | Cluster 9 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9MaxSOHPoINTNo | 簇9最高电池SOH对应点号 |  | Cluster 9 Highest Battery SOH Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MinBattSOH | 簇9最低电池SOH |  | Cluster 9 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9MinSOHPoINTNo | 簇9最低电池SOH对应点号 |  | Cluster 9 Lowest Battery SOH Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9TotalCharE | 簇9累计充电电量 |  | Cluster 9 Cumulative Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str9TotalDischarE | 簇9累计放电电量 |  | Cluster 9 Cumulative Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str9CharESingle | 簇9单次累计充电电量 |  | Cluster 9 Single Charge Accumulated Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str9DischarESingle | 簇9单次累计放电电量 |  | Cluster 9 Single Discharge Accumulated Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str9CharAvaiE | 簇9可充电量 |  | Cluster 9 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str9DischarAvaiE | 簇9可放电量 |  | Cluster 9 Dischargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str10Run | 簇10运行状态 |  | Cluster 10 Operational Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str10MaxCharILim | 簇10允许最大充电电流 |  | Cluster 10 Maximum Allowable Charging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str10MaxDischarILim | 簇10允许最大放电电流 |  | Cluster 10 Maximum Allowable Discharging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str10MaxCharPLim | 簇10允许最大充电功率 |  | Cluster 10 Maximum Allowable Charging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str10MaxDischarPLim | 簇10允许最大放电功率 |  | Cluster 10 Maximum Allowable Discharging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str10MaxCharULim | 簇10允许最大充电电压 |  | Cluster 10 Maximum Allowable Charging Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10MaxDischarULim | 簇10允许最大放电电压 |  | Cluster 10 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10U | 簇10电压 |  | Cluster 10 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10I | 簇10电流 |  | Cluster 10 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str10SOC | 簇10SOC |  | Cluster 10 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10SOH | 簇10SOH |  | Cluster 10 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10ESBCMTemp | 簇10模块温度 |  | Cluster 10 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str10InsulationR | 簇10绝缘电阻 |  | Cluster 10 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str10UAvg | 簇10平均电池电压 |  | Cluster 10 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10TempAvg | 簇10平均电池温度 |  | Cluster 10 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str10MaxBattU | 簇10最高电池电压 |  | Cluster 10 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10MaxUPoINTNo | 簇10最高电压电池对应点号 |  | Cluster 10 highest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MinBattU | 簇10最低电池电压 |  | Cluster 10 lowest battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str10MinUPoINTNo | 簇10最低电压电池对应点号 |  | Cluster 10 lowest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MaxBattTemp | 簇10最高电池温度 |  | Cluster 10 highest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str10MaxTempPoINTNo | 簇10最高温度电池对应点号 |  | Cluster 10 highest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MinBattTemp | 簇10最低电池温度 |  | Cluster 10 lowest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str10MINTempPoINTNo | 簇10最低温度电池对应点号 |  | Cluster 10 lowest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MaxBattSOC | 簇10最高电池SOC |  | Cluster 10 highest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10MaxSOCPoINTNo | 簇10最高电池SOC对应点号 |  | Cluster 10 highest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MinBattSOC | 簇10最低电池SOC |  | Cluster 10 lowest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10MinSOCPoINTNo | 簇10最低电池SOC对应点号 |  | Cluster 10 lowest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MaxBattSOH | 簇10最高电池SOH |  | Cluster 10 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10MaxSOHPoINTNo | 簇10最高电池SOH对应点号 |  | Cluster 10 highest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10MinBattSOH | 簇10最低电池SOH |  | Cluster 10 lowest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str10MinSOHPoINTNo | 簇10最低电池SOH对应点号 |  | Cluster 10 lowest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str10TotalCharE | 簇10累计充电电量 |  | Cluster 10 cumulative charge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str10TotalDischarE | 簇10累计放电电量 |  | Cluster 10 cumulative discharge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str10CharESingle | 簇10单次累计充电电量 |  | Cluster 10 single cumulative charge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str10DischarESingle | 簇10单次累计放电电量 |  | Cluster 10 single cumulative discharge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str10CharAvaiE | 簇10可充电量 |  | Cluster 10 rechargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str10DischarAvaiE | 簇10可放电量 |  | Cluster 10 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str11Run | 簇11运行状态 |  | Cluster 11 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str11MaxCharILim | 簇11允许最大充电电流 |  | Cluster 11 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str11MaxDischarILim | 簇11允许最大放电电流 |  | Cluster 11 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str11MaxCharPLim | 簇11允许最大充电功率 |  | Cluster 11 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str11MaxDischarPLim | 簇11允许最大放电功率 |  | Cluster 11 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str11MaxCharULim | 簇11允许最大充电电压 |  | Cluster 11 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11MaxDischarULim | 簇11允许最大放电电压 |  | Cluster 11 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11U | 簇11电压 |  | Cluster 11 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11I | 簇11电流 |  | Cluster 11 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str11SOC | 簇11SOC |  | Cluster 11 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11SOH | 簇11SOH |  | Cluster 11 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11ESBCMTemp | 簇11模块温度 |  | Cluster 11 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str11InsulationR | 簇11绝缘电阻 |  | Cluster 11 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str11UAvg | 簇11平均电池电压 |  | Cluster 11 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11TempAvg | 簇11平均电池温度 |  | Cluster 11 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str11MaxBattU | 簇11最高电池电压 |  | Cluster 11 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11MaxUPoINTNo | 簇11最高电压电池对应点号 |  | Cluster 11 Highest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MinBattU | 簇11最低电池电压 |  | Cluster 11 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str11MinUPoINTNo | 簇11最低电压电池对应点号 |  | Cluster 11 Lowest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MaxBattTemp | 簇11最高电池温度 |  | Cluster 11 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str15I | 簇15电流 |  | Cluster 15 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str15SOC | 簇15SOC |  | Cluster 15 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15SOH | 簇15SOH |  | Cluster 15 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15ESBCMTemp | 簇15模块温度 |  | Cluster 15 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str15InsulationR | 簇15绝缘电阻 |  | Cluster 15 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str15UAvg | 簇15平均电池电压 |  | Cluster 15 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str15TempAvg | 簇15平均电池温度 |  | Cluster 15 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str15MaxBattU | 簇15最高电池电压 |  | Cluster 15 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str15MaxUPoINTNo | 簇15最高电压电池对应点号 |  | Cluster 15 Maximum Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MinBattU | 簇15最低电池电压 |  | Cluster 15 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str15MinUPoINTNo | 簇15最低电压电池对应点号 |  | Point Number Corresponding to Lowest Voltage Battery in Cluster 15 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MaxBattTemp | 簇15最高电池温度 |  | Cluster 15 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str15MaxTempPoINTNo | 簇15最高温度电池对应点号 |  | Point Number Corresponding to Highest Temperature Battery in Cluster 15 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MinBattTemp | 簇15最低电池温度 |  | Cluster 15 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str15MINTempPoINTNo | 簇15最低温度电池对应点号 |  | Point Number Corresponding to Lowest Temperature Battery in Cluster 15 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MaxBattSOC | 簇15最高电池SOC |  | Cluster 15 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15MaxSOCPoINTNo | 簇15最高电池SOC对应点号 |  | Point Number Corresponding to Highest Battery State of Charge (SOC) in Cluster 15 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MinBattSOC | 簇15最低电池SOC |  | Cluster 15 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15MinSOCPoINTNo | 簇15最低电池SOC对应点号 |  | Point Number Corresponding to Lowest Battery State of Charge (SOC) in Cluster 15 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MaxBattSOH | 簇15最高电池SOH |  | Cluster 15 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15MaxSOHPoINTNo | 簇15最高电池SOH对应点号 |  | Cluster 15 highest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15MinBattSOH | 簇15最低电池SOH |  | Cluster 15 lowest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str15MinSOHPoINTNo | 簇15最低电池SOH对应点号 |  | Cluster 15 lowest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str15TotalCharE | 簇15累计充电电量 |  | Cluster 15 cumulative charge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str15TotalDischarE | 簇15累计放电电量 |  | Cluster 15 cumulative discharge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str15CharESingle | 簇15单次累计充电电量 |  | Cluster 15 single charge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str15DischarESingle | 簇15单次累计放电电量 |  | Cluster 15 single discharge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str15CharAvaiE | 簇15可充电量 |  | Cluster 15 chargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str15DischarAvaiE | 簇15可放电量 |  | Cluster 15 dischargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str16Run | 簇16运行状态 |  | Cluster 16 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str16MaxCharILim | 簇16允许最大充电电流 |  | Cluster 16 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str16MaxDischarILim | 簇16允许最大放电电流 |  | Cluster 16 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str16MaxCharPLim | 簇16允许最大充电功率 |  | Cluster 16 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str16MaxDischarPLim | 簇16允许最大放电功率 |  | Cluster 16 Maximum Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str16MaxCharULim | 簇16允许最大充电电压 |  | Cluster 16 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16MaxDischarULim | 簇16允许最大放电电压 |  | Cluster 16 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16U | 簇16电压 |  | Cluster 16 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16I | 簇16电流 |  | Cluster 16 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str16SOC | 簇16SOC |  | Cluster 16 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16SOH | 簇16SOH |  | Cluster 16 SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16ESBCMTemp | 簇16模块温度 |  | Cluster 16 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str16InsulationR | 簇16绝缘电阻 |  | Cluster 16 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str16UAvg | 簇16平均电池电压 |  | Cluster 16 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16TempAvg | 簇16平均电池温度 |  | Cluster 16 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str16MaxBattU | 簇16最高电池电压 |  | Cluster 16 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16MaxUPoINTNo | 簇16最高电压电池对应点号 |  | Cluster 16 Highest Voltage Battery Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MinBattU | 簇16最低电池电压 |  | Cluster 16 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str16MinUPoINTNo | 簇16最低电压电池对应点号 |  | Cluster 16 Lowest Voltage Battery Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MaxBattTemp | 簇16最高电池温度 |  | Cluster 16 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str16MaxTempPoINTNo | 簇16最高温度电池对应点号 |  | Cluster 16 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MinBattTemp | 簇16最低电池温度 |  | Cluster 16 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str16MINTempPoINTNo | 簇16最低温度电池对应点号 |  | Cluster 16 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MaxBattSOC | 簇16最高电池SOC |  | Cluster 16 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16MaxSOCPoINTNo | 簇16最高电池SOC对应点号 |  | Cluster 16 Highest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MinBattSOC | 簇16最低电池SOC |  | Cluster 16 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16MinSOCPoINTNo | 簇16最低电池SOC对应点号 |  | Cluster 16 Lowest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MaxBattSOH | 簇16最高电池SOH |  | Cluster 16 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16MaxSOHPoINTNo | 簇16最高电池SOH对应点号 |  | Cluster 16 Highest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16MinBattSOH | 簇16最低电池SOH |  | Cluster 16 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str16MinSOHPoINTNo | 簇16最低电池SOH对应点号 |  | Cluster 16 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str16TotalCharE | 簇16累计充电电量 |  | Cluster 16 Total Charge Energy Accumulated | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str16TotalDischarE | 簇16累计放电电量 |  | Cluster 16 Total Discharge Energy Accumulated | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str16CharESingle | 簇16单次累计充电电量 |  | Cluster 16 Single Charge Energy Accumulated | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str16DischarESingle | 簇16单次累计放电电量 |  | Cluster 16 Single Discharge Energy Accumulated | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str16CharAvaiE | 簇16可充电量 |  | Cluster 16 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str16DischarAvaiE | 簇16可放电量 |  | Cluster 16 Dischargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str17Run | 簇17运行状态 |  | Cluster 17 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str17MaxCharILim | 簇17允许最大充电电流 |  | Cluster 17 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str17MaxDischarILim | 簇17允许最大放电电流 |  | Cluster 17 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str17MaxCharPLim | 簇17允许最大充电功率 |  | Cluster 17 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str17MaxDischarPLim | 簇17允许最大放电功率 |  | Cluster 17 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str17MaxCharULim | 簇17允许最大充电电压 |  | Cluster 17 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17MaxDischarULim | 簇17允许最大放电电压 |  | Cluster 17 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17U | 簇17电压 |  | Cluster 17 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17I | 簇17电流 |  | Cluster 17 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str17SOC | 簇17SOC |  | Cluster 17 State Of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17SOH | 簇17SOH |  | Cluster 17 State Of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17ESBCMTemp | 簇17模块温度 |  | Cluster 17 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str17InsulationR | 簇17绝缘电阻 |  | Cluster 17 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str17UAvg | 簇17平均电池电压 |  | Cluster 17 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17TempAvg | 簇17平均电池温度 |  | Cluster 17 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str17MaxBattU | 簇17最高电池电压 |  | Cluster 17 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17MaxUPoINTNo | 簇17最高电压电池对应点号 |  | Cluster 17 Maximum Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MinBattU | 簇17最低电池电压 |  | Cluster 17 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str17MinUPoINTNo | 簇17最低电压电池对应点号 |  | Cluster 17 Minimum Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MaxBattTemp | 簇17最高电池温度 |  | Cluster 17 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str17MaxTempPoINTNo | 簇17最高温度电池对应点号 |  | Cluster 17 Maximum Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MinBattTemp | 簇17最低电池温度 |  | Cluster 17 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str17MINTempPoINTNo | 簇17最低温度电池对应点号 |  | Cluster 17 Minimum Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MaxBattSOC | 簇17最高电池SOC |  | Cluster 17 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17MaxSOCPoINTNo | 簇17最高电池SOC对应点号 |  | Point Number of Cluster 17 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MinBattSOC | 簇17最低电池SOC |  | Cluster 17 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17MinSOCPoINTNo | 簇17最低电池SOC对应点号 |  | Point Number of Cluster 17 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MaxBattSOH | 簇17最高电池SOH |  | Cluster 17 Highest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17MaxSOHPoINTNo | 簇17最高电池SOH对应点号 |  | Point Number of Cluster 17 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17MinBattSOH | 簇17最低电池SOH |  | Cluster 17 Lowest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str17MinSOHPoINTNo | 簇17最低电池SOH对应点号 |  | Point Number of Cluster 17 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str17TotalCharE | 簇17累计充电电量 |  | Cluster 17 Total Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str17TotalDischarE | 簇17累计放电电量 |  | Cluster 17 Total Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str17CharESingle | 簇17单次累计充电电量 |  | Cluster 17 Single Charge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str17DischarESingle | 簇17单次累计放电电量 |  | Cluster 17 Single Discharge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str17CharAvaiE | 簇17可充电量 |  | Cluster 17 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str17DischarAvaiE | 簇17可放电量 |  | Cluster 18 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str18Run | 簇18运行状态 |  | Cluster 18 Operational Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str18MaxCharILim | 簇18允许最大充电电流 |  | Cluster 18 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str18MaxDischarILim | 簇18允许最大放电电流 |  | Cluster 18 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str18MaxCharPLim | 簇18允许最大充电功率 |  | Cluster 18 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str18MaxDischarPLim | 簇18允许最大放电功率 |  | Cluster 18 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str18MaxCharULim | 簇18允许最大充电电压 |  | Cluster 18 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18MaxDischarULim | 簇18允许最大放电电压 |  | Cluster 18 Maximum Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18U | 簇18电压 |  | Cluster 18 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18I | 簇18电流 |  | Cluster 18 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str18SOC | 簇18SOC |  | Cluster 18 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18SOH | 簇18SOH |  | Cluster 18 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18ESBCMTemp | 簇18模块温度 |  | Cluster 18 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str18InsulationR | 簇18绝缘电阻 |  | Cluster 18 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str18UAvg | 簇18平均电池电压 |  | Cluster 18 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18TempAvg | 簇18平均电池温度 |  | Cluster 18 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str18MaxBattU | 簇18最高电池电压 |  | Cluster 18 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18MaxUPoINTNo | 簇18最高电压电池对应点号 |  | Cluster 18 highest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MinBattU | 簇18最低电池电压 |  | Cluster 18 lowest battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str18MinUPoINTNo | 簇18最低电压电池对应点号 |  | Cluster 18 lowest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MaxBattTemp | 簇18最高电池温度 |  | Cluster 18 highest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str18MaxTempPoINTNo | 簇18最高温度电池对应点号 |  | Cluster 18 highest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MinBattTemp | 簇18最低电池温度 |  | Cluster 18 lowest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str18MINTempPoINTNo | 簇18最低温度电池对应点号 |  | Cluster 18 minimum temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MaxBattSOC | 簇18最高电池SOC |  | Cluster 18 highest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18MaxSOCPoINTNo | 簇18最高电池SOC对应点号 |  | Cluster 18 highest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MinBattSOC | 簇18最低电池SOC |  | Cluster 18 lowest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18MinSOCPoINTNo | 簇18最低电池SOC对应点号 |  | Cluster 18 Lowest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MaxBattSOH | 簇18最高电池SOH |  | Cluster 18 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18MaxSOHPoINTNo | 簇18最高电池SOH对应点号 |  | Cluster 18 Highest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18MinBattSOH | 簇18最低电池SOH |  | Cluster 18 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str18MinSOHPoINTNo | 簇18最低电池SOH对应点号 |  | Cluster 18 Lowest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str18TotalCharE | 簇18累计充电电量 |  | Cluster 18 Accumulated Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str18TotalDischarE | 簇18累计放电电量 |  | Cluster 18 Accumulated Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str18CharESingle | 簇18单次累计充电电量 |  | Cluster 18 Single Charge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str18DischarESingle | 簇18单次累计放电电量 |  | Cluster 18 Single Discharge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str18CharAvaiE | 簇18可充电量 |  | Cluster 18 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str18DischarAvaiE | 簇18可放电量 |  | Cluster 18 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str19Run | 簇19运行状态 |  | Cluster 19 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str19MaxCharILim | 簇19允许最大充电电流 |  | Cluster 19 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str19MaxDischarILim | 簇19允许最大放电电流 |  | Cluster 19 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str19MaxCharPLim | 簇19允许最大充电功率 |  | Cluster 19 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str19MaxDischarPLim | 簇19允许最大放电功率 |  | Cluster 19 allows maximum discharge power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str19MaxCharULim | 簇19允许最大充电电压 |  | Cluster 19 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str19MaxDischarULim | 簇19允许最大放电电压 |  | Cluster 19 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str19U | 簇19电压 |  | Cluster 19 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str19I | 簇19电流 |  | Cluster 19 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str19SOC | 簇19SOC |  | Cluster 19 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19SOH | 簇19SOH |  | Cluster 19 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19ESBCMTemp | 簇19模块温度 |  | Cluster 19 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str19InsulationR | 簇19绝缘电阻 |  | Cluster 19 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str19UAvg | 簇19平均电池电压 |  | Cluster 19 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4UAvg | 簇4平均电池电压 |  | Cluster 4 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4TempAvg | 簇4平均电池温度 |  | Cluster 4 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str4MaxBattU | 簇4最高电池电压 |  | Cluster 4 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4MaxUPoINTNo | 簇4最高电压电池对应点号 |  | Point Number of Cluster 4 Highest Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MinBattU | 簇4最低电池电压 |  | Cluster 4 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4MinUPoINTNo | 簇4最低电压电池对应点号 |  | Point Number of Cluster 4 Lowest Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MaxBattTemp | 簇4最高电池温度 |  | Cluster 4 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str4MaxTempPoINTNo | 簇4最高温度电池对应点号 |  | Point Number of Cluster 4 Highest Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MinBattTemp | 簇4最低电池温度 |  | Cluster 4 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str4MINTempPoINTNo | 簇4最低温度电池对应点号 |  | Point Number of Cluster 4 Lowest Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MaxBattSOC | 簇4最高电池SOC |  | Cluster 4 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4MaxSOCPoINTNo | 簇4最高电池SOC对应点号 |  | Cluster 4 Maximum Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MinBattSOC | 簇4最低电池SOC |  | Cluster 4 Minimum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4MinSOCPoINTNo | 簇4最低电池SOC对应点号 |  | Cluster 4 Minimum Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MaxBattSOH | 簇4最高电池SOH |  | Cluster 4 Maximum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4MaxSOHPoINTNo | 簇4最高电池SOH对应点号 |  | Cluster 4 Maximum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4MinBattSOH | 簇4最低电池SOH |  | Cluster 4 Minimum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4MinSOHPoINTNo | 簇4最低电池SOH对应点号 |  | Cluster 4 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str4TotalCharE | 簇4累计充电电量 |  | Cluster 4 Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str4TotalDischarE | 簇4累计放电电量 |  | Cluster 4 Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str4CharESingle | 簇4单次累计充电电量 |  | Cluster 4 Single Cycle Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str4DischarESingle | 簇4单次累计放电电量 |  | Cluster 4 Total Discharge Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str4CharAvaiE | 簇4可充电量 |  | Cluster 4 Rechargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str4DischarAvaiE | 簇4可放电量 |  | Cluster 4 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str5Run | 簇5运行状态 |  | Cluster 5 Operational Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str5MaxCharILim | 簇5允许最大充电电流 |  | Cluster 5 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str5MaxDischarILim | 簇5允许最大放电电流 |  | Cluster 5 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str5MaxCharPLim | 簇5允许最大充电功率 |  | Cluster 5 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str5MaxDischarPLim | 簇5允许最大放电功率 |  | Cluster 5 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str5MaxCharULim | 簇5允许最大充电电压 |  | Cluster 5 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5MaxDischarULim | 簇5允许最大放电电压 |  | Cluster 5 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5U | 簇5电压 |  | Cluster 5 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5I | 簇5电流 |  | Cluster 5 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str5SOC | 簇5SOC |  | Cluster 5 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5SOH | 簇5SOH |  | Cluster 5 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5ESBCMTemp | 簇5模块温度 |  | Cluster 5 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str5InsulationR | 簇5绝缘电阻 |  | Cluster 5 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str5UAvg | 簇5平均电池电压 |  | Cluster 5 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5TempAvg | 簇5平均电池温度 |  | Cluster 5 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str5MaxBattU | 簇5最高电池电压 |  | Cluster 5 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5MaxUPoINTNo | 簇5最高电压电池对应点号 |  | Cluster 5 Battery with Highest Voltage | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MinBattU | 簇5最低电池电压 |  | Cluster 5 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str5MinUPoINTNo | 簇5最低电压电池对应点号 |  | Cluster 5 Lowest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MaxBattTemp | 簇5最高电池温度 |  | Cluster 5 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str5MaxTempPoINTNo | 簇5最高温度电池对应点号 |  | Cluster 5 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MinBattTemp | 簇5最低电池温度 |  | Cluster 5 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str5MINTempPoINTNo | 簇5最低温度电池对应点号 |  | Cluster 5 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MaxBattSOC | 簇5最高电池SOC |  | Cluster 5 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5MaxSOCPoINTNo | 簇5最高电池SOC对应点号 |  | Cluster 5 Highest Battery State of Charge (SOC) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MinBattSOC | 簇5最低电池SOC |  | Cluster 5 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5MinSOCPoINTNo | 簇5最低电池SOC对应点号 |  | Cluster 5 Lowest Battery State of Charge (SOC) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MaxBattSOH | 簇5最高电池SOH |  | Cluster 5 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5MaxSOHPoINTNo | 簇5最高电池SOH对应点号 |  | Cluster 5 Highest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5MinBattSOH | 簇5最低电池SOH |  | Cluster 5 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str5MinSOHPoINTNo | 簇5最低电池SOH对应点号 |  | Cluster 5 Lowest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str5TotalCharE | 簇5累计充电电量 |  | Cluster 5 Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str5TotalDischarE | 簇5累计放电电量 |  | Cluster 5 Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str5CharESingle | 簇5单次累计充电电量 |  | Cluster 5 Single-Time Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str5DischarESingle | 簇5单次累计放电电量 |  | Cluster 5 Single-Time Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str5CharAvaiE | 簇5可充电量 |  | Cluster 5 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str5DischarAvaiE | 簇5可放电量 |  | Cluster 5 Dischargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str6Run | 簇6运行状态 |  | Cluster 6 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str6MaxCharILim | 簇6允许最大充电电流 |  | Cluster 6 Maximum Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str6MaxDischarILim | 簇6允许最大放电电流 |  | Cluster 6 Maximum Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str6MaxCharPLim | 簇6允许最大充电功率 |  | Cluster 6 Maximum Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str6MaxDischarPLim | 簇6允许最大放电功率 |  | Cluster 6 Maximum Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str6MaxCharULim | 簇6允许最大充电电压 |  | Cluster 6 Maximum Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6MaxDischarULim | 簇6允许最大放电电压 |  | Cluster 6 Maximum Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6U | 簇6电压 |  | Cluster 6 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6I | 簇6电流 |  | Cluster 6 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str6SOC | 簇6SOC |  | Cluster 6 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6SOH | 簇6SOH |  | Cluster 6 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6ESBCMTemp | 簇6模块温度 |  | Cluster 6 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str6InsulationR | 簇6绝缘电阻 |  | Cluster 6 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str6UAvg | 簇6平均电池电压 |  | Cluster 6 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6TempAvg | 簇6平均电池温度 |  | Cluster 6 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str6MaxBattU | 簇6最高电池电压 |  | Cluster 6 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6MaxUPoINTNo | 簇6最高电压电池对应点号 |  | Cluster 6 Highest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MinBattU | 簇6最低电池电压 |  | Cluster 6 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str6MinUPoINTNo | 簇6最低电压电池对应点号 |  | Cluster 6 Lowest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MaxBattTemp | 簇6最高电池温度 |  | Cluster 6 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str6MaxTempPoINTNo | 簇6最高温度电池对应点号 |  | Cluster 6 highest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MinBattTemp | 簇6最低电池温度 |  | Cluster 6 lowest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str11MaxTempPoINTNo | 簇11最高温度电池对应点号 |  | Cluster 11 highest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MinBattTemp | 簇11最低电池温度 |  | Cluster 11 lowest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str11MINTempPoINTNo | 簇11最低温度电池对应点号 |  | Cluster 11 lowest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MaxBattSOC | 簇11最高电池SOC |  | Cluster 11 highest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11MaxSOCPoINTNo | 簇11最高电池SOC对应点号 |  | Cluster 11 highest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MinBattSOC | 簇11最低电池SOC |  | Cluster 11 lowest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11MinSOCPoINTNo | 簇11最低电池SOC对应点号 |  | Cluster 11 lowest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MaxBattSOH | 簇11最高电池SOH |  | Cluster 11 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11MaxSOHPoINTNo | 簇11最高电池SOH对应点号 |  | Cluster 11 maximum battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11MinBattSOH | 簇11最低电池SOH |  | Cluster 11 minimum battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str11MinSOHPoINTNo | 簇11最低电池SOH对应点号 |  | Cluster 11 minimum battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str11TotalCharE | 簇11累计充电电量 |  | Cluster 11 cumulative charge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str11TotalDischarE | 簇11累计放电电量 |  | Cluster 11 cumulative discharge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str11CharESingle | 簇11单次累计充电电量 |  | Cluster 11 single charge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str11DischarESingle | 簇11单次累计放电电量 |  | Cluster 11 single discharge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str11CharAvaiE | 簇11可充电量 |  | Cluster 11 chargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str11DischarAvaiE | 簇11可放电量 |  | Cluster 11 dischargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str12Run | 簇12运行状态 |  | Cluster 12 operation status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str12MaxCharILim | 簇12允许最大充电电流 |  | Cluster 12 allows maximum charging current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str12MaxDischarILim | 簇12允许最大放电电流 |  | Cluster 12 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str12MaxCharPLim | 簇12允许最大充电功率 |  | Cluster 12 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str12MaxDischarPLim | 簇12允许最大放电功率 |  | Cluster 12 Maximum Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str12MaxCharULim | 簇12允许最大充电电压 |  | Cluster 12 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12MaxDischarULim | 簇12允许最大放电电压 |  | Cluster 12 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12U | 簇12电压 |  | Cluster 12 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12I | 簇12电流 |  | Cluster 12 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str12SOC | 簇12SOC |  | Cluster 12 State of Charge | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12SOH | 簇12SOH |  | Cluster 12SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12ESBCMTemp | 簇12模块温度 |  | Cluster 12 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str12InsulationR | 簇12绝缘电阻 |  | Cluster 12 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str12UAvg | 簇12平均电池电压 |  | Cluster 12 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12TempAvg | 簇12平均电池温度 |  | Cluster 12 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str12MaxBattU | 簇12最高电池电压 |  | Cluster 12 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12MaxUPoINTNo | 簇12最高电压电池对应点号 |  | Cluster 12 Highest Voltage Battery Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MinBattU | 簇12最低电池电压 |  | Cluster 12 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str12MinUPoINTNo | 簇12最低电压电池对应点号 |  | Cluster 12 Lowest Voltage Battery Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MaxBattTemp | 簇12最高电池温度 |  | Cluster 12 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str12MaxTempPoINTNo | 簇12最高温度电池对应点号 |  | Cluster 12 Highest Temperature Battery Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MinBattTemp | 簇12最低电池温度 |  | Cluster 12 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str12MINTempPoINTNo | 簇12最低温度电池对应点号 |  | Point Number for Cluster 12 Minimum Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MaxBattSOC | 簇12最高电池SOC |  | Cluster 12 Maximum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12MaxSOCPoINTNo | 簇12最高电池SOC对应点号 |  | Point Number for Cluster 12 Maximum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MinBattSOC | 簇12最低电池SOC |  | Cluster 12 Minimum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12MinSOCPoINTNo | 簇12最低电池SOC对应点号 |  | Point Number for Cluster 12 Minimum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MaxBattSOH | 簇12最高电池SOH |  | Cluster 12 Maximum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12MaxSOHPoINTNo | 簇12最高电池SOH对应点号 |  | Point Number for Cluster 12 Maximum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12MinBattSOH | 簇12最低电池SOH |  | Cluster 12 Minimum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str12MinSOHPoINTNo | 簇12最低电池SOH对应点号 |  | Cluster 12 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str12TotalCharE | 簇12累计充电电量 |  | Cluster 12 Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str12TotalDischarE | 簇12累计放电电量 |  | Cluster 12 Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str12CharESingle | 簇12单次累计充电电量 |  | Cluster 12 Single Cycle Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str12DischarESingle | 簇12单次累计放电电量 |  | Cluster 12 Single Cycle Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str12CharAvaiE | 簇12可充电量 |  | Cluster 12 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str12DischarAvaiE | 簇12可放电量 |  | Cluster 12 Dischargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str13Run | 簇13运行状态 |  | Cluster 13 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str13MaxCharILim | 簇13允许最大充电电流 |  | Cluster 13 Maximum Allowable Charging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str13MaxDischarILim | 簇13允许最大放电电流 |  | Cluster 13 Maximum Allowable Discharging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str13MaxCharPLim | 簇13允许最大充电功率 |  | Cluster 13 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str13MaxDischarPLim | 簇13允许最大放电功率 |  | Cluster 13 Maximum Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str13MaxCharULim | 簇13允许最大充电电压 |  | Cluster 13 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13MaxDischarULim | 簇13允许最大放电电压 |  | Cluster 13 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13U | 簇13电压 |  | Cluster 13 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13I | 簇13电流 |  | Cluster 13 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str13SOC | 簇13SOC |  | Cluster 13 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13SOH | 簇13SOH |  | Cluster 13 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13ESBCMTemp | 簇13模块温度 |  | Cluster 13 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str13InsulationR | 簇13绝缘电阻 |  | Cluster 13 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str13UAvg | 簇13平均电池电压 |  | Cluster 13 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13TempAvg | 簇13平均电池温度 |  | Cluster 13 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str13MaxBattU | 簇13最高电池电压 |  | Cluster 13 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13MaxUPoINTNo | 簇13最高电压电池对应点号 |  | Point Number of Battery with Maximum Voltage in Cluster 13 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MinBattU | 簇13最低电池电压 |  | Cluster 13 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str13MinUPoINTNo | 簇13最低电压电池对应点号 |  | Point Number of Battery with Minimum Voltage in Cluster 13 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MaxBattTemp | 簇13最高电池温度 |  | Cluster 13 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str13MaxTempPoINTNo | 簇13最高温度电池对应点号 |  | Point Number of Battery with Maximum Temperature in Cluster 13 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MinBattTemp | 簇13最低电池温度 |  | Cluster 13 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str13MINTempPoINTNo | 簇13最低温度电池对应点号 |  | Point Number of Battery with Minimum Temperature in Cluster 13 | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MaxBattSOC | 簇13最高电池SOC |  | Cluster 13 Max Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13MaxSOCPoINTNo | 簇13最高电池SOC对应点号 |  | Cluster 13 Max Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MinBattSOC | 簇13最低电池SOC |  | Cluster 13 Min Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13MinSOCPoINTNo | 簇13最低电池SOC对应点号 |  | Cluster 13 Min Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MaxBattSOH | 簇13最高电池SOH |  | Cluster 13 Max Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13MaxSOHPoINTNo | 簇13最高电池SOH对应点号 |  | Cluster 13 Max Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13MinBattSOH | 簇13最低电池SOH |  | Cluster 13 Min Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str13MinSOHPoINTNo | 簇13最低电池SOH对应点号 |  | Cluster 13 Min Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str13TotalCharE | 簇13累计充电电量 |  | Cluster 13 Cumulative Charge Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str13TotalDischarE | 簇13累计放电电量 |  | Cluster 13 Cumulative Discharge Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str13CharESingle | 簇13单次累计充电电量 |  | Cluster 13 Single Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str13DischarESingle | 簇13单次累计放电电量 |  | Cluster 13 Single Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str13CharAvaiE | 簇13可充电量 |  | Cluster 13 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str13DischarAvaiE | 簇13可放电量 |  | Cluster 13 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str14Run | 簇14运行状态 |  | Cluster 14 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str14MaxCharILim | 簇14允许最大充电电流 |  | Cluster 14 Maximum Allowable Charging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str14MaxDischarILim | 簇14允许最大放电电流 |  | Cluster 14 Maximum Allowable Discharging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str14MaxCharPLim | 簇14允许最大充电功率 |  | Cluster 14 Maximum Allowable Charging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str14MaxDischarPLim | 簇14允许最大放电功率 |  | Cluster 14 Maximum Allowable Discharging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str14MaxCharULim | 簇14允许最大充电电压 |  | Cluster 14 Maximum Allowable Charging Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14MaxDischarULim | 簇14允许最大放电电压 |  | Cluster 14 Allowable Maximum Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14U | 簇14电压 |  | Cluster 14 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14I | 簇14电流 |  | Cluster 14 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str14SOC | 簇14SOC |  | Cluster 14 SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14SOH | 簇14SOH |  | Cluster 14 SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14ESBCMTemp | 簇14模块温度 |  | Cluster 14 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str14InsulationR | 簇14绝缘电阻 |  | Cluster 14 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str14UAvg | 簇14平均电池电压 |  | Cluster 14 Average Cell Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14TempAvg | 簇14平均电池温度 |  | Cluster 14 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str14MaxBattU | 簇14最高电池电压 |  | Cluster 14 Maximum Cell Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14MaxUPoINTNo | 簇14最高电压电池对应点号 |  | Point Number of Cluster 14 Maximum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MinBattU | 簇14最低电池电压 |  | Cluster 14 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str14MinUPoINTNo | 簇14最低电压电池对应点号 |  | Point Number of Cluster 14 Minimum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MaxBattTemp | 簇14最高电池温度 |  | Cluster 14 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str14MaxTempPoINTNo | 簇14最高温度电池对应点号 |  | Point Number of Cluster 14 Maximum Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MinBattTemp | 簇14最低电池温度 |  | Cluster 14 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str14MINTempPoINTNo | 簇14最低温度电池对应点号 |  | Point Number of Cluster 14 Minimum Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MaxBattSOC | 簇14最高电池SOC |  | Cluster 14 Maximum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14MaxSOCPoINTNo | 簇14最高电池SOC对应点号 |  | Point Number of Cluster 14 Maximum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MinBattSOC | 簇14最低电池SOC |  | Cluster 14 Minimum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14MinSOCPoINTNo | 簇14最低电池SOC对应点号 |  | Point Number of Cluster 14 Minimum Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MaxBattSOH | 簇14最高电池SOH |  | Cluster 14 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14MaxSOHPoINTNo | 簇14最高电池SOH对应点号 |  | Cluster 14 highest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14MinBattSOH | 簇14最低电池SOH |  | Cluster 14 lowest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str14MinSOHPoINTNo | 簇14最低电池SOH对应点号 |  | Cluster 14 lowest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str14TotalCharE | 簇14累计充电电量 |  | Cluster 14 cumulative charge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str14TotalDischarE | 簇14累计放电电量 |  | Cluster 14 cumulative discharge capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str14CharESingle | 簇14单次累计充电电量 |  | Cluster 14 single charge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str14DischarESingle | 簇14单次累计放电电量 |  | Cluster 14 single discharge cumulative capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str14CharAvaiE | 簇14可充电量 |  | Cluster 14 chargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str14DischarAvaiE | 簇14可放电量 |  | Cluster 14 dischargeable capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str15Run | 簇15运行状态 |  | Cluster 15 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str15MaxCharILim | 簇15允许最大充电电流 |  | Cluster 15 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str15MaxDischarILim | 簇15允许最大放电电流 |  | Cluster 15 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str15MaxCharPLim | 簇15允许最大充电功率 |  | Cluster 15 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str15MaxDischarPLim | 簇15允许最大放电功率 |  | Cluster 15 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str15MaxCharULim | 簇15允许最大充电电压 |  | Cluster 15 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str15MaxDischarULim | 簇15允许最大放电电压 |  | Cluster 15 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str15U | 簇15电压 |  | Cluster 15 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SysDayDischarCount | 当天放电次数 |  | Today's Discharge Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| SysDayCharCount | 当天充电次数 |  | Today's Charge Count | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | x |  |
| SysDischarAvaiE | 堆可放电量 |  | Stack Usable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| MinBattTemp | 最低电池温度 |  | Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| MINTempBattStrNo | 最低温度电池组号 |  | Minimum Temperature Battery Group Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MINTempPoINTNo | 最低温度电池所在组中点号 |  | Point Number of the Group with the Lowest Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| SysTotalCharE | 堆累计充电电量 |  | Stack Total Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysTotalDischarE | 堆累计放电电量 |  | Stack Total Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysCharESingle | 堆单次累计充电电量 |  | Stack Single Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysDischarESingle | 堆单次累计放电电量 |  | Stack Single Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysCharAvaiE | 堆可充电量 |  | Stack Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| MaxTempPoINTNo | 最高温度电池所在组中点号 |  | Point Number of the Group with the Highest Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| SysCharAvaiT | 可用充电时间 |  | Available Charge Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| SysDischarAvaiT | 可用放电时间 |  | Available Discharge Time | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| SysDayDischarE | 当天放电电量 |  | Daily Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysDayCharE | 当天充电电量 |  | Daily Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| SysTemp | 电池堆运行温度 |  | Battery Stack Operating Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| MaxBattU | 最高电池电压 |  | Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SysMaxDischarILim | 电池堆允许最大放电电流 |  | Battery Stack Maximum Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SysMaxCharPLim | 电池堆允许最大充电功率 |  | Battery Stack Maximum Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| SysMaxDischarPLim | 电池堆允许最大放电功率 |  | Battery Stack Maximum Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Sta_SysCB | 电池堆电操状态 |  | Battery Stack Control Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"分"<br>			},<br>			"itemValue":"分",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合"<br>			},<br>			"itemValue":"合",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SysU | 电池堆电压 |  | Battery Stack Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SysI | 电池堆电流 |  | Battery Stack Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SysSOC | 电池堆SOC |  | Battery Stack State of Charge | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SysSOH | 电池堆SOH |  | Battery Stack State of Health | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SysMaxCharILim | 电池堆允许最大充电电流 |  | Battery Stack Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| MaxUBattStrNo | 最高电压电池组号 |  | Group Number of Highest Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MaxUPoINTNo | 最高电压电池所在组中的点号 |  | Point Number of Highest Voltage Battery in Group | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MinBattU | 最低电池电压 |  | Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| MinUBattStrNo | 最低电压电池组号 |  | Group Number of Lowest Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MinUPoINTNo | 最低电压电池所在组中的点号 |  | Point Number of Lowest Voltage Battery in Group | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MaxBattTemp | 最高电池温度 |  | Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| MaxTempBattStrNo | 最高温度电池组号 |  | Battery Group Number with Highest Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Sta_SysRun | 堆运行状态 |  | Stack Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电中"<br>			},<br>			"itemValue":"下电中",<br>			"itemKey":"11"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电完成"<br>			},<br>			"itemValue":"下电完成",<br>			"itemKey":"12"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_CharDischar | 充放电状态 |  | Charge and Discharge Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"待机"<br>			},<br>			"itemValue":"待机",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SysInsulationR | 电池堆绝缘电阻 |  | Battery Stack Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| SysTotalCharT | 堆累计充电时间 |  | Total Charge Time of the Stack | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | s |  |
| SysTotalDischarT | 堆累计放电时间 |  | Total Discharge Time of the Stack | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | s |  |
| Err_PCSandBMSComm | PCS和BMS通信故障 |  | PCS and BMS Communication Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"通信正常"<br>			},<br>			"itemValue":"通信正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"通信故障"<br>			},<br>			"itemValue":"通信故障",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_EMSandBMSComm | EMS和BMS通信故障 |  | EMS and BMS Communication Failure | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"通信正常"<br>			},<br>			"itemValue":"通信正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"通信故障"<br>			},<br>			"itemValue":"通信故障",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ESBCMCommFault | 堆内各主控失联汇总 |  | Summary of Main Controller Disconnection Within the Stack | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ESBMMCommFault | 堆内各从控失联汇总 |  | Internal Sub-control Disconnection Summary | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_StringsU | 堆内各组电压异常 |  | Abnormal Voltages in Battery Packs | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ContactorOpen | 堆内接触器断开异常 |  | Abnormal Opening of Internal Contactor | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_ContactorClose | 堆内接触器闭合异常 |  | Abnormal Closure of Internal Contactor | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_Nochar | 充电禁止 |  | Charging Prohibited | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_NoDischar | 放电禁止 |  | Discharging Prohibited | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_BMSAlarmSum | BMS系统告警汇总 |  | BMS System Alarm Summary | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_BMSFaultSum | BMS系统故障汇总 |  | BMS System Failure Summary | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_VoltAcquFault | 电压采集失联 |  | Voltage Acquisition Disconnected | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Err_TempAcquFault | 温度采集失联 |  | Temperature Acquisition Disconnected | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无告警"<br>			},<br>			"itemValue":"无告警",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"告警"<br>			},<br>			"itemValue":"告警",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Sta_Str1Run | 簇1运行状态 |  | Cluster 1 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str1MaxCharILim | 簇1允许最大充电电流 |  | Cluster 1 Max Charging Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str1MaxDischarILim | 簇1允许最大放电电流 |  | Cluster 1 Max Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str1MaxCharPLim | 簇1允许最大充电功率 |  | Cluster 1 Max Charging Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str1MaxDischarPLim | 簇1允许最大放电功率 |  | Cluster 1 Max Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str1MaxCharULim | 簇1允许最大充电电压 |  | Cluster 1 Max Charging Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1MaxDischarULim | 簇1允许最大放电电压 |  | Cluster 1 Max Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1U | 簇1电压 |  | Cluster 1 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1I | 簇1电流 |  | Cluster 1 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str1SOC | 簇1SOC |  | Cluster 1 SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1SOH | 簇1SOH |  | Cluster 1 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1ESBCMTemp | 簇1模块温度 |  | Cluster 1 module temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str1InsulationR | 簇1绝缘电阻 |  | Cluster 1 insulation resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str1UAvg | 簇1平均电池电压 |  | Cluster 1 average battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1TempAvg | 簇1平均电池温度 |  | Cluster 1 average battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str1MaxBattU | 簇1最高电池电压 |  | Cluster 1 highest battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1MaxUPoINTNo | 簇1最高电压电池对应点号 |  | Cluster 1 highest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MinBattU | 簇1最低电池电压 |  | Cluster 1 lowest battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str1MinUPoINTNo | 簇1最低电压电池对应点号 |  | Cluster 1 lowest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MaxBattTemp | 簇1最高电池温度 |  | Cluster 1 highest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str1MaxTempPoINTNo | 簇1最高温度电池对应点号 |  | Cluster 1 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MinBattTemp | 簇1最低电池温度 |  | Cluster 1 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str1MINTempPoINTNo | 簇1最低温度电池对应点号 |  | Cluster 1 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MaxBattSOC | 簇1最高电池SOC |  | Cluster 1 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1MaxSOCPoINTNo | 簇1最高电池SOC对应点号 |  | Cluster 1 Highest Battery State of Charge (SOC) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MinBattSOC | 簇1最低电池SOC |  | Cluster 1 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1MinSOCPoINTNo | 簇1最低电池SOC对应点号 |  | Cluster 1 Lowest Battery State of Charge (SOC) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MaxBattSOH | 簇1最高电池SOH |  | Cluster 1 Highest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1MaxSOHPoINTNo | 簇1最高电池SOH对应点号 |  | Cluster 1 Highest Battery State of Health (SOH) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1MinBattSOH | 簇1最低电池SOH |  | Cluster 1 Lowest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str1MinSOHPoINTNo | 簇1最低电池SOH对应点号 |  | Cluster 1 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str1TotalCharE | 簇1累计充电电量 |  | Cluster 1 Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str1TotalDischarE | 簇1累计放电电量 |  | Cluster 1 Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str1CharESingle | 簇1单次累计充电电量 |  | Cluster 1 Single Cycle Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str1DischarESingle | 簇1单次累计放电电量 |  | Cluster 1 Single Cycle Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str1CharAvaiE | 簇1可充电量 |  | Cluster 1 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str1DischarAvaiE | 簇1可放电量 |  | Cluster 1 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str2Run | 簇2运行状态 |  | Cluster 2 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str2MaxCharILim | 簇2允许最大充电电流 |  | Cluster 2 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str2MaxDischarILim | 簇2允许最大放电电流 |  | Cluster 2 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str2MaxCharPLim | 簇2允许最大充电功率 |  | Cluster 2 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str2MaxDischarPLim | 簇2允许最大放电功率 |  | Cluster 2 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str2MaxCharULim | 簇2允许最大充电电压 |  | Cluster 2 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2MaxDischarULim | 簇2允许最大放电电压 |  | Cluster 2 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2U | 簇2电压 |  | Cluster 2 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2I | 簇2电流 |  | Cluster 2 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str2SOC | 簇2SOC |  | Cluster 2 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2SOH | 簇2SOH |  | Cluster 2 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2ESBCMTemp | 簇2模块温度 |  | Cluster 2 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str2InsulationR | 簇2绝缘电阻 |  | Cluster 2 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str2UAvg | 簇2平均电池电压 |  | Cluster 2 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2TempAvg | 簇2平均电池温度 |  | Cluster 2 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str2MaxBattU | 簇2最高电池电压 |  | Cluster 2 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2MaxUPoINTNo | 簇2最高电压电池对应点号 |  | Cluster 2 Maximum Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MinBattU | 簇2最低电池电压 |  | Cluster 2 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str2MinUPoINTNo | 簇2最低电压电池对应点号 |  | Cluster 2 Minimum Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MaxBattTemp | 簇2最高电池温度 |  | Cluster 2 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str2MaxTempPoINTNo | 簇2最高温度电池对应点号 |  | Cluster 2 Maximum Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MinBattTemp | 簇2最低电池温度 |  | Cluster 2 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str2MINTempPoINTNo | 簇2最低温度电池对应点号 |  | Cluster 2 Minimum Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MaxBattSOC | 簇2最高电池SOC |  | Cluster 2 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2MaxSOCPoINTNo | 簇2最高电池SOC对应点号 |  | Cluster 2 Highest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MinBattSOC | 簇2最低电池SOC |  | Cluster 2 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2MinSOCPoINTNo | 簇2最低电池SOC对应点号 |  | Cluster 2 Lowest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MaxBattSOH | 簇2最高电池SOH |  | Cluster 2 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2MaxSOHPoINTNo | 簇2最高电池SOH对应点号 |  | Cluster 2 Highest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2MinBattSOH | 簇2最低电池SOH |  | Cluster 2 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str2MinSOHPoINTNo | 簇2最低电池SOH对应点号 |  | Cluster 2 Lowest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str2TotalCharE | 簇2累计充电电量 |  | Cluster 2 Total Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str2TotalDischarE | 簇2累计放电电量 |  | Cluster 2 Total Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str2CharESingle | 簇2单次累计充电电量 |  | Cluster 2 Single Charge Accumulated Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str2DischarESingle | 簇2单次累计放电电量 |  | Cluster 2 Single Discharge Accumulated Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str2CharAvaiE | 簇2可充电量 |  | Cluster 2 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str2DischarAvaiE | 簇2可放电量 |  | Cluster 2 Available Discharge Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str3Run | 簇3运行状态 |  | Cluster 3 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str3MaxCharILim | 簇3允许最大充电电流 |  | Cluster 3 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str3MaxDischarILim | 簇3允许最大放电电流 |  | Cluster 3 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str3MaxCharPLim | 簇3允许最大充电功率 |  | Cluster 3 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str3MaxDischarPLim | 簇3允许最大放电功率 |  | Cluster 3 Maximum Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str3MaxCharULim | 簇3允许最大充电电压 |  | Cluster 3 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3MaxDischarULim | 簇3允许最大放电电压 |  | Cluster 3 Allowed Maximum Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3U | 簇3电压 |  | Cluster 3 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3I | 簇3电流 |  | Cluster 3 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str3SOC | 簇3SOC |  | Cluster 3 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3SOH | 簇3SOH |  | Cluster 3 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3ESBCMTemp | 簇3模块温度 |  | Cluster 3 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str3InsulationR | 簇3绝缘电阻 |  | Cluster 3 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str3UAvg | 簇3平均电池电压 |  | Cluster 3 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3TempAvg | 簇3平均电池温度 |  | Cluster 3 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str3MaxBattU | 簇3最高电池电压 |  | Cluster 3 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3MaxUPoINTNo | 簇3最高电压电池对应点号 |  | Cluster 3 highest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MinBattU | 簇3最低电池电压 |  | Cluster 3 lowest battery voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str3MinUPoINTNo | 簇3最低电压电池对应点号 |  | Cluster 3 lowest voltage battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MaxBattTemp | 簇3最高电池温度 |  | Cluster 3 highest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str3MaxTempPoINTNo | 簇3最高温度电池对应点号 |  | Cluster 3 highest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MinBattTemp | 簇3最低电池温度 |  | Cluster 3 lowest battery temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str3MINTempPoINTNo | 簇3最低温度电池对应点号 |  | Cluster 3 lowest temperature battery corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MaxBattSOC | 簇3最高电池SOC |  | Cluster 3 highest battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3MaxSOCPoINTNo | 簇3最高电池SOC对应点号 |  | Cluster 3 highest battery State of Charge (SOC) corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MinBattSOC | 簇3最低电池SOC |  | Cluster 3 lowest battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3MinSOCPoINTNo | 簇3最低电池SOC对应点号 |  | Cluster 3 Minimum Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MaxBattSOH | 簇3最高电池SOH |  | Cluster 3 Maximum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3MaxSOHPoINTNo | 簇3最高电池SOH对应点号 |  | Cluster 3 Maximum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3MinBattSOH | 簇3最低电池SOH |  | Cluster 3 Minimum Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str3MinSOHPoINTNo | 簇3最低电池SOH对应点号 |  | Cluster 3 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str3TotalCharE | 簇3累计充电电量 |  | Cluster 3 Cumulative Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str3TotalDischarE | 簇3累计放电电量 |  | Cluster 3 Cumulative Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str3CharESingle | 簇3单次累计充电电量 |  | Cluster 3 Single Charge Cumulative Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str3DischarESingle | 簇3单次累计放电电量 |  | Cluster 3 Single Discharge Cumulative Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str3CharAvaiE | 簇3可充电量 |  | Cluster 3 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str3DischarAvaiE | 簇3可放电量 |  | Cluster 3 Remaining Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str4Run | 簇4运行状态 |  | Cluster 4 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str4MaxCharILim | 簇4允许最大充电电流 |  | Cluster 4 Maximum Allowed Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str4MaxDischarILim | 簇4允许最大放电电流 |  | Cluster 4 Maximum Allowed Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str4MaxCharPLim | 簇4允许最大充电功率 |  | Cluster 4 Maximum Allowed Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str4MaxDischarPLim | 簇4允许最大放电功率 |  | Cluster 4 Maximum Allowed Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str4MaxCharULim | 簇4允许最大充电电压 |  | Cluster 4 Maximum Allowed Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4MaxDischarULim | 簇4允许最大放电电压 |  | Cluster 4 Maximum Allowed Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4U | 簇4电压 |  | Cluster 4 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str4I | 簇4电流 |  | Cluster 4 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str4SOC | 簇4SOC |  | Cluster 4 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4SOH | 簇4SOH |  | Cluster 4 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str4ESBCMTemp | 簇4模块温度 |  | Cluster 4 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str4InsulationR | 簇4绝缘电阻 |  | Cluster 4 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str19TempAvg | 簇19平均电池温度 |  | Cluster 19 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str19MaxBattU | 簇19最高电池电压 |  | Cluster 19 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str19MaxUPoINTNo | 簇19最高电压电池对应点号 |  | Point Number of Cluster 19 Maximum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MinBattU | 簇19最低电池电压 |  | Cluster 19 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str19MinUPoINTNo | 簇19最低电压电池对应点号 |  | Point Number of Cluster 19 Minimum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MaxBattTemp | 簇19最高电池温度 |  | Cluster 19 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str19MaxTempPoINTNo | 簇19最高温度电池对应点号 |  | Cluster 19 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MinBattTemp | 簇19最低电池温度 |  | Cluster 19 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str19MINTempPoINTNo | 簇19最低温度电池对应点号 |  | Cluster 19 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MaxBattSOC | 簇19最高电池SOC |  | Cluster 19 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19MaxSOCPoINTNo | 簇19最高电池SOC对应点号 |  | Cluster 19 Highest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MinBattSOC | 簇19最低电池SOC |  | Cluster 19 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19MinSOCPoINTNo | 簇19最低电池SOC对应点号 |  | Cluster 19 Lowest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MaxBattSOH | 簇19最高电池SOH |  | Cluster 19 Highest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19MaxSOHPoINTNo | 簇19最高电池SOH对应点号 |  | Cluster 19 Highest Battery State of Health (SOH) Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19MinBattSOH | 簇19最低电池SOH |  | Cluster 19 Lowest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str19MinSOHPoINTNo | 簇19最低电池SOH对应点号 |  | Cluster 19 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str19TotalCharE | 簇19累计充电电量 |  | Cluster 19 Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str19TotalDischarE | 簇19累计放电电量 |  | Cluster 19 Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str19CharESingle | 簇19单次累计充电电量 |  | Cluster 19 Single Cycle Cumulative Charged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str19DischarESingle | 簇19单次累计放电电量 |  | Cluster 19 Single Cycle Cumulative Discharged Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str19CharAvaiE | 簇19可充电量 |  | Cluster 19 Chargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str19DischarAvaiE | 簇19可放电量 |  | Cluster 19 Dischargeable Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str20Run | 簇20运行状态 |  | Cluster 20 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str20MaxCharILim | 簇20允许最大充电电流 |  | Cluster 20 Maximum Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str20MaxDischarILim | 簇20允许最大放电电流 |  | Cluster 20 Maximum Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str20MaxCharPLim | 簇20允许最大充电功率 |  | Cluster 20 Maximum Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str20MaxDischarPLim | 簇20允许最大放电功率 |  | Cluster 20 Maximum Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str20MaxCharULim | 簇20允许最大充电电压 |  | Cluster 20 Maximum Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20MaxDischarULim | 簇20允许最大放电电压 |  | Cluster 20 Maximum Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20U | 簇20电压 |  | Cluster 20 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20I | 簇20电流 |  | Cluster 20 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str20SOC | 簇20SOC |  | Cluster 20 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20SOH | 簇20SOH |  | Cluster 20 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20ESBCMTemp | 簇20模块温度 |  | Cluster 20 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str20InsulationR | 簇20绝缘电阻 |  | Cluster 20 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str20UAvg | 簇20平均电池电压 |  | Cluster 20 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20TempAvg | 簇20平均电池温度 |  | Cluster 20 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str20MaxBattU | 簇20最高电池电压 |  | Cluster 20 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20MaxUPoINTNo | 簇20最高电压电池对应点号 |  | Point Number of Cluster 20 Maximum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MinBattU | 簇20最低电池电压 |  | Cluster 20 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str20MinUPoINTNo | 簇20最低电压电池对应点号 |  | Point Number of Cluster 20 Minimum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MaxBattTemp | 簇20最高电池温度 |  | Cluster 20 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str20MaxTempPoINTNo | 簇20最高温度电池对应点号 |  | Point Number of Cluster 20 Maximum Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MinBattTemp | 簇20最低电池温度 |  | Cluster 20 Minimum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str20MINTempPoINTNo | 簇20最低温度电池对应点号 |  | Point Number of Cluster 20 Minimum Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MaxBattSOC | 簇20最高电池SOC |  | Cluster 20 highest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20MaxSOCPoINTNo | 簇20最高电池SOC对应点号 |  | Cluster 20 highest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MinBattSOC | 簇20最低电池SOC |  | Cluster 20 lowest battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20MinSOCPoINTNo | 簇20最低电池SOC对应点号 |  | Cluster 20 lowest battery SOC corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MaxBattSOH | 簇20最高电池SOH |  | Cluster 20 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20MaxSOHPoINTNo | 簇20最高电池SOH对应点号 |  | Cluster 20 highest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20MinBattSOH | 簇20最低电池SOH |  | Cluster 20 lowest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str20MinSOHPoINTNo | 簇20最低电池SOH对应点号 |  | Cluster 20 lowest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str20TotalCharE | 簇20累计充电电量 |  | Cluster 20 cumulative charged energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str20TotalDischarE | 簇20累计放电电量 |  | Cluster 20 cumulative discharged energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str20CharESingle | 簇20单次累计充电电量 |  | Cluster 20 Single Charge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str20DischarESingle | 簇20单次累计放电电量 |  | Cluster 20 Single Discharge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str20CharAvaiE | 簇20可充电量 |  | Cluster 20 Rechargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str20DischarAvaiE | 簇20可放电量 |  | Cluster 20 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | kWh |  |
| StringNumber | 电池簇数量 |  | Battery Cluster Quantity | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| SysFaultReset | 系统故障复位 |  | System Fault Reset | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"不复位"<br>			},<br>			"itemValue":"不复位",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"复位"<br>			},<br>			"itemValue":"复位",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SysCBCtrl | 电操控制 |  | Electric Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"不操作"<br>			},<br>			"itemValue":"不操作",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| SysPowerCtrl | 系统上下电控制 |  | System Power On/Off Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"不操作"<br>			},<br>			"itemValue":"不操作",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上高压"<br>			},<br>			"itemValue":"上高压",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下高压"<br>			},<br>			"itemValue":"下高压",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str1MainModeCtrl | 簇1维护模式控制 |  | Cluster 1 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str3MainModeCtrl | 簇3维护模式控制 |  | Cluster 3 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str4MainModeCtrl | 簇4维护模式控制 |  | Cluster 4 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str5MainModeCtrl | 簇5维护模式控制 |  | Cluster 5 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str6MainModeCtrl | 簇6维护模式控制 |  | Cluster 6 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str7MainModeCtrl | 簇7维护模式控制 |  | Cluster 7 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str8MainModeCtrl | 簇8维护模式控制 |  | Cluster 8 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str9MainModeCtrl | 簇9维护模式控制 |  | Cluster 9 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str10MainModeCtrl | 簇10维护模式控制 |  | Cluster 10 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str11MainModeCtrl | 簇11维护模式控制 |  | Cluster 11 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str12MainModeCtrl | 簇12维护模式控制 |  | Cluster 12 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str13MainModeCtrl | 簇13维护模式控制 |  | Cluster 13 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str14MainModeCtrl | 簇14维护模式控制 |  | Cluster 14 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str15MainModeCtrl | 簇15维护模式控制 |  | Cluster 15 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str16MainModeCtrl | 簇16维护模式控制 |  | Cluster 16 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str17MainModeCtrl | 簇17维护模式控制 |  | Cluster 17 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str18MainModeCtrl | 簇18维护模式控制 |  | Cluster 18 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str19MainModeCtrl | 簇19维护模式控制 |  | Cluster 19 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str20MainModeCtrl | 簇20维护模式控制 |  | Cluster 20 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str2MainModeCtrl | 簇2维护模式控制 |  | Cluster 2 Maintenance Mode Control | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"无效"<br>			},<br>			"itemValue":"无效",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"上电"<br>			},<br>			"itemValue":"上电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"下电"<br>			},<br>			"itemValue":"下电",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | RW |  |  |
| Str6MINTempPoINTNo | 簇6最低温度电池对应点号 |  | Cluster 6 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MaxBattSOC | 簇6最高电池SOC |  | Cluster 6 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6MaxSOCPoINTNo | 簇6最高电池SOC对应点号 |  | Cluster 6 Highest Battery State of Charge (SOC) Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MinBattSOC | 簇6最低电池SOC |  | Cluster 6 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6MinSOCPoINTNo | 簇6最低电池SOC对应点号 |  | Cluster 6 Lowest Battery State of Charge (SOC) Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MaxBattSOH | 簇6最高电池SOH |  | Cluster 6 Highest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6MaxSOHPoINTNo | 簇6最高电池SOH对应点号 |  | Cluster 6 Highest Battery State of Health (SOH) Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6MinBattSOH | 簇6最低电池SOH |  | Cluster 6 Lowest Battery State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str6MinSOHPoINTNo | 簇6最低电池SOH对应点号 |  | Cluster 6 Lowest Battery State of Health (SOH) Corresponding Point | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str6TotalCharE | 簇6累计充电电量 |  | Cluster 6 Total Accumulated Charge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str6TotalDischarE | 簇6累计放电电量 |  | Cluster 6 Total Accumulated Discharge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str6CharESingle | 簇6单次累计充电电量 |  | Cluster 6 Total Accumulated Charge | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str6DischarESingle | 簇6单次累计放电电量 |  | Cluster 6 Single Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str6CharAvaiE | 簇6可充电量 |  | Cluster 6 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str6DischarAvaiE | 簇6可放电量 |  | Cluster 6 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str7Run | 簇7运行状态 |  | Cluster 7 Operating Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str7MaxCharILim | 簇7允许最大充电电流 |  | Cluster 7 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str7MaxDischarILim | 簇7允许最大放电电流 |  | Cluster 7 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str7MaxCharPLim | 簇7允许最大充电功率 |  | Cluster 7 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str7MaxDischarPLim | 簇7允许最大放电功率 |  | Cluster 7 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str7MaxCharULim | 簇7允许最大充电电压 |  | Cluster 7 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7MaxDischarULim | 簇7允许最大放电电压 |  | Cluster 7 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7U | 簇7电压 |  | Cluster 7 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7I | 簇7电流 |  | Cluster 7 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str7SOC | 簇7SOC |  | Cluster 7 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7SOH | 簇7SOH |  | Cluster 7 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7ESBCMTemp | 簇7模块温度 |  | Cluster 7 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str7InsulationR | 簇7绝缘电阻 |  | Cluster 7 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str7UAvg | 簇7平均电池电压 |  | Cluster 7 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7TempAvg | 簇7平均电池温度 |  | Cluster 7 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str7MaxBattU | 簇7最高电池电压 |  | Cluster 7 Max Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7MaxUPoINTNo | 簇7最高电压电池对应点号 |  | Cluster 7 Max Voltage Battery Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MinBattU | 簇7最低电池电压 |  | Cluster 7 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str7MinUPoINTNo | 簇7最低电压电池对应点号 |  | Point Number of Cluster 7 Lowest Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MaxBattTemp | 簇7最高电池温度 |  | Cluster 7 Highest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str7MaxTempPoINTNo | 簇7最高温度电池对应点号 |  | Point Number of Cluster 7 Highest Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MinBattTemp | 簇7最低电池温度 |  | Cluster 7 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str7MINTempPoINTNo | 簇7最低温度电池对应点号 |  | Point Number of Cluster 7 Lowest Temperature Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MaxBattSOC | 簇7最高电池SOC |  | Cluster 7 Highest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7MaxSOCPoINTNo | 簇7最高电池SOC对应点号 |  | Point Number of Cluster 7 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MinBattSOC | 簇7最低电池SOC |  | Cluster 7 Lowest Battery State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7MinSOCPoINTNo | 簇7最低电池SOC对应点号 |  | Point Number of Cluster 7 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MaxBattSOH | 簇7最高电池SOH |  | Cluster 7 highest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7MaxSOHPoINTNo | 簇7最高电池SOH对应点号 |  | Cluster 7 highest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7MinBattSOH | 簇7最低电池SOH |  | Cluster 7 lowest battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str7MinSOHPoINTNo | 簇7最低电池SOH对应点号 |  | Cluster 7 lowest battery SOH corresponding point number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str7TotalCharE | 簇7累计充电电量 |  | Cluster 7 cumulative charge energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str7TotalDischarE | 簇7累计放电电量 |  | Cluster 7 cumulative discharge energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str7CharESingle | 簇7单次累计充电电量 |  | Cluster 7 single cumulative charge energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str7DischarESingle | 簇7单次累计放电电量 |  | Cluster 7 single discharge energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str7CharAvaiE | 簇7可充电量 |  | Cluster 7 chargeable energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str7DischarAvaiE | 簇7可放电量 |  | Cluster 7 dischargeable energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str8Run | 簇8运行状态 |  | Cluster 8 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str8MaxCharILim | 簇8允许最大充电电流 |  | Cluster 8 Max Charge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str8MaxDischarILim | 簇8允许最大放电电流 |  | Cluster 8 Max Discharge Current Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str8MaxCharPLim | 簇8允许最大充电功率 |  | Cluster 8 Max Charge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str8MaxDischarPLim | 簇8允许最大放电功率 |  | Cluster 8 Max Discharge Power Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str8MaxCharULim | 簇8允许最大充电电压 |  | Cluster 8 Max Charge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8MaxDischarULim | 簇8允许最大放电电压 |  | Cluster 8 Max Discharge Voltage Allowed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8U | 簇8电压 |  | Cluster 8 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8I | 簇8电流 |  | Cluster 8 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str8SOC | 簇8SOC |  | Cluster 8 SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8SOH | 簇8SOH |  | Cluster 8 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8ESBCMTemp | 簇8模块温度 |  | Cluster 8 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str8InsulationR | 簇8绝缘电阻 |  | Cluster 8 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str8UAvg | 簇8平均电池电压 |  | Cluster 8 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8TempAvg | 簇8平均电池温度 |  | Cluster 8 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str8MaxBattU | 簇8最高电池电压 |  | Cluster 8 Maximum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8MaxUPoINTNo | 簇8最高电压电池对应点号 |  | Point Number Corresponding to Cluster 8 Maximum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MinBattU | 簇8最低电池电压 |  | Cluster 8 Minimum Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str8MinUPoINTNo | 簇8最低电压电池对应点号 |  | Point Number Corresponding to Cluster 8 Minimum Voltage Battery | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MaxBattTemp | 簇8最高电池温度 |  | Cluster 8 Maximum Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str8MaxTempPoINTNo | 簇8最高温度电池对应点号 |  | Cluster 8 Highest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MinBattTemp | 簇8最低电池温度 |  | Cluster 8 Lowest Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str8MINTempPoINTNo | 簇8最低温度电池对应点号 |  | Cluster 8 Lowest Temperature Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MaxBattSOC | 簇8最高电池SOC |  | Cluster 8 Highest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8MaxSOCPoINTNo | 簇8最高电池SOC对应点号 |  | Cluster 8 Highest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MinBattSOC | 簇8最低电池SOC |  | Cluster 8 Lowest Battery SOC | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8MinSOCPoINTNo | 簇8最低电池SOC对应点号 |  | Cluster 8 Lowest Battery SOC Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MaxBattSOH | 簇8最高电池SOH |  | Cluster 8 Highest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8MaxSOHPoINTNo | 簇8最高电池SOH对应点号 |  | Cluster 8 Highest Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8MinBattSOH | 簇8最低电池SOH |  | Cluster 8 Lowest Battery SOH | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str8MinSOHPoINTNo | 簇8最低电池SOH对应点号 |  | Cluster 8 Minimum Battery SOH Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str8TotalCharE | 簇8累计充电电量 |  | Cluster 8 Accumulated Charge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str8TotalDischarE | 簇8累计放电电量 |  | Cluster 8 Accumulated Discharge Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str8CharESingle | 簇8单次累计充电电量 |  | Cluster 8 Single Charge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str8DischarESingle | 簇8单次累计放电电量 |  | Cluster 8 Single Discharge Accumulated Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str8CharAvaiE | 簇8可充电量 |  | Cluster 8 Chargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Str8DischarAvaiE | 簇8可放电量 |  | Cluster 8 Dischargeable Capacity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Sta_Str9Run | 簇9运行状态 |  | Cluster 9 Operation Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"初始状态"<br>			},<br>			"itemValue":"初始状态",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充电"<br>			},<br>			"itemValue":"充电",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"放电"<br>			},<br>			"itemValue":"放电",<br>			"itemKey":"2"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"就绪"<br>			},<br>			"itemValue":"就绪",<br>			"itemKey":"3"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"簇维护"<br>			},<br>			"itemValue":"簇维护",<br>			"itemKey":"4"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁充"<br>			},<br>			"itemValue":"禁充",<br>			"itemKey":"5"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"禁放"<br>			},<br>			"itemValue":"禁放",<br>			"itemKey":"6"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"充放禁止"<br>			},<br>			"itemValue":"充放禁止",<br>			"itemKey":"7"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障"<br>			},<br>			"itemValue":"故障",<br>			"itemKey":"8"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"故障恢复"<br>			},<br>			"itemValue":"故障恢复",<br>			"itemKey":"9"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"测试模式"<br>			},<br>			"itemValue":"测试模式",<br>			"itemKey":"10"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Str9MaxCharILim | 簇9允许最大充电电流 |  | Cluster 9 Maximum Allowable Charge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str9MaxDischarILim | 簇9允许最大放电电流 |  | Cluster 9 Maximum Allowable Discharge Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str9MaxCharPLim | 簇9允许最大充电功率 |  | Cluster 9 Maximum Allowable Charge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str9MaxDischarPLim | 簇9允许最大放电功率 |  | Cluster 9 Maximum Allowable Discharge Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Str9MaxCharULim | 簇9允许最大充电电压 |  | Cluster 9 Maximum Allowable Charge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str9MaxDischarULim | 簇9允许最大放电电压 |  | Cluster 9 Maximum Allowable Discharge Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str9U | 簇9电压 |  | Cluster 9 Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str9I | 簇9电流 |  | Cluster 9 Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Str9SOC | 簇9SOC |  | Cluster 9 State of Charge (SOC) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9SOH | 簇9SOH |  | Cluster 9 State of Health (SOH) | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Str9ESBCMTemp | 簇9模块温度 |  | Cluster 9 Module Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str9InsulationR | 簇9绝缘电阻 |  | Cluster 9 Insulation Resistance | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kΩ |  |
| Str9UAvg | 簇9平均电池电压 |  | Cluster 9 Average Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str9TempAvg | 簇9平均电池温度 |  | Cluster 9 Average Battery Temperature | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Str9MaxBattU | 簇9最高电池电压 |  | Cluster 9 Highest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Str9MaxUPoINTNo | 簇9最高电压电池对应点号 |  | Cluster 9 Highest Voltage Battery Corresponding Point Number | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Str9MinBattU | 簇9最低电池电压 |  | Cluster 9 Lowest Battery Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorPCSandBMSComm | PCS和BMS通信故障 |  | PCS and BMS communication failure | FAULT | Err_PCSandBMSComm | Err_PCSandBMSComm = 1 |  |
| ErrorEMSandBMSComm | EMS和BMS通信故障 |  | EMS and BMS communication failure | FAULT | Err_EMSandBMSComm | Err_EMSandBMSComm = 1 |  |
| ErrorESBCMCommFault | 堆内各主控失联汇总 |  | Internal Master Controllers Disconnection Summary | FAULT | Err_ESBCMCommFault | Err_ESBCMCommFault = 1 |  |
| ErrorESBMMCommFault | 堆内各从控失联汇总 |  | Internal Slave Controllers Disconnection Summary | FAULT | Err_ESBMMCommFault | Err_ESBMMCommFault = 1 |  |
| ErrorrStringsU | 堆内各组电压异常 |  | Abnormal Voltage of Each Group in the Stack | FAULT | Err_StringsU | Err_StringsU = 1 |  |
| ErrorContactorOpen | 堆内接触器断开异常 |  | Abnormal Disconnection of Internal Contactor | FAULT | Err_ContactorOpen | Err_ContactorOpen = 1 |  |
| ErrorContactorClose | 堆内接触器闭合异常 |  | Abnormal Closure of Internal Contactor | FAULT | Err_ContactorClose | Err_ContactorClose = 1 |  |
| ErrorNochar | 充电禁止 |  | Charging Prohibited | FAULT | Err_Nochar | Err_Nochar = 1 |  |
| ErrorNoDischar | 放电禁止 |  | Discharge Prohibited | FAULT | Err_NoDischar | Err_NoDischar = 1 |  |
| AlaorBMSAlarmSum | BMS系统告警汇总 |  | BMS System Alarm Summary | ALARM | Ala_BMSAlarmSum | Ala_BMSAlarmSum = 1 |  |
| ErrorBMSFaultSum | BMS系统故障汇总 |  | BMS System Failure Summary | FAULT | Err_BMSFaultSum | Err_BMSFaultSum = 1 |  |
| ErrorVoltAcquFault | 电压采集失联 |  | Voltage Acquisition Disconnected | FAULT | Err_VoltAcquFault | Err_VoltAcquFault = 1 |  |
| ErrorTempAcquFault | 温度采集失联 |  | Temperature Acquisition Disconnected | FAULT | Err_TempAcquFault | Err_TempAcquFault = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| Str2MainModeCtrlCmd | 簇2维护模式控制 |  | Cluster 2 Maintenance Mode Control | Str2MainModeCtrl |  |  |
| SysPowerCtrlCmd | 系统上下电控制 |  | System Power On/Off Control | SysPowerCtrl |  |  |
| SysFaultResetCmd | 系统故障复位 |  | System Fault Reset | SysFaultReset |  |  |
| SysCBCtrlCmd | 电操控制 |  | Electric Control | SysCBCtrl |  |  |
| StringNumberCmd | 电池簇数量 |  | Battery Cluster Count | StringNumber |  |  |
| Str9MainModeCtrlCmd | 簇9维护模式控制 |  | Cluster 9 Maintenance Mode Control | Str9MainModeCtrl |  |  |
| Str8MainModeCtrlCmd | 簇8维护模式控制 |  | Cluster 8 Maintenance Mode Control | Str8MainModeCtrl |  |  |
| Str7MainModeCtrlCmd | 簇7维护模式控制 |  | Cluster 7 Maintenance Mode Control | Str7MainModeCtrl |  |  |
| Str6MainModeCtrlCmd | 簇6维护模式控制 |  | Cluster 6 Maintenance Mode Control | Str6MainModeCtrl |  |  |
| Str5MainModeCtrlCmd | 簇5维护模式控制 |  | Cluster 5 Maintenance Mode Control | Str5MainModeCtrl |  |  |
| Str4MainModeCtrlCmd | 簇4维护模式控制 |  | Cluster 4 Maintenance Mode Control | Str4MainModeCtrl |  |  |
| Str3MainModeCtrlCmd | 簇3维护模式控制 |  | Cluster 3 Maintenance Mode Control | Str3MainModeCtrl |  |  |
| Str10MainModeCtrlCmd | 簇10维护模式控制 |  | Cluster 10 Maintenance Mode Control | Str10MainModeCtrl |  |  |
| Str20MainModeCtrlCmd | 簇20维护模式控制 |  | Cluster 20 Maintenance Mode Control | Str20MainModeCtrl |  |  |
| Str1MainModeCtrlCmd | 簇1维护模式控制 |  | Cluster 1 Maintenance Mode Control | Str1MainModeCtrl |  |  |
| Str19MainModeCtrlCmd | 簇19维护模式控制 |  | Cluster 19 Maintenance Mode Control | Str19MainModeCtrl |  |  |
| Str18MainModeCtrlCmd | 簇18维护模式控制 |  | Cluster 18 Maintenance Mode Control | Str18MainModeCtrl |  |  |
| Str17MainModeCtrlCmd | 簇17维护模式控制 |  | Cluster 17 Maintenance Mode Control | Str17MainModeCtrl |  |  |
| Str16MainModeCtrlCmd | 簇16维护模式控制 |  | Cluster 16 Maintenance Mode Control | Str16MainModeCtrl |  |  |
| Str15MainModeCtrlCmd | 簇15维护模式控制 |  | Cluster 15 Maintenance Mode Control | Str15MainModeCtrl |  |  |
| Str14MainModeCtrlCmd | 簇14维护模式控制 |  | Cluster 14 Maintenance Mode Control | Str14MainModeCtrl |  |  |
| Str13MainModeCtrlCmd | 簇13维护模式控制 |  | Cluster 13 Maintenance Mode Control | Str13MainModeCtrl |  |  |
| Str12MainModeCtrlCmd | 簇12维护模式控制 |  | Cluster 12 Maintenance Mode Control | Str12MainModeCtrl |  |  |
| Str11MainModeCtrlCmd | 簇11维护模式控制 |  | Cluster 11 Maintenance Mode Control | Str11MainModeCtrl |  |  |
