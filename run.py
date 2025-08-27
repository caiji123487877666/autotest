import os
import shutil
import subprocess


def run_tests():
    print("Running tests...")

    # 清理旧的报告文件
    if os.path.exists('./report/allure-results'):
        print("Cleaning old Allure results...")
        shutil.rmtree('./report/allure-results')

    # 确保 environment.xml 文件存在
    if os.path.exists('./environment.xml'):
        print("Copying environment.xml...")
        shutil.copy('./environment.xml', './report/allure-results')
    else:
        print("environment.xml file does not exist!")

    # 运行 pytest，生成 Allure 结果
    pytest_args = ['pytest', '--alluredir=./report/allure-results']
    result = subprocess.run(pytest_args, capture_output=True, text=True)

    # 输出 pytest 执行日志
    # 生成 Allure 报告
    print("Generating Allure report...")
    subprocess.run(['allure', 'serve', './report/allure-results'])


if __name__ == "__main__":
    run_tests()
