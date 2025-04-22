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

if __name__ == '__main__':
    test_files = glob.glob("test_overview*.py")
    # [
    #     "test_overview01.py",
    #     "test_overview02.py"
    # ]
    pytest.main([
        "-v",
        *test_files
    ])