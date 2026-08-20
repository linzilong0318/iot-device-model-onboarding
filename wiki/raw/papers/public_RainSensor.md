# public_RainSensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_RainSensor | 雨量传感器 |  | Rainfall Sensor | NORMAL | public |  |  |

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

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DayRainFall | 当日降雨量 |  | Daily rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| TotalRainfall | 总降雨量 |  | Total rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| InstantRainFall | 瞬时降雨量 |  | Instantaneous rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| LastDayRainFall | 昨日降雨量 |  | Yesterday's rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| HourRainFall | 小时降雨量 |  | Hourly rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| LastHourRainfall | 上小时降雨量 |  | Rainfall in the last hour | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| MaxRainFallPeriod | 最大降雨量时段 |  | Maximum rainfall time | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| MinRainfallPeriod | 最小降雨量时段 |  | Minimum rainfall time | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | h |  |
| MaxHourRainFall | 最大时段降雨量 |  | Maximum rainfall period | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| MinHourRainFall | 最小时段降雨量 |  | Minimum rainfall period | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
