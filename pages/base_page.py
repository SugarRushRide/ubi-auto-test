#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：base_page.py
@Desc    ：封装所有页面基本操作
@Author  ：Byleth
@Date    ：2025/4/18 14:22 
"""
from abc import abstractmethod

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

    def wait_for_page_ready(self, timeout=15):
        try:
            # 调用子类实现的定位器
            locator = self._get_ready_locator()
            print(f"等待页面就绪，使用的定位器：{locator}")  # 调试输出
            # 验证定位器类型
            if not isinstance(locator, tuple) or len(locator) != 2:
                raise ValueError(f"无效的定位器格式: {locator}")
            return self.wait_for_element(*locator, timeout)
        except Exception as e:
            # 抛出包含具体页面类名的异常
            class_name = self.__class__.__name__
            raise TimeoutError(
                f"Page [{class_name}] not ready"
                f"Element {locator} not found within {timeout} seconds"
            ) from e

    @abstractmethod
    def _get_ready_locator(self):
        """子类必须实现的抽象方法：返回页面就绪的定位器"""
        pass

    def wait_for_element(self, by, value, timeout=15):
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

    def find_element(self, by, value):
        """寻找指定元素"""
        self.wait_for_element(by, value)
        return self.driver.find_element(by, value)

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

    def wait_for_change(self, locator, get_value_fn=None, timeout=10):
        """
        等待某个元素的值发生变化（text 或任意属性）
        :param locator: 元素定位器（By, value）
        :param get_value_fn: 可选，自定义提取值的方法（默认取 element.text）
        :param timeout: 最大等待秒数
        """
        if get_value_fn is None:
            get_value_fn = lambda e : e.text

        element = self.find_element(*locator)
        old_value = get_value_fn(element)

        WebDriverWait(self.driver, timeout).until(
            lambda d: get_value_fn(d.find_element(*locator)) != old_value
        )
