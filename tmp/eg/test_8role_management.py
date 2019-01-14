import time
import unittest

from BeautifulReport import BeautifulReport

from common import read_config
from common.basics import open_browser
from common.logger import Log, img_path
from page.page_child_login import ChildLoginPage
from tmp.eg.page_role_management import RoleManagementPage


class TestRoleManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.rolemag = RoleManagementPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_search_role')
    def test_01_search_role(self):
        rolemag = self.rolemag
        rolemag.open(self.url,t='育儿锦囊后台管理系统')
        self.log.info('输入账号密码登录......')
        self.login.input_user('sunbin')
        self.login.input_password('sunbin_2018')
        self.login.click_login_btn()
        time.sleep(2)
        rolemag.click_permission_manager()
        time.sleep(2)
        rolemag.click_role_management()
        time.sleep(2)
        rolemag.input_role_text()
        rolemag.click_button_search()
        rolemag.click_icon_search() #点击搜索图标进行搜索
        time.sleep(2)
        self.save_img('搜索角色名称')

    @BeautifulReport.add_test_img('test_add_role')
    def test_02_add_role(self):
        self.log.info('------------------add role---------------------')
        rolemag = self.rolemag
        rolemag.click_btn_addrole()
        time.sleep(1)
        rolemag.input_dialog_addrole()
        rolemag.click_checkBox_add_permissionConfig()
        self.save_img('创建角色')
        time.sleep(2)
        rolemag.click_dialog_addRoleName_cancel()
        time.sleep(1)
        rolemag.click_role_management()
        time.sleep(1)


    @BeautifulReport.add_test_img('test_set_permission')
    def test_03_set_permission(self):
        self.log.info('----------set permission start----------')
        rolemag = self.rolemag
        rolemag.click_btn_set_permission()
        print(type(rolemag.checkBox_permissionConfiguration_loc))
        time.sleep(1)
        rolemag.input_dialogInput_rolename()
        time.sleep(1)
        rolemag.click_checkbox_permissionConfiguration()
        time.sleep(1)
        rolemag.click_dialog_permissionconfig_cancel()
        time.sleep(2)

    @BeautifulReport.add_test_img('test_select_pagerow')
    def test_04_select_pagerow(self):
        self.log.info('----------select page row start ----------')
        rolemag = self.rolemag
        rolemag.click_spinner_selectrow()
        time.sleep(1)
        rolemag.send_keys_enter()
        self.save_img('选择每页显示条数')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_select_pages')
    def test_05_select_pages(self):
        self.log.info('----------select pages start----------')
        rolemag = self.rolemag
        rolemag.input_jumperpages()
        time.sleep(1)
        rolemag.send_keys_enter()
        self.save_img('跳转N页')
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()


