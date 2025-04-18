#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：base_page.py
@Desc    ：封装所有页面基本操作
@Author  ：Byleth
@Date    ：2025/4/18 14:22 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """等待元素可见"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def click(self, by, value):
        """点击元素"""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        """文本输入"""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        """获取元素文本"""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        return element.text

    def is_element_present(self, by, value):
        """检查元素是否存在"""
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False

    def find_elements(self, by, value):
        """寻找元素集"""
        self.wait_for_element(by, value)
        return self.driver.find_elements(by, value)