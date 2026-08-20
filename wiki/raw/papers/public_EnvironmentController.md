# public_EnvironmentController

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_EnvironmentController | 环境控制器 | 环境控制器 | Environment Controller | NORMAL | distribution |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| EquipmentType | 设备型号 | 设备型号 | Device Version | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RelativeHumidity1 | 环境湿度1 | 环境湿度1 | Relative Humidity 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| Temperature1 | 环境温度1 | 环境温度1 | Temperature 1 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Temperature2 | 环境温度2 | 环境温度2 | Temperature 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| RelativeHumidity2 | 环境湿度2 | 环境湿度2 | Relative Humidity 2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| RelativeHumidity1HighLimit | 环境1湿度上限 | 环境1湿度上限 | Relative Humidity 1 High Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | %RH |  |
| Temperature1HighLimit | 环境1温度上限 | 环境1温度上限 | Temperature 1 High Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| Temperature1LowLimit | 环境1温度下限 | 环境1温度下限 | Temperature 1 Low Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| RelativeHumidity2HighLimit | 环境2湿度上限 | 环境2湿度上限 | Relative Humidity 2 High Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | %RH |  |
| Temperature2HighLimit | 环境2温度上限 | 环境2温度上限 | Temperature 2 High Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| Temperature2LowLimit | 环境2温度下限 | 环境2温度下限 | Temperature 2 Low Limit | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW | °C |  |
| States | 状态 | 状态 | States | BITMAP |  | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| SetRelativeHumidity1HighLimit | 设置环境1湿度上限 | 设置环境1湿度上限 | Set Relative Humidity 1 High Limit | RelativeHumidity1HighLimit |  |  |
| SetRelativeHumidity2HighLimit | 设置环境2湿度上限 | 设置环境2湿度上限 | Set Relative Humidity 2 High Limit | RelativeHumidity2HighLimit |  |  |
| SetTemperature1HighLimit | 设置环境1温度上限 | 设置环境1温度上限 | Set Temperature 1 High Limit | Temperature1HighLimit |  |  |
| SetTemperature1LowLimit | 设置环境1温度下限 | 设置环境1温度下限 | Set Temperature 1 Low Limit | Temperature1LowLimit |  |  |
| SetTemperature2HighLimit | 设置环境2温度上限 | 设置环境2温度上限 | Set Temperature 2 High Limit | Temperature2HighLimit |  |  |
| SetTemperature2LowLimit | 设置环境2温度下限 | 设置环境2温度下限 | Set Temperature 2 Low Limit | Temperature2LowLimit |  |  |
