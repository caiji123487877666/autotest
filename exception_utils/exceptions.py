# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/21 17:23
# @Author  : _Gy
# @File    : exceptions.py
# @Software: PyCharm
class AssertionTypeError(Exception):
    '''
    yaml文件断言错误
    '''
    def __init__(self,message = "不支持此类型异常"):
        self.message = message
        super().__init__(self.message)