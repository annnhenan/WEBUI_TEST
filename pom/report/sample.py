"""
run_case.py
1.将需要执行的测试用例，添加到测试套中
2.将用例执行结果生成的HTML格式的测试报告
HTMLTestRunner.py文件放置在python安装目录中的Lib目录中
备注:
    运行结果三种:
    ok  表示用例执行通过
    F   表示用例执行失败
    E   表示代码错误
"""
import os
import unittest
import HTMLTestRunner
import time

# 确定测试用例路径
case_path = "./testcase"

# 将测试文件夹中的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")

# 执行测试用例比并生成测试报告
# 测试报告存放路径
report_path = "./report"

# 确定测试报告名称
now = time.strftime("%Y_%m_%d %H-%M-%S")
report_file = report_path + "/" + now + "report.html"

# 写入数据
with open(report_file, "wb") as fp:
    runner = HTMLTestRunner.HTMLTestRunner(
        title="XXX项目的web自动化测试报告",
        description="xxx功能",
        verbosity=2,
        stream=fp
    )
    runner.run(discover)