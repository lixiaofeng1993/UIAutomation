#coding:utf-8

import os
import time
import unittest

from BeautifulReport import BeautifulReport

from common import read_config
from common.basics import open_browser
from common.logger import Log,img_path
from page.page_child_login import ChildLoginPage
from tmp.eg.page_teacher_management import TeacherManagementPage


class TestTeacherManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.url = read_config.url
        cls.login = ChildLoginPage(cls.driver)
        cls.teamag = TeacherManagementPage(cls.driver)
        cls.log = Log()
        cls.img_path = img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self,img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path,img_name))

    @BeautifulReport.add_test_img('teacher_management')
    def test_01_teacher_management(self):
        teamag = self.teamag
        teamag.open(self.url,t='育儿锦囊后台管理系统')
        time.sleep(1)
        self.log.info('输入账号密码登录...')
        self.login.input_user('sunbin')
        self.login.input_password('sunbin_2018')
        self.login.click_login_btn()
        time.sleep(2)
        teamag.click_teacher_management()
        time.sleep(2)


    @BeautifulReport.add_test_img('search_teacher')
    def test_02_search_teacher(self):
        teamag = self.teamag
        self.log.info('------搜索老师------')
        teamag.input_search_teachername()
        teamag.click_query_btn()
        time.sleep(2)


    @BeautifulReport.add_test_img('add_teacher')
    def test_03_add_teacher(self):
        teamag = self.teamag
        self.log.info('------添加老师------')
        teamag.click_add_teacher()
        time.sleep(1)
        teamag.input_add_teacher_name()
        teamag.input_add_teacher_phone()
        teamag.input_add_teacher_title()
        teamag.click_select_sex_girl()
        teamag.click_addtea_upload_photo()
        os.system(r'D:\GitHub\SnapeSun_Lolita\UIAutomation\driver\\upfile1.exe "D:\UIAutomation\data\ad\1.gif"')
        time.sleep(1)
        self.save_img('添加老师')
        teamag.click_addtea_determine_btn()
        time.sleep(1)


    @BeautifulReport.add_test_img('edit_teacher')
    def test_04_edit_teacher(self):
        teamag = self.teamag
        self.log.info('------编辑老师信息------')
        teamag.click_teacher_management()
        teamag.move_edittea_operating_btn()
        time.sleep(1)
        teamag.input_add_teacher_name()
        teamag.input_add_teacher_phone()
        teamag.input_add_teacher_title()
        teamag.click_select_sex_girl()
        teamag.click_edittea_upload_photo()
        os.system(r'D:\GitHub\SnapeSun_Lolita\UIAutomation\driver\upfile1.exe "D:\UIAutomation\data\ad\1.gif"')
        time.sleep(1)
        self.save_img('编辑老师')
        teamag.click_edittea_detemine_btn()
        time.sleep(1)

    @BeautifulReport.add_test_img('delete_teacher')
    def test_05_delete_teacher(self):
        teamag = self.teamag
        self.log.info('------删除老师------')
        teamag.move_deletetea_operating_btn()
        time.sleep(1)
        self.save_img('删除老师')
        teamag.click_dialog_delete_teacher_determine()
        time.sleep(1)

    def test_06_jump_page(self):
        teamag = self.teamag
        self.log.info('----------页面跳转----------')
        teamag.click_spinner_select_row()
        teamag.send_keys_arrow_down()
        teamag.send_keys_enter()
        time.sleep(1)
        teamag.input_jumper_page()
        teamag.send_keys_enter()
        time.sleep(1)







if __name__ == '__main__':
    unittest.main()
