import pytest
import os
import shutil

if __name__ == '__main__':
    pytest.main()
    os.system('allure serve ./report/temp')