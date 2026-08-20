# public_ElectricMeter_3P_V1_0_2

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ElectricMeter_3P_V1_0_2 | 三相电表 |  | Three-phase Meter | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EQt | 总无功电能 |  | Total Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| DeviceTime | 设备时间 |  | Equipment Time | DATETIME |  | RW |  |  |
| Ua | A相电压 |  | Phase A Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | B相电压 |  | Phase B Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | C相电压 |  | Phase C Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Un | 中性点对地电压 |  | Neutral Point to Ground Voltage | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uab | AB线电压 |  | Line Voltage AB | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | BC线电压 |  | Line Voltage BC | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uca | CA线电压 |  | Line Voltage CA | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ia | A相电流 |  | Phase A Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | B相电流 |  | Phase B Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | C相电流 |  | Phase C Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| In | 中性线电流 |  | Neutral Line Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| TempPhaseA | A相温度 |  | Phase A Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| EPt | 总有功电能 |  | Total Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEP | 组合有功总电能 |  | Total Combined Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEQ | 组合无功总电能 |  | Composite Reactive Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT1 | 组合有功费率1电能 |  | Composite Active Power Rate 1 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT2 | 组合有功费率2电能 |  | Composite Active Power Rate 2 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT3 | 组合有功费率3电能 |  | Composite Active Power Rate 3 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT4 | 组合有功费率4电能 |  | Composite Active Power Rate 4 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| ComEPT5 | 组合有功费率5电能 |  | Composite Active Power Rate 5 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI | 正向有功电能 |  | Import Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT1 | 正向有功费率1电能 |  | Forward Active Power Rate 1 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT2 | 正向有功费率2电能 |  | Forward Active Power Rate 2 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT3 | 正向有功费率3电能 |  | Active energy rate 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT4 | 正向有功费率4电能 |  | Active energy rate 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPIT5 | 正向有功费率5电能 |  | Active energy rate 5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE | 反向有功电能 |  | Export Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET1 | 反向有功费率1电能 |  | Reverse active energy rate 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET2 | 反向有功费率2电能 |  | Reverse active energy rate 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET3 | 反向有功费率3电能 |  | Reverse active energy rate 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET4 | 反向有功费率4电能 |  | Reverse active energy rate 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPET5 | 反向有功费率5电能 |  | Reverse active energy rate 5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Q1EQ | 第一象限无功总电能 |  | Total reactive energy quadrant 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQT1 | 第一象限无功费率1电能 |  | Quadrant 1 Reactive Power Rate 1 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQT2 | 第一象限无功费率2电能 |  | Quadrant 1 Reactive Power Rate 2 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQT3 | 第一象限无功费率3电能 |  | Quadrant 1 Reactive Power Rate 3 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q1EQT4 | 第一象限无功费率4电能 |  | Quadrant 1 Reactive Power Rate 4 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQ | 第二象限无功总电能 |  | Quadrant 2 Reactive Power Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQT1 | 第二象限无功费率1电能 |  | Quadrant 2 Reactive Power Rate 1 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQT2 | 第二象限无功费率2电能 |  | Quadrant 2 Reactive Power Rate 2 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQT3 | 第二象限无功费率3电能 |  | Quadrant 2 Reactive Power Rate 3 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQT4 | 第二象限无功费率4电能 |  | Quadrant 2 Reactive Power Rate 4 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQ | 第三象限无功总电能 |  | Quadrant 3 Reactive Power Total Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQT1 | 第三象限无功费率1电能 |  | Reactive energy rate 1 energy in quadrant 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQT2 | 第三象限无功费率2电能 |  | Reactive energy rate 2 energy in quadrant 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQT3 | 第三象限无功费率3电能 |  | Reactive energy rate 3 energy in quadrant 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQT4 | 第三象限无功费率4电能 |  | Reactive energy rate 4 energy in quadrant 3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQ | 第四象限无功总电能 |  | Total reactive energy in quadrant 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQT1 | 第四象限无功费率1电能 |  | Reactive energy rate 1 energy in quadrant 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQT2 | 第四象限无功费率2电能 |  | Reactive energy rate 2 energy in quadrant 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQT3 | 第四象限无功费率3电能 |  | Reactive energy rate 3 energy in quadrant 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQT4 | 第四象限无功费率4电能 |  | Reactive energy rate 4 energy in quadrant 4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQI | 正向无功电能 |  | Forward reactive energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EQE | 反向无功电能 |  | Reverse Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| EPI_PhaseA | A相正向有功电能 |  | Phase A Positive Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_PhaseB | B相正向有功电能 |  | Phase B Positive Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPI_PhaseC | C相正向有功电能 |  | Phase C Positive Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_PhaseA | A相反向有功电能 |  | Phase A Negative Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_PhaseB | B相反向有功电能 |  | Phase B Negative Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EPE_PhaseC | C相反向有功电能 |  | Phase C Negative Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQI_PhaseA | A相正向无功电能 |  | Phase A Positive Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQI_PhaseB | B相正向无功电能 |  | Phase B Positive Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQI_PhaseC | C相正向无功电能 |  | Phase C Positive Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQE_PhaseA | A相反向无功电能 |  | Phase A Negative Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQE_PhaseB | B相反向无功电能 |  | Phase B Negative Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| EQE_PhaseC | C相反向无功电能 |  | Phase C Negative Reactive Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPIT2 | （冻结）月费率2正向有功电能 |  | Frozen Monthly Rate 2 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPIT3 | （冻结）月费率3正向有功电能 |  | Frozen Monthly Rate 3 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPIT4 | （冻结）月费率4正向有功电能 |  | Frozen Monthly Rate for Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPIT5 | （冻结）月费率5正向有功电能 |  | (Frozen) Monthly Rate 5 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPET1 | （冻结）月费率1反向有功电能 |  | Frozen monthly rate 1 reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPET2 | （冻结）月费率2反向有功电能 |  | (Frozen) Monthly Rate 2 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPET3 | （冻结）月费率3反向有功电能 |  | (Frozen) Monthly Rate 3 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPET4 | （冻结）月费率4反向有功电能 |  | Monthly Rate 4 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPET5 | （冻结）月费率5反向有功电能 |  | Monthly Rate 5 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPIT1 | （冻结）日费率1正向有功电能 |  | (Frozen) Daily Rate 1 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPIT2 | （冻结）日费率2正向有功电能 |  | (Frozen) Daily Rate 2 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPIT3 | （冻结）日费率3正向有功电能 |  | (Frozen) Daily Rate 3 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPIT4 | （冻结）日费率4正向有功电能 |  | (Frozen) Daily Rate 4 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPIT5 | （冻结）日费率5正向有功电能 |  | (Frozen) Daily Rate 5 Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPET1 | （冻结）日费率1反向有功电能 |  | (Frozen) Daily Rate 1 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPET2 | （冻结）日费率2反向有功电能 |  | Frozen Daily Rate 2 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPET3 | （冻结）日费率3反向有功电能 |  | Daily Rate 3 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPET4 | （冻结）日费率4反向有功电能 |  | Daily Rate 4 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPET5 | （冻结）日费率5反向有功电能 |  | Daily Rate 5 Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| Pt | 总有功功率 |  | Total Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pa | A相有功功率 |  | Phase A Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pb | B相有功功率 |  | Phase B Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pc | C相有功功率 |  | Phase C Active Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Qt | 总无功功率 |  | Total Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qa | A相无功功率 |  | Phase A Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qb | B相无功功率 |  | Phase B Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qc | C相无功功率 |  | Phase C Reactive Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| St | 总视在功率 |  | Total Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sa | A相视在功率 |  | Phase A Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sb | B相视在功率 |  | Phase B Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sc | C相视在功率 |  | Phase C Apparent Power | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| PFt | 总功率因数 |  | Total Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFa | A相功率因数 |  | Phase A Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFb | B相功率因数 |  | Phase B Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFc | C相功率因数 |  | Phase C Power Factor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| THDUa | A相电压总谐波畸变率 |  | Phase A Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUb | B相电压总谐波畸变率 |  | Phase B Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUc | C相电压总谐波畸变率 |  | Phase C Voltage Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIa | A相电流总谐波畸变率 |  | Phase A Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIb | B相电流总谐波畸变率 |  | Phase B Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIc | C相电流总谐波畸变率 |  | Phase C Current Total Harmonic Distortion | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| FundamentalIa | A相电流基波值 |  | Phase A Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIa | A相电流谐波有效值 |  | Phase A Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIb | B相电流基波值 |  | Phase B Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIb | B相电流谐波有效值 |  | Phase B Current Harmonic RMS Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| FundamentalIc | C相电流基波值 |  | Phase C Current Fundamental Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| HarmonicRmsIc | C相电流谐波有效值 |  | Phase C Current Harmonic RMS | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| UUnB | 电压不平衡度 |  | Voltage Unbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| TempPhaseB | B相温度 |  | Phase B Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempPhaseC | C相温度 |  | Phase C Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempN | 中性线温度 |  | Neutral Line Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempCir1 | 第一路温度 |  | Channel 1 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempCir2 | 第二路温度 |  | Channel 2 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempCir3 | 第三路温度 |  | Channel 3 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TempCir4 | 第四路温度 |  | Channel 4 Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Freq | 电网频率 |  | Grid Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| MaxDmdEPI | 正向有功最大需量 |  | Maximum Forward Active Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| MaxDmdEPE | 反向有功最大需量 |  | Reverse Active Maximum Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| EnergyRemain | 剩余电量 |  | Remaining Battery | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| CreditRemain | 剩余金额 |  | Remaining Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| CreditTotal | 总购电金额 |  | Total Electricity Purchase Amount | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| VoltageRatio | 电压变比 |  | Voltage Ratio | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| CurrentRatio | 电流变比 |  | Current Ratio | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  |  |
| ClearE | 电能清零 |  | Energy Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| RemoteReset | 远方复位 |  | Remote Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| FactoryReset | 恢复出厂设置 |  | Restore Factory Settings | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  |  |
| Sta_Device | 设备状态 |  | Device Status | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"合闸",<br>				"en_US":"Close Circuit"<br>			},<br>			"itemValue":"合闸",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"分闸",<br>				"en_US":"Trip"<br>			},<br>			"itemValue":"分闸",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_Smoke | 烟感告警 |  | Smoke detector alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverVoltage | 过压告警 |  | Overvoltage alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderVoltage | 欠压告警 |  | Undervoltage alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverCurrent | 过载告警 |  | Overload alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverFreq | 过频告警 |  | Overfrequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UnderFreq | 欠频告警 |  | Under-frequency alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_PhaseLoss | 断相告警 |  | Phase failure alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_UUnB | 电压不平衡告警 |  | Voltage unbalance alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_IUnB | 电流不平衡告警 |  | Current unbalance alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevU | 电压逆序告警 |  | Voltage reverse sequence alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevP_PhaseA | A相有功功率反向告警 |  | Phase A Active Power Reverse Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevP_PhaseB | B相有功功率反向告警 |  | Phase B Active Power Reverse Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevP_PhaseC | C相有功功率反向告警 |  | Phase C Active Power Reverse Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_RevP | 总有功功率反向告警 |  | Reverse Power Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTempC1 | 第一路温度越限告警 |  | First Channel Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTempC2 | 第二路温度越限告警 |  | Second Channel Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTempC3 | 第三路温度越限告警 |  | Third Channel Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverTempC4 | 第四路温度越限告警 |  | Fourth Channel Temperature Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| Ala_OverIres | 剩余电流越限告警 |  | Residual Current Limit Alarm | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"正常",<br>				"en_US":"Normal"<br>			},<br>			"itemValue":"正常",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"异常",<br>				"en_US":"Abnormal"<br>			},<br>			"itemValue":"异常",<br>			"itemKey":"1"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| SeqU1 | 电压正序分量 |  | Voltage Positive Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU2 | 电压负序分量 |  | Voltage Negative Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| SeqU0 | 电压零序分量 |  | Voltage Zero Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| IUnB | 电流不平衡度 |  | Current Imbalance | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| SeqI1 | 电流正序分量 |  | Current Positive Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI2 | 电流负序分量 |  | Current Negative Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| SeqI0 | 电流零序分量 |  | Current Zero Sequence Component | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Q1EQT5 | 第一象限无功费率5电能 |  | First Quadrant Reactive Power Rate 5 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q2EQT5 | 第二象限无功费率5电能 |  | Quadrant 2 Reactive Power Rate 5 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q3EQT5 | 第三象限无功费率5电能 |  | Third Quadrant Reactive Power Rate 5 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| Q4EQT5 | 第四象限无功费率5电能 |  | Fourth Quadrant Reactive Power Rate 5 Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvarh |  |
| FroMonEPI | (冻结)月正向有功电能 |  | Frozen Monthly Forward Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPIT1 | （冻结）月费率1正向有功电能 |  | (Frozen) Monthly rate 1 forward active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroMonEPE | (冻结)月反向有功电能 |  | Frozen monthly reverse active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPI | (冻结)日正向有功电能 |  | Frozen daily active energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| FroDEPE | (冻结)日反向有功电能 |  | (Frozen) Daily Reverse Active Energy | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kWh |  |
| CurrentDmdP | 当前有功需量 |  | Current Active Demand | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| DI1 | 开关量输入1 |  | Digital Input 1 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI2 | 开关量输入2 |  | Digital Input 2 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI3 | 开关量输入3 |  | Digital input 3 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI4 | 开关量输入4 |  | Digital input 4 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI5 | 开关量输入5 |  | Digital input 5 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI6 | 开关量输入6 |  | Digital input 6 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI7 | 开关量输入7 |  | Digital input 7 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DI8 | 开关量输入8 |  | Digital input 8 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | R |  |  |
| DO1 | 开关量输出1 |  | Digital output 1 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO2 | 开关量输出2 |  | Digital Output 2 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO3 | 开关量输出3 |  | Digital Output 3 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| DO4 | 开关量输出4 |  | Digital Output 4 | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"1",<br>				"en_US":"1"<br>			},<br>			"itemValue":"1",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"0",<br>				"en_US":"0"<br>			},<br>			"itemValue":"0",<br>			"itemKey":"0"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} | W |  |  |
| Ires | 剩余电流 |  | Residual Current | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AlarmRevU | 电压逆序告警 |  | Voltage Reverse Sequence Alarm | ALARM | Ala_RevU | Ala_RevU = 1 |  |
| AlarmOverVoltage | 过压告警 |  | Overvoltage Alarm | ALARM | Ala_OverVoltage | Ala_OverVoltage = 1 |  |
| AlarmUnderVoltage | 欠压告警 |  | Undervoltage Alarm | ALARM | Ala_UnderVoltage | Ala_UnderVoltage = 1 |  |
| AlarmOverCurrent | 过载告警 |  | Overload Alarm | ALARM | Ala_OverCurrent | Ala_OverCurrent = 1 |  |
| AlarmOverFreq | 过频告警 |  | Frequent Alarm | ALARM | Ala_OverFreq | Ala_OverFreq = 1 |  |
| AlarmUnderFreq | 欠频告警 |  | Undervoltage Frequency Alarm | ALARM | Ala_UnderFreq | Ala_UnderFreq = 1 |  |
| AlarmPhaseLoss | 断相告警 |  | Phase Loss Alarm | ALARM | Ala_PhaseLoss | Ala_PhaseLoss = 1 |  |
| AlarmUUnB | 电压不平衡告警 |  | Voltage Imbalance Alarm | ALARM | Ala_UUnB | Ala_UUnB = 1 |  |
| AlarmIUnB | 电流不平衡告警 |  | Current Imbalance Alarm | ALARM | Ala_IUnB | Ala_IUnB = 1 |  |
| AlarmRevP_PhaseA | A相有功功率反向告警 |  | Phase A Active Power Reverse Alarm | ALARM | Ala_RevP_PhaseA | Ala_RevP_PhaseA = 1 |  |
| AlarmSmoke | 烟感告警 |  | Smoke Alarm | ALARM | Ala_Smoke | Ala_Smoke = 1 |  |
| AlarmRevP_PhaseB | B相有功功率反向告警 |  | Phase B Active Power Reverse Alarm | ALARM | Ala_RevP_PhaseB | Ala_RevP_PhaseB = 1 |  |
| AlarmRevP_PhaseC | C相有功功率反向告警 |  | Phase C Active Power Reverse Alarm | ALARM | Ala_RevP_PhaseC | Ala_RevP_PhaseC = 1 |  |
| Ala_RevP | 总有功功率反向告警 |  | Total Active Power Reverse Alarm | ALARM | Ala_RevP | Ala_RevP = 1 |  |
| AlarmOverTempC1 | 第一路温度越限告警 |  | Channel 1 Temperature Over-Limit Alarm | ALARM | Ala_OverTempC1 | Ala_OverTempC1 = 1 |  |
| AlarmOverTempC2 | 第二路温度越限告警 |  | Channel 2 Temperature Over-Limit Alarm | ALARM | Ala_OverTempC2 | Ala_OverTempC2 = 1 |  |
| AlarmOverTempC3 | 第三路温度越限告警 |  | Channel 3 Temperature Over-Limit Alarm | ALARM | Ala_OverTempC3 | Ala_OverTempC3 = 1 |  |
| AlarmOverTempC4 | 第四路温度越限告警 |  | Channel 4 Temperature Over-Limit Alarm | ALARM | Ala_OverTempC4 | Ala_OverTempC4 = 1 |  |
| AlarmOverIres | 剩余电流越限告警 |  | Residual Current Limit Alarm | ALARM | Ala_OverIres | Ala_OverIres = 1 |  |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| ClearECmd | 电能清零 |  | Energy Reset | ClearE |  |  |
| DO1Cmd | 开关量输出1控制 |  | Switch Output 1 Control | DO1 |  |  |
| DO2Cmd | 开关量输出2控制 |  | Switch Output 2 Control | DO2 |  |  |
| DO3Cmd | 开关量输出3控制 |  | Switch Output 3 Control | DO3 |  |  |
| DO4Cmd | 开关量输出4控制 |  | Digital Output 4 Control | DO4 |  |  |
| FactoryResetCmd | 恢复出厂设置 |  | Factory Reset | FactoryReset |  |  |
| RemoteResetCmd | 远方复位 |  | Remote Reset | RemoteReset |  |  |
