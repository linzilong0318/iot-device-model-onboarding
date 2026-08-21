#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from pipeline_v2 import verify_main
    raise SystemExit(verify_main())

"""
交付物校验脚本(verify_output.py)—— 多 agent 流程的质量闸门
对生成的 Excel 做机器可检校验,失败即 fail-fast(exit 1),供校验 agent 调用。

本脚本是命令行入口，实际校验逻辑由 pipeline_v2.verify_main 实现
（调用 verify_model / verify_type / verify_point，含协议语义校验和 catalog 一致性校验）。

支持三类产物:
  --kind model   设备模型 Excel(分支 A)
  --kind type    设备类型 Excel(分支 B)
  --kind point   点表 Excel(需 --model 指定对应设备模型 Excel 做一致性比对)

用法:
  python verify_output.py --kind model  --xlsx <模型xlsx>
  python verify_output.py --kind type   --xlsx <类型xlsx>
  python verify_output.py --kind point  --xlsx <点表xlsx> --model <模型xlsx> --protocol <协议名>

退出码: 0=通过  1=有校验失败项
输出: JSON 格式的校验报告(同时打印到 stdout),含 passed/errors/warnings
"""
