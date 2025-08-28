# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/8/11 15:02
# @Author  : _Gy
# @File    : fileHandler.py
# @Software: PyCharm
import datetime

import yaml, os
from config.setting import *


def read_yaml(file_path):
    """
    将YAML文件转换为字典

    参数:
        file_path (str): YAML文件的路径

    返回:
        dict: 转换后的字典

    异常:
        FileNotFoundError: 如果文件不存在
        yaml.YAMLError: 如果YAML格式错误
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:

            data = yaml.safe_load(file)  # 使用safe_load避免潜在安全风险
            return data if data is not None else {}  # 处理空文件情况
    except UnicodeDecodeError as e:
        raise yaml.YAMLError(f"YAML解析错误: {e}")
    except Exception as e:
        raise Exception(f"读取文件时出错: {e}")


def write_yaml(data):
    file_path = FILE_PATH['extract']
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            pass
    try:
        file = open(file_path, 'a', encoding='utf-8')
        if isinstance(data, dict):
            write_data = yaml.dump(data, allow_unicode=True, sort_keys=False)
            file.write(write_data)
        else:
            print('写入数据格式错误')
    except Exception as e:
        raise e


# 获取所有路径下的yaml文件
def get_yaml_files_recursive(folder_path):
    """递归获取所有子文件夹中的 .yaml 和 .yml 文件"""
    yaml_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                yaml_files.append(os.path.join(root, file))  # 返回完整路径
    return yaml_files


def clean_yaml():
    with open(FILE_PATH['extract'], 'w', encoding='utf-8') as file:
        file.truncate()


def get_target_data(first_node, sec_node=None):
    try:
        with open(FILE_PATH['extract'], 'r', encoding='utf-8') as file:
            extract_data = yaml.safe_load(file)
            if sec_node is None:
                return extract_data[first_node]
            else:
                return extract_data.get(first_node, {}).get(sec_node)
    except yaml.YAMLError as e:
        print(f'读取失败，请检查格式-{e}')
    except Exception as e:
        print(f'读取文件未知异常-{e}')



# 使用示例
if __name__ == "__main__":
    pass
