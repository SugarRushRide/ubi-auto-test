#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：auth.py
@Desc    ：跳过cg平台直接登录学校页面
@Author  ：Byleth
@Date    ：2025/4/18 11:54 
"""
from config.settings import config
import requests

def get_token(login_name, password):
    url = "https://cg-beta.gaojidata.com/api/v1/sso/login/loginByPwd"
    headers = {
        "Accept": "application/json, text/plain, */*; charset=utf-8",
        "Referer": "https://cg-beta.gaojidata.com/login",
    }

    # multipart/form-data 构建
    files = {
        "LoginName": (None, login_name),
        "Password": (None, password)
    }
    response = requests.post(url, files=files, headers=headers, verify=False)
    print(response)
    if response.status_code != 200:
        raise Exception(f"请求失败，状态码：{response.status_code}")

    res_json = response.json()
    token = res_json.get("data")
    if not token:
        raise Exception("未能获取 token，响应内容为：" + str(res_json))
    return token

def get_login_url(login_name, password, login__type_id, univ_code):
    cred = config.credentials
    token = get_token(login_name, password)
    login_url = (
        f"https://ubi.gaojidata.com/login"
        f"?loginTypeId={cred['login_type_id']}"
        f"&univCode={cred['univ_code']}"
        f"&loginName={cred['login_name']}"
        f"&token={token}"
    )

    return login_url

if __name__ == "__main__":
    login_name = "chengjun.jiang"
    password = "shanghai0303"
    login_type_id = "2"
    univ_code = "RC00001"

    login_url = get_login_url(login_name, password, login_type_id, univ_code)
    print("登录 URL：", login_url)