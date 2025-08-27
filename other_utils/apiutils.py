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





class RequestBase:

    def __init__(self):
        self.conf = ConfigParse()
        self.sendRequests = RequestHandler()
        self.assertions = Assertions()


    def data_test_handler(self, yaml_data):
        yaml_data_str = yaml_data if isinstance(yaml_data, str) else json.dumps(yaml_data, ensure_ascii=False)
        for _ in range(yaml_data_str.count('${')):
            if '${' in yaml_data_str and '}' in yaml_data_str:
                start_index = yaml_data_str.index('${')
                end_index = yaml_data_str.index('}')
                d_data = yaml_data_str[start_index:end_index + 1]

    def execute_test_case(self, api_info):
        try:
            conf_host = self.conf.get_host('host')
            url  = conf_host + api_info['base_info']['url']
            allure.dynamic.title(api_info['base_info']['api_name'])
            api_name = api_info['base_info']['api_name']
            method = api_info['base_info']['method']
            headers = api_info['base_info'].get('headers', None)
            allure.attach(url,'接口地址:',attachment_type=allure.attachment_type.TEXT)
            allure.attach(api_name,'接口名称:',attachment_type=allure.attachment_type.TEXT)
            allure.attach(method,'请求方式:',attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(headers),'headers',attachment_type=allure.attachment_type.JSON)

            for testcase in api_info['testCase']:
                case_name = testcase.pop('case_name')
                # case_data = testcase.pop('data')
                # for param_type,param_value in testcase.items():
                #     if param_type in ['json','data','params']:
                #         request_value = param_value
                print(testcase)
                res = self.sendRequests.do_request(api_name=api_name, method=method, url=url, case_name=case_name, headers=headers,**testcase)
                status_code , res_json = res.status_code, res.json()
                #断言
                self.assertions.assert_result([{"code":200}],res.json(),status_code)
        except Exception as e:
            raise e



if __name__ == '__main__':
    ry = read_yaml('../qiyuanlab/modelzoo/example.yaml')[0]
    req = RequestBase()
    res = req.execute_test_case(ry)
