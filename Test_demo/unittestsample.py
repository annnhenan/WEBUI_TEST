from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCaseLogin(unittest.TestCase):
    def setUp(self) -> None:
        """
        前置函数
        用于打开浏览器、连接数据库、初始化数据等
        """
        # 打开浏览器
        self.driver = webdriver.Chrome()

        # 打开网站
        url = "https://sso.kuaidi100.com/sso/authorize.do"
        self.driver.get(url)
        time.sleep(3)

    def tearDown(self) -> None:
        """
        后置函数
        用于关闭浏览器，断开数据库，清理测试数据等操作
        """

        # 关闭浏览器
        self.driver.quit()

    def testLogin(self):
        """登录用例"""
        # 编写定位器
        name_input_locator = ('id', "name")
        passwd_input_locator = ('id', "password")
        submit_button_locator = ('id', "submit")

        # 等待元素出现后再操作
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(name_input_locator))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(passwd_input_locator))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(submit_button_locator))
        self.driver.find_element(id, "name").send_keys("xxxxxxxx")
        self.driver.find_element(id, "password").send_keys("xxxxxxxx")
        self.driver.find_element(id, "submit").click()


if __name__ == '__main__':
    unittest.main()
