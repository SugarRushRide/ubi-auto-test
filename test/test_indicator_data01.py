#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_indicator_data01.py
@Desc    ：全部指标明细查看
@Author  ：Byleth
@Date    ：2025/4/24 09:41 
"""
import time
from pages.indicator_data_page import IndicatorDataPage
from pages.base_page import print_element_text_by_element


def test_indicator_data01(univ_page):
    page = IndicatorDataPage(univ_page)
    page.jump_to_miscellaneous_indicators()
    page.wait_for_page_ready()
    details = page.get_all_detail_elements()
    print(details)
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
        print(f"Success, overview page, detail of published version exist")
        time.sleep(0.5)