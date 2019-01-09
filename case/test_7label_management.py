import unittest
import time
from common.logger import Log,img_path
from common import read_config
from common.basics import open_browser
from BeautifulReport import BeautifulReport
from page.page_child_login import ChildLoginPage
from page.page_label_management import LabelManagementPage


class TestLabelManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.url = read_config.url
        cls.login = ChildLoginPage(cls.driver)
        cls.labelmag = LabelManagementPage(cls.driver)
        cls.log = Log()
        cls.img_path = img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self,img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path,img_name))

    def test_01_label_management(self):
        labelmag = self.labelmag
        labelmag.open(self.url,t='育儿锦囊后台管理系统')
        self.log.info('输入账号密码登录...')
        self.login.input_user('sunbin')
        self.login.input_password('sunbin_2018')
        self.login.click_login_btn()
        time.sleep(2)
        labelmag.click_configration_management()
        labelmag.cliak_label_management()
        time.sleep(2)

    @BeautifulReport.add_test_img('search_label')
    def test_02_search_label(self):
        labelmag = self.labelmag
        self.log.info('----------查询标签----------')
        labelmag.input_search_label_name()
        labelmag.click_btn_search()
        self.save_img('查询标签')
        time.sleep(2)

    @unittest.skip
    @BeautifulReport.add_test_img('new_label')
    def test_03_new_label(self):
        labelmag = self.labelmag
        self.log.info('----------新增标签----------')
        labelmag.cliak_label_management()
        labelmag.click_new_label()
        time.sleep(1)
        labelmag.click_spinner_label_type()
        labelmag.send_keys_arrow_down()
        labelmag.send_keys_enter()
        labelmag.input_newlabel_label_name()
        time.sleep(1)
        self.save_img('新增标签')
        labelmag.click_determine_btn()
        time.sleep(2)

    @unittest.skip
    def test_04_modify_label(self):
        labelmag = self.labelmag
        self.log.info('----------修改标签----------')
        labelmag.cliak_label_management()
        labelmag.move_click_modify_label()
        time.sleep(2)
        labelmag.click_edit_spinner_label_type()
        labelmag.send_keys_arrow_down()
        labelmag.send_keys_enter()
        labelmag.input_newlabel_label_name()
        time.sleep(1)
        self.save_img('修改标签')
        labelmag.click_cancel_btn()
        time.sleep(3)

    def test_05_delete_label(self):
        labelmag = self.labelmag
        self.log.info('----------删除标签----------')
        labelmag.cliak_label_management()
        labelmag.move_click_delete_label()
        time.sleep(1)
        self.log.info('----删除标签弹出dialog，取消与确定按钮元素----------')
        labelmag.click_cancel_btn()

        time.sleep(2)





if __name__ == '__main__':
    unittest.main()