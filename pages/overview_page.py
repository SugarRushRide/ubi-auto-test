#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：overview_page.py
@Desc    ：总体定位页面
@Author  ：Byleth
@Date    ：2025/4/18 14:55 
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OverviewPage(BasePage):
    # 明细检验
    DETAIL_DATA = (By.CLASS_NAME, "ind-detail")
    MODAL = (By.CLASS_NAME, "detail-layout")
    MODAL_FORM = (By.CLASS_NAME, "ant-table-tbody")
    CLOSE_BUTTON = (By.CLASS_NAME, "ant-modal-close")
    # 历史版本
    VERSION_SELECT_BUTTON = (By.CLASS_NAME, "version-select-box")
    # 最近历史版本
    PREVIOUS_VERSION = (By.XPATH, "//div[.//span[contains(normalize-space(string(.)), '2025年03月')] and @class = 'ant-select-item-option-content']")
    # 最近发布版本
    LAST_PUBLISHED_VERSION = (By.XPATH, "//div[.//span[contains(normalize-space(string(.)), '2024年08月')] and @class = 'ant-select-item-option-content']")


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

    # 点击版本切换按钮
    def click_version_select(self):
        self.click(*self.VERSION_SELECT_BUTTON)

    # 最近版本
    def change_version_previous(self):
        self.click(*self.PREVIOUS_VERSION)
        sleep(0.5)

    # 最近发布版
    def change_version_published(self):
        self.click(*self.LAST_PUBLISHED_VERSION)
        sleep(0.5)
