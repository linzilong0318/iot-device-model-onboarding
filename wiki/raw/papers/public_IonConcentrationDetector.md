# public_IonConcentrationDetector

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_IonConcentrationDetector | 离子浓度检测仪 | 离子浓度检测仪 | Ion Concentration Detector | NORMAL | public |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| DeviceVersion | 设备型号 | 设备型号 | Device Version | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IonConcentration | 离子浓度值 | 离子浓度值 | IonConcentration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ppm |  |
| Temperature | 温度 | 温度 | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| TemperatureDeviation | 温度偏差值 | 温度偏差值 | TemperatureDeviation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| IonConcentrationDeviation | 离子浓度偏差值 | 离子浓度偏差值 | IonConcentrationDeviation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ppm |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
