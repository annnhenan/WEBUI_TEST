import time
import os
import unittest
import HTMLTestRunner

# 定位测试用例目录
project_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
testcase_dir = project_dir + r"\testcase"


def createsuite():
    """获取测试集"""
    # 寻找测试用例
    testcases = unittest.defaultTestLoader.discover(testcase_dir, pattern="test*.py", top_level_dir=None)
    return testcases


def run(title=u'自动化测试报告', description=u'环境配置等信息'):
    """执行测试并生成报告"""
    # 如果没有测试报告目录则创建
    for filename in os.listdir(project_dir):
        if filename == "reports":
            break
    else:
        os.mkdir(project_dir + r'\reports')

    # 执行测试用例并生成测试报告
    #  确定存放测试报告路径
    report_path = project_dir + r'\reports'
    print(report_path)
    # 确定测试报告名称
    now = time.strftime("%Y_%m_%d_%H-%M-%S")
    report_file = report_path + '\\' + now + "report.html"

    # 写入
    with open(report_file, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            title=title,
            description=description,
            verbosity=2,
            stream=fp
        )
        runner.run(createsuite())


if __name__ == '__main__':
    run()