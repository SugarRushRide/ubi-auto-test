#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：common.py
@Desc    ：工具类
@Author  ：Byleth
@Date    ：2025/4/25 13:32 
"""
import re

def extract_number(text:str) -> float:
    """
    从字符串中提取第一个浮点数或整数
    :param text: 输入字符串，如 "当前得分：43.8"
    :return: 提取到的数值，默认返回 0.0
    """
    match = re.search(r"\d+\.?\d*", text)
    return float(match.group()) if match else 0.0