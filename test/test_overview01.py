#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_overview01.py
@Desc    ：总体定位页面明细查看测试
@Author  ：Byleth
@Date    ：2025/4/18 15:03 
"""
import time

from pages.base_page import print_element_text_by_element
from pages.overview_page import OverviewPage


def test_overview01(univ_page):
    page = OverviewPage(univ_page)
    details = page.get_all_detail_elements()
    assert details, "Find anything."

    for idx, detail in enumerate(details):
        print(f"clicking {idx+1} element now")
        page.click_detail(detail)
        modal = page.wait_for_modal()
        modal_form = page.wait_for_modal_form()
        assert modal.is_displayed(), f"{idx+1} no found"
        assert page.is_modal_form_not_empty(), f"{idx+1} is empty"
        print_element_text_by_element(modal_form)
        page.close_modal()
        time.sleep(0.5)