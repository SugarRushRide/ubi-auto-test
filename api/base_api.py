#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ubi-auto-test 
@File    ：base_api.py
@Desc    ：所有接口请求的“基类”
@Author  ：Byleth
@Date    ：2025/4/21 14:39 
"""
from http.client import responses

import requests
from requests import RequestException

from config.settings import BASE_URL

class BaseAPI:
    def __init__(self, base_url = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()  # 用 session 维持会话，可自动处理 cookie 等

    def _handle_response(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise RequestException(f"HTTP Error: {e} | Response:{response.text}")
        try:
            return response.json()
        except ValueError:
            return response.text

    def get(self, endpoint, params=None, headers=None):
        url = self.base_url + endpoint
        try:
            response = self.session.get(url, params=params, headers=headers)
            return self._handle_response(response)
        except RequestException as e:
            raise Exception(f"GET请求失败: {e}")

    def post(self, endpoint, data=None, json=None, headers=None, files=None):
        url = self.base_url + endpoint
        try:
            response = self.session.post(url, data=data, json=json, headers=headers, files=files)
            return self._handle_response(response)
        except RequestException as e:
            raise Exception(f"POST请求失败: {e}")

    def put(self, endpoint, data=None, json=None, headers=None, timeout=10):
        """PUT请求"""
        url = self.base_url + endpoint
        try:
            response = self.session.put(
                url,
                data=data,
                json=json,
                headers=headers,
                timeout=timeout
            )
            return self._handle_response(response)
        except RequestException as e:
            raise Exception(f"PUT请求失败: {e}")

    def delete(self, endpoint, headers=None, timeout=10):
        """DELETE请求"""
        url = self.base_url + endpoint
        try:
            response = self.session.delete(
                url,
                headers=headers,
                timeout=timeout
            )
            return self._handle_response(response)
        except RequestException as e:
            raise Exception(f"DELETE请求失败: {e}")

    def set_auth_header(self, token):
        """设置认证头（示例）"""
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def update_headers(self, headers):
        """更新会话默认请求头"""
        self.session.headers.update(headers)