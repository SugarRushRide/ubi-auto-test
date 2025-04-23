#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：simulate_page.py
@Desc    ：ARWU推演页面
@Author  ：Byleth
@Date    ：2025/4/22 10:41 
"""
from pages.base_page import BasePage


class SimulatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)