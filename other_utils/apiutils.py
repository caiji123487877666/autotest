# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/12 15:32
# @Author  : _Gy
# @File    : apiutils.py
# @Software: PyCharm
import json

from other_utils import sendRequests
from other_utils.fileHandler import *
from other_utils.config_parse import *
from other_utils.sendRequests import *
from other_utils.assertions import *
import allure
import re

from other_utils.default_data_handler import DefaultDataHandler


class RequestBase:

    def __init__(self):
        self.conf = ConfigParse()
        self.sendRequests = RequestHandler()
        self.assertions = Assertions()

    def parse_and_replace_value(self, yaml_data):
        # yaml_data_str = yaml_data if isinstance(yaml_data, str) else json.dumps(yaml_data, ensure_ascii=False)
        # for _ in range(yaml_data_str.count('${')):
        #     if '${' in yaml_data_str and '}' in yaml_data_str:
        #         start_index = yaml_data_str.index('${')
        #         end_index = yaml_data_str.index('}')
        #         d_data = yaml_data_str[start_index:end_index + 1]
        #         # 正则提取函数名
        #         print(d_data)
        #         match = re.match('\$\{(\w+)\((.*?)\)\}',d_data)
        #         if match:
        #             func_name ,func_params = match.groups()
        #             func_params = func_params.split('.') if func_params else []
        #             # 反射
        #             extract_data = getattr(DefaultDataHandler(), func_name)(*func_params)
        #             yaml_data_str = re.sub(re.escape(d_data), str(extract_data), yaml_data_str)
        # try:
        #     data = json.loads(yaml_data_str)
        # except json.JSONDecodeError as e:
        #     data = yaml_data_str
        #
        # return data

        # 将yaml_data转换为字符串形式，如果已经是字符串则保持不变
        yaml_data_str = yaml_data if isinstance(yaml_data, str) else json.dumps(yaml_data, ensure_ascii=False)

        # 预编译正则表达式，以提高效率
        func_pattern = re.compile(r'\$\{(\w+)\((.*?)\)\}')

        # 使用循环替换所有匹配项
        while True:
            # 查找符合格式的 `${}` 表达式
            match = func_pattern.search(yaml_data_str)
            if not match:
                break  # 没有匹配项时退出循环

            # 提取函数名和参数
            d_data = match.group(0)
            func_name, func_params = match.groups()
            func_params = func_params.split('.') if func_params else []

            # 反射调用相应的方法
            try:
                handler = DefaultDataHandler()  # 只创建一个实例
                extract_data = getattr(handler, func_name)(*func_params)
                # 替换原字符串中的表达式
                yaml_data_str = yaml_data_str.replace(d_data, str(extract_data))
            except Exception as e:
                # 如果反射调用失败，可以记录错误并跳过
                print(f"Error calling function '{func_name}' with params '{func_params}': {e}")
                break

        # 试图将替换后的字符串转换为JSON
        try:
            data = json.loads(yaml_data_str)
        except json.JSONDecodeError:
            # 如果转换失败，返回原始字符串
            data = yaml_data_str

        return data

    def execute_test_case(self, api_info):
        try:
            conf_host = self.conf.get_host('host')
            url = conf_host + api_info['base_info']['url']
            allure.dynamic.title(api_info['base_info']['api_name'])
            api_name = api_info['base_info']['api_name']
            method = api_info['base_info']['method']
            headers = api_info['base_info'].get('headers', None)
            allure.attach(url, '接口地址:', attachment_type=allure.attachment_type.TEXT)
            allure.attach(api_name, '接口名称:', attachment_type=allure.attachment_type.TEXT)
            allure.attach(method, '请求方式:', attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(headers), 'headers', attachment_type=allure.attachment_type.JSON)

            for testcase in api_info['testCase']:
                case_name = testcase.pop('case_name')
                # case_data = testcase.pop('data')
                # for param_type,param_value in testcase.items():
                #     if param_type in ['json','data','params']:
                #         request_value = param_value
                print(testcase)
                res = self.sendRequests.do_request(api_name=api_name, method=method, url=url, case_name=case_name,
                                                   headers=headers, **testcase)
                status_code, res_json = res.status_code, res.json()
                # 断言
                self.assertions.assert_result([{"code": 200}], res.json(), status_code)
        except Exception as e:
            raise e


if __name__ == '__main__':
    data = {'name': 'gy', 'age': '30', 'tall': 180, 'ltime': '${get_now_time()}','headers':'${get_headers(data)}'}
    p = RequestBase()
    print(p.parse_and_replace_value(data))
