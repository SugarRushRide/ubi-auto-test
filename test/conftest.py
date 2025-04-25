#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：conftest.py
@Desc    ：配置
@Author  ：Byleth
@Date    ：2025/4/18 14:24 
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import config
from pages.base_page import BasePage
from pages.overview_page import OverviewPage
from api.auth import get_login_url

@pytest.fixture(scope="session")
def driver():
    cfg = config.browser
    chrome_options = Options()

    # 从配置中读取是否 headless
    if cfg.get("headless", False):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    # 设置窗口大小
    width = cfg.get("window_size", {}).get("width")
    height = cfg.get("window_size", {}).get("height")
    chrome_options.add_argument(f"--window-size={width},{height}")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def univ_url():
    cred = config.credentials
    return get_login_url(
        login_name=cred['login_name'],
        password=cred['password'],
        login__type_id=cred['login_type_id'],
        univ_code=cred['univ_code']
    )

@pytest.fixture(scope="session")
def univ_page(driver, univ_url):
    driver.get(univ_url)
    return driver