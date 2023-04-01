"""
    封装公共方法
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browser="chrome"):
        """
        初始化driver
        :param browser: 浏览器名称
        """
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = None
            print("请输入正确的浏览器：chrome or firefox or edge")

    def open_url(self, url):
        """
        打开地址
        :param url: 被测试地址
        :return:
        """
        self.driver.get(url)
        time.sleep(2)

    def find_element(self, locator, timeout=10):
        """
        定位单个元素，如果成功返回元素本身，失败返回false
        :param locator:
        :param timeout:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"{locator}元素未找到")
            return False

    def click(self, locator):
        """
        点击元素
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator:定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        """
        关闭浏览器
        :return:
        """
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    base = Base()
    base.open_url("https://sso.kuaidi100.com/sso/authorize.do")
    base.close()
