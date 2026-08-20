# public_PWZB

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_PWZB | 微机保护装置 | 微机保护装置 | PWZB | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| DeviceVersion | 设备型号 | 设备型号 | Device Model | STRING |  |  | True |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PowerFactor | 功率因数 | 功率因数 | PowerFactor | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| ApparentPower | 视在功率 | 视在功率 | ApparentPower | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | VA |  |
| ReactivePower | 无功功率 | B相无功功率 | ReactivePower | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | var |  |
| ActivePowe | 有功功率 | 有功功率 | ActivePowe | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W |  |
| Ia | A相电流 | A相电流 | Ia | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ib | B相电流 | B相电流 | Ib | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ic | C相电流 | C相电流 | Ic | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | A |  |
| Ua | A相电压 | A相电压 | Ua | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ub | B相电压 | B相电压 | Ub | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uc | C相电压 | C相电压 | Uc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uab | A、B相线电压 | A、B相线电压 | Uab | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Ubc | B、C相线电压 | B、C相线电压 | Ubc | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Uca | C、A相线电压 | C、A相线电压 | Uca | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | V |  |
| Frequency | 频率 | 频率 | Frequency | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Hz |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
