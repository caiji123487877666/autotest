import os
import shutil
import subprocess
import sys

import pytest
if __name__ == "__main__":
    pytest.main()
    shutil.copy('./environment.xml', './report/allure-result')
    os.system('allure serve ./report/allure-result')

