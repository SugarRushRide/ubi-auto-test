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
from utils.auth import get_login_url

@pytest.fixture(scope="session")
def driver():
    cfg = config.browser
    chrome_opt