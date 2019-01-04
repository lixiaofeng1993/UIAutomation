import unittest

import paramunittest

from common import read_config
from common.basics import open_browser
from common.logger import Log
from tmp.eg.page_login import LoginPage


@paramunittest.parametrized(
        {'user': '18701137212', 'psw': '123456'},
        {'user': 'lixiaofeng', 'psw': 'fengzi80230'},
        # {'user': 'python', 'psw': 'fengzi80230'},
        # {'user': 'java', 'psw': 'fengzi80230'},
        # {'user': 'lal', 'psw': 'fengzi80230'},
        # {'user': 'demaxiy', 'psw': 'fengzi80230'},
        # {'user': '德玛西亚', 'psw': 'fengzi80230'},
        # {'user': '哈哈', 'psw': 'fengzi80230'},
        # {'user': 'AASADSADAS', 'psw': 'fengzi80230'},
    )
class TestSmithereensLogin(unittest.TestCase):

    def setUp(self):
        self.driver = open_browser()
        self.log = Log()
        self.login = LoginPage(self.driver)
        self.url = read_config.url

    def setParameters(self, user, psw):
        self.user = user
        self.psw = psw

    def test_login(self):
        login = self.login
        login.open(url=self.url + 'login/', t='login')
        self.log.info('输入手机号,密码,点击登录按钮.')
        login.input_phone(self.user)
        login.input_pass(self.psw)
        login.click_login_btn()
        self.assertIn('你好', login.check_login(), '登录失败!')
        self.log.info('登录成功!')

    def tearDown(self):
        self.login.close()

if __name__ == '__main__':
    unittest.main()