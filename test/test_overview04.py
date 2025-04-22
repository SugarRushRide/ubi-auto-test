#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_overview04.py
@Desc    ：最近发布版本切换校验
@Author  ：Byleth
@Date    ：2025/4/22 09:56 
"""
import time

def test_overview02(univ_page):
    page = univ_page
    page.click_version_select()
    page.change_version_published()
    details = page.get_all_detail_elements()
    assert details, "Find anything."
    print(f"change version success, published version.")
    time.sleep(2)