# public_MotorProtector

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_MotorProtector | 马达保护器 | 马达保护器 | Motor Protector | NORMAL | public |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| DeviceVersion | 设备型号 | 设备型号 | Device Version | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |
| RatedVoltage | 额定电压 | 额定电压 | Rated Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | V | False |  |
| RatedCurrent | 额定电流 | 额定电流 | Rated Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedCurrentType | 额定电流规格 | 额定电流规格 | RatedCurrentType | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} |  | False |  |
| RatedCurrentHigh | 额定电流（高速） | 额定电流（高速） | RatedCurrentHigh | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | A | False |  |
| RatedFrequency | 额定频率 | 额定频率 | RatedFrequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | Hz | False |  |
| RatedPower | 额定功率 | 额定功率 | RatedPower | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kW | False |  |
| RatedPowerHigh | 额定功率（高速） | 额定功率（高速） | RatedPowerHigh | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | kW | False |  |
| MotorType | 电机类型 | 电机类型 | MotorType | STRING |  |  | False |  |
| Connection | 接线方式 | 接线方式 | Connection | STRING |  |  | False |  |
| CtScale | CT变比 | CT变比 | CtScale | STRING |  |  | False |  |
| ProtectSelect | 保护选择 | 保护选择 | ProtectSelect | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pc | C相有功功率 | C相有功功率 | Phase C Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| PFb | B相功率因数 | B相功率因数 | Phase B Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Qa | A相无功功率 | A相无功功率 | A Phase Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Qb | B相无功功率 | B相无功功率 | Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Qc | C相无功功率 | C相无功功率 | Phase C Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| Sa | A相视在功率 | A相视在功率 | Phase A Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Sb | B相视在功率 | B相视在功率 | Phase B apparent power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| Sc | C相视在功率 | C相视在功率 | Phase C Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| PFa | A相功率因数 | A相功率因数 | Phase A power factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFc | C相功率因数 | C相功率因数 | C phase power factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Pa | A相有功功率 | A相有功功率 | Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| PhaseAngleA | A相相位角 | A相相位角 | Phase A Phase Angle | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ° |  |
| PhaseAngleB | B相相位角 | B相相位角 | Phase B Phase Angle | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ° |  |
| PhaseAngleC | C相相位角 | C相相位角 | C phase phase angle | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ° |  |
| FundamentalVa | A相电压基波值 | A相电压基波值 | A Phase Fundamental Voltage Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| FundamentalVb | B相电压基波值 | B相电压基波值 | Phase B fundamental voltage value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| FundamentalVc | C相电压基波值 | C相电压基波值 | C phase fundamental voltage value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| FundamentalIa | A相电流基波值 | A相电流基波值 | Phase A fundamental current value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| FundamentalIb | B相电流基波值 | B相电流基波值 | Phase B Fundamental Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| FundamentalIc | C相电流基波值 | C相电流基波值 | Phase C Fundamental Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| LeakCurrent | 漏电流 | 漏电流 | Leakage current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uca | CA线电压 | CA线电压 | CA Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ua | A相电压 | A相电压 | A Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | B相电压 | B相电压 | B Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | C相电压 | C相电压 | C Phase Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Un | 中性点对地电压 | 中性点对地电压 | Neutral Point to Ground Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ia | A相电流 | A相电流 | A Phase Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | B相电流 | B相电流 | B Phase Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | C相电流 | C相电流 | Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Uab | AB线电压 | AB线电压 | AB Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 | BC线电压 | BC Line Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| GroundCurrent | 接地电流 | 接地电流 | Ground Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Temp | 温度 | 温度 | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| EP | 总有功电能 | 总有功电能 | Total active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_PhaseA | A相正向有功电能 | A相正向有功电能 | Phase A forward active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_PhaseB | B相正向有功电能 | B相正向有功电能 | Phase B forward active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_PhaseC | C相正向有功电能 | C相正向有功电能 | C Phase Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQI_PhaseA | A相正向无功电能 | A相正向无功电能 | Phase A forward reactive energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI_PhaseB | B相正向无功电能 | B相正向无功电能 | Phase B Forward Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI_PhaseC | C相正向无功电能 | C相正向无功电能 | Phase C forward reactive energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
