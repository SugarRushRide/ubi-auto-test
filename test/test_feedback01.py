#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_feedback01.py
@Desc    ：明细查看
@Author  ：Byleth
@Date    ：2025/4/25 17:43 
"""
import time

from pages.base_page import print_element_text_by_element
from pages.feedback_page import FeedbackPage


def test_feedback01(univ_page):
    page = FeedbackPage(univ_page)

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