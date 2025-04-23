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


def print_element_text_by_element(element):
    """直接打印传入 element 的文本"""
    try:
        text = element.text.strip()
        if not text:
            text = element.get_attribute("value")
        print(f"元素文本内容: {text}")
        return text
    except Exception as e:
        print(f"获取元素文本失败: {e}")
        return None


class BasePage:
    # 明细检验
    DETAIL_DATA = (By.CLASS_NAME, "ind-detail")
    MODAL = (By.CLASS_NAME, "detail-layout")
    MODAL_FORM = (By.CLASS_NAME, "ant-table-tbody")
    CLOSE_BUTTON = (By.CLASS_NAME, "ant-modal-close")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """等待元素可见"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def click(self, by, value):
        """点击元素"""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()
        # self.driver.execute_script("arguments[0].click();", element)

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

    def print_element_test(self, by, value):
        """打印元素及其子元素文本"""
        self.wait_for_element(by, value)
        try:
            element = self.driver.find_element(by, value)
            text = element.text.strip()
            if not text:
                # 可能是输入框等
                text = element.get_attribute("value")
            print(f"text: {text}")
            return text
        except Exception as e:
            print(f"get text failed: {e}")
            return None

    def get_all_detail_elements(self):
        """获取所有有明细的元素"""
        return self.find_elements(*self.DETAIL_DATA)

    def click_detail(self, element):
        # self.scroll_into_view(element)
        element.click()

    def wait_for_modal(self):
        try:
            return self.wait_for_element(*self.MODAL, timeout=15)
        except Exception as e:
            raise Exception("Modal did not appear.") from e
        # try:
        #     modal = WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located(self.MODAL)
        #     )
        #     return modal
        # except Exception as e:
        #     raise Exception("Modal did not appear.") from e

    def wait_for_modal_form(self):
        try:
            return self.wait_for_element(*self.MODAL_FORM, timeout=15)
        except Exception as e:
            raise Exception("Modal did not appear.") from e

    def is_modal_form_not_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(*self.MODAL_FORM).text.strip() != ""
            )
            return True
        except:
            return False

    def close_modal(self):
        self.click(*self.CLOSE_BUTTON)