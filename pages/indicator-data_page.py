#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：indicator-data_page.py
@Desc    ：全部指标页面
@Author  ：Byleth
@Date    ：2025/4/22 18:06 
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class IndicatorDataPage(BasePage):
    # 全部指标
    MISCELLANEOUS_INDICATORS = (By.XPATH, "//aside//li[@data-menu-id='/indicator-data']")
    # 总体表单
    TABLE = (By.XPATH, "//table[@class='vxe-table--body']")
    
    def __init__(self, driver):
        super().__init__(driver)

    # 跳转至全部指标页面
    def jump_to_miscellaneous_indicators(self):
        self.click(*self.MISCELLANEOUS_INDICATORS)



