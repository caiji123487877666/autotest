# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/12 10:08
# @Author  : _Gy
# @File    : setting.py
# @Software: PyCharm
import os
import sys

DIR_PATH =os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH)

FILE_PATH = {
    'ini': os.path.join(DIR_PATH, 'config','conf.ini'),
    'extract': os.path.join(DIR_PATH, 'extract.yaml'),
}