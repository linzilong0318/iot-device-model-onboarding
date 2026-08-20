# public_ChintSDEdge

## BasicInfo

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Category | *Domain | Desc | ParentType |
| --- | --- | --- | --- | --- | --- | --- | --- |
| public_ChintSDEdge | ChintSDEdge |  |  | GATEWAY | public | 111 |  |

## Attribute

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | Unit | *IsRequired | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EdgeType | Edge系列 | Edge系列 | EdgeType | ENUM | {<br>	"mappingItemList":[<br>		{<br>			"itemI18nValue":{<br>				"default":"EchoGate",<br>				"en_US":"EchoGate",<br>				"zh_CN":"EchoGate"<br>			},<br>			"itemValue":"EchoGate",<br>			"itemKey":"0"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"VegaGate",<br>				"en_US":"VegaGate",<br>				"zh_CN":"VegaGate"<br>			},<br>			"itemValue":"VegaGate",<br>			"itemKey":"1"<br>		},<br>		{<br>			"itemI18nValue":{<br>				"default":"TitanGate",<br>				"en_US":"TitanGate",<br>				"zh_CN":"TitanGate"<br>			},<br>			"itemValue":"TitanGate",<br>			"itemKey":"2"<br>		}<br>	],<br>	"enumKeyCode":"INT"<br>} |  | True |  |
| SN | SN |  |  | STRING |  |  | False |  |
| InstallLocation | 安装地址 | 安装地址 | InstallLocation | STRING |  |  | False |  |
| SoftwareVersion | 软件版本号 | 软件版本号 | SoftwareVersion | STRING |  |  | True |  |
| HardwareVersion | 硬件版本号 | 硬件版本号 | HardwareVersion | STRING |  |  | True |  |
| SubCode | 子型号 | 子型号 | SubCode | STRING |  |  | True |  |

## MeasurePoint

| *ID | *Name_default | Name_zh_CN | Name_en_US | *DataType | DataDefine | *R/W | Unit | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WifiSpec | WifiSpec | WiFi硬件规格 | WifiSpec | STRING |  | R |  |  |
| WifiApSsid | WifiApSsid | 网关热点名称 | WifiApSsid | STRING |  | RW |  |  |
| CPUCores | CPUCores | CPU核心数 | CPUCores | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| MemorySize | MemorySize | 内存大小 | MemorySize | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | MB |  |
| DiskSize | DiskSize | 磁盘大小 | DiskSize | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | MB |  |
| CPU | CPU | CPU占用率 | CPU | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Memory | Memory | 内存占用率 | Memory | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| Disk | Disk | 磁盘占用率 | Disk | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | % |  |
| CPUProcessTop10 | CPUProcessTop10 | 前10进程CPU各自占比 | CPUProcessTop10 | STRING |  | R |  |  |
| EdgeIP | EdgeIP | 当前上网IP | EdgeIP | STRING |  | R |  |  |
| EthMac | EthMac | 当前上网MAC地址 | EthMac | STRING |  | R |  |  |
| DNS | DNS | DNS服务器 | DNS | STRING |  | RW |  |  |
| ServerMode | ServerMode | ModbusTcp模式 | ServerMode | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  | 0：关闭<br>1：tcp<br>2：tcptls |
| WifiApPwd | WifiApPwd | 网关热点密码 | WifiApPwd | STRING |  | RW |  |  |
| WifiStaSsid | WifiStaSsid | Station ssid | WifiStaSsid | STRING |  | R |  |  |
| Priority | Priority | 上网方式优先级设置 | Priority | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  | 1：ETH<br>2：Wi-Fi<br>3：移动网络 |
| WifiStaRssi | WifiStaRssi | 作为Station时信号强度 | WifiStaRssi | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| CellularSpec | CellularSpec | 4G硬件规格 | CellularSpec | STRING |  | R |  |  |
| CellularRssi | CellularRssi | 4G信号强度 | CellularRssi | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| CellularNumber | CellularNumber | 4G卡号 | CellularNumber | STRING |  | R |  |  |
| ServerCard | ServerCard | ModbusTcp绑定网卡 | ServerCard | STRING |  | R |  |  |
| ServerCardServerCard | ServerCardServerCard | ModbusTcp端口 | ServerCardServerCard | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  |  |
| Led | Led | led控制 | Led | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  | 0：灭<br>1：亮 |
| Reset | Reset | 复位 | Reset | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | W |  | 1：重启<br>2：重置（恢复出厂设置） |
| Log | Log | log开关 | Log | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  | 0：关闭<br>1：debug<br>2：info<br>3: warning<br>4: fault |
| HttpClientMode | HttpClientMode | http模式 | HttpClientMode | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | RW |  | 0：关闭<br>1：http<br>2：https |
| Connection | Connection | 当前上网方式 | Connection | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R |  | 1：ETH<br>2：Wi-Fi<br>3：移动网络 |
| CpuClockSpeed | CpuClockSpeed | CPU主频 | CpuClockSpeed | INT | {<br>	"minValue":"",<br>	"maxValue":""<br>} | R | MHz |  |
| Hardware | HardwareVersion | 当前硬件版本 | HardwareVersion | STRING |  | R |  |  |
| Firmware | FirmwareVersion | 当前固件版本 | FirmwareVersion | STRING |  | R |  |  |
| Software | Software | 当前软件版本 | Software | STRING |  | R |  |  |

## Event

| *ID | *Name_default | Name_zh_CN | Name_en_US | *EventType | *Output | *Condition | Desc |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Service

| *ID | *Name_default | Name_zh_CN | Name_en_US | *Input | Output | Desc |
| --- | --- | --- | --- | --- | --- | --- |
| LedCmd | LedCmd |  |  | Led |  |  |
| setHttpClientMode | setHttpClientMode |  |  | HttpClientMode |  |  |
| SetLog | SetLog |  |  | Log |  |  |
| SetReset | SetReset |  |  | Reset |  |  |
