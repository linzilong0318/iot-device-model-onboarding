#!/usr/bin/env python3
"""会话工作目录解析工具 —— 集中管理本技能产物的落盘位置。

约定：一次会话的所有中间产物（points/match/spec JSON）与最终 Excel
统一落盘到

    /opt/data/workspace/<sessionId>/

其中 sessionId 取自环境变量 HERMES_SESSION_ID；未设置时回退为 "default"。
工作目录根可用环境变量 HERMES_WORKSPACE_ROOT 覆盖，默认 /opt/data/workspace。

设计要点：
  - 单一来源：所有生成/校验脚本、以及主 agent / 子 agent 都通过本模块
    解析工作目录，避免产物散落各处。
  - 可覆盖：命令行或 spec.output 提供的显式输出路径优先于工作目录约定。
  - 幂等：ensure_workspace() 可重复调用，目录已存在时静默返回。
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# 工作目录根：可用环境变量覆盖，默认 /opt/data/workspace
WORKSPACE_ROOT_ENV = "HERMES_WORKSPACE_ROOT"
DEFAULT_WORKSPACE_ROOT = "/opt/data/workspace"
SESSION_ENV = "HERMES_SESSION_ID"
DEFAULT_SESSION = "default"


def workspace_root() -> Path:
    """返回工作目录根（不含 sessionId）。"""
    return Path(os.environ.get(WORKSPACE_ROOT_ENV, DEFAULT_WORKSPACE_ROOT))


def session_id() -> str:
    """返回当前会话 id（缺省回退 'default'）。"""
    return os.environ.get(SESSION_ENV, "").strip() or DEFAULT_SESSION


def session_workspace() -> Path:
    """返回当前会话工作目录 /opt/data/workspace/<sessionId>/。"""
    return workspace_root() / session_id()


def ensure_workspace() -> Path:
    """创建并返回会话工作目录（幂等）。"""
    path = session_workspace()
    path.mkdir(parents=True, exist_ok=True)
    return path


def resolve_out(path=None, basename=None) -> Path:
    """解析产物输出路径。

    输入：
      path     —— 显式路径（CLI 或 spec.output 提供的覆盖值），为空时用工作目录
      basename —— path 为空时使用的默认文件名
    输出：
      显式 path 原样返回；否则返回 ensure_workspace()/basename。
    """
    if path:
        return Path(path)
    return ensure_workspace() / (basename or "output")


def main() -> int:
    parser = argparse.ArgumentParser(description="泰无界物模型技能：会话工作目录解析")
    parser.add_argument("--mkdir", action="store_true",
                        help="创建会话工作目录后输出其路径")
    parser.add_argument("--print", dest="echo", action="store_true",
                        help="仅打印会话工作目录路径（不创建）")
    parser.add_argument("--root", action="store_true",
                        help="仅打印工作目录根（不含 sessionId）")
    args = parser.parse_args()
    if args.root:
        print(workspace_root())
    elif args.mkdir:
        print(ensure_workspace())
    else:
        print(session_workspace())
    return 0


if __name__ == "__main__":
    sys.exit(main())
