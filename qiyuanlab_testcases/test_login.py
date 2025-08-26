# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/22 10:44
# @Author  : _Gy
# @File    : test_model_list.py
# @Software: PyCharm
import pytest
from other_utils.fileHandler import read_yaml
from other_utils.apiutils import RequestBase
import allure

rb  = RequestBase()
@allure.feature('登录模块')
class TestLogin:

    @pytest.mark.parametrize('base_info',read_yaml("./qiyuanlab/login/login.yaml"))
    def test_model_list(self,base_info):
        res = rb.execute_test_case(base_info)


