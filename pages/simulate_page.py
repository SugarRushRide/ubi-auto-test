#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：simulate_page.py
@Desc    ：ARWU推演页面
@Author  ：Byleth
@Date    ：2025/4/22 10:41 
"""
import time

import pandas as pd
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import List

from utils.common import extract_number


class SimulatePage(BasePage):
    # ARWU推演
    ARWU_SIMULATION = (By.XPATH, "//aside//li[@data-menu-id='/simulate']")
    # 校验元素（当前排名的div）
    CHECK_ELEMENT = (By.CLASS_NAME, "ranking-wrap")
    # 模拟按钮
    SIMULATE_BUTTON = (By.XPATH, "//div[@class='btns']/div[1]")
    # 重置按钮
    RESET_BUTTON = (By.XPATH, "//div[@class='btns']/div[2]")
    # 当前排名
    CURRENT_RANKING = (By.XPATH, "//div[@class='ranking-wrap']//div[@class='value']")
    # 当前得分
    CURRENT_SCORE = (By.XPATH, "//div[@class='ranking-wrap']//div[@class='tips']")
    # 模拟排名
    SIMULATION_RANKING = (By.XPATH, "//div[@class='simulation-wrapper']//div[@class='value']")
    # 模拟得分
    SIMULATION_SCORE = (By.XPATH, "//div[@class='simulation-wrapper']//div[@class='tips']")
    # 表头单元格
    TABLE_HEADER_CELLS = (By.XPATH, "//div[@class='table-wrap custom-scroll']/div[@class='table-header']/div")
    # 表
    TABLE = (By.XPATH, "//div[@class='table-wrap custom-scroll']/div[@class='table-body']")
    # 集合
    MODULE = (By.XPATH, "//div[@class='module']")
    # 行
    ROW = (By.XPATH, ".//div[contains(@class, 'table-tr')]")
    # 单元格
    CELL = (By.XPATH, ".//div[contains(@class, 'table-td')]")
    # 特殊单元格，目标数据输入框中的数值
    INPUT_ELEM = (By.CSS_SELECTOR, "input[aria-valuenow]")
    # 设为目标1（全球1-100）
    USE1 = (By.XPATH, "(//div[@class='target']/div[@class='btn'])[1]")
    # 设为目标2（美国IVY）
    USE2 = (By.XPATH, "(//div[@class='target']/div[@class='btn'])[2]")
    # 设为目标3（中国985）
    USE3 = (By.XPATH, "(//div[@class='target']/div[@class='btn'])[3]")

    def __init__(self, driver):
        super().__init__(driver)

    def _get_ready_locator(self):
        return self.CHECK_ELEMENT

    def jump_to_simulation(self):
        self.click(*self.ARWU_SIMULATION)

    def extract_table_data(self) -> pd.DataFrame:
        """
            提取模拟页面表格中所有非隐藏行的数据。
            优先提取 input[aria-valuenow] 的值，否则使用文本内容。
            :return: 表格数据的 DataFrame
        """
        # 提取表头
        header_cells = self.find_elements(*self.TABLE_HEADER_CELLS)
        headers = [cell.text.replace('设为目标','').replace('\n', '').strip() for cell in header_cells]

        # 提取整个表格容器
        table_body = self.find_element(*self.TABLE)
        modules = table_body.find_elements(*self.MODULE)
        table_data: List[List[str]] = []

        for module in modules:
            rows = module.find_elements(*self.ROW)
            visible_row = None
            for row in rows:
                # if "display: none;" not in (row.get_attribute("style") or ""):
                visible_row = row
                # print(visible_row.text)
                break  # 只取第一个可见 row

            if not visible_row:
                continue  # 当前模块没有可见 row，跳过

            row_data = []
            cells = visible_row.find_elements(*self.CELL)

            for cell in cells:
                try:
                    input_elem = cell.find_element(*self.INPUT_ELEM)
                    value = input_elem.get_attribute("aria-valuenow")
                    row_data.append(value)
                except:
                    row_data.append(cell.text)

            table_data.append(row_data)

        # 构造dataframe
        df = pd.DataFrame(table_data, columns=headers[:len(table_data[0])])
        return df

    def get_current_rank_score(self) -> dict:
        rank = self.find_element(*self.CURRENT_RANKING).text
        score = self.find_element(*self.CURRENT_SCORE).text
        score = extract_number(score)
        data = {"rank": rank, "score": score}
        return data

    def get_simulate_rank_score(self) -> dict:
        rank = self.find_element(*self.SIMULATION_RANKING).text
        score = self.find_element(*self.SIMULATION_SCORE).text
        score = extract_number(score)
        data = {"rank": rank, "score": score}
        return data

    # 等待模拟排名
    def wait_for_simulate_score_update(self):
        # 逻辑待完善
        # self.wait_for_change(self.SIMULATION_SCORE, timeout=15)
        time.sleep(0.5)

    # 点击模拟
    def click_simulate(self):
        self.click(*self.SIMULATE_BUTTON)

    # 点击重置
    def click_reset(self):
        self.click(*self.RESET_BUTTON)

    # 点击目标1
    def click_use1(self):
        self.click(*self.USE1)

    # 点击目标2
    def click_use2(self):
        self.click(*self.USE2)

    # 点击目标3
    def click_use3(self):
        self.click(*self.USE3)