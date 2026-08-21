#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from pipeline_v2 import type_main, run
    raise SystemExit(run(type_main))

"""
生成设备类型 Excel(分支 B)—— 基于说明书四维度点位新建私有设备类型

本脚本是命令行入口，实际生成逻辑由 pipeline_v2.generate_type 实现
（含契约校验、点位分组校验、引用完整性校验、原子写入）。

输入:
  type_spec.json —— 设备类型配置(类型元信息 + 四维度点位全集)

输出:
  按模板 type_template.xlsx 结构生成的设备类型 xlsx

用法:
  python gen_device_type.py <type_spec.json> [输出路径覆盖]

铁律:
  - 内容全部来自用户文档(spec.points),标识符规范化(优先文档已有英文 ID,
    否则按语义译 CamelCase)。
  - 生成物 ID 一律 project_ 前缀;私有类型不回灌公有知识库。
  - 模板 type_template.xlsx 5 sheet,无 FromDeviceType(类型不引用其他类型)。
  - 列序与模型模板不同(DataDefine 在前、R/W 在后),按表头列名映射填充。

type_spec.json 结构:
{
  "template": "templates/type_template.xlsx",
  "output": "/opt/data/output/xxx_设备类型_yyyyMMdd.xlsx",
  "type": {
    "id": "project_xxx", "name": "...", "name_zh": "...", "name_en": "...",
    "category": "NORMAL", "domain": "配电", "desc": "...", "parent_type": ""
  },
  "points": {
    "Attribute": [{"*ID": "...", "*Name_default": "...", "*DataType": "...",
                   "DataDefine": "...", "Unit": "...", "*IsRequired": "False", "Desc": "..."}],
    "MeasurePoint": [{"*ID": "...", ..., "*R/W": "R", "Unit": "...", "Desc": "..."}],
    "Event": [{"*ID": "...", ..., "*EventType": "...", "*Output": "...", "*Condition": "...", "Desc": "..."}],
    "Service": [{"*ID": "...", ..., "*Input": "...", "Output": "...", "Desc": "..."}]
  }
}
"""
