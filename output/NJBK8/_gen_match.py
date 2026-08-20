#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语义匹配:用户点位(points.json) vs 公有类型 public_MotorProtector
产出 match.json(每个用户点位 -> 命中类型标识符 / uncovered)
"""
import json
from pathlib import Path

BASE = Path(r"d:\项目\iot-device-model-onboarding")
POINTS = BASE / "output" / "NJBK8" / "points.json"
OUT = BASE / "output" / "NJBK8" / "match.json"

# public_MotorProtector 点位标识符 -> (中文名, 维度, 单位, 数据类型)
TYPE_POINTS = {
    # Attribute (14)
    "InstallLocation": ("安装位置", "Attribute", "", "STRING"),
    "DeviceVersion": ("设备型号", "Attribute", "", "STRING"),
    "SN": ("设备SN", "Attribute", "", "STRING"),
    "RatedVoltage": ("额定电压", "Attribute", "V", "FLOAT"),
    "RatedCurrent": ("额定电流", "Attribute", "A", "FLOAT"),
    "RatedCurrentType": ("额定电流规格", "Attribute", "", "FLOAT"),
    "RatedCurrentHigh": ("额定电流（高速）", "Attribute", "A", "FLOAT"),
    "RatedFrequency": ("额定频率", "Attribute", "Hz", "FLOAT"),
    "RatedPower": ("额定功率", "Attribute", "kW", "FLOAT"),
    "RatedPowerHigh": ("额定功率（高速）", "Attribute", "kW", "FLOAT"),
    "MotorType": ("电机类型", "Attribute", "", "STRING"),
    "Connection": ("接线方式", "Attribute", "", "STRING"),
    "CtScale": ("CT变比", "Attribute", "", "STRING"),
    "ProtectSelect": ("保护选择", "Attribute", "", "STRING"),
    # MeasurePoint (40)
    "Pc": ("C相有功功率", "MeasurePoint", "W", "FLOAT"),
    "PFb": ("B相功率因数", "MeasurePoint", "", "FLOAT"),
    "Qa": ("A相无功功率", "MeasurePoint", "var", "FLOAT"),
    "Qb": ("B相无功功率", "MeasurePoint", "var", "FLOAT"),
    "Qc": ("C相无功功率", "MeasurePoint", "var", "FLOAT"),
    "Sa": ("A相视在功率", "MeasurePoint", "VA", "FLOAT"),
    "Sb": ("B相视在功率", "MeasurePoint", "VA", "FLOAT"),
    "Sc": ("C相视在功率", "MeasurePoint", "VA", "FLOAT"),
    "PFa": ("A相功率因数", "MeasurePoint", "", "FLOAT"),
    "PFc": ("C相功率因数", "MeasurePoint", "", "FLOAT"),
    "Pa": ("A相有功功率", "MeasurePoint", "W", "FLOAT"),
    "PhaseAngleA": ("A相相位角", "MeasurePoint", "°", "FLOAT"),
    "PhaseAngleB": ("B相相位角", "MeasurePoint", "°", "FLOAT"),
    "PhaseAngleC": ("C相相位角", "MeasurePoint", "°", "FLOAT"),
    "FundamentalVa": ("A相电压基波值", "MeasurePoint", "V", "FLOAT"),
    "FundamentalVb": ("B相电压基波值", "MeasurePoint", "V", "FLOAT"),
    "FundamentalVc": ("C相电压基波值", "MeasurePoint", "V", "FLOAT"),
    "FundamentalIa": ("A相电流基波值", "MeasurePoint", "V", "FLOAT"),
    "FundamentalIb": ("B相电流基波值", "MeasurePoint", "V", "FLOAT"),
    "FundamentalIc": ("C相电流基波值", "MeasurePoint", "V", "FLOAT"),
    "LeakCurrent": ("漏电流", "MeasurePoint", "A", "FLOAT"),
    "Uca": ("CA线电压", "MeasurePoint", "V", "FLOAT"),
    "Ua": ("A相电压", "MeasurePoint", "V", "FLOAT"),
    "Ub": ("B相电压", "MeasurePoint", "V", "FLOAT"),
    "Uc": ("C相电压", "MeasurePoint", "V", "FLOAT"),
    "Un": ("中性点对地电压", "MeasurePoint", "V", "FLOAT"),
    "Ia": ("A相电流", "MeasurePoint", "A", "FLOAT"),
    "Ib": ("B相电流", "MeasurePoint", "A", "FLOAT"),
    "Ic": ("C相电流", "MeasurePoint", "A", "FLOAT"),
    "Uab": ("AB线电压", "MeasurePoint", "V", "FLOAT"),
    "Ubc": ("BC线电压", "MeasurePoint", "V", "FLOAT"),
    "GroundCurrent": ("接地电流", "MeasurePoint", "A", "FLOAT"),
    "Temp": ("温度", "MeasurePoint", "°C", "FLOAT"),
    "EP": ("总有功电能", "MeasurePoint", "kWh", "FLOAT"),
    "EPI_PhaseA": ("A相正向有功电能", "MeasurePoint", "kWh", "FLOAT"),
    "EPI_PhaseB": ("B相正向有功电能", "MeasurePoint", "kWh", "FLOAT"),
    "EPI_PhaseC": ("C相正向有功电能", "MeasurePoint", "kWh", "FLOAT"),
    "EQI_PhaseA": ("A相正向无功电能", "MeasurePoint", "kvarh", "FLOAT"),
    "EQI_PhaseB": ("B相正向无功电能", "MeasurePoint", "kvarh", "FLOAT"),
    "EQI_PhaseC": ("C相正向无功电能", "MeasurePoint", "kvarh", "FLOAT"),
}

# 用户测点语义 -> 类型标识符映射(基于名称语义 + 单位)
# POWER_PARAMETER 测量数据
MEASURE_MATCH = {
    "Total_AB_Voltage": ("Uab", "AB线电压->AB线电压,单位V一致"),
    "Total_BC_Voltage": ("Ubc", "BC线电压->BC线电压,单位V一致"),
    "Total_AC_Voltage": ("Uca", "CA线电压->CA线电压(AC即CA),单位V一致"),
    "LA_result->Voltage": ("Ua", "A相电压->A相电压,单位V一致"),
    "LB_result->Voltage": ("Ub", "B相电压->B相电压,单位V一致"),
    "LC_result->Voltage": ("Uc", "C相电压->C相电压,单位V一致"),
    "Voltage_N": ("Un", "N相电压->中性点对地电压,语义同指,单位V一致"),
    "LA_result->Current": ("Ia", "A相电流->A相电流,单位A一致"),
    "LB_result->Current": ("Ib", "B相电流->B相电流,单位A一致"),
    "LC_result->Current": ("Ic", "C相电流->C相电流,单位A一致"),
    "Total_Creepage": ("LeakCurrent", "漏电流->漏电流,语义同指(单位mA vs A,量纲同)"),
    "Current_Ground": ("GroundCurrent", "接地电流->接地电流,单位A一致"),
    "Total_Electric_Quantity": ("EP", "总电量->总有功电能,语义同指,单位KWh一致"),
    "LA_result->Active_Energy": ("EPI_PhaseA", "A有功电量->A相正向有功电能,语义同指,单位KWh一致"),
    "LB_result->Active_Energy": ("EPI_PhaseB", "B有功电量->B相正向有功电能,语义同指,单位KWh一致"),
    "LC_result->Active_Energy": ("EPI_PhaseC", "C有功电量->C相正向有功电能,语义同指,单位KWh一致"),
    "LA_result->Reactive_Energy": ("EQI_PhaseA", "A无功电量->A相正向无功电能,语义同指,单位KWh(类型为kvarh,量纲同)"),
    "LB_result->Reactive_Energy": ("EQI_PhaseB", "B无功电量->B相正向无功电能,语义同指"),
    "LC_result->Reactive_Energy": ("EQI_PhaseC", "C无功电量->C相正向无功电能,语义同指"),
    "Total_Active_Power": (None, "总有功功率:类型无总功率测点(类型只有分相 Pa/Pb/Pc),未覆盖"),
    "LA_result->Active_Power": ("Pa", "A相有功功率->A相有功功率(单位kvar vs W,文档单位标注有误,语义同指)"),
    "LB_result->Active_Power": (None, "B相有功功率:类型无 Pb 测点(类型缺B相有功),未覆盖"),
    "LC_result->Active_Power": ("Pc", "C相有功功率->C相有功功率(单位kvar vs W,文档单位标注有误,语义同指)"),
    "Total_Reactive_Power": (None, "总无功功率:类型无总无功测点,未覆盖"),
    "LA_result->Reactive_Power": ("Qa", "A相无功功率->A相无功功率,语义同指"),
    "LB_result->Reactive_Power": ("Qb", "B相无功功率->B相无功功率,语义同指"),
    "LC_result->Reactive_Power": ("Qc", "C相无功功率->C相无功功率,语义同指"),
    "Total_Apparent_Power": (None, "总视在功率:类型无总视在测点,未覆盖"),
    "LA_result->Apparent_Power": ("Sa", "A相视在功率->A相视在功率,语义同指"),
    "LB_result->Apparent_Power": ("Sb", "B相视在功率->B相视在功率,语义同指"),
    "LC_result->Apparent_Power": ("Sc", "C相视在功率->C相视在功率,语义同指"),
    "Total_Power_Factor": (None, "总功率因数:类型无总PF测点,未覆盖"),
    "LA_result->Power_Factor": ("PFa", "A相功率因数->A相功率因数,语义同指"),
    "LB_result->Power_Factor": ("PFb", "B相功率因数->B相功率因数,语义同指"),
    "LC_result->Power_Factor": ("PFc", "C相功率因数->C相功率因数,语义同指"),
    "LA_result->Angle[0]": ("PhaseAngleA", "A相相位角->A相相位角,语义同指"),
    "LB_result->Angle[0]": ("PhaseAngleB", "B相相位角->B相相位角,语义同指"),
    "LC_result->Angle[0]": ("PhaseAngleC", "C相相位角->C相相位角,语义同指"),
    "LA_result->Voltage_wave": ("FundamentalVa", "基波A相电压->A相电压基波值,语义同指"),
    "LB_result->Voltage_wave": ("FundamentalVb", "基波B相电压->B相电压基波值,语义同指"),
    "LC_result->Voltage_wave": ("FundamentalVc", "基波C相电压->C相电压基波值,语义同指"),
    "LA_result->Current_wave": ("FundamentalIa", "基波A相电流->A相电流基波值,语义同指"),
    "LB_result->Current_wave": ("FundamentalIb", "基波B相电流->B相电流基波值,语义同指"),
    "LC_result->Current_wave": ("FundamentalIc", "基波C相电流->C相电流基波值,语义同指"),
    "LA_result->harmonic_voltage": (None, "A相电压谐波:类型无谐波测点,未覆盖"),
    "LB_result->harmonic_voltage": (None, "B相电压谐波:类型无谐波测点,未覆盖"),
    "LC_result->harmonic_voltage": (None, "C相电压谐波:类型无谐波测点,未覆盖"),
    "LA_result->harmonic_current": (None, "A相电流谐波:类型无谐波测点,未覆盖"),
    "LB_result->harmonic_current": (None, "B相电流谐波:类型无谐波测点,未覆盖"),
    "LC_result->harmonic_current": (None, "C相电流谐波:类型无谐波测点,未覆盖"),
    "LA_result->harmonic_power": (None, "A相功率谐波:类型无谐波测点,未覆盖"),
    "LB_result->harmonic_power": (None, "B相功率谐波:类型无谐波测点,未覆盖"),
    "LC_result->harmonic_power": (None, "C相功率谐波:类型无谐波测点,未覆盖"),
    "DI_state[0]": (None, "DI0状态:类型无DI状态测点,未覆盖"),
    "DI_state[1]": (None, "DI1状态:类型无DI状态测点,未覆盖"),
    "DI_state[2]": (None, "DI2状态:类型无DI状态测点,未覆盖"),
    "DI_state[3]": (None, "DI3状态:类型无DI状态测点,未覆盖"),
    "DI_state[4]": (None, "DI4状态:类型无DI状态测点,未覆盖"),
    "DI_state[5]": (None, "DI5状态:类型无DI状态测点,未覆盖"),
    "DO_state[0]": (None, "DO0状态:类型无DO状态测点,未覆盖"),
    "DO_state[1]": (None, "DO1状态:类型无DO状态测点,未覆盖"),
    "DO_state[2]": (None, "DO2状态:类型无DO状态测点,未覆盖"),
    "DO_state[3]": (None, "DO3状态:类型无DO状态测点,未覆盖"),
    "LA_result->Angle[1]": (None, "A相电流相位角:类型无电流相位角测点(只有电压相位角),未覆盖"),
    "LB_result->Angle[1]": (None, "B相电流相位角:类型无电流相位角测点,未覆盖"),
    "LC_result->Angle[1]": (None, "C相电流相位角:类型无电流相位角测点,未覆盖"),
}

# SYSTEM_PARAMETER 运行测点
SYS_MEASURE_MATCH = {
    "run_time_now": (None, "本次运行时间:类型无运行时间测点,未覆盖"),
    "stop_time_now": (None, "本次停车时间:类型无停车时间测点,未覆盖"),
    "run_time_all": (None, "总运行时间:类型无总运行时间测点,未覆盖"),
    "stop_time_all": (None, "总停车时间:类型无总停车时间测点,未覆盖"),
    "start_number": (None, "起动次数:类型无起动次数测点,未覆盖"),
    "trip_number": (None, "脱扣次数:类型无脱扣次数测点,未覆盖"),
    "start_current_max": (None, "最大起动电流:类型无最大起动电流测点,未覆盖"),
    "run_current_max": (None, "最大运行电流:类型无最大运行电流测点,未覆盖"),
    "work_mode": (None, "工作模式:类型无工作模式测点,未覆盖"),
}

# 属性匹配(SYSTEM_PARAMETER 配置 + DEVICE_SET_PARAMETER + MANUFACTURER)
ATTR_MATCH = {
    # SYSTEM_PARAMETER 额定参数配置
    "rated_current_type": ("RatedCurrentType", "额定电流规格->额定电流规格,语义同指"),
    "rated_current": ("RatedCurrent", "额定电流->额定电流,单位A一致"),
    "rated_current_high": ("RatedCurrentHigh", "额定电流（高速）->额定电流（高速）,单位A一致"),
    "rated_voltage_type": ("RatedVoltage", "额定电压规格->额定电压(规格含电压值,语义同指,单位V)"),
    "rated_power": ("RatedPower", "额定功率->额定功率,单位KW vs kW一致"),
    "rated_power_high": ("RatedPowerHigh", "额定功率（高速）->额定功率（高速）,单位KW一致"),
    "rated_freq": ("RatedFrequency", "额定频率->额定频率,单位HZ vs Hz一致"),
    "motor_type": ("MotorType", "电机类型->电机类型,语义同指"),
    "connection": ("Connection", "接线方式->接线方式,语义同指"),
    "ct_scale": ("CtScale", "CT变比->CT变比,语义同指"),
    "protect_selec": ("ProtectSelect", "保护选择->保护选择,语义同指"),
}


def main():
    data = json.loads(POINTS.read_text(encoding="utf-8"))
    points = data["points"]

    match = {"recommend_type": "public_MotorProtector", "matches": {}}
    used_type_ids = set()

    # 测点匹配
    for p in points["MeasurePoint"]:
        var = p["source_var"]
        if p["struct"] == "POWER_PARAMETER":
            m = MEASURE_MATCH.get(var)
        else:
            m = SYS_MEASURE_MATCH.get(var)
        if m is None:
            match["matches"][f"MP::{var}"] = {
                "user_name": p["name"], "dim": "MeasurePoint",
                "uncovered": True, "basis": "未在映射表中(需人工确认)",
                "need_user_confirm": True,
            }
            continue
        tid, basis = m
        if tid is None:
            match["matches"][f"MP::{var}"] = {
                "user_name": p["name"], "dim": "MeasurePoint",
                "uncovered": True, "basis": basis,
            }
        else:
            # 同一类型点位不可重复计
            if tid in used_type_ids:
                match["matches"][f"MP::{var}"] = {
                    "user_name": p["name"], "dim": "MeasurePoint",
                    "uncovered": True, "basis": f"{basis}(类型点位 {tid} 已被其他点位占用)",
                    "need_user_confirm": True,
                }
            else:
                used_type_ids.add(tid)
                match["matches"][f"MP::{var}"] = {
                    "user_name": p["name"], "dim": "MeasurePoint",
                    "matched_type_id": tid, "basis": basis,
                }

    # 属性匹配
    for p in points["Attribute"]:
        var = p["source_var"]
        m = ATTR_MATCH.get(var)
        if m:
            tid, basis = m
            if tid in used_type_ids:
                match["matches"][f"AT::{var}"] = {
                    "user_name": p["name"], "dim": "Attribute",
                    "uncovered": True, "basis": f"{basis}(类型点位 {tid} 已被占用)",
                    "need_user_confirm": True,
                }
            else:
                used_type_ids.add(tid)
                match["matches"][f"AT::{var}"] = {
                    "user_name": p["name"], "dim": "Attribute",
                    "matched_type_id": tid, "basis": basis,
                }
        else:
            # 保护配置/通讯配置/DI/DO 配置/厂内参数 -> 类型无对应,未覆盖
            match["matches"][f"AT::{var}"] = {
                "user_name": p["name"], "dim": "Attribute",
                "uncovered": True, "basis": f"{p['struct']} 配置项,类型无对应属性",
                "inferred": p.get("inferred", False),
            }

    # 事件匹配:类型无事件 -> 全部未覆盖(但可新增)
    for p in points["Event"]:
        match["matches"][f"EV::{p['suggested_id']}"] = {
            "user_name": p["name"], "dim": "Event",
            "uncovered": True, "basis": "类型无事件定义(public_MotorProtector 事件为空)",
            "inferred": True,
        }

    # 服务匹配:类型无服务 -> 全部未覆盖(但可新增)
    for p in points["Service"]:
        match["matches"][f"SV::{p['suggested_id']}"] = {
            "user_name": p["name"], "dim": "Service",
            "uncovered": True, "basis": "类型无服务定义(public_MotorProtector 服务为空)",
        }

    # 统计
    stats = {"Attribute": {"covered": 0, "uncovered": 0},
             "MeasurePoint": {"covered": 0, "uncovered": 0},
             "Event": {"covered": 0, "uncovered": 0},
             "Service": {"covered": 0, "uncovered": 0}}
    for v in match["matches"].values():
        d = v["dim"]
        if v.get("uncovered"):
            stats[d]["uncovered"] += 1
        else:
            stats[d]["covered"] += 1
    match["stats"] = stats

    OUT.write_text(json.dumps(match, ensure_ascii=False, indent=2), encoding="utf-8")
    print("match.json 已生成:", OUT)
    print("\n四维度覆盖明细:")
    for d, s in stats.items():
        print(f"  {d}: 覆盖 {s['covered']} / 未覆盖 {s['uncovered']}")
    print(f"\n类型点位命中数(去重): {len(used_type_ids)}")


if __name__ == "__main__":
    main()
