#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 17:04
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_c_child_video.py
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
from common.random_upload import uploaded


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
        teacher_name = video.elements_check_teacher_name()
        self.random_check(teacher_name, list_name='teacher_name')
        time.sleep(1)
        video.click_video_class1()
        time.sleep(1)
        video_class2 = video.elements_video_class2()
        self.random_check(video_class2, list_name='video_class2')
        time.sleep(1)
        video_class3 = video.elements_video_class3()
        self.random_check(video_class3, list_name='video_class3')
        video.input_video_title('这是一个测试视频')
        video.input_description('这是一个测试描述')
        time.sleep(1)
        course_tag = video.elements_course_tag()
        self.random_check(course_tag, list_name='course_user_tag')
        course_user_tag = video.elements_course_user_tag()
        self.random_check(course_user_tag, list_name='course_user_tag')
        img_type = video.elements_img_type()
        self.random_check(img_type)
        read_link = video.elements_read_link()
        read_link_num = self.random_check(read_link, make=1, list_name='read_link')
        time.sleep(1)
        if read_link_num:
            video.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        else:
            video.input_article('test课程介绍.')
        video.click_cover_img()
        uploaded()
        video.click_share_img()
        uploaded()
        time.sleep(1)
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
        video.input_upload_video_name('测试视频')
        video.input_upload_video_dec('测试视频描述')
        typesetting = video.elements_typesetting()
        self.random_check(typesetting, list_name='typesetting')
        video.click_upload_img()
        uploaded()
        video.click_upload_video()
        uploaded(type=1)
        while True:
            video_success = video.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', video_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('视频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        time.sleep(1)
        video.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('测试视频', video.text_check_upload_success(), '上传视频失败！')
        self.log.info('上传视频成功.')

    @BeautifulReport.add_test_img('test_d_edit_video_num')
    def test_d_edit_video_num(self):
        """上传视频编辑"""
        video = self.video
        self.assertEqual('+ 上传', video.text_upload_btn(), '当前页面没有上传按钮，无法继续操作！')
        self.log.info('编辑上传视频操作开始.')
        video.move_edit_upload_video()
        time.sleep(1)
        video.input_upload_video_name('编辑测试视频')
        video.input_upload_video_dec('编辑测试视频描述')
        typesetting = video.elements_typesetting()
        self.random_check(typesetting, list_name='typesetting')
        video.click_upload_img()
        uploaded()
        video.click_upload_video()
        uploaded(type=1)
        while True:
            video_success = video.text_upload_success()
            mb_list = re.findall('(\d+\.\d+)', video_success)
            if float(mb_list[0]) == float(mb_list[1]):
                break
            else:
                self.log.info('视频大小：{}mb，已上传：{}mb'.format(mb_list[1], mb_list[0]))
                time.sleep(2)
        time.sleep(1)
        video.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('编辑测试视频', video.text_check_upload_success(), '编辑上传视频失败！')
        self.log.info('编辑上传视频成功.')

    @BeautifulReport.add_test_img('test_e_edit_video')
    def test_e_edit_video(self):
        """视频信息编辑"""
        video = self.video
        video.click_video_manage()
        self.assertEqual('+ 新增视频', video.text_newly_btn_video(), '当前页面不在视频管理页，无法进行编辑操作！')
        self.log.info('选择视频专辑，进行编辑操作.')
        video.click_lower_btn()
        if not self.check_video_is_test(video, make=1, name='这是一个测试视频'):
            return
        video.click_teacher()
        teacher_name = video.elements_check_teacher_name()
        self.random_check(teacher_name, list_name='teacher_name')
        time.sleep(1)
        video.click_video_class1()
        time.sleep(1)
        video_class2 = video.elements_video_class2()
        self.random_check(video_class2, list_name='video_class2')
        time.sleep(1)
        video_class3 = video.elements_video_class3()
        self.random_check(video_class3, list_name='video_class3')
        video.input_video_title('这是一个编辑测试视频')
        video.input_description('这是一个编辑测试描述')
        time.sleep(1)
        course_tag = video.elements_course_tag()
        self.random_check(course_tag, list_name='course_user_tag')
        course_user_tag = video.elements_course_user_tag()
        self.random_check(course_user_tag, list_name='course_user_tag')
        img_type = video.elements_img_type()
        self.random_check(img_type)
        read_link = video.elements_read_link()
        read_link_num = self.random_check(read_link, make=1, list_name='read_link')
        time.sleep(1)
        if read_link_num:
            video.input_link_info('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        else:
            video.input_article('test课程介绍.')
        video.click_cover_img()
        uploaded()
        video.click_share_img()
        uploaded()
        time.sleep(1)
        video.click_sure_btn()
        time.sleep(1)
        if self.check_lower_btn(video) == 1:
            video.click_lower_btn()
            time.sleep(1)
        if not self.check_video_is_test(video, make=2, name='这是一个编辑测试视频'):
            self.log.info('视频信息编辑保存失败，跳转页面错误！')
        else:
            self.log.info('视频信息编辑保存成功.')

    @BeautifulReport.add_test_img('test_f_page_video')
    def test_f_page_video(self):
        """视频翻页"""
        video = self.video
        video.click_lower_btn()
        time.sleep(1)
        if self.check_lower_btn(video) == 0:
            video.move_upper_video()
            time.sleep(1)
            video.click_delete_sure_btn()
            time.sleep(1)
            video.click_upper()
        self.log.info('开始进行翻页操作.')
        time.sleep(1)
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
            else:
                self.log.info('页面小于3，不切换.')
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
        self.check_top(video)
        time.sleep(1)
        video.input_video_query('测试视频')
        video.click_video_query_btn()
        if self.check_video_is_test(video, make=2, name='这是一个编辑测试视频'):
            self.log.info('视频查询成功.')
        else:
            self.log.error('查询失败，没有发现查询视频！')

    @BeautifulReport.add_test_img('test_h_scene_video')
    def test_h_scene_video(self):
        """情景配置"""
        video = self.video
        self.assertEqual(video.text_newly_btn_video(), '+ 新增视频', '不在 视频管理 页面，无法进行情景配置操作！')
        self.log.info('正在进行视频情景配置操作...')
        if not self.check_video_is_test(video, make=2, name='这是一个编辑测试视频'):
            return
        video.click_edit_video_num()
        video.move_edit_scene_video()
        time.sleep(1)
        self.assertEqual('情景配置', video.text_check_scene(), '进入情景配置失败！')
        self.log.info('进入情景配置成功.')
        video.click_play_time_m()
        video.send_keys_down()
        video.send_keys_down()
        video.send_keys_enter()
        video.click_play_time_s()
        video.send_keys_down()
        video.send_keys_down()
        video.send_keys_enter()
        time.sleep(1)
        position_list = video.elements_play_position()
        self.random_check(position_list)
        in_type = video.elements_type_btn()
        self.check_scene_content(video, in_type)
        time.sleep(1)
        end_type = video.elements_end_video_btn()
        self.check_scene_content(video, end_type)
        time.sleep(1)
        video.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('保存成功', video.text_check_scene_success(), '没有检测到保存成功提示！')
        self.log.info('设置情景配置成功.')

    @BeautifulReport.add_test_img('test_i_delete_video')
    def test_i_delete_video(self):
        """删除视频"""
        video = self.video
        self.assertEqual('+ 上传', video.text_upload_btn(), '不在上传页面，无法进行删除上传视频操作！')
        self.log.info('开始删除上传视频.')
        video.click_choice_video()
        video.click_delete_btn()
        time.sleep(1)
        video.click_delete_sure_btn()
        time.sleep(1)
        self.assertEqual('暂无数据', video.text_check_delete_video(), '删除失败！')
        self.log.info('上传视频删除成功！')
        video.click_video_manage()
        time.sleep(1)
        self.assertEqual(video.text_newly_btn_video(), '+ 新增视频', '不在 视频管理 页面，无法进行删除视频操作！')
        if self.check_lower_btn(video) == 1:
            video.click_lower_btn()
            time.sleep(1)
        if not self.check_video_is_test(video, make=2, name='这是一个编辑测试视频'):
            return
        video.move_delete_btn()
        time.sleep(1)
        video.click_delete_sure_btn()
        if self.check_video_is_test(video, name='这是一个编辑测试视频'):
            self.log.error('视频课程删除失败！')
        else:
            self.log.info('删除视频课程成功.')

    def check_video_is_test(self, video, name, make=0):
        """检测操作视频是不是test video"""
        time.sleep(1)
        video_name_list = video.elements_edit_video_name()
        print(video_name_list[0].text, 1111111111111111111111111)
        if video_name_list[0].text != name:
            self.log.error('选择视频错误，非测试创建视频！')
            return 0
        if make == 1:
            video_name_list[0].click()
            time.sleep(1)
            return 1
        elif make == 2:
            return 1

    def check_scene_content(self, video, lis):
        """选择情景配置内容"""
        self.random_check(lis)
        time.sleep(1)
        self.assertEqual('选择配置方案', video.text_check_config(), '选择配置方案页面没有弹出！')
        self.log.info('选择选择配置方案中.')
        content_list = video.elements_check_content()
        self.random_check(content_list)
        video.click_scene_sure_btn()

    def random_check(self, lis, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
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

    def check_top(self, video):
        time.sleep(1)
        self.log.info('向上滑动页面.')
        while True:
            if not video.text_video_manage():
                video.js_scroll_top()
                time.sleep(2)
            else:
                break

    def check_lower_btn(self, video):
        """是否选中下架中按钮"""
        lower_btn = video.elements_check_lower_btn()
        for element in lower_btn:
            if element.text == '已下架' and 'checked' in element.get_attribute('class'):
                self.log.info('当前选中的是下架中按钮，切换为上架中.')
                return 0
            elif element.text == '上架中' and 'checked' in element.get_attribute('class'):
                self.log.info('当前选中的是上架中按钮，切换为下架架中.')
                return 1


if __name__ == '__main__':
    unittest.main()
