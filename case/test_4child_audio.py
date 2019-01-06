#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:19
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_4child_audio.py
# @Software: PyCharm
import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_audio import ChildAudioPage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class Testaudio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.audio = ChildAudioPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_audio')
    def test_a_audio(self):
        """进入音频管理"""
        audio = self.audio
        audio.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        audio.click_audio_manage()
        self.assertEqual(audio.text_audio_manage(), '音频管理', '进入音频管理栏失败！')
        self.log.info('进入 音频管理 成功.')
        self.save_img('音频管理')

    @BeautifulReport.add_test_img('test_b_newly_audio')
    def test_b_newly_audio(self):
        """新建音频"""
        audio = self.audio
        audio.click_newly_audio()
        self.assertEqual(audio.text_newly_audio(), '新增音频', '进入 新增音频 页失败！')
        self.log.info('进入 新增音频 页成功.')
        audio.click_one_audio()
        audio.click_teacher()
        audio.send_keys_enter()
        time.sleep(1)
        audio.click_audio_class1()
        try:
            time.sleep(1)
            audio.click_audio_class2()
            audio.click_audio_class3()
        except AttributeError:
            audio.click_audio_class2_2()
            audio.click_audio_class3_3()
        audio.input_audio_title('test')
        audio.click_link()
        time.sleep(1)
        audio.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        audio.click_cover_img()
        os.system('G:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        audio.click_share_img()
        os.system('G:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        self.log.info('上传封面图片和分享图片成功.')
        time.sleep(1)
        audio.click_sure_btn()
        self.assertEqual('+ 上传', audio.text_upload_btn(), '音频信息保存错误！')
        self.log.info('音频信息保存成功.')

    @BeautifulReport.add_test_img('test_c_upload_audio')
    def test_c_upload_audio(self):
        """上传音频"""
        audio = self.audio
        self.assertEqual('+ 上传', audio.text_upload_btn(), '当前页面没有上传按钮，无法继续操作！')
        self.log.info('上传音频操作开始.')
        audio.click_upload_btn()
        time.sleep(1)
        audio.input_upload_audio_name('test')
        audio.click_typesetting()
        audio.click_upload_img()
        os.system('G:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        time.sleep(1)
        audio.click_upload_audio()
        os.system('G:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.wav"')
        time.sleep(1)
        while True:
            audio_success = audio.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', audio_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('音频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        audio.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('test', audio.text_check_upload_success(), '上传音频失败！')
        self.log.info('上传音频成功.')
        audio.click_audio_manage()

    @BeautifulReport.add_test_img('test_d_edit_audio')
    def test_d_edit_audio(self):
        """音频信息编辑"""
        audio = self.audio
        self.assertEqual('+ 新增音频', audio.text_newly_btn_audio(), '当前页面不在音频管理页，无法进行编辑操作！')
        self.log.info('选择第一个音频专辑，进行编辑操作.')
        audio_name = audio.text_edit_audio_name()
        try:
            audio.click_edit_audio_name()
        except Exception:
            time.sleep(1)
            audio.click_edit_audio_name()
        self.assertEqual(audio_name, audio.text_audio_title(), '进入音频编辑页面错误！')
        self.log.info('进入音频：{} 编辑页成功.'.format(audio_name))
        time.sleep(1)
        audio.input_audio_title(audio_name + 'test')
        audio.click_edit_audio_tag()
        audio.click_edit_audio_user_tag()
        audio.js_scroll_top()
        audio.click_edit_save()
        if audio.element_video_name_error():
            self.log.error('视频名称过长错误，重新输入.')
            audio.input_audio_title('test')
            audio_name = ''
            audio.click_edit_save()
        time.sleep(1)
        audio_name_new = audio.text_edit_audio_name()
        self.assertEqual(audio_name + 'test', audio_name_new, '编辑失败，音频名称验证错误！')
        self.log.info('编辑音频成功.')

    @BeautifulReport.add_test_img('test_e_edit_audio_num')
    def test_e_edit_audio_num(self):
        """音频编辑"""
        audio = self.audio
        if audio.element_top():
            time.sleep(1)
            audio.click_top()
            time.sleep(1)
            self.log.info('返回页面顶部.')
        self.assertEqual('+ 新增音频', audio.text_newly_btn_audio(), '当前页面不在音频管理页，无法进行编辑操作！')
        try:
            audio.click_edit_audio_num()
        except Exception:
            time.sleep(1)
            audio.click_edit_audio_num()
        self.assertEqual('+ 上传', audio.text_upload_btn(), '当前页面没有上传按钮，无法进行删除操作！')
        if audio.text_no_data() == '暂无数据':
            self.log.info('页面暂无数据，请先上传音频.')
        else:
            self.log.info('页面确认，可以进行删除操作.')
            audio.click_choice_audio()
            self.assertEqual('删 除', audio.text_delete_btn(), '勾选音频失败！')
            self.log.info('勾选音频成功.')
            audio.click_delete_btn()
            time.sleep(1)
            # audio.click_delete_sure_btn()
            try:
                audio.click_cancel_btn1()
            except AttributeError:
                audio.click_cancel_btn()
            # self.assertIsNone(audio.text_delete_btn(), '删除音频失败！')
            self.log.info('删除音频成功.')
        audio.back()

    @BeautifulReport.add_test_img('test_f_page_audio')
    def test_f_page_audio(self):
        """音频翻页"""
        audio = self.audio
        page_num = audio.text_page_audio()
        nun = int(re.findall('(\d+)', page_num)[0])
        if nun > 10:
            skip_page = int(random.randint(0, nun) / 10) + 1  # 取整数 + 1
            print(skip_page)
            audio.input_skip_page(skip_page)
            audio.send_keys_enter()
            page_num_list = audio.elements_page_num()
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
            if audio.element_top():
                time.sleep(1)
                audio.click_top()
                time.sleep(1)
                self.log.info('返回页面顶部.')
        else:
            self.log.info('音频数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_g_audio_query')
    def test_g_audio_query(self):
        """查询音频"""
        audio = self.audio
        self.assertEqual(audio.text_newly_btn_audio(), '+ 新增音频', '不在 音频管理 页面，无法进行查询操作！')
        self.log.info('正在进行音频查询操作...')
        time.sleep(1)
        audio.click_one_audio_btn()
        audio.input_audio_query('test')
        audio.click_audio_query_btn()
        time.sleep(1)
        self.assertIn('test', audio.text_edit_audio_name(), '查询失败，没有发现查询音频！')
        self.log.info('音频查询成功.')


if __name__ == '__main__':
    unittest.main()
