import unittest
import time
from BeautifulReport import BeautifulReport
from common.logger import Log, img_path
from common.basics import open_browser
from page.page_account_management import AccountManagementPage
from page.page_child_login import ChildLoginPage
from common import read_config


class TestAccountManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.url = read_config.url
        cls.login = ChildLoginPage(cls.driver)
        cls.accmag = AccountManagementPage(cls.driver)
        cls.img_path = img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_account_management')
    def test_01_account_management(self):
        accmag = self.accmag
        accmag.open(self.url, t='育儿锦囊后台管理系统')
        self.log.info('输入账号密码登录...')
        self.login.input_user('sunbin')
        self.login.input_password('sunbin_2018')
        self.login.click_login_btn()
        time.sleep(2)
        accmag.click_permission_manager()
        time.sleep(1)
        accmag.click_account_management()
        self.save_img('账号管理')
        time.sleep(1)



    @BeautifulReport.add_test_img('test_add_account')
    def test_02_add_account(self):
        accmag = self.accmag
        accmag.click_add_account_btn()
        time.sleep(2)
        accmag.input_addacc_username()
        accmag.input_addacc_password()
        accmag.input_addacc_name()
        accmag.input_addacc_phone()
        accmag.input_addacc_remark()
        time.sleep(2)
        accmag.select_addacc_role()
        accmag.send_keys_arrow_down()
        accmag.send_keys_enter()
        time.sleep(1)
        self.save_img('新增账号')
        accmag.click_addaccount_cancel()
        time.sleep(2)

    @BeautifulReport.add_test_img('test_edit_account')
    def test_03_edit_account(self):
        accmag = self.accmag
        accmag.click_edit_account_btn()
        time.sleep(2)
        accmag.input_dialog_editacc_name()
        accmag.input_dialog_editacc_phone()
        accmag.input_dialog_editacc_remark()
        try:
            accmag.click_dialog_editacc_selectrole()
        except AttributeError:
            accmag.click_dialog_editacc_selectrole02()
        # time.sleep(2)
        accmag.send_keys_arrow_down()
        accmag.send_keys_enter()
        self.save_img('编辑账号')
        time.sleep(1)
        accmag.click_dialog_editacc_cancel()
        time.sleep(1)

    @BeautifulReport.add_test_img('is_enable_disable_btn')
    def test_04_enable_disable_account(self):
        accmag = self.accmag
        accmag.click_enable_disable_account_btn()
        time.sleep(1)
        accmag.click_isEnable_Disable_Detemine_btn()
        self.save_img('账号是否启/禁用')
        time.sleep(1)

    @BeautifulReport.add_test_img('jump_page')
    def test_05_jumper_page(self):
        accmag = self.accmag
        try:
            accmag.input_jumper_page()
        except AttributeError:
            accmag.input_jumper_page02()
        accmag.send_keys_enter()
        time.sleep(2)
        accmag.click_previous_page()
        time.sleep(1)
        accmag.click_spinner_select_row()
        accmag.send_keys_arrow_down()
        accmag.send_keys_enter()
        time.sleep(1)
        self.save_img('账号管理页面跳转')
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()
