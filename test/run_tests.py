#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：run_tests.py
@Desc    ：描述
@Author  ：Byleth
@Date    ：2025/4/21 17:36 
"""
import glob
import pytest

def get_sorted_files(prefix):
    """按数字排序特定前缀的测试文件"""
    files = glob.glob(f"{prefix}*.py")
    return files

if __name__ == '__main__':
    test_files = []
    # test_files += get_sorted_files("test_overview")
    test_files += get_sorted_files("test_simulate")
    # test_files += get_sorted_files("test_indicator_data")

    pytest.main([
        "-v",
        *test_files
    ])