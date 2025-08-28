# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/28 14:30
# @Author  : _Gy
# @File    : default_data_handler.py
# @Software: PyCharm
import random
import datetime
from fileHandler import get_target_data
import re


class DefaultDataHandler:
    def get_extract_data(self, node_name, out_format=None):
        data = get_target_data(node_name)
        if out_format is None and bool(re.compile(r'^[+-]?\d+$').match(str(out_format))):
            out_format = int(out_format)
            data_value = {
                out_format: self.seq_read(data, out_format),
                0: random.choice(data),
                -1: ','.join(data),
                -2: ','.join(data).split(','),

            }
            data = data_value[out_format]
        else:
            data = get_target_data(node_name, out_format)
        return data

    def seq_read(self, data, out_format):
        if out_format not in [0, -1, -2]:
            return data[out_format - 1]
        else:
            return None

    def get_now_time(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def get_headers(self, params_type):
        headers_mapping = {
            'data': {'content-type': 'application/json'},
            'json': {'content-type': 'application/json'},
        }
        headers = headers_mapping.get(params_type)
        if headers is None:
            raise ValueError('不支持该类型请求头')
        return headers


if __name__ == '__main__':
    de = DefaultDataHandler()
    res = de.get_extract_data('cookies', 'token')
    print(res)
