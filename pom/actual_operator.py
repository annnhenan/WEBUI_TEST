import unittest
from pom.Page_operate import LoginPage


# 定义测试类
class TestCaseLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = LoginPage()
        self.driver.open_url(LoginPage.url)

    def tearDown(self) -> None:
        self.driver.close()

    def testLogin(self):
        """实际的登录测试用例"""
        self.driver.name_input()
        self.driver.passwd_input()
        self.driver.click_submit()


if __name__ == "__main__":
    unittest.main()