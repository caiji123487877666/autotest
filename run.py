import pytest
import os
import shutil

if __name__ == '__main__':
    pytest.main(['--alluredir= ./report/temp','./qiyuanlab_testcases'])
    os.system('allure serve ./report/temp')