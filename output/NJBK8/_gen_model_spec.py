#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 model_spec.json(设备模型配置)"""
import json
from pathlib import Path

BASE = Path(r"d:\项目\iot-device-model-onboarding")
OUT_DIR = BASE / "output" / "NJBK8"
POINTS = OUT_DIR / "points.json"
MATCH = OUT_DIR / "match.json"
SPEC = OUT_DIR / "model_spec.json"

data = json.loads(POINTS.read_text(encoding="utf-8"))
match = json.loads(MATCH.read_text(encoding="utf-8"))
points = data["points"]

# === select:从类型引用的点位(匹配上的) ===
select = {"Attribute": [], "MeasurePoint": [], "Event": [], "Service": []}
for k, v in match["matches"].items():
    if v.get("matched_type_id"):
        select[v["dim"]].append(v["matched_type_id"])

# === add:新增点位(类型中无,用户设备特有,筛选后纳入) ===
add = {"Attribute": [], "MeasurePoint": [], "Event": [], "Service": []}

# --- 新增测点:运行统计 + DI/DO 状态(筛除谐波/电流相位角/总功率,非核心) ---
# 运行统计测点
sys_measure_add = {
    "run_time_now": ("RunTimeNow", "本次运行时间", "INT", "s", "R"),
    "run_time_all": ("RunTimeAll", "总运行时间", "INT", "s", "R"),
    "start_number": ("StartNumber", "起动次数", "INT", "次", "R"),
    "trip_number": ("TripNumber", "脱扣次数", "INT", "次", "R"),
    "start_current_max": ("StartCurrentMax", "最大起动电流", "FLOAT", "A", "R"),
    "run_current_max": ("RunCurrentMax", "最大运行电流", "FLOAT", "A", "R"),
    "work_mode": ("WorkMode", "工作模式", "ENUM", "", "R"),
}
for p in points["MeasurePoint"]:
    if p["struct"] == "SYSTEM_PARAMETER" and p["source_var"] in sys_measure_add:
        sid, sname, dtype, unit, rw = sys_measure_add[p["source_var"]]
        enum = p.get("enum")
        dd = {"enum": enum} if enum else {"minValue": "", "maxValue": ""}
        add["MeasurePoint"].append({
            "*ID": sid, "*Name_default": sname, "Name_zh_CN": sname,
            "Name_en_US": sid, "*DataType": dtype,
            "DataDefine": dd, "*R/W": rw, "Unit": unit, "Desc": "",
        })

# DI/DO 状态测点(开关量监测,核心)
di_do_add = {
    "DI_state[0]": ("DI0", "DI0状态", "BOOL", "R"),
    "DI_state[1]": ("DI1", "DI1状态", "BOOL", "R"),
    "DI_state[2]": ("DI2", "DI2状态", "BOOL", "R"),
    "DI_state[3]": ("DI3", "DI3状态", "BOOL", "R"),
    "DI_state[4]": ("DI4", "DI4状态", "BOOL", "R"),
    "DI_state[5]": ("DI5", "DI5状态", "BOOL", "R"),
    "DO_state[0]": ("DO0", "DO0状态", "BOOL", "R"),
    "DO_state[1]": ("DO1", "DO1状态", "BOOL", "R"),
    "DO_state[2]": ("DO2", "DO2状态", "BOOL", "R"),
    "DO_state[3]": ("DO3", "DO3状态", "BOOL", "R"),
}
for p in points["MeasurePoint"]:
    if p["source_var"] in di_do_add:
        sid, sname, dtype, rw = di_do_add[p["source_var"]]
        add["MeasurePoint"].append({
            "*ID": sid, "*Name_default": sname, "Name_zh_CN": sname,
            "Name_en_US": sid, "*DataType": dtype,
            "DataDefine": {"minValue": "", "maxValue": ""},
            "*R/W": rw, "Unit": "", "Desc": "",
        })

# --- 新增属性:核心保护配置(筛除厂内参数/细分通讯配置) ---
# 选取关键保护使能与阈值(过载/短路/堵转/断相/不平衡/接地/漏电/过欠压)
core_protect_vars = {
    # 使能类(ENUM)
    "protect_en[ZT_INVVERSE_OVERLOAD]": ("ProtectEnInverseOverload", "反时限过载使能"),
    "protect_en[ZT_CONSTANT_OVERLOAD]": ("ProtectEnConstantOverload", "定时限过载使能"),
    "protect_en[ZT_SHORT_CIRCUIT]": ("ProtectEnShortCircuit", "短路使能"),
    "protect_en[ZT_LOCKEDROTOR]": ("ProtectEnLockedRotor", "堵转使能"),
    "protect_en[ZT_BLOCK]": ("ProtectEnBlock", "阻塞使能"),
    "protect_en[ZT_LACK]": ("ProtectEnLack", "断相使能"),
    "protect_en[ZT_CURRENT_IMBALANCE]": ("ProtectEnCurrentImbalance", "电流不平衡使能"),
    "protect_en[ZT_GROUND]": ("ProtectEnGround", "接地使能"),
    "protect_en[ZT_LEAKAGE]": ("ProtectEnLeakage", "漏电使能"),
    "protect_en[ZT_OVERVOLTAGE]": ("ProtectEnOverVoltage", "过电压使能"),
    "protect_en[ZT_UNDERVOLTAGE]": ("ProtectEnUnderVoltage", "欠电压使能"),
    "protect_en[ZT_PHASE]": ("ProtectEnPhase", "相序使能"),
    # 阈值类(INT/FLOAT)
    "protect_threshold[ZT_INVVERSE_OVERLOAD]": ("ProtectThresholdInverseOverload", "反时限过载启动门限值"),
    "protect_threshold[ZT_CONSTANT_OVERLOAD]": ("ProtectThresholdConstantOverload", "定时限过载脱扣门限值"),
    "protect_threshold[ZT_SHORT_CIRCUIT]": ("ProtectThresholdShortCircuit", "短路运行脱扣值"),
    "protect_threshold[ZT_LOCKEDROTOR]": ("ProtectThresholdLockedRotor", "堵转脱扣门限值"),
    "protect_threshold[ZT_BLOCK]": ("ProtectThresholdBlock", "阻塞脱扣门限值"),
    "protect_threshold[ZT_CURRENT_IMBALANCE]": ("ProtectThresholdCurrentImbalance", "电流不平衡脱扣门限值"),
    "protect_threshold[ZT_GROUND]": ("ProtectThresholdGround", "接地脱扣门限值"),
    "protect_threshold[ZT_LEAKAGE]": ("ProtectThresholdLeakage", "漏电脱扣门限值"),
    "protect_threshold[ZT_OVERVOLTAGE]": ("ProtectThresholdOverVoltage", "过电压脱扣门限值"),
    "protect_threshold[ZT_UNDERVOLTAGE]": ("ProtectThresholdUnderVoltage", "欠电压脱扣门限值"),
    # 延时类
    "protect_delay[ZT_CONSTANT_OVERLOAD]": ("ProtectDelayConstantOverload", "定时限过载脱扣延时"),
    "protect_delay[ZT_SHORT_CIRCUIT]": ("ProtectDelayShortCircuit", "短路脱扣延时"),
    "protect_delay[ZT_LOCKEDROTOR]": ("ProtectDelayLockedRotor", "堵转脱扣延时"),
    "protect_delay[ZT_BLOCK]": ("ProtectDelayBlock", "阻塞脱扣延时"),
    "protect_delay[ZT_LACK]": ("ProtectDelayLack", "断相脱扣延时"),
    "protect_delay[ZT_CURRENT_IMBALANCE]": ("ProtectDelayCurrentImbalance", "电流不平衡脱扣延时"),
    "protect_delay[ZT_GROUND]": ("ProtectDelayGround", "接地脱扣延时"),
    "protect_delay[ZT_LEAKAGE]": ("ProtectDelayLeakage", "漏电脱扣延时"),
    "protect_delay[ZT_OVERVOLTAGE]": ("ProtectDelayOverVoltage", "过电压脱扣延时"),
    "protect_delay[ZT_UNDERVOLTAGE]": ("ProtectDelayUnderVoltage", "欠电压脱扣延时"),
}
for p in points["Attribute"]:
    var = p["source_var"]
    if var in core_protect_vars:
        sid, sname = core_protect_vars[var]
        enum = p.get("enum")
        dtype = "ENUM" if enum else p["platform_dtype"]
        dd = {"enum": enum} if enum else {"minValue": "", "maxValue": ""}
        add["Attribute"].append({
            "*ID": sid, "*Name_default": sname, "Name_zh_CN": sname,
            "Name_en_US": sid, "*DataType": dtype,
            "DataDefine": dd, "Unit": p["unit"], "*IsRequired": "False", "Desc": "",
        })

# --- 新增事件:4 类记录(类型无事件) ---
# 事件 Output/Condition 引用的点位必须在模型全集中
# 跳闸记录:Output 引用故障相关;用 TripFlag 测点触发
# 简化:事件 Output 引用新增测点,Condition 用等式
events_def = [
    {
        "*ID": "TripRecord", "*Name_default": "跳闸记录", "Name_zh_CN": "跳闸记录",
        "Name_en_US": "Trip Record", "*EventType": "FAULT",
        "*Output": "TripNumber", "*Condition": "TripNumber=1", "Desc": "故障跳闸记录",
    },
    {
        "*ID": "AlarmRecord", "*Name_default": "告警记录", "Name_zh_CN": "告警记录",
        "Name_en_US": "Alarm Record", "*EventType": "ALARM",
        "*Output": "TripNumber", "*Condition": "TripNumber=2", "Desc": "告警记录",
    },
    {
        "*ID": "OperationRecord", "*Name_default": "操作记录", "Name_zh_CN": "操作记录",
        "Name_en_US": "Operation Record", "*EventType": "INFO",
        "*Output": "StartNumber", "*Condition": "StartNumber=1", "Desc": "操作记录",
    },
    {
        "*ID": "StateChangeRecord", "*Name_default": "状态变化记录", "Name_zh_CN": "状态变化记录",
        "Name_en_US": "State Change Record", "*EventType": "INFO",
        "*Output": "DI0", "*Condition": "DI0=1", "Desc": "DI/DO 状态变化记录(SOE)",
    },
]
add["Event"] = events_def

# --- 新增服务:10 个控制命令(类型无服务) ---
# 服务 Input 引用的点位必须在模型全集中;控制命令无 Input 依赖(直接下发)
services_def = [
    {"*ID": "Start1Cmd", "*Name_default": "起动1", "Name_zh_CN": "起动1", "Name_en_US": "Start1", "*Input": "", "Output": "", "Desc": "起动1控制命令"},
    {"*ID": "Start2Cmd", "*Name_default": "起动2", "Name_zh_CN": "起动2", "Name_en_US": "Start2", "*Input": "", "Output": "", "Desc": "起动2控制命令"},
    {"*ID": "StopCmd", "*Name_default": "停机", "Name_zh_CN": "停机", "Name_en_US": "Stop", "*Input": "", "Output": "", "Desc": "停机控制命令"},
    {"*ID": "ResetCmd", "*Name_default": "复位", "Name_zh_CN": "复位", "Name_en_US": "Reset", "*Input": "", "Output": "", "Desc": "复位控制命令"},
    {"*ID": "PowerClearCmd", "*Name_default": "电量清零", "Name_zh_CN": "电量清零", "Name_en_US": "PowerClear", "*Input": "", "Output": "", "Desc": "电量清零命令"},
    {"*ID": "EventClearCmd", "*Name_default": "事件总清", "Name_zh_CN": "事件总清", "Name_en_US": "EventClear", "*Input": "", "Output": "", "Desc": "事件总清命令"},
    {"*ID": "OperationClearCmd", "*Name_default": "运行信息清零", "Name_zh_CN": "运行信息清零", "Name_en_US": "OperationClear", "*Input": "", "Output": "", "Desc": "运行信息清零命令"},
    {"*ID": "ResetRunTimeoutCmd", "*Name_default": "复位运行超时", "Name_zh_CN": "复位运行超时", "Name_en_US": "ResetRunTimeout", "*Input": "", "Output": "", "Desc": "复位运行超时命令"},
    {"*ID": "ResetFaultNumberCmd", "*Name_default": "复位故障次数", "Name_zh_CN": "复位故障次数", "Name_en_US": "ResetFaultNumber", "*Input": "", "Output": "", "Desc": "复位故障次数命令"},
    {"*ID": "FlashClearCmd", "*Name_default": "恢复出厂", "Name_zh_CN": "恢复出厂", "Name_en_US": "FlashClear", "*Input": "", "Output": "", "Desc": "恢复出厂命令"},
]
add["Service"] = services_def

spec = {
    "raw_doc": str(BASE / "wiki" / "raw" / "papers" / "public_MotorProtector.md"),
    "template": str(BASE / "templates" / "model_template.xlsx"),
    "output": str(OUT_DIR / "NJBK8_设备模型_20260820.xlsx"),
    "model": {
        "id": "project_NJBK8",
        "name": "NJBK8马达保护器",
        "name_zh": "NJBK8马达保护器",
        "name_en": "NJBK8 Motor Protector",
        "device_type": "public_MotorProtector",
    },
    "select": select,
    "add": add,
}

SPEC.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
print("model_spec.json 已生成:", SPEC)
print(f"select: 属性 {len(select['Attribute'])} / 测点 {len(select['MeasurePoint'])} / 事件 {len(select['Event'])} / 服务 {len(select['Service'])}")
print(f"add:    属性 {len(add['Attribute'])} / 测点 {len(add['MeasurePoint'])} / 事件 {len(add['Event'])} / 服务 {len(add['Service'])}")
