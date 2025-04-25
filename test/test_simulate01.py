#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_simulate01.py
@Desc    ：初始页面排名、得分校验
@Author  ：Byleth
@Date    ：2025/4/24 18:06 
"""
from pages.simulate_page import SimulatePage
import pandas as pd
def test_simulate01(univ_page):
    # 页面加载
    page = SimulatePage(univ_page)
    page.jump_to_simulation()
    page.wait_for_page_ready()

    # 数据提取
    current_data = page.get_current_rank_score()
    simulate_data = page.get_simulate_rank_score()

    # 数值判断
    assert current_data["rank"] == simulate_data["rank"], f"Current rank is different from simulate rank!"
    print(f"Pass! Current rank is {current_data["rank"]}. Simulate rank is {simulate_data["rank"]}")
    assert current_data["score"] == simulate_data["score"], f"Current score is different from simulate score!"
    print(f"Pass! Current score is {current_data["score"]}. Simulate score is {simulate_data["score"]}")
