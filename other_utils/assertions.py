# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/13 17:28
# @Author  : _Gy
# @File    : assertions.py
# @Software: PyCharm
import operator
from typing import Callable,Any
from exception_utils.exceptions import AssertionTypeError

class Assertions:

    @classmethod
    def status_code_assertion(cls,expect_status_code,actual_status_code):
        fail_code = 0
        if actual_status_code == expect_status_code:
            print('状态码断言成功')
        else:
            print(f'状态码断言失败，实际状态码{actual_status_code}!={expect_status_code}预期状态码')
            fail_code += 1
        return fail_code

    @classmethod
    def contain_assertion(cls,expect_result,response):
        '''
        :param expect_result: 预期结果
        :param response:
        :return:
        '''
        fail_code = 0
        try:
            for assert_key,assert_value in expect_result.items():
                pass
        except Exception as e:
            raise e
        return fail_code

    @classmethod
    def assert_eq(cls,expect_result,response):
        fail_code = 0
        if isinstance(expect_result,dict) and isinstance(response,dict):
            common_key = [expect_result.keys() & response.keys()]
            if common_key:
                common_key = common_key[0]
                actual_result = {common_key:response[common_key]}
                eq_result = operator.eq(expect_result,actual_result)
                if eq_result:
                    print(f"相等断言成功，预期结果{expect_result}=={actual_result}实际结果")
                else:
                    fail_code += 1
                    print(f"相等断言失败，预期结果{expect_result}!={actual_result}实际结果")
                return fail_code
            else:
                fail_code += 1
                print('yaml解析失败或返回错误，不存在common_key')


    @classmethod
    def assert_result(cls,expect_result,response,actual_status_code):
        '''
        断言主函数 通过标识断言 如果等于0代表成功 不等于0代表失败
        :param expect_result:  预期结果/yaml文件的预期结果
        :param response: 接口的实际响应信息
        :param actual_status_code: 接口的实际响应状态码
        :return:
        '''
        all_flag = 0
        assert_types = {
            'code':cls.status_code_assertion,
            'contain':cls.contain_assertion,
            'eq':cls.assert_eq,
        }
        try:
            for i in expect_result:
                for assert_type,assert_value in i.items():
                    # 接收两个任意类型的参数并返回一个int
                    assert_method:Callable[[Any,Any],int] = assert_types.get(assert_type)
                    if assert_method:
                        if assert_type == 'code':
                            flag=  assert_method(assert_value,actual_status_code)
                        elif assert_type == 'contain':
                            flag = assert_method(assert_value,response)
                        else:
                            flag = assert_method(assert_value,response)
                        all_flag += flag
                    else:
                        # print(f'不支持的断言模式{assert_type}')
                        raise AssertionTypeError(f'不支持的断言模式{assert_type}')
        except Exception as e:
            raise e