#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：settings.py
@Desc    ：读取yaml信息
@Author  ：Byleth
@Date    ：2025/4/18 11:47 
"""

import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

class Config:
    def __init__(self, config_file=CONFIG_PATH):
        with open(config_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        self.credentials = data.get("credentials", {})
        self.browser = data.get("browser", {})

        # 默认值
        # 默认值设置
        if "timeout" not in self.browser:
            self.browser["timeout"] = 30
        if "window_size" not in self.browser:
            self.browser["window_size"] = {"width": 1920, "height": 1080}

config = Config()