# public_PFC_Panel

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_PFC_Panel | 无功补偿柜 |  | Reactive Power Compensation Cabinet | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Group1 | Group1 | Group1 | Group1 | STRING |  | R |  |  |
| Group2 | Group2 | Group2 | Group2 | STRING |  | R |  |  |
| Sa_Load | 负载A相视在功率 | 负载A相视在功率 | Sa_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Qa | 源侧A相无功功率 | 源侧A相无功功率 | Qa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qb | 源侧B相无功功率 | 源侧B相无功功率 | Qb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qc | 源侧C相无功功率 | 源侧C相无功功率 | Qc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qa_Load | 负载A相无功功率 | 负载A相无功功率 | Qa_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qb_Load | 负载B相无功功率 | 负载B相无功功率 | Qb_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Qc_Load | 负载C相无功功率 | 负载C相无功功率 | Qc_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kvar |  |
| Ia_Comp | A相补偿电流 | A相补偿电流 | Ia_Comp | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib_Comp | B相补偿电流 | B相补偿电流 | Ib_Comp | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic_Comp | C相补偿电流 | C相补偿电流 | Ic_Comp | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Temp4 | 温度4 | 温度4 | Temp4 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Temp5 | 温度5 | 温度5 | Temp5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Temp6 | 温度6 | 温度6 | Temp6 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Temp2 | 温度2 | 温度2 | Temp2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Sb_Load | 负载B相视在功率 | 负载B相视在功率 | Sb_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sc_Load | 负载C相视在功率 | 负载C相视在功率 | Sc_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Pa_Load | 负载A相有功功率 | 负载A相有功功率 | Pa_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pb_Load | 负载B相有功功率 | 负载B相有功功率 | Pb_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Pc_Load | 负载C相有功功率 | 负载C相有功功率 | Pc_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Ua | 源侧A相电压 | 源侧A相电压 | Ua | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | 源侧B相电压 | 源侧B相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | 源侧C相电压 | 源侧C相电压 | Uc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Freq_A | 源侧A相频率 | 源侧A相频率 | Freq_A | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Freq_B | 源侧B相频率 | 源侧B相频率 | Freq_B | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| Freq_C | 源侧C相频率 | 源侧C相频率 | Freq_C | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |
| THDUa | 源侧A相THDU | 源侧A相THDU | THDUa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUb | 源侧B相THDU | 源侧B相THDU | THDUb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDUc | 源侧C相THDU | 源侧C相THDU | THDUc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Pb | 源侧B相有功功率 | 源侧B相有功功率 | Pb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Ia_Load | 负载A相电流 | 负载A相电流 | Ia_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib_Load | 负载B相电流 | 负载B相电流 | Ib_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic_Load | 负载C相电流 | 负载C相电流 | Ic_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| THDIa_Load | 负载A相THDI | 负载A相THDI | THDIa_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIb_Load | 负载B相THDI | 负载B相THDI | THDIb_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIc_Load | 负载C相THDI | 负载C相THDI | THDIc_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| PFa_Load | 负载A相功率因数 | 负载A相功率因数 | PFa_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFb_Load | 负载B相功率因数 | 负载B相功率因数 | PFb_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFc_Load | 负载C相功率因数 | 负载C相功率因数 | PFc_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Sa | 源侧A相视在功率 | 源侧A相视在功率 | Sa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sb | 源侧B相视在功率 | 源侧B相视在功率 | Sb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Sc | 源侧C相视在功率 | 源侧C相视在功率 | Sc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kVA |  |
| Pa | 源侧A相有功功率 | 源侧A相有功功率 | Pa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| Temp3 | 温度3 | 温度3 | Temp3 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Pc | 源侧C相有功功率 | 源侧C相有功功率 | Pc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kW |  |
| In | 源侧N线电流 | 源侧N线电流 | In | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| In_Load | 负载N线电流 | 负载N线电流 | In_Load | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ia | 源侧A相电流 | 源侧A相电流 | Ia | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | 源侧B相电流 | 源侧B相电流 | Ib | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | 源侧C相电流 | 源侧C相电流 | Ic | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| THDIa | 源侧A相THDI | 源侧A相THDI | THDIa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIb | 源侧B相THDI | 源侧B相THDI | THDIb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| THDIc | 源侧C相THDI | 源侧C相THDI | THDIc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| PFa | 源侧A相功率因数 | 源侧A相功率因数 | PFa | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFb | 源侧B相功率因数 | 源侧B相功率因数 | PFb | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| PFc | 源侧C相功率因数 | 源侧C相功率因数 | PFc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Temp1 | 温度1 | 温度1 | Temp1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
