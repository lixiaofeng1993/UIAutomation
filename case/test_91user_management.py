import unittest
import time
from common import read_config
from page.page_user_management import UserManagementPage
from page.page_child_login import ChildLoginPage
from common.basics import open_browser
from BeautifulReport import BeautifulReport
from common.logger import Log,img_path


class TetsUserManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.usermag = UserManagementPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = read_config.img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self,img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path,img_name))

    @BeautifulReport.add_test_img('user_management')
    def test_01_user_management(self):
        usermag = self.usermag
        usermag.open(self.url,t='育儿锦囊后台管理系统')
        self.log.info('输入账号密码登录...')
        self.login.input_user('sunbin')
        self.login.input_password('sunbin_2018')
        self.login.click_login_btn()
        time.sleep(2)
        self.log.info('----------用户管理----------')
        usermag.click_user_management()
        self.save_img('用户管理')
        time.sleep(2)

    @BeautifulReport.add_test_img('search_data')
    def test_02_search_data(self):
        usermag = self.usermag
        self.log.info('----------查询用户----------')
        usermag.click_start_end_date()
        time.sleep(1)
        usermag.click_select_year()
        usermag.click_select_year_item()
        time.sleep(1)
        usermag.click_select_month()
        usermag.click_select_month_item()
        usermag.click_start_data()
        usermag.click_end_date()
        time.sleep(2)
        usermag.send_keys_enter()
        time.sleep(2)
        usermag.input_user_name()
        time.sleep(1)
        # usermag.send_keys_enter()
        usermag.click_query_btn()
        self.save_img('查询用户')
        time.sleep(1)

    @BeautifulReport.add_test_img('jump_page')
    def test_03_jump_page(self):
        usermag = self.usermag
        usermag.click_user_management()
        time.sleep(1)
        usermag.click_next_page()
        time.sleep(1)
        usermag.click_previous_page()
        time.sleep(1)
        usermag.select_page_number()
        time.sleep(1)
        try:
            usermag.input_jumper_page()
        except AttributeError:
            usermag.input_jumper_page02()
        usermag.send_keys_enter()
        self.save_img('用户管理页面跳转')
        time.sleep(1)
        usermag.click_spinner_select_row()
        usermag.send_keys_arrow_down()
        usermag.send_keys_enter()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()