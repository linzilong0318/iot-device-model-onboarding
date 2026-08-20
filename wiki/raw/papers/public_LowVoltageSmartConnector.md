# public_LowVoltageSmartConnector

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_LowVoltageSmartConnector | 低压智能接插件 | 低压智能接插件 | Low Voltage Smart Connector | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| DeviceVersion | 设备型号 | 设备型号 | Device Version | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |
| RatedVoltage | 额定电压 | 额定电压 | Rated Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedCurrent | 额定电流 | 额定电流 | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedFrequency | 额定频率 | 额定频率 | Rated Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| MaxCurrent | 最大电流 | 最大电流 | Max Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorFlag | 故障事件标志 | 故障事件标志 | ErrorFlag | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| PowerFactorC | C相功率因数 | C相功率因数 | PowerFactorC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorB | B相功率因数 | B相功率因数 | PowerFactorB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorAll | 总功率因数 | 总功率因数 | PowerFactorAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorA | A相功率因数 | A相功率因数 | PowerFactorA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Ic | C相电流 | C相电流 | Ic | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ActivePowerAll | 总有功功率 | 总有功功率 | ActivePowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ActivePowerB | B相有功功率 | B相有功功率 | ActivePowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ActivePowerC | C相有功功率 | C相有功功率 | ActivePowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ApparentEnergyAll | 总视在电能 | 总视在电能 | ApparentEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VAh |  |
| ApparentPowerA | A相视在功率 | A相视在功率 | ApparentPowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ApparentPowerAll | 总视在功率 | 总视在功率 | ApparentPowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ApparentPowerB | B相视在功率 | B相视在功率 | ApparentPowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ApparentPowerC | C相视在功率 | C相视在功率 | ApparentPowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Ia | A相电流 | A相电流 | Ia | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | B相电流 | B相电流 | Ib | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| ErrorDataD | 故障数据D | 故障数据D | ErrorDataD | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ActivePowerA | A相有功功率 | A相有功功率 | ActivePowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ReactivePowerA | A相无功功率 | A相无功功率 | ReactivePowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerAll | 总无功功率 | 总无功功率 | ReactivePowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerB | B相无功功率 | B相无功功率 | ReactivePowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerC | C相无功功率 | C相无功功率 | ReactivePowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Ua | A相电压 | A相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | B相电压 | B相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | C相电压 | C相电压 | Uc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uba | BA线电压 | BA线电压 | Uba | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| TempInB | B相进线端子温度 | B相进线端子温度 | TempInB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| ReactiveEnergyAll | 无功总电能 | 无功总电能 | ReactiveEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| TempInC | C相进线端子温度 | C相进线端子温度 | TempInC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Uac | AC线电压 | AC线电压 | Uac | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| ActiveEnergyAll | 有功总电能 | 有功总电能 | ActiveEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| PosActiveEnergy | 正向有功电能 | 正向有功电能 | PosActiveEnergy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| NegActiveEnergy | 反向有功电能 | 反向有功电能 | PosActiveEnergy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Frequency | 电压频率 | 电网频率 | Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| VoltageUnbalanceRate | 电压不平衡率 | 电压不平衡率 | VoltageUnbalanceRate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| CurrentUnbalanceRate | 电流不平衡率 | 电流不平衡率 | CurrentUnbalanceRate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| TempInA | A相进线端子温度 | A相进线端子温度 | TempInA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempOutA | A相出线端子温度 | A相出线端子温度 | TempOutA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| ApparentPowerDemandAll | 视在总需量 | 视在总需量 | ApparentPowerDemandAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| TempOutB | B相出线端子温度 | B相出线端子温度 | TempOutB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Ucb | CB线电压 | CB线电压 | Ucb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| TempOutC | C相出线端子温度 | C相出线端子温度 | TempOutC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| PosActivePowerDemandAll | 正向有功总需量 | 正向有功总需量 | PosActivePowerDemandAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| NegActivePowerDemandAll | 反向有功总需量 | 反向有功总需量 | NegActivePowerDemandAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| ErrorCode | 故障代码 | 故障代码 | ErrorCode | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ErrorTime | 故障时间 | 故障时间 | ErrorTime | DATETIME |  | R |  |  |
| ErrorDataA | 故障数据A | 故障数据A | ErrorDataA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ErrorDataB | 故障数据B | 故障数据B | ErrorDataB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ErrorDataC | 故障数据C | 故障数据C | ErrorDataC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ErrorRecord | 故障事件 | 故障事件 | ErrorRecord | ALARM | ErrorCode,ErrorDataA,ErrorDataB,ErrorDataC,ErrorDataD,ErrorTime,ErrorFlag | ErrorCode != 0000000000000000 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
