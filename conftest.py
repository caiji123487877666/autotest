# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/25 17:21
# @Author  : _Gy
# @File    : conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope="session",autouse=True)
def print_info():
    print('------测试开始-------')
    yield
    print('------测试结束-------')