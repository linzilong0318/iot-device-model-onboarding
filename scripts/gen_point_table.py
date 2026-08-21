#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from pipeline_v2 import point_main, run
    raise SystemExit(run(point_main))

"""
生成点表 Excel(分支 A2)—— 基于设备模型 Excel + 寄存器映射,按通信协议选模板

本脚本是命令行入口，实际生成逻辑由 pipeline_v2.generate_point_table 实现
（含契约校验、协议语义校验、catalog 一致性校验、原子写入）。

输入:
  point_reg.json —— 点表配置(协议 + 模型路径 + 寄存器映射 pointKey -> 寄存器信息)
  设备模型 Excel —— pointKey/pointName/unit 的来源(平台按名称+标识符映射)
  模型 catalog  —— 同名 .catalog.json，由 gen_device_model.py 生成

输出:
  按协议模板(templates/<协议名>.xlsx)结构生成的点表 xlsx

用法:
  python gen_point_table.py <point_reg.json> [输出路径覆盖]

铁律:
  - pointName/pointKey/unit 与设备模型一致(从模型 catalog 读取),绝不从用户文档直抄。
  - address 必须十进制(支持 0x 十六进制自动转换);dataType 以 spec 为准,
    缺省时按模型数据类型推断并标注。
  - 以说明书为准:spec 中无寄存器信息的测点【不生成行】,进 todo 清单供总结告知用户。
  - 点表只收录测点(MeasurePoint)维度,属性/事件/服务不入表。
  - 按通信协议选模板:模板文件位于 templates/<协议名>.xlsx,各协议列定义不同,
    一律按目标模板表头列名映射填充,不硬编码列号。

point_reg.json 结构:
{
  "protocol": "ModbusTCP_Vega_ARM64_V1.1.0",
  "template": "templates/ModbusTCP_Vega_ARM64_V1.1.0.xlsx",
  "model_xlsx": "/opt/data/output/xxx_设备模型_yyyyMMdd.xlsx",
  "output": "/opt/data/output/xxx_点表_yyyyMMdd.xlsx",
  "rows": {
    "Ua": {"address": "0x0040", "registerCount": 2, "functionCode": "[03,00]",
           "dataType": "float32", "coefficient": null, "unit": "V"},
    "ClearE": {"address": "0x000D", "registerCount": 1, "functionCode": "[03,06]",
               "dataType": "u16"}
  }
}
说明:
  - rows 的 key 是模型 pointKey(与设备模型 MeasurePoint 的 *ID 一致)
  - address 支持 int 或 "0x..." 字符串(自动转十进制)
  - dataType 缺省时按模型 *DataType 推断(FLOAT->float32, INT->i32, ENUM->u16...)
  - rows 中不出现的 pointKey = 说明书无寄存器信息,进 todo 清单,不生成行
  - 各协议特有列(如 MQTT 的 topic/jsonpath、OPC UA 的 tag)直接在 rows[pointKey] 里
    按模板列名提供即可,脚本按表头列名透传
"""
