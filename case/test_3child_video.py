#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 17:04
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_3child_video.py
# @Software: PyCharm
import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_video import ChildVideoPage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class TestVideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.video = ChildVideoPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_video')
    def test_a_video(self):
        """进入视频管理"""
        video = self.video
        video.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        video.click_video_manage()
        self.assertEqual(video.text_video_manage(), '视频管理', '进入视频管理栏失败！')
        self.log.info('进入 视频管理 成功.')
        self.save_img('视频管理')

    @BeautifulReport.add_test_img('test_b_newly_video')
    def test_b_newly_video(self):
        """新建视频"""
        video = self.video
        video.click_newly_video()
        self.assertEqual(video.text_newly_video(), '新增视频', '进入 新增视频 页失败！')
        self.log.info('进入 新增视频 页成功.')
        video.click_teacher()
        video.send_keys_enter()
        time.sleep(1)
        video.click_video_class1()
        try:
            time.sleep(1)
            video.click_video_class2()
            video.click_video_class3()
        except AttributeError:
            video.click_video_class2_2()
            video.click_video_class3_3()
        video.input_video_title('test')
        video.click_link()
        time.sleep(1)
        video.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        video.click_cover_img()
        os.system('D:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        video.click_share_img()
        os.system('D:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        self.log.info('上传封面图片和分享图片成功.')
        video.click_sure_btn()
        self.assertEqual('+ 上传', video.text_upload_btn(), '视频信息保存错误！')
        self.log.info('视频信息保存成功.')

    @BeautifulReport.add_test_img('test_c_upload_video')
    def test_c_upload_video(self):
        """上传视频"""
        video = self.video
        self.assertEqual('+ 上传', video.text_upload_btn(), '当前页面没有上传按钮，无法继续操作！')
        self.log.info('上传视频操作开始.')
        video.click_upload_btn()
        time.sleep(1)
        video.input_upload_video_name('test')
        video.click_typesetting()
        video.click_upload_img()
        os.system('D:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        time.sleep(1)
        video.click_upload_video()
        os.system('D:\\UIAutomation\driver\\upvideo1.exe "D:\\UIAutomation\data\\1.mp4"')
        time.sleep(1)
        while True:
            video_success = video.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', video_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('视频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        video.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('test', video.text_check_upload_success(), '上传视频失败！')
        self.log.info('上传视频成功.')
        video.click_video_manage()

    @BeautifulReport.add_test_img('test_d_edit_video')
    def test_d_edit_video(self):
        """视频信息编辑"""
        video = self.video
        self.assertEqual('+ 新增视频', video.text_newly_btn_video(), '当前页面不在视频管理页，无法进行编辑操作！')
        self.log.info('选择第一个视频专辑，进行编辑操作.')
        video_name = video.text_edit_video_name()
        print(video_name)
        try:
            video.click_edit_video_name()
        except Exception:
            time.sleep(1)
            video.click_edit_video_name()
        self.assertEqual(video_name, video.text_video_title(), '进入视频编辑页面错误！')
        self.log.info('进入视频：{} 编辑页成功.'.format(video_name))
        time.sleep(1)
        video.input_video_title(video_name + 'test')
        video.click_edit_video_tag()
        video.click_edit_video_user_tag()
        video.js_scroll_top()
        video.click_edit_save()
        time.sleep(1)
        video_name_new = video.text_edit_video_name()
        self.assertEqual(video_name + 'test', video_name_new, '编辑失败，视频名称验证错误！')
        self.log.info('编辑视频成功.')

    @BeautifulReport.add_test_img('test_e_edit_video_num')
    def test_e_edit_video_num(self):
        """视频编辑"""
        video = self.video
        self.assertEqual('+ 新增视频', video.text_newly_btn_video(), '当前页面不在视频管理页，无法进行编辑操作！')
        try:
            video.click_edit_video_num()
        except Exception:
            time.sleep(1)
            video.click_edit_video_num()
        self.assertEqual('+ 上传', video.text_upload_btn(), '当前页面没有上传按钮，无法进行删除操作！')
        if video.text_no_data() == '暂无数据':
            self.log.info('页面暂无数据，请先上传视频.')
        else:
            self.log.info('页面确认，可以进行删除操作.')
            video.click_choice_video()
            self.assertEqual('删 除', video.text_delete_btn(), '勾选视频失败！')
            self.log.info('勾选视频成功.')
            video.click_delete_btn()
            time.sleep(1)
            # video.click_delete_sure_btn()
            try:
                video.click_cancel_btn()
            except AttributeError:
                video.click_cancel_btn1()
            # self.assertIsNone(video.text_delete_btn(), '删除视频失败！')
            self.log.info('删除视频成功.')
        video.back()

    @BeautifulReport.add_test_img('test_f_page_video')
    def test_f_page_video(self):
        """视频翻页"""
        video = self.video
        page_num = video.text_page_video()
        nun = int(re.findall('(\d+)', page_num)[0])
        self.log.info('nun: {}'.format(nun))
        if nun > 10:
            skip_page = int(random.randint(0, nun) / 10) + 1  # 取整数 + 1
            video.input_skip_page(skip_page)
            video.send_keys_enter()
            page_num_list = video.elements_page_num()
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
            if video.element_top():
                time.sleep(1)
                video.click_top()
                time.sleep(1)
                self.log.info('返回页面顶部.')
        else:
            self.log.info('视频数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_g_video_query')
    def test_g_video_query(self):
        """查询视频"""
        video = self.video
        self.assertEqual(video.text_newly_btn_video(), '+ 新增视频', '不在 视频管理 页面，无法进行查询操作！')
        self.log.info('正在进行视频查询操作...')
        time.sleep(1)
        video.input_video_query('test')
        video.click_video_query_btn()
        time.sleep(1)
        self.assertIn('test', video.text_edit_video_name(), '查询失败，没有发现查询视频！')
        self.log.info('视频查询成功.')


if __name__ == '__main__':
    unittest.main()
