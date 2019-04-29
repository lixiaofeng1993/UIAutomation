#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:11
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_g_child_teacher.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_teacher import ChildTeacherPage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config
from common.random_upload import uploaded


class Testteacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.teacher = ChildTeacherPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_teacher')
    def test_a_teacher(self):
        """进入老师管理"""
        teacher = self.teacher
        teacher.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        teacher.click_teacher_manage()
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '进入老师管理栏失败！')
        self.log.info('进入 老师管理 成功.')
        self.save_img('老师管理')

    @BeautifulReport.add_test_img('test_b_newly_teacher')
    def test_b_newly_teacher(self):
        """新增老师"""
        teacher = self.teacher
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '当前页面不在老师管理栏，无法进行新增操作！')
        self.log.info('开始进行新增老师管理操作.')
        teacher.click_new_add_teacher_btn()
        time.sleep(1)
        self.assertEqual('添加老师', teacher.text_new_add_teacher(), '添加老师页面弹出异常！')
        self.log.info('添加老师页面正常显示，开始进行添加操作.')
        teacher.input_teacher_name('test')
        teacher.input_teacher_phone('18701137212')
        teacher.input_tsocialTitle_phone('测试职称')
        sex_list = teacher.elements_teacher_sex()
        self.random_check(sex_list, teacher)
        teacher.click_upload_teacher_img()
        uploaded()
        time.sleep(1)
        teacher.click_sure_btn()
        time.sleep(1)
        self.check_add_teacher(teacher)

    @BeautifulReport.add_test_img('test_c_edit_teacher')
    def test_c_edit_teacher(self):
        """编辑老师"""
        teacher = self.teacher
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '当前页面不在老师管理栏，无法进行编辑操作！')
        self.log.info('开始进行编辑老师管理操作.')
        self.check_add_teacher(teacher, make=1)
        time.sleep(1)
        self.assertEqual('修改老师', teacher.text_new_add_teacher(), '修改老师页面弹出异常！')
        self.log.info('修改老师页面正常显示，开始进行修改操作.')
        teacher.input_teacher_name('这是一个测试老师')
        teacher.input_teacher_phone('18701137211')
        teacher.input_tsocialTitle_phone('这是一个测试职称')
        sex_list = teacher.elements_teacher_sex()
        self.random_check(sex_list, teacher)
        teacher.click_upload_teacher_img()
        uploaded()
        time.sleep(1)
        teacher.click_sure_btn()
        time.sleep(1)
        self.check_add_teacher(teacher)

    @BeautifulReport.add_test_img('test_d_page_teacher')
    def test_d_page_teacher(self):
        """查询"""
        teacher = self.teacher
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '当前页面不在老师管理栏，无法进行查询操作！')
        self.log.info('开始进行查询操作.')
        self.check_add_teacher(teacher, make=4)
        teacher.input_text('这是一个测试老师')
        teacher.click_query_btn()
        self.check_add_teacher(teacher)
        self.driver.refresh()  # 刷新页面

    @BeautifulReport.add_test_img('test_e_delete_teacher')
    def test_e_delete_teacher(self):
        """删除老师"""
        teacher = self.teacher
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '当前页面不在老师管理栏，无法进行删除操作！')
        self.log.info('开始进行删除老师管理操作.')
        self.check_add_teacher(teacher, make=2)
        time.sleep(1)
        teacher.click_delete_sure_btn()
        if not self.check_add_teacher(teacher, make=3):
            self.log.info('测试老师删除成功.')
        else:
            self.log.error('测试老师删除失败！')

    @BeautifulReport.add_test_img('test_f_page_teacher')
    def test_f_page_teacher(self):
        """老师管理翻页"""
        teacher = self.teacher
        self.assertEqual(teacher.text_check_teacher_text(), '老师管理', '当前页面不在老师管理栏，无法进行翻页操作！')
        self.log.info('开始进行翻页操作.')
        t_num, num = self.get_page_number(teacher)
        skip_page = int(random.randint(0, num) / 10) + 1  # 取整数 + 1
        if t_num > 10:
            teacher.input_skip_page(skip_page)
            teacher.send_keys_enter()
            page_num_list = teacher.elements_page_num()
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
            self.log.info('老师管理项数量太少，无法切换页面.')

    def check_add_teacher(self, teacher, make=0):
        time.sleep(1)
        t_num, num = self.get_page_number(teacher)
        for i in range(num):
            time.sleep(1)
            already_info_name = teacher.elements_page_teacher_name()
            for j in range(len(already_info_name)):
                if already_info_name[j].text in ['test', '这是一个测试老师']:
                    option_btn_loc = (
                        'xpath', '//tbody[@class="ant-table-tbody"]/tr[{}]/td[last()]/button'.format(j + 1))
                    if make == 1:
                        edit_btn_loc = ('xpath', '//body/div[last()]/div/div/ul/li[1]')
                        teacher.move(option_btn_loc, edit_btn_loc)
                        time.sleep(1)
                        self.log.info('选择 测试老师 成功，准备进行编辑操作. {}'.format(already_info_name[j].text))
                        return
                    elif make == 2:
                        delete_btn_loc = ('xpath', '//body/div[last()]/div/div/ul/li[2]')
                        teacher.move(option_btn_loc, delete_btn_loc)
                        time.sleep(1)
                        self.log.info('选择 测试老师 成功，准备进行删除操作. {}'.format(already_info_name[j].text))
                        return
                    elif make == 3:
                        return True
                    elif make == 4:
                        self.log.info('准备进行查询操作.')
                    else:
                        self.log.info('添加/编辑/查询老师成功. {}'.format(already_info_name[j].text))
            time.sleep(1)
            teacher.click_next_page()

    def get_page_number(self, teacher):
        time.sleep(1)
        tag_num = teacher.text_tag_number()
        t_nun = int(re.findall('(\d+)', tag_num)[0])
        self.log.info('老师数量是：{}'.format(str(t_nun)))
        num = int(int(t_nun) / 10) + 1
        return t_nun, num

    def random_check(self, lis, teacher, make=0, list_name='', info=0):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
            self.log.info('传入list长度：{}'.format(len(lis)))
            if info == 1:
                random_num = random.randint(0, len(lis) - 2)
            else:
                random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 6
            if make == 1:
                update_class = teacher.elements_page_info_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            elif make == 2:
                update_class = teacher.elements_check_info_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            time.sleep(1)
            if make in [1, 2]:
                return [update_class, random_num]
        else:
            self.log.error('random_check函数传参错误！')


if __name__ == '__main__':
    unittest.main()
