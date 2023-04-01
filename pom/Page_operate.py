"""
    管理页面的所有元素
    以及操作这些元素的方法
"""
from pom.Base_function import Base


class LoginPage(Base):
    # 编写定位器与页面元素
    name_input_locator = ("id", "name")
    passwd_input_locator = ("id", "password")
    submit_button_locator = ("id", "submit")
    username = 'xxxxxxx'
    userpasswd = 'xxxxxx'
    url = 'https://sso.kuaidi100.com/sso/authorize.do'

    # 封装元素操作
    # 输入用户名
    def name_input(self):
        self.send_keys(self.name_input_locator, self.username)

    # 输入密码
    def passwd_input(self):
        self.send_keys(self.passwd_input_locator, self.userpasswd)

    # 点击登录
    def click_submit(self):
        self.click(self.submit_button_locator)


if __name__ == '__main__':
    base = Base('chrome')
    base.open_url(url=LoginPage.url)