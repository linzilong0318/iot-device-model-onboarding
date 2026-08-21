# 点表协议 profile

构造 `point_reg.json`、选择点表模板或诊断点表校验时阅读本文件。字段名大小写敏感，因为它们映射到工作簿表头。

| 协议族 | 识别的协议前缀 | 每行必填字段 | 定位字段 |
| --- | --- | --- | --- |
| Modbus | `Modbus...` | `address`、`registerCount`、`functionCode` | `address` |
| MQTT | `MQTT...` | `topic`、`jsonpath` | `topic` |
| OPC UA | `OPC UA...` / `OPCUA...` | `tag` | `tag` |
| IEC 104 | `IEC_104...` / `IEC104...` | `pointNum`、`pointType` | `pointNum` |
| DL/T 645 | `DL_T_645...` / `DLT645...` | `dataTag`、`dataLength`、`ctrlCode` | `dataTag` |
| DL/T 698 | `DL_T_698...` / `DLT698...` | `OAD`、`operationCode` | `OAD` |
| 网关 | `Gateway...` | `southSample` | `southSample` |

缺少任一必填字段的行在替换输出文件前就会报错。profile 之外的字段按工作簿表头名透传。

仓库当前的协议工作簿是单列占位（`pointName`）。对于这种已知形态，生成器会把第 1 行扩展为上表的标准 profile 列加上通用字段（`pointKey`、`unit`、`dataType`、`coefficient`、`map`、`wait`）。如果工作簿已有多列，则保留其真实表头，且必须包含 profile 的必填列。

## Modbus 语义

- `address` 在工作簿中为整数。spec 中可使用十进制或 `0x` 十六进制字符串。
- `registerCount` 为正整数。`u32`、`i32`、`float32` 至少需要两个 16 位寄存器；64 位值至少需要四个。
- 读功能码为 `01`、`02`、`03`、`04`；写功能码为 `05`、`06`、`0F`、`10`。可写的模型点位必须暴露写功能码。
- 寄存器范围不得重叠。共享位域仅当两行处于同一寄存器且提供不重叠的 `mask` 值时才允许。
- `mask` 接受正整数、十进制/十六进制字符串或非空位索引数组（如 `[6,7]`）。`map` 必须是 JSON 对象/数组或合法 JSON 字符串。字节/字序字段在所选模板提供时，必须从说明书中原样带入，不得推断。
