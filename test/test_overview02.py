#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_overview02.py
@Desc    ：最近历史版本切换校验
@Author  ：Byleth
@Date    ：2025/4/21 10:29 
"""
import time

from pages.overview_page import OverviewPage


def test_overview02(univ_page):
    page = OverviewPage(univ_page)
    page.click_version_select()
    page.change_version_previous()
    details = page.get_all_detail_elements()
    assert details, "Find anything."
    print(f"change version success, previous version")
    time.sleep(2)