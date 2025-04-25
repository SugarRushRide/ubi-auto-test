#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：test_simulate03.py
@Desc    ：“全球1-100”，“目标数据”列数据校验;
           “全球1-100”模拟、重置功能校验
@Author  ：Byleth
@Date    ：2025/4/25 14:13 
"""
import pandas as pd

from pages.simulate_page import SimulatePage

def test_simulate03(univ_page):
    page = SimulatePage(univ_page)
    origin_df = page.extract_table_data()
    pd.set_option('display.max_columns', None)
    # print(origin_data)

    # 获取“当前数据”、“全球1-100”数据中每条数据更大的一项
    check_data = origin_df.apply(lambda row: max(float(row["当前数据"]), float(row["全球1-100"])),
                                 axis=1).tolist()
    print(check_data)
    # 点击设为目标获取数据变化
    page.click_use1()
    new_df = page.extract_table_data()
    # print(new_data)
    page_data = new_df["目标数据"].astype(float).tolist()
    print(page_data)

    # 数据校验
    assert check_data == page_data, f"Something wrong on target data."
    print(f"Pass! Actual data is {check_data}, data on page is {page_data}")

    # 模拟
    page.click_simulate()
    page.wait_for_simulate_score_update()
    # 数据提取
    current_data = page.get_current_rank_score()
    simulate_data = page.get_simulate_rank_score()


    # 数值判断
    if check_data != origin_df["当前数据"].astype(float).tolist():
        assert current_data["score"] != simulate_data["score"], f"Current score is different from simulate score!"
    else:
        assert current_data["score"] == simulate_data["score"], f"Current score is different from simulate score!"

    print(f"Pass! Current score is {current_data["score"]}. Simulate score is {simulate_data["score"]}")

    # 重置按钮测试
    page.click_reset()
    # 数据提取
    simulate_data = page.get_simulate_rank_score()

    # 数值判断
    assert current_data["rank"] == simulate_data["rank"], f"Current rank is different from simulate rank! There's something wrong on Reset button!"
    print(f"Pass! Current rank is {current_data["rank"]}. Simulate rank is {simulate_data["rank"]}")
    assert current_data["score"] == simulate_data["score"], f"Current score is different from simulate score!There's something wrong on Reset button!"
    print(f"Pass! Current score is {current_data["score"]}. Simulate score is {simulate_data["score"]}")





