#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：feedback_page.py
@Desc    ：数据反馈页面
@Author  ：Byleth
@Date    ：2025/4/25 15:53 
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FeedbackPage(BasePage):
    # 数据反馈页面
    FEEDBACK = (By.XPATH, "//aside//li[@data-menu-id='/data-feedback']")
    # 页面加载监测元素
    CHECK_ELEMENT = (By.XPATH, "(//span[@class='custom-name'])[1]")
    # 表头
    TABLE_HEADER = (By.CLASS_NAME, "vxe-header--row")
    # 表
    TABLE = (By.XPATH, "//table[@class='vxe-table--body']")
    # 行
    ROW = (By.CLASS_NAME, "vxe-body--row")

    def __init__(self, driver):
        super().__init__(driver)

    def _get_ready_locator(self):
        return self.CHECK_ELEMENT

    def jump_to_feedback(self):
        self.click(*self.FEEDBACK)

    # 获取

