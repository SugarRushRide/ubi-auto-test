#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：overview_page.py
@Desc    ：总体定位页面
@Author  ：Byleth
@Date    ：2025/4/18 14:55 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OverviewPage(BasePage):
    DETAIL_DATA = (By.CLASS_NAME, "ind-detail")
    MODAL = (By.CLASS_NAME, "detail-layout")
    MODAL_FORM = (By.CLASS_NAME, "ant-table-tbody")
    CLOSE_BUTTON = (By.CLASS_NAME, "ant-modal-close")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_ready(self):
        self.wait_for_element(*self.DETAIL_DATA)

    def get_all_detail_elements(self):
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

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
