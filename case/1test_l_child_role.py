#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 10:35
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_h_child_cla.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from selenium.common.exceptions import *
from BeautifulReport import BeautifulReport
from page.page_child_role import ChildRolePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class Testcla(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.role = ChildRolePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_role')
    def test_a_role(self):
        """进入角色管理"""
        role = self.role
        role.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        role.click_role_manage()
        role.elements_all_manage()[0].click()
        self.assertEqual(role.text_check_role_text(), '角色管理', '进入角色管理栏失败！')
        self.log.info('进入 角色管理 成功.')
        self.save_img('角色管理')

    @BeautifulReport.add_test_img('test_b_new_add_cla')
    def test_b_new_add_cla(self):
        """添加角色管理"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行添加角色管理操作！')
        self.log.info('开始进行添加角色管理操作.')
        if self.check_page_test(role):
            self.log.info('角色 测试部门 已存在.')
            return
        else:
            role.click_new_add_role_btn()
            time.sleep(1)
            self.assertEqual('新增角色', role.text_check_text_role(), '新增角色页面弹出异常！')
            self.log.info('开始进行新增操作.')
            role.input_new_role_name('测试部门')
            role_config = role.elements_new_role_config()
            self.random_check(role_config, role)
            role.click_sure_btn()
            time.sleep(1)
            if self.check_page_test(role):
                self.log.info('新增 测试部门 角色成功.')
            else:
                self.log.info('新增 测试部门 角色失败！')

    @BeautifulReport.add_test_img('test_c_edit_cla')
    def test_c_edit_cla(self):
        """编辑角色管理"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行编辑角色管理操作！')
        self.log.info('开始进行编辑角色管理操作.')
        j = self.check_page_test(role, make=1)
        if not j:
            self.log.info('没有找到 测试部门 无法进行编辑操作！')
            return
        else:
            time.sleep(1)
            self.assertEqual('编辑角色', role.text_check_text_role(), '编辑角色页面弹出异常！')
            self.log.info('开始进行编辑操作.')
            role.input_new_role_name('test')
            role_config = role.elements_new_role_config()
            check_power, random_num = self.random_check(role_config, role, make=1)
            role.click_sure_btn()
            time.sleep(1)
            role.elements_set_power_btn()[j].click()
            time.sleep(1)
            if self.check_page_test(role):
                self.log.info('编辑 test 角色成功.')
            else:
                self.log.info('编辑 test 角色失败！')
            role.click_cancel_btn()

    @BeautifulReport.add_test_img('test_d_page_role')
    def test_d_page_role(self):
        """角色管理翻页"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行翻页操作！')
        self.log.info('开始进行翻页操作.')
        t_num, num = self.get_page_number(role)
        skip_page = int(random.randint(0, num) / 10) + 1  # 取整数 + 1
        if t_num > 10:
            role.input_skip_page(skip_page)
            role.send_keys_enter()
            page_num_list = role.elements_page_num()
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
            self.log.info('角色管理项数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_e_query_role')
    def test_e_query_role(self):
        """角色管理查询"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行查询操作！')
        self.log.info('开始进行查询操作.')
        role.input_query_info('测试')
        time.sleep(1)
        role.click_query_info_btn()
        if self.check_page_test(role):
            self.log.info('查询成功.')
        else:
            self.log.error('查询失败！')

    def check_page_test(self, role, make=0):
        t_num, num = self.get_page_number(role)
        if t_num > 10:
            for i in range(num):
                time.sleep(1)
                for j in range(len(role.elements_role_name())):
                    if role.elements_role_name()[j].text in ['测试部门', 'test']:
                        if make == 1:
                            role.elements_set_power_btn()[j].click()
                        return j
            time.sleep(1)
            role.click_next_page()
        else:
            for j in range(len(role.elements_role_name())):
                if role.elements_role_name()[j].text in ['测试部门', 'test']:
                    if make == 1:
                        role.elements_set_power_btn()[j].click()
                    return j

    def get_page_number(self, role):
        time.sleep(1)
        tag_num = role.text_tag_number()
        t_nun = int(re.findall('(\d+)', tag_num)[0])  # 条数
        self.log.info('标签数量是：{}'.format(str(t_nun)))
        num = int(int(t_nun) / 10) + 1  # 页数
        return t_nun, num

    def random_check(self, lis, role, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
            self.log.info('传入list长度：{}'.format(len(lis)))
            random_num = random.randint(0, len(lis) - 1)
            if make == 1:
                update_class = role.elements_check_role_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            if 'checked' in role.elements_check_is_checked()[random_num].get_attribute('class'):
                pass
            else:
                lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            time.sleep(1)
            if make == 1:
                return [update_class, random_num]
        else:
            self.log.error('random_check函数传参错误！')


if __name__ == '__main__':
    # unittest.main()
    from selenium import webdriver

    # 驱动路径
    driver_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # chrome启动静默模式;默认显示浏览器界面
    if read_config.chrome_interface != 'True':
        option.add_argument('headless')
    executable_path = os.path.join(driver_path, 'driver\\chromedriver.exe')
    # executable_path = os.path.join(driver_path, 'driver/chromedriver')
    driver = webdriver.Chrome(chrome_options=option, executable_path=executable_path)
    driver.get('file:///C:/Users/liyongfeng/Desktop/1.html')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath(".//*[@id='selectdemo']/option[3]").click()
    driver.implicitly_wait(5)
    # driver.find_element_by_name('lanqiu').click() 一般的下拉框，点两下，都可以选中的