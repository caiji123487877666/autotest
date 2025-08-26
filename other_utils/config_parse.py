# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/12 10:16
# @Author  : _Gy
# @File    : config_parse.py
# @Software: PyCharm
import configparser
from config.setting import FILE_PATH

class ConfigParse:

    def __init__(self,file_path = FILE_PATH['ini']):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def read_config(self):
        self.config.read(self.file_path)


    def get_value(self,section,option):
        try:
            return self.config.get(section,option)
        except Exception as e:
            raise e

    def get_host(self,option):
        return self.get_value('HOST',option)

if __name__ == '__main__':
    pass