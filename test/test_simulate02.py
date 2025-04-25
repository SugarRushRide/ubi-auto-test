#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_simulate02.py
@Desc    ：不选择目标进行模拟
@Author  ：Byleth
@Date    ：2025/4/25 13:39 
"""
from pages.simulate_page import SimulatePage


def test_simulate02(univ_page):
    page = SimulatePage(univ_page)
    page.click_simulate()
    page.wait_for_simulate_score_update()
    # 数据提取
    current_data = page.get_current_rank_score()
    simulate_data = page.get_simulate_rank_score()

    # 数值判断
    assert current_data["rank"] == simulate_data["rank"], f"Current rank is different from simulate rank!"
    print(f"Pass! Current rank is {current_data["rank"]}. Simulate rank is {simulate_data["rank"]}")
    assert current_data["score"] == simulate_data["score"], f"Current score is different from simulate score!"
    print(f"Pass! Current score is {current_data["score"]}. Simulate score is {simulate_data["score"]}")
