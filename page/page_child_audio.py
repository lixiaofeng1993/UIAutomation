#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 14:26
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_audio.py
# @Software: PyCharm
from common.basics import Crazy


class ChildAudioPage(Crazy):
    """视频管理"""

    audio_manage_loc = ('xpath', '//ul[@class="ant-menu ant-menu-light ant-menu-root ant-menu-inline"]/li[4]/a')

    def click_audio_manage(self):
        self.click(self.audio_manage_loc)

    # 验证
    text_audio_manage_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[1]/div/span/span[1]/span')

    def text_audio_manage(self):
        return self.get_text(self.text_audio_manage_loc)

    # 新增视频
    newly_audio_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[2]/div[2]/div/div/button[2]')

    def click_newly_audio(self):
        self.click(self.newly_audio_loc)

    def text_newly_btn_audio(self):
        return self.get_text(self.newly_audio_loc)

    # 验证新增
    text_newly_audio_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[1]/div/span[2]/span[1]/span')

    def text_newly_audio(self):
        return self.get_text(self.text_newly_audio_loc)

    # 老师
    teacher_loc = ('xpath',
                   '//form[@class="ant-form ant-form-horizontal"]/div[1]/div[1]/div[2]/div[2]/div/span/div/div')

    def click_teacher(self):
        self.click(self.teacher_loc)

    check_teacher_name_loc = ('xpath',
                              '//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]/li')

    def elements_check_teacher_name(self):
        return self.find_elements(self.check_teacher_name_loc)

    # 课程分类
    audio_class1_loc = ('xpath',
                        '//form[@class="ant-form ant-form-horizontal"]/div[1]/div[1]/div[3]/div[2]/div/span/span')

    def click_audio_class1(self):
        self.click(self.audio_class1_loc)

    audio_class2_loc = ('xpath', '//ul[@class="ant-cascader-menu"]/li')

    def elements_audio_class2(self):
        return self.find_elements(self.audio_class2_loc)

    audio_class3_loc = (
        'xpath', '//div[@class="ant-cascader-menus ant-cascader-menus-placement-bottomLeft"]/div/ul[2]/li')

    def elements_audio_class3(self):
        return self.find_elements(self.audio_class3_loc)

    audio_title_loc = ('id', 'title')

    def input_audio_title(self, title):
        self.send_keys(self.audio_title_loc, title)

    # 视频描述
    audio_description_loc = ('id', 'description')

    def input_description(self, description):
        self.send_keys(self.audio_description_loc, description)

    # 课程标签
    course_tag_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/div/label/span[1]')

    def elements_course_tag(self):
        return self.find_elements(self.course_tag_loc)

    # 课程用户标签
    course_user_tag_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[3]/div[2]/div/span/div/label/span[1]')

    def elements_course_user_tag(self):
        return self.find_elements(self.course_user_tag_loc)

    # 图片类型
    img_type_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[4]/div[2]/div/span/div/label/span[1]')

    def elements_img_type(self):
        return self.find_elements(self.img_type_loc)

    # 读取形式
    read_link_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[5]/div[2]/div/span/div/label/span[1]')

    def elements_read_link(self):
        return self.find_elements(self.read_link_loc)

    # 写入图文
    input_article_loc = ('xpath', '//div[@class="DraftEditor-editorContainer"]/div')

    def input_article(self, text):
        self.send_keys(self.input_article_loc, text)

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
                     '//form[@class="ant-form ant-form-horizontal"]/div[1]/div[2]/div[1]/div[2]/div/span/div/span/div')

    def click_cover_img(self):
        self.click(self.cover_img_loc)

    # 分享图片
    share_img_loc = ('xpath',
                     '//form[@class="ant-form ant-form-horizontal"]/div[1]/div[2]/div[2]/div[2]/div/span/div/span/div')

    def click_share_img(self):
        self.click(self.share_img_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[last()]/div/button')

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

    # 视频描述
    upload_audio_dec_loc = ('id', 'subtitle')

    def input_upload_audio_dec(self, dec):
        self.send_keys(self.upload_audio_dec_loc, dec)

    # 排版，横版
    typesetting_loc = ('xpath', '//*[@id="typeSettings"]/label/span[1]')

    def elements_typesetting(self):
        return self.find_elements(self.typesetting_loc)

    # 上传图片
    upload_img_loc = (
        'xpath', '//div[@class="ant-modal-body"]/form/div[5]/div[2]/div/span/span/div')

    def click_upload_img(self):
        self.click(self.upload_img_loc)

    # 上传视频
    upload_audio_loc = (
        'xpath', '//div[@class="ant-modal-body"]/form/div[6]/div[2]/div/span/span/div')

    def click_upload_audio(self):
        self.click(self.upload_audio_loc)

    # 上传成功
    upload_success_loc = (
        'xpath', '//div[@class="ant-modal-body"]/form/div[6]/div[2]/div/span/div/span')

    def text_upload_success(self):
        return self.get_text(self.upload_success_loc)

    # 视频连接
    audio_url_loc = ('id', 'videoUrl')

    def input_audio_url(self, url):
        self.send_keys(self.audio_url_loc, url)

    # 确定按钮
    upload_sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_upload_sure_btn(self):
        self.click(self.upload_sure_btn_loc)

    # 验证
    check_upload_success_loc = ('xpath',
                                '//*[@id="mainContainer"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[4]')

    def text_check_upload_success(self):
        return self.get_text(self.check_upload_success_loc)

    # 编辑上传视频
    edit_upload_audio_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[1]/td[9]/button')

    edit_upload_audio_loc = ('xpath',
                             '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')
    edit_scene_loc = ('xpath',
                      '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[3]')

    def move_edit_upload_audio(self):
        self.move(self.edit_upload_audio_btn_loc, self.edit_upload_audio_loc)

    # 情景配置
    def move_edit_scene_audio(self):
        self.move(self.edit_upload_audio_btn_loc, self.edit_scene_loc)

    # 验证进入情景配置
    check_scene_loc = ('xpath', '//div[@class="ant-modal-content"]/div[1]/div')

    def text_check_scene(self):
        return self.get_text(self.check_scene_loc)

    # 播放时间
    play_time_m_loc = ('xpath', '//div[@class="ant-row"]/div/div[1]/div/div/div')

    def click_play_time_m(self):
        self.click(self.play_time_m_loc)

    check_time_m_loc = ('xpath',
                        '//div[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft  ant-select-dropdown-hidden"]/div/ul/li')

    def elements_check_time_m(self):
        return self.find_elements(self.check_time_m_loc)

    play_time_s_loc = ('xpath', '//div[@class="ant-row"]/div/div[2]/div/div/div')

    def click_play_time_s(self):
        self.click(self.play_time_s_loc)

    check_time_s_loc = ('xpath',
                        '//div[last()]/div/div[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft  ant-select-dropdown-hidden"]/div/ul/li')

    def elements_check_time_s(self):
        return self.find_elements(self.check_time_s_loc)

    # 播出中间位置
    play_position_loc = ('xpath', '//div[@class="block___3eMO0"]/div/div[2]/div[2]/div/label/span[1]')

    def elements_play_position(self):
        return self.find_elements(self.play_position_loc)

    type_btn_loc = ('xpath', '//div[@class="block___3eMO0"]/div[2]/div[2]/div/button')

    def elements_type_btn(self):
        return self.find_elements(self.type_btn_loc)

    # 验证选择
    check_config_loc = ('xpath', '//body[@class="browser-chrome"]/div[last()]/div/div[2]/div/div/div[1]/div')

    def text_check_config(self):
        return self.get_text(self.check_config_loc)

    # 选择内容
    check_content_loc = ('xpath',
                         '//body[@class="browser-chrome"]/div[last()]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td/span[1]/label/span')

    def elements_check_content(self):
        return self.find_elements(self.check_content_loc)

    # 确定 //body[@class="browser-chrome"]/div[last()]/div/div[2]/div/div[1]/div[3]/div/button[2]
    scene_sure_btn_loc = (
        'xpath', '//body[@class="browser-chrome"]/div[last()]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_scene_sure_btn(self):
        self.click(self.scene_sure_btn_loc)

    # 结束视频
    end_audio_btn_loc = ('xpath', '//div[@class="block___3eMO0"]/div[1]/div[2]/div/button')

    def elements_end_audio_btn(self):
        return self.find_elements(self.end_audio_btn_loc)

    # 验证成功
    check_scene_success_loc = ('xpath', '//div[@class="ant-message"]/span/div/div/div/span')

    def text_check_scene_success(self):
        return self.get_text(self.check_scene_success_loc)

    # 编辑视频信息
    edit_audio_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[1]/td[10]/button')

    upper_btn_loc = ('xpath',
                     '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[4]')

    delete_btn_loc = ('xpath',
                      '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')

    def move_delete_btn(self):
        self.move(self.edit_audio_loc, self.delete_btn_loc)

    def move_edit_audio(self):
        self.move(self.edit_audio_loc, self.edit_upload_audio_loc)

    # 上架
    def move_upper_audio(self):
        self.move(self.edit_audio_loc, self.upper_btn_loc)

    # 删除视频

    # 勾选视频 //tbody[@class="ant-table-tbody"]/tr[1]/td[1]/span/label/span
    choice_audio_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[1]/span/label/span')

    def click_choice_audio(self):
        self.click(self.choice_audio_loc)

    # 删除按钮
    choice_delete_btn_loc = ('xpath', '//div[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]/button')

    def click_delete_btn(self):
        self.click(self.choice_delete_btn_loc)

    def text_delete_btn(self):
        return self.get_text(self.delete_btn_loc)

    # 确定
    delete_sure_btn_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_delete_sure_btn(self):
        self.click(self.delete_sure_btn_loc)

    # 验证删除成功
    check_delete_audio_loc = ('xpath', '//div[@class="ant-table-placeholder"]')

    def text_check_delete_audio(self):
        return self.get_text(self.check_delete_audio_loc)

    # 编辑视频信息 //tbody[@class="ant-table-tbody"]/tr/td[5]
    edit_audio_name_loc = (
        'xpath', '//tbody[@class="ant-table-tbody"]/tr/td[5]')

    def elements_edit_audio_name(self):
        return self.find_elements(self.edit_audio_name_loc)

    # 下架中按钮
    lower_btn_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label[2]/span[2]')

    def click_lower_btn(self):
        self.click(self.lower_btn_loc)

    # 验证选中下架中
    check_lower_btn_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label')

    def elements_check_lower_btn(self):
        return self.find_elements(self.check_lower_btn_loc)

    # 上架中按钮
    upper_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label[1]/span[2]')

    def click_upper(self):
        self.click(self.upper_loc)

    # 课程标签
    edit_audio_tag_loc = ('xpath',
                          '//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/div/label[1]/span[1]')

    def click_edit_audio_tag(self):
        self.click(self.edit_audio_tag_loc)

    # 用户标签
    edit_audio_user_tag_loc = ('xpath',
                               '//form[@class="ant-form ant-form-horizontal"]/div[3]/div[2]/div/span/div/label[1]/span[1]')

    def click_edit_audio_user_tag(self):
        self.click(self.edit_audio_user_tag_loc)

    # 视频名称过长错误提示
    audio_name_error_loc = ('class name', 'ant-form-explain')

    def element_audio_name_error(self):
        return self.find_element(self.audio_name_error_loc)

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
    skip_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last()]/div[2]/input')

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

    # 查询按钮
    audio_query_btn_loc = ('xpath', '//div[@class="ant-row"]/div[2]/div/div/button[1]')

    def click_audio_query_btn(self):
        self.click(self.audio_query_btn_loc)

    # 下架按钮
    audio_lower_btn_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label[2]/span[2]')

    def click_audio_lower_btn(self):
        self.click(self.audio_lower_btn_loc)
