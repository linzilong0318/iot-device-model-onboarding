# public_WeatherStation

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_WeatherStation | 气象站 | 气象站 | ​Weather Station | NORMAL | public |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InstallLocation | 安装位置 | 安装位置 | Install Location | STRING |  |  | False |  |
| DeviceVersion | 设备型号 | 设备型号 | Device Version | STRING |  |  | True |  |
| SN | 设备SN | 设备SN | SN | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WindSpeed | 风速值 | 风速值 | WindSpeed | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | m/s |  |
| WindPower | 风力 | 风力 | WindPower | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| WindDirection | 风向 | 风向 | WindDirection | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ° |  |
| Humidity | 湿度值 | 湿度值 | Humidity | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | %RH |  |
| Temperature | 温度值 | 温度值 | Temperature | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | °C |  |
| Noise | 噪声值 | 噪声值 | Noise | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | dB |  |
| PM2_5 | PM2.5值 | PM2.5值 | PM2.5 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | μg/m³ |  |
| PM10 | PM10值 | PM10值 | PM10 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | μg/m³ |  |
| CO2 | CO2值 | CO2值 | CO2 | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ppm |  |
| AtmosphericPressure | 大气压值 | 大气压值 | AtmosphericPressure | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | kPa |  |
| HighLuxValueFor20W | 20W的Lux值高16位值 | 20W的Lux值高16位值 | HighLuxValueFor20W | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Lux |  |
| LowLuxValueFor20W | 20W的Lux值低16位值 | 20W的Lux值低16位值 | LowLuxValueFor20W | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Lux |  |
| IlluminationFor20W | 20W的光照值 | 20W的光照值 | IlluminationFor20W | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | Lux |  |
| Rainfall | 雨量值 | 雨量值 | Rainfall | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | mm |  |
| ElectronicCompassAngle | 电子指南针角度 | 电子指南针角度 | ElectronicCompassAngle | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | ° |  |
| TotalSolarRadiation | 太阳总辐射值 | 太阳总辐射值 | TotalSolarRadiation | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W/m² |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
