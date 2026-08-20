# public_GHISensor

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_GHISensor | 太阳总辐射传感器 |  | Solar Total Radiation Sensor | NORMAL | public |  |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | 设备SN |  | Device Serial Number | STRING |  |  | False |  |
| Manufacturer | 生产厂家 |  | Manufacturer | STRING |  |  | False |  |
| ProductCategory | 产品分类 |  | Product Category | STRING |  |  | False |  |
| ProductSeries | 产品系列 |  | Product Series | STRING |  |  | False |  |
| DeviceModel | 设备型号 |  | Device Model | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 |  | Software Version Number | STRING |  |  | False |  |
| HardwareVersion | 硬件版本号 |  | Hardware Version Number | STRING |  |  | False |  |
| InstallLocation | 安装位置 |  | Installation Location | STRING |  |  | False |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TotalRad | 总辐射瞬时值 |  | Total Radiation Instantaneous Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W/m² |  |
| DirectRad | 直接辐射瞬时值 |  | Direct Radiation Instantaneous Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W/m² |  |
| DiffuseRad | 散射辐射瞬时值 |  | Diffuse Radiation Instantaneous Value | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | W/m² |  |
| DaySunTime | 当日日照时长 |  | Daily Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalSunTime | 总日照时长 |  | Total Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| AvgSunTime | 平均日照时长 |  | Average Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| DayPeakSunTime | 当日日照峰值时长 |  | Daily Peak Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| TotalPeakSunTime | 总日照峰值时长 |  | Total Peak Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |
| AvgPeakSunTime | 平均日照峰值时长 |  | Average Peak Sunshine Duration | FLOAT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | min |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
