#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:19
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_d_child_audio.py
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
from common.random_upload import uploaded


class Testaudio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.audio = ChildAudioPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

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
        audio.click_teacher()
        teacher_name = audio.elements_check_teacher_name()
        self.random_check(teacher_name, list_name='teacher_name')
        time.sleep(1)
        audio.click_audio_class1()
        time.sleep(1)
        audio_class2 = audio.elements_audio_class2()
        self.random_check(audio_class2, list_name='audio_class2')
        time.sleep(1)
        audio_class3 = audio.elements_audio_class3()
        self.random_check(audio_class3, list_name='audio_class3')
        audio.input_audio_title('这是一个测试音频')
        audio.input_description('这是一个测试描述')
        time.sleep(1)
        course_tag = audio.elements_course_tag()
        self.random_check(course_tag, list_name='course_user_tag')
        course_user_tag = audio.elements_course_user_tag()
        self.random_check(course_user_tag, list_name='course_user_tag')
        img_type = audio.elements_img_type()
        self.random_check(img_type)
        read_link = audio.elements_read_link()
        read_link_num = self.random_check(read_link, make=1, list_name='read_link')
        time.sleep(1)
        if read_link_num:
            audio.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        else:
            audio.input_article('test课程介绍.')
        audio.click_cover_img()
        uploaded()
        audio.click_share_img()
        uploaded()
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
        audio.input_upload_audio_name('测试音频')
        audio.input_upload_audio_dec('测试音频描述')
        typesetting = audio.elements_typesetting()
        self.random_check(typesetting, list_name='typesetting')
        audio.click_upload_img()
        uploaded()
        audio.click_upload_audio()
        uploaded(type=2)
        while True:
            audio_success = audio.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', audio_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('音频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        time.sleep(1)
        audio.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('测试音频', audio.text_check_upload_success(), '上传音频失败！')
        self.log.info('上传音频成功.')

    @BeautifulReport.add_test_img('test_d_edit_audio_num')
    def test_d_edit_audio_num(self):
        """上传音频编辑"""
        audio = self.audio
        self.assertEqual('+ 上传', audio.text_upload_btn(), '当前页面没有上传按钮，无法继续操作！')
        self.log.info('编辑上传音频操作开始.')
        audio.move_edit_upload_audio()
        time.sleep(1)
        audio.input_upload_audio_name('编辑测试音频')
        audio.input_upload_audio_dec('编辑测试音频描述')
        typesetting = audio.elements_typesetting()
        self.random_check(typesetting, list_name='typesetting')
        audio.click_upload_img()
        uploaded()
        audio.click_upload_audio()
        uploaded(type=2)
        while True:
            audio_success = audio.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', audio_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('音频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        time.sleep(1)
        audio.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('编辑测试音频', audio.text_check_upload_success(), '编辑上传音频失败！')
        self.log.info('编辑上传音频成功.')

    @BeautifulReport.add_test_img('test_e_edit_audio')
    def test_e_edit_audio(self):
        """音频信息编辑"""
        audio = self.audio
        audio.click_audio_manage()
        self.assertEqual('+ 新增音频', audio.text_newly_btn_audio(), '当前页面不在音频管理页，无法进行编辑操作！')
        self.log.info('选择音频专辑，进行编辑操作.')
        audio.click_lower_btn()
        if not self.check_audio_is_test(audio, make=1, name='这是一个测试音频'):
            return
        audio.click_teacher()
        teacher_name = audio.elements_check_teacher_name()
        self.random_check(teacher_name, list_name='teacher_name')
        time.sleep(1)
        audio.click_audio_class1()
        time.sleep(1)
        audio_class2 = audio.elements_audio_class2()
        self.random_check(audio_class2, list_name='audio_class2')
        time.sleep(1)
        audio_class3 = audio.elements_audio_class3()
        self.random_check(audio_class3, list_name='audio_class3')
        audio.input_audio_title('这是一个编辑测试音频')
        audio.input_description('这是一个编辑测试描述')
        time.sleep(1)
        course_tag = audio.elements_course_tag()
        self.random_check(course_tag, list_name='course_user_tag')
        course_user_tag = audio.elements_course_user_tag()
        self.random_check(course_user_tag, list_name='course_user_tag')
        img_type = audio.elements_img_type()
        self.random_check(img_type)
        read_link = audio.elements_read_link()
        read_link_num = self.random_check(read_link, make=1, list_name='read_link')
        time.sleep(1)
        if read_link_num:
            audio.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        else:
            audio.input_article('test课程介绍.')
        audio.click_cover_img()
        uploaded()
        audio.click_share_img()
        uploaded()
        time.sleep(1)
        audio.click_sure_btn()
        time.sleep(1)
        if self.check_lower_btn(audio) == 1:
            audio.click_lower_btn()
            time.sleep(1)
        if not self.check_audio_is_test(audio, make=2, name='这是一个编辑测试音频'):
            self.log.info('音频信息编辑保存失败，跳转页面错误！')
        else:
            self.log.info('音频信息编辑保存成功.')

    @BeautifulReport.add_test_img('test_f_page_audio')
    def test_f_page_audio(self):
        """音频翻页"""
        audio = self.audio
        audio.click_lower_btn()
        time.sleep(1)
        if self.check_lower_btn(audio) == 0:
            audio.move_upper_audio()
            time.sleep(1)
            audio.click_delete_sure_btn()
            time.sleep(1)
            audio.click_upper()
        self.log.info('开始进行翻页操作.')
        time.sleep(1)
        page_num = audio.text_page_audio()
        nun = int(re.findall('(\d+)', page_num)[0])
        self.log.info('nun: {}'.format(nun))
        if nun > 10:
            skip_page = int(random.randint(0, nun) / 10) + 1  # 取整数 + 1
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
            else:
                self.log.info('页面小于3，不切换.')
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
        self.check_top(audio)
        time.sleep(1)
        audio.input_audio_query('测试音频')
        audio.click_audio_query_btn()
        if self.check_audio_is_test(audio, make=2, name='这是一个编辑测试音频'):
            self.log.info('音频查询成功.')
        else:
            self.log.error('查询失败，没有发现查询音频！')

    @skip
    @BeautifulReport.add_test_img('test_h_scene_audio')
    def test_h_scene_audio(self):
        """情景配置"""
        audio = self.audio
        self.assertEqual(audio.text_newly_btn_audio(), '+ 新增音频', '不在 音频管理 页面，无法进行情景配置操作！')
        self.log.info('正在进行音频情景配置操作...')
        if not self.check_audio_is_test(audio, make=2, name='这是一个编辑测试音频'):
            return
        audio.click_edit_audio_num()
        audio.move_edit_scene_audio()
        time.sleep(1)
        self.assertEqual('情景配置', audio.text_check_scene(), '进入情景配置失败！')
        self.log.info('进入情景配置成功.')
        audio.click_play_time_m()
        audio.send_keys_down()
        audio.send_keys_down()
        audio.send_keys_enter()
        audio.click_play_time_s()
        audio.send_keys_down()
        audio.send_keys_down()
        audio.send_keys_enter()
        time.sleep(1)
        position_list = audio.elements_play_position()
        self.random_check(position_list)
        in_type = audio.elements_type_btn()
        self.check_scene_content(audio, in_type)
        time.sleep(1)
        end_type = audio.elements_end_audio_btn()
        self.check_scene_content(audio, end_type)
        time.sleep(1)
        audio.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('保存成功', audio.text_check_scene_success(), '没有检测到保存成功提示！')
        self.log.info('设置情景配置成功.')

    @BeautifulReport.add_test_img('test_i_delete_audio')
    def test_i_delete_audio(self):
        """删除音频"""
        audio = self.audio
        if not self.check_audio_is_test(audio, make=2, name='这是一个编辑测试音频'):
            return
        audio.click_edit_audio_num()
        self.assertEqual('+ 上传', audio.text_upload_btn(), '不在上传页面，无法进行删除上传音频操作！')
        self.log.info('开始删除上传音频.')
        try:
            audio.click_choice_audio()
        except Exception:
            audio.click_choice_audio()
        audio.click_delete_btn()
        time.sleep(1)
        audio.click_delete_sure_btn()
        time.sleep(1)
        self.assertEqual('暂无数据', audio.text_check_delete_audio(), '删除失败！')
        self.log.info('上传音频删除成功！')
        audio.click_audio_manage()
        time.sleep(1)
        self.assertEqual(audio.text_newly_btn_audio(), '+ 新增音频', '不在 音频管理 页面，无法进行删除音频操作！')
        if self.check_lower_btn(audio) == 1:
            audio.click_lower_btn()
            time.sleep(1)
        if not self.check_audio_is_test(audio, make=2, name='这是一个编辑测试音频'):
            return
        audio.move_delete_btn()
        time.sleep(1)
        audio.click_delete_sure_btn()
        if self.check_audio_is_test(audio, name='这是一个编辑测试音频', make=3):
            self.log.error('音频课程删除失败！')
        else:
            self.log.info('删除音频课程成功.')

    def check_audio_is_test(self, audio, name, make=0):
        """检测操作音频是不是test audio"""
        time.sleep(1)
        audio_name_list = audio.elements_edit_audio_name()
        self.log.info('检测到的音频名称是：{}'.format(audio_name_list[0].text))
        if audio_name_list[0].text != name:
            if make == 3:
                pass
            else:
                self.log.error('选择音频错误，非测试创建音频！')
            return 0
        if make == 1:
            audio_name_list[0].click()
            time.sleep(1)
            return 1
        elif make == 2:
            return 1

    def check_scene_content(self, audio, lis):
        """选择情景配置内容"""
        self.random_check(lis)
        time.sleep(1)
        self.assertEqual('选择配置方案', audio.text_check_config(), '选择配置方案页面没有弹出！')
        self.log.info('选择选择配置方案中.')
        content_list = audio.elements_check_content()
        self.random_check(content_list)
        audio.click_scene_sure_btn()

    def random_check(self, lis, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 6
            if make == 2:
                update_class = lis[random_num].text
            lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            if make == 1:
                print(random_num)
                return random_num
            elif make == 2:
                return [update_class, random_num]
        else:
            self.log.error('random_check函数传参错误！')

    def check_bottom(self, shop):
        time.sleep(1)
        self.log.info('向下滑动页面.')
        while True:
            if not shop.element_bottom():
                shop.js_scroll_bottom()
                time.sleep(2)
            else:
                break

    def check_top(self, audio):
        time.sleep(1)
        self.log.info('向上滑动页面.')
        while True:
            if not audio.text_audio_manage():
                audio.js_scroll_top()
                time.sleep(2)
            else:
                break

    def check_lower_btn(self, audio):
        """是否选中下架中按钮"""
        lower_btn = audio.elements_check_lower_btn()
        for element in lower_btn:
            if element.text == '已下架' and 'checked' in element.get_attribute('class'):
                self.log.info('当前选中的是下架中按钮，切换为上架中.')
                return 0
            elif element.text == '上架中' and 'checked' in element.get_attribute('class'):
                self.log.info('当前选中的是上架中按钮，切换为下架架中.')
                return 1


if __name__ == '__main__':
    unittest.main()
