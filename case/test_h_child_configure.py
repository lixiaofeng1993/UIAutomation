#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 10:35
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_h_child_configure.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from selenium.common.exceptions import *
from BeautifulReport import BeautifulReport
from page.page_child_configure import ChildConfigurePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class TestConfigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.configure = ChildConfigurePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_configure')
    def test_a_configure(self):
        """进入标签管理"""
        configure = self.configure
        configure.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        configure.click_configure_manage()
        configure.elements_all_manage()[0].click()
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '进入标签管理栏失败！')
        self.log.info('进入 标签管理 成功.')
        self.save_img('标签管理')

    @BeautifulReport.add_test_img('test_b_newly_user_tag_configure')
    def test_b_newly_user_tag_configure(self):
        """新建用户标签"""
        configure = self.configure
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行新建用户标签操作！')
        self.log.info('开始进行新建用户标签操作.')
        self.check_tag_already_exist(configure, type='用户标签', edit=0)
        time.sleep(1)
        configure.click_newly_tag_btn()
        time.sleep(1)
        self.assertEqual('新增标签', configure.text_check_newly_tag(), '没有弹出新增标签弹框！')
        self.log.info('新增标签弹框显示正常.')
        configure.click_tag_type()
        configure.elements_check_tag_type()[0].click()
        self.log.info('选择用户标签.')
        configure.input_tag_name('test')
        configure.click_upload_sure_btn()
        if configure.text_tag_already_exist_error() == '已经有重复的标签了，不能多次添加':
            self.log.error('标签已存在，删除已存在标签失败！')
            configure.click_upload_cancel_btn()
        else:
            self.driver.refresh()  # 刷新页面
            self.check_tag_already_exist(configure, type='用户标签', edit=2)

    @BeautifulReport.add_test_img('test_c_newly_lesson_tag_configure')
    def test_c_newly_lesson_tag_configure(self):
        """新建课程标签"""
        configure = self.configure
        self.driver.refresh()  # 刷新页面
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行新建课程标签操作！')
        self.log.info('开始进行新建课程标签操作.')
        self.check_tag_already_exist(configure, type='课程标签', edit=0)
        time.sleep(1)
        configure.click_newly_tag_btn()
        time.sleep(1)
        self.assertEqual('新增标签', configure.text_check_newly_tag(), '没有弹出新增标签弹框！')
        self.log.info('新增标签弹框显示正常.')
        configure.click_tag_type()
        configure.elements_check_tag_type()[1].click()
        self.log.info('选择课程标签.')
        configure.input_tag_name('测试标签')
        configure.click_upload_sure_btn()
        if configure.text_tag_already_exist_error() == '已经有重复的标签了，不能多次添加':
            self.log.error('标签已存在，删除已存在标签失败！')
            configure.click_upload_cancel_btn()
        else:
            self.driver.refresh()  # 刷新页面
            self.check_tag_already_exist(configure, type='课程标签', edit=2)

    @BeautifulReport.add_test_img('test_d_edit_user_tag_configure')
    def test_d_edit_user_tag_configure(self):
        """编辑用户标签"""
        configure = self.configure
        self.driver.refresh()  # 刷新页面
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行编辑用户标签操作！')
        self.log.info('开始进行编辑用户标签操作.')
        self.check_tag_already_exist(configure, type='用户标签', edit=1)
        self.assertEqual('编辑标签', configure.text_check_newly_tag(), '没有弹出编辑标签弹框！')
        self.log.info('编辑标签弹框显示正常.')
        configure.click_tag_type()
        configure.elements_check_tag_type()[0].click()
        self.log.info('选择用户标签.')
        configure.input_tag_name('测试标签')
        configure.click_upload_sure_btn()
        if configure.text_tag_already_exist_error() == '已经有重复的标签了，不能多次添加':
            self.log.error('标签已存在，删除已存在标签失败！')
            configure.click_upload_cancel_btn()
        else:
            self.driver.refresh()  # 刷新页面
            self.check_tag_already_exist(configure, type='用户标签', edit=2)

    @BeautifulReport.add_test_img('test_e_edit_user_tag_configure')
    def test_e_edit_user_tag_configure(self):
        """编辑课程标签"""
        configure = self.configure
        self.driver.refresh()  # 刷新页面
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行编辑课程标签操作！')
        self.log.info('开始进行编辑课程标签操作.')
        self.check_tag_already_exist(configure, type='课程标签', edit=1)
        self.assertEqual('编辑标签', configure.text_check_newly_tag(), '没有弹出编辑标签弹框！')
        self.log.info('编辑标签弹框显示正常.')
        configure.click_tag_type()
        configure.elements_check_tag_type()[1].click()
        self.log.info('选择课程标签.')
        configure.input_tag_name('test')
        configure.click_upload_sure_btn()
        if configure.text_tag_already_exist_error() == '已经有重复的标签了，不能多次添加':
            self.log.error('标签已存在，删除已存在标签失败！')
            configure.click_upload_cancel_btn()
        else:
            self.driver.refresh()  # 刷新页面
            self.check_tag_already_exist(configure, type='课程标签', edit=2)

    @BeautifulReport.add_test_img('test_f_page_configure')
    def test_f_page_configure(self):
        """标签翻页"""
        configure = self.configure
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行翻页操作！')
        self.log.info('开始进行翻页操作.')
        t_num, num = self.get_page_number(configure)
        skip_page = int(random.randint(0, num) / 10) + 1  # 取整数 + 1
        if t_num > 10:
            configure.input_skip_page(skip_page)
            configure.send_keys_enter()
            page_num_list = configure.elements_page_num()
            for element in page_num_list:
                class_name = element.get_attribute('class')
                if 'ant-pagination-item-active' in class_name:
                    title = element.get_attribute('title')  # 取出当前页面选中的页数
                    self.assertEqual(skip_page, int(title), '跳转页面失败！')
                    self.log.info('跳转页面成功.')
            if len(page_num_list) > 3:
                time.sleep(1)
                page_num_list[1].click()
                time.sleep(1)
                page_num_list[-2].click()
                self.log.info('切换页面完成.')
        else:
            self.log.info('标签数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_g_page_configure')
    def test_g_page_configure(self):
        """查询"""
        configure = self.configure
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行查询操作！')
        self.log.info('开始进行查询操作.')
        configure.input_text('test')
        configure.click_query_btn()
        num = self.get_page_number(configure)[1]
        for i in range(num):
            tag_name = configure.elements_already_exist_tag_name()
            for element in tag_name:
                if 'test' in element.text:
                    self.log.info('查询成功. {}'.format(element.text))
            time.sleep(1)
            configure.click_next_page()

    def get_page_number(self, configure):
        time.sleep(1)
        tag_num = configure.text_tag_number()
        t_nun = int(re.findall('(\d+)', tag_num)[0])
        self.log.info('标签数量是：{}'.format(str(t_nun)))
        num = int(int(t_nun) / 10) + 1
        return t_nun, num

    def check_tag_already_exist(self, configure, type='', edit=0):
        """检查标签是否已经存在"""
        time.sleep(1)
        num = self.get_page_number(configure)[1]
        make = False
        g = 0
        for i in range(num):
            time.sleep(1)
            tag_name = configure.elements_already_exist_tag_name()
            tag_type = configure.elements_exist_tag_type()
            for j in range(len(tag_name)):
                try:
                    tag_type_name = tag_type[j].text
                    if tag_type_name == type:
                        if tag_name[j].text in ['test', '测试标签']:
                            if edit == 1:
                                self.log.info('{} 已经存在 {} ，进行编辑操作.'.format(tag_type_name, tag_name[j].text))
                                option_btn_loc = (
                                    'xpath',
                                    '//div[@class="ant-table-body"]/table/tbody/tr[{}]/td[4]/button'.format(j + 1))
                                delete_btn_loc = ('xpath',
                                                  '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')
                                time.sleep(1)
                                configure.move(option_btn_loc, delete_btn_loc)
                                time.sleep(1)
                                return
                            if edit == 2:
                                if tag_name[j].text in ['test', '测试标签'] and tag_type[j].text == type:
                                    tag_type_name = tag_type[j].text
                                    self.log.info('{} 新增/编辑 {} 成功.'.format(tag_type_name, tag_name[j].text))
                                else:
                                    self.log.error('')
                            else:
                                self.log.info('{} 已经存在 {} ，进行删除操作.'.format(tag_type_name, tag_name[j].text))
                                if make:
                                    option_btn_loc = (
                                        'xpath',
                                        '//div[@class="ant-table-body"]/table/tbody/tr[{}]/td[4]/button'.format(j - g))
                                    g += 1
                                else:
                                    option_btn_loc = (
                                        'xpath',
                                        '//div[@class="ant-table-body"]/table/tbody/tr[{}]/td[4]/button'.format(j + 1))
                                delete_btn_loc = ('xpath',
                                                  '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')
                                time.sleep(1)
                                configure.move(option_btn_loc, delete_btn_loc)
                                time.sleep(1)
                                configure.click_delete_sure_btn()
                                make = True
                except StaleElementReferenceException:
                    pass
            time.sleep(1)
            configure.click_next_page()


if __name__ == '__main__':
    unittest.main()
