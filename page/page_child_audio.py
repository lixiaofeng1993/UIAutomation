#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 14:26
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_audio.py
# @Software: PyCharm
from common.basics import Crazy


class ChildAudioPage(Crazy):
    """音频管理"""
    # //*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[4]/a
    audio_manage_loc = ('xpath', '//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[4]/a')

    def click_audio_manage(self):
        self.click(self.audio_manage_loc)

    # 验证
    text_audio_manage_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[1]/div/span/span[1]/span')

    def text_audio_manage(self):
        return self.get_text(self.text_audio_manage_loc)

    # 新增视频
    newly_audio_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/button[2]')

    def click_newly_audio(self):
        self.click(self.newly_audio_loc)

    def text_newly_btn_audio(self):
        return self.get_text(self.newly_audio_loc)

    # 验证新增
    text_newly_audio_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[1]/div/span[2]/span[1]/span')

    def text_newly_audio(self):
        return self.get_text(self.text_newly_audio_loc)

    # 单节
    one_audio_loc = ('xpath', '//*[@id="videoType"]/label[2]/span[1]')

    def click_one_audio(self):
        self.click(self.one_audio_loc)

    # 老师
    teacher_loc = ('xpath',
                   '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div[2]/div/span/div/div/div')

    def click_teacher(self):
        self.click(self.teacher_loc)

    # 课程分类
    audio_class1_loc = ('xpath',
                        '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div[2]/div/span/span/span')

    def click_audio_class1(self):
        self.click(self.audio_class1_loc)

    # /html/body/div[3]/div/div/div/ul[1]/li[2]
    audio_class2_loc = ('xpath', '/html/body/div[3]/div/div/div/ul/li[2]')
    audio_class2_2_loc = ('xpath', '/html/body/div[2]/div/div/div/ul/li[1]')

    def click_audio_class2(self):
        self.click(self.audio_class2_loc)

    def click_audio_class2_2(self):
        self.click(self.audio_class2_2_loc)

    audio_class3_loc = ('xpath', '/html/body/div[3]/div/div/div/ul[2]/li[2]')
    audio_class3_3_loc = ('xpath', '/html/body/div[2]/div/div/div/ul[2]/li[2]')

    def click_audio_class3(self):
        self.click(self.audio_class3_loc)

    def click_audio_class3_3(self):
        self.click(self.audio_class3_3_loc)

    audio_title_loc = ('id', 'title')

    def input_audio_title(self, title):
        self.send_keys(self.audio_title_loc, title)

    # 验证
    def text_audio_title(self):
        return self.get_attribute(self.audio_title_loc, 'value')

    # 读取形式
    link_loc = ('xpath', '//*[@id="contentClass"]/label[2]/span[1]')

    def click_link(self):
        self.click(self.link_loc)

    link_info_loc = ('id', 'content')

    def input_link_info(self, content):
        self.send_keys(self.link_info_loc, content)

    # 封面图片
    cover_img_loc = ('xpath',
                     '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/span/div/span/div/span/button')

    def click_cover_img(self):
        self.click(self.cover_img_loc)

    # 分享图片
    share_img_loc = ('xpath',
                     '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div[2]/div/span/div/span/div/span/button')

    def click_share_img(self):
        self.click(self.share_img_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[7]/div/button')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 上传按钮

    upload_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/button')

    def click_upload_btn(self):
        self.click(self.upload_btn_loc)

    def text_upload_btn(self):
        return self.get_text(self.upload_btn_loc)

    # 视频名称
    upload_audio_name_loc = ('id', 'videoName')

    def input_upload_audio_name(self, name):
        self.send_keys(self.upload_audio_name_loc, name)

    # 排版，横版
    typesetting_loc = ('xpath', '//*[@id="typeSettings"]/label[1]/span[1]')

    def click_typesetting(self):
        self.click(self.typesetting_loc)

    # 上传图片   /html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/span/div/span/button
    upload_img_loc = (
        'xpath', '/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/span/div')

    def click_upload_img(self):
        self.click(self.upload_img_loc)

    # 上传视频      /html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/span/span/div/span/button
    upload_audio_loc = (
        'xpath', '/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/span/span/div')

    def click_upload_audio(self):
        self.click(self.upload_audio_loc)

    # 上传成功
    upload_success_loc = (
        'xpath', '/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/span/div/span')

    def text_upload_success(self):
        return self.get_text(self.upload_success_loc)

    # 确定按钮
    upload_sure_btn_loc = ('xpath', '/html/body/div[5]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_upload_sure_btn(self):
        self.click(self.upload_sure_btn_loc)

    # 验证
    check_upload_success_loc = ('xpath',
                                '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[4]')

    def text_check_upload_success(self):
        return self.get_text(self.check_upload_success_loc)

    # 删除视频

    no_data_loc = (
        'xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]')

    def text_no_data(self):
        return self.get_text(self.no_data_loc)

    # 勾选视频 //tbody[@class="ant-table-tbody"]/tr[1]/td[1]/span/label/span
    choice_audio_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[1]/span/label/span')

    def click_choice_audio(self):
        self.click(self.choice_audio_loc)

    # 删除按钮
    delete_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/button')

    def click_delete_btn(self):
        self.click(self.delete_btn_loc)

    def text_delete_btn(self):
        return self.get_text(self.delete_btn_loc)

    # 确定
    delete_sure_btn_loc = ('xpath', '/html/body/div[6]/div/div[2]/div/div[1]/div/div/div[2]/button[2]')

    def click_delete_sure_btn(self):
        self.click(self.delete_sure_btn_loc)

    # 取消
    cancel_btn_loc = ('xpath', '/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[1]')
    cancel_btn1_loc = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    def click_cancel_btn1(self):
        self.click(self.cancel_btn1_loc)

    # 编辑视频信息 //*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/span/a
    edit_audio_name_loc = (
        'xpath', '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]/a')

    def click_edit_audio_name(self):
        self.click(self.edit_audio_name_loc)

    def text_edit_audio_name(self):
        return self.get_text(self.edit_audio_name_loc)

    # 课程标签
    edit_audio_tag_loc = ('xpath',
                          '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/span/div/label[1]/span[1]')

    def click_edit_audio_tag(self):
        self.click(self.edit_audio_tag_loc)

    # 用户标签
    edit_audio_user_tag_loc = ('xpath',
                               '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/span/div/label[1]/span[1]')

    def click_edit_audio_user_tag(self):
        self.click(self.edit_audio_user_tag_loc)

    # 保存
    edit_save_loc = ('xpath', '//div[@class="ant-col-offset-3"]/button')

    def click_edit_save(self):
        self.click(self.edit_save_loc)

    # 编辑视频  //*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/a
    edit_audio_num_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[1]/td[9]/a')

    def click_edit_audio_num(self):
        self.click(self.edit_audio_num_loc)

    # 翻页
    page_audio_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li[1]')

    def text_page_audio(self):
        return self.get_text(self.page_audio_loc)

    # 跳至
    skip_page_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li[7]/div[2]/input')

    def input_skip_page(self, num):
        self.send_keys(self.skip_page_loc, num)

    # 显示的页数
    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)

    # 返回顶部
    top_loc = ('class name', 'ant-back-top')

    def element_top(self):
        return self.find_element(self.top_loc)

    def click_top(self):
        self.click(self.top_loc)

    # 查询
    audio_query_loc = ('id', 'queryString')

    def input_audio_query(self, name):
        self.send_keys(self.audio_query_loc, name)

    # 按钮
    audio_query_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/button[1]')

    def click_audio_query_btn(self):
        self.click(self.audio_query_btn_loc)

    # 选择单节音频
    one_audio_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div/div/label[2]')

    def click_one_audio_btn(self):
        self.click(self.one_audio_btn_loc)
