#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from pipeline_v2 import model_main, run
    raise SystemExit(run(model_main))

"""
生成设备模型 Excel(分支 A)—— 从设备类型筛选点位 + 私有新增点位

本脚本是命令行入口，实际生成逻辑由 pipeline_v2.generate_model 实现
（含契约校验、引用补全、原子写入、catalog 生成）。

输入:
  model_spec.json  —— 设备模型配置(模型元信息 + SELECT 引用清单 + ADD 新增点位)
  raw 物模型文档   —— 引用点位的字段来源(类型标准定义)

输出:
  按模板 model_template.xlsx 结构生成的设备模型 xlsx
  同时生成同名 .catalog.json（点位清单，供点表生成器读取）

用法:
  python gen_device_model.py <model_spec.json> [输出路径覆盖]
  (model_spec.json 内可指定 raw_doc / template / output 路径,命令行参数优先)

铁律:
  - FromDeviceType 子表 = 从类型引用的点位清单(匹配上的类型点位);
    四张子表(Attribute/MeasurePoint/Event/Service)只能写 FromDeviceType 中
    未引用的【新增点位】,从类型引用的点位绝不重复写入四张子表。
  - 引用点位字段取自类型(raw 文档)标准定义;新增点位字段取自 spec(类型中无此点位)。
  - 生成物 ID 一律 project_ 前缀(public_ 仅用于引用知识库公有类型)。
  - 引用服务/事件的 Input/Output 依赖点位,生成器自动补入引用。

model_spec.json 结构:
{
  "raw_doc": "/opt/data/wiki/raw/papers/public_ElectricMeter_3P_V1_0_2.md",
  "template": "templates/model_template.xlsx",
  "output": "/opt/data/output/xxx_设备模型_yyyyMMdd.xlsx",
  "model": {
    "id": "project_xxx", "name": "...", "name_zh": "...", "name_en": "...",
    "device_type": "public_ElectricMeter_3P_V1_0_2"
  },
  "select": {
    "Attribute": ["SN", "ProductCategory"],
    "MeasurePoint": ["Ua", "Ub"],
    "Event": ["AlarmRevU"],
    "Service": ["ClearECmd"]
  },
  "add": {
    "Attribute": [{"*ID": "Net", "*Name_default": "...", "*DataType": "ENUM",
                   "DataDefine": "{...}", "Unit": "", "*IsRequired": "False", "Desc": "..."}],
    "MeasurePoint": [...],
    "Event": [],
    "Service": []
  }
}
"""
