# public_FireDetector

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_FireDetector | 火灾探测器 | 火灾探测器 | FireDetector | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| EquipmentType | 设备型号 | 设备型号 | Device Version | STRING |  |  | False |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PowerFactorC | C相功率因数 | C相功率因数 | PowerFactorC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorB | B相功率因数 | B相功率因数 | PowerFactorB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorAll | 总功率因数 | 总功率因数 | PowerFactorAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PowerFactorA | A相功率因数 | A相功率因数 | PowerFactorA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| UxZsUnbalFactor | 电压零序不平衡度 | 电压零序不平衡度 | UxZsUnbalFactor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ApparentEnergyAll | 总视在电能 | 总视在电能 | ApparentEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VAh |  |
| Frequency | 电网频率 | 电网频率 | Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| CurrentUnbalanceRate | 电流不平衡率 | 电流不平衡率 | CurrentUnbalanceRate | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PosActiveEnergy | 正向有功电能 | 正向有功电能 | PosActiveEnergy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| NegActiveEnergy | 反向有功电能 | 反向有功电能 | PosActiveEnergy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| PosReactiveEnergyAll | 正向无功总电能 | 正向无功总电能 | ReactiveEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| NegReactiveEnergyAll | 反向无功总电能 | 反向无功总电能 | NegReactiveEnergyAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| PosActivePowerDemandAll | 正向有功总需量 | 正向有功总需量 | PosActivePowerDemandAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| NegActivePowerDemandAll | 反向有功总需量 | 反向有功总需量 | NegActivePowerDemandAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| StateFire4 | 状态信号4 | 状态信号4 | StateFire4 | BITMAP |  | R |  |  |
| Ia | A相电流 | A相电流 | Ia | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | B相电流 | B相电流 | Ib | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | C相电流 | C相电流 | Ic | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ua | A相电压 | A相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | B相电压 | B相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | C相电压 | C相电压 | Uc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uac | AC线电压 | AC线电压 | Uac | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uba | BA线电压 | BA线电压 | Uba | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ucb | CB线电压 | CB线电压 | Ucb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| ActivePowerAll | 总有功功率 | 总有功功率 | ActivePowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ApparentPowerC | C相视在功率 | C相视在功率 | ApparentPowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ActivePowerB | B相有功功率 | B相有功功率 | ActivePowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ActivePowerC | C相有功功率 | C相有功功率 | ActivePowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| ReactivePowerAll | 总无功功率 | 总无功功率 | ReactivePowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerA | A相无功功率 | A相无功功率 | ReactivePowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerB | B相无功功率 | B相无功功率 | ReactivePowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ReactivePowerC | C相无功功率 | C相无功功率 | ReactivePowerC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ApparentPowerAll | 总视在功率 | 总视在功率 | ApparentPowerAll | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ApparentPowerA | A相视在功率 | A相视在功率 | ApparentPowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ApparentPowerB | B相视在功率 | B相视在功率 | ApparentPowerB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| IxZsUnbalFactor | 电流零序不平衡度 | 电流零序不平衡度 | IxZsUnbalFactor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ActivePowerA | A相有功功率 | A相有功功率 | ActivePowerA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| SysState1 | 状态信号1 | 状态信号1 | State1 | BITMAP |  | R |  |  |
| SysState2 | 状态信号2 | 状态信号2 | State2 | BITMAP |  | R |  |  |
| SysState3 | 状态信号3 | 状态信号3 | State3 | BITMAP |  | R |  |  |
| SysState4 | 状态信号4 | 状态信号4 | State4 | BITMAP |  | R |  |  |
| StateFire1 | 状态信号1 | 状态信号1 | StateFire1 | BITMAP |  | R |  |  |
| StateFire2 | 状态信号2 | 状态信号2 | StateFire2 | BITMAP |  | R |  |  |
| StateFire3 | 状态信号3 | 状态信号3 | StateFire3 | BITMAP |  | R |  |  |
| IR_Current | 剩余电流 | 剩余电流 | IR_Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
