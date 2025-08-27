# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/22 10:44
# @Author  : _Gy
# @File    : test_model_list.py
# @Software: PyCharm
import allure
import pytest
from other_utils.fileHandler import read_yaml
from other_utils.apiutils import RequestBase

rb = RequestBase()


@allure.feature('测试')
class TestModelList:

    @allure.story('登录成功')
    @allure.title('用例标题')
    @allure.description('用例描述信息')

    @pytest.mark.parametrize('base_info', read_yaml("./qiyuanlab/dataset/datasetList.yaml"))
    def test_model_list(self, base_info):
        rb.execute_test_case(base_info)


