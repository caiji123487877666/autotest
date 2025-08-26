# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/11 10:26
# @Author  : _Gy
# @File    : sendRequests.py
# @Software: PyCharm
import json

import requests
import requests


class RequestHandler:
    def __init__(self):
        # 可以在这里初始化会话、基础URL等
        self.session = requests.Session()

    def sendRequests(self, api_name, method, url, case_name=None, headers=None, **testcase):
        """
        原始请求方法（假设已存在）
        :param api_name: 接口名称
        :param method: 请求方法 (get/post/put/delete等)
        :param url: 请求URL
        :param case_name: 用例名称（可选）
        :param headers: 请求头（可选）
        :param testcase: 其他参数（如params/data/json等）
        :return: 响应对象
        """
        # 这里假设是原始方法的实现
        method = method.lower()

        try:
            if method == 'get':
                res = self.session.get(url, headers=headers, **testcase)
            elif method == 'post':
                res = self.session.post(url, headers=headers, **testcase)
            elif method == 'put':
                res = self.session.put(url, headers=headers, **testcase)
            elif method == 'delete':
                res = self.session.delete(url, headers=headers, **testcase)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            # 可以在这里添加响应处理逻辑
            return res

        except Exception as e:
            # 异常处理
            print(f"Request failed for {api_name}({case_name}): {str(e)}")
            raise

    def do_request(self, api_name, method, url, case_name=None, headers=None, **kwargs):
        """
        封装的通用请求方法
        :param api_name: 接口名称（用于标识）
        :param method: HTTP方法
        :param url: 请求地址
        :param case_name: 测试用例名称
        :param headers: 请求头
        :param kwargs: 支持requests库的所有参数，如：
            - params: 字典，URL查询参数
            - data: 字典/字符串，表单数据
            - json: 字典，JSON数据
            - files: 文件上传
            - timeout: 超时时间
            - etc.
        :return: 响应对象
        """
        # 预处理参数（可添加默认值或参数校验）
        headers = headers or {}

        # 调用原始sendRequests方法
        return self.sendRequests(
            api_name=api_name,
            method=method,
            url=url,
            case_name=case_name,
            headers=headers,
            **kwargs
        )

if __name__ == '__main__':
    handler = RequestHandler()




