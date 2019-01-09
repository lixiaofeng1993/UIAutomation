#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildShopPage(Crazy):
    """店铺装修"""
    shop_manage_loc = ('xpath', '//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[1]/a')

    def click_shop_manage(self):
        self.click(self.shop_manage_loc)

    # 验证
    check_shop_manage_loc = ('xpath', '//span[@class="ant-breadcrumb-link"]/span')

    def text_check_shop_manage(self):
        return self.get_text(self.check_shop_manage_loc)

    # 新增页面
    new_page_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/button[1]')

    def click_new_page_btn(self):
        self.click(self.new_page_btn_loc)

    # 页面名称
    page_name_loc = ('id', 'name')

    def input_page_name(self, name):
        self.send_keys(self.page_name_loc, name)

    # 分享标题
    page_share_name_loc = ('id', 'shareTitle')

    def input_page_share_name(self, name):
        self.send_keys(self.page_share_name_loc, name)

    # 分享图片
    share_img_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div[2]/div/span/span/div/span/button')

    def click_share_img(self):
        self.click(self.share_img_loc)

    # 是否分享
    is_share_loc = ('xpath', '//*[@id="allowShare"]/label[1]/span[1]')

    def click_is_share(self):
        self.click(self.is_share_loc)

    # 确定 ant-btn ant-btn-primary
    sure_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 取消
    cancel_btn_lco = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_lco)

    # 未分组                        //*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div[5]/div[1]
    not_grouped_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div[last()]/div[1]')

    def click_not_grouped(self):
        self.click(self.not_grouped_loc)

    #           //*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div[1]/div/span[1]
    #           //*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div[2]/div/span[1]
    check_page_name_loc = (
        'xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div[last()]/div[2]/div/div/span[1]')

    def elements_check_page_name(self):
        return self.find_elements(self.check_page_name_loc)

    # 装修页面名称
    page_title_loc = ('class name', 'zent-design-component-config-preview__title')

    def text_page_title(self):
        return self.get_text(self.page_title_loc)

    # 单列
    single_row_loc = ('xpath',
                      '//div[@class="zent-design-editor-add-component__grouped-list"]/div[2]/a')

    def click_single_model(self):
        self.click(self.single_row_loc)

    # 两列
    two_row_loc = ('xpath',
                   '//div[@class="zent-design-editor-add-component__grouped-list"]/div[3]/a')

    def click_two_model(self):
        self.click(self.two_row_loc)

    # 三列
    three_row_loc = ('xpath',
                     '//div[@class="zent-design-editor-add-component__grouped-list"]/div[4]/a')

    def click_three_model(self):
        self.click(self.three_row_loc)

    # 四列
    four_row_loc = ('xpath',
                    '//div[@class="zent-design-editor-add-component__grouped-list"]/div[5]/a')

    def click_four_model(self):
        self.click(self.four_row_loc)

    # 轮播
    carousel_row_loc = ('xpath',
                        '//div[@class="zent-design-editor-add-component__grouped-list"]/div[6]/a')

    def click_carousel_model(self):
        self.click(self.carousel_row_loc)

    # 左滑
    left_row_loc = ('xpath',
                    '//div[@class="zent-design-editor-add-component__grouped-list"]/div[7]/a')

    def click_left_model(self):
        self.click(self.left_row_loc)

    # 空白
    blank_row_loc = ('xpath',
                     '//div[@class="zent-design-editor-add-component__grouped-list"]/div[8]/a')

    def click_blank_model(self):
        self.click(self.blank_row_loc)

    # 页面
    page_row_loc = ('xpath',
                    '//div[@class="zent-design-editor-add-component__grouped-list"]/div[9]/a')

    def click_page_model(self):
        self.click(self.page_row_loc)

    # 添加视频
    add_video_loc = ('xpath', '//div[@class="zent-design-component-columns1-editor-add-btn"]/a[1]')

    def click_add_video(self):
        self.click(self.add_video_loc)

    # 选择数据
    check_data_loc = ('class name', 'ant-modal-title')

    def text_check_data(self):
        return self.get_text(self.check_data_loc)

    # 选择专辑数据
    choice_data_loc = ('class name', 'ant-checkbox-input')

    def element_choice_data(self):
        return self.find_elements(self.choice_data_loc)

    # 广告图选择视频、音频、文章
    choice_vaa_loc = ('class name', 'ant-radio-input')

    def element_choice_vaa(self):
        return self.find_elements(self.choice_vaa_loc)

    # video、audio名称
    choice_video_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[4]')

    def elements_choice_video_name(self):
        return self.find_elements(self.choice_video_name_loc)

    # article名称
    choice_article_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[3]')

    def elements_choice_article_name(self):
        return self.find_elements(self.choice_article_name_loc)

    # video、audioID
    choice_video_id_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[3]')

    def elements_choice_video_id(self):
        return self.find_elements(self.choice_video_id_loc)

    # article、page ID
    choice_article_id_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[2]')

    def elements_choice_article_id(self):
        return self.find_elements(self.choice_article_id_loc)

    # 确定按钮
    sure_data_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_data_btn(self):
        self.click(self.sure_data_btn_loc)

    # 页面数据条数
    page_num_loc = ('class name', 'ant-pagination-total-text')

    def text_page_num(self):
        return self.get_text(self.page_num_loc)

    # li 数量
    choice_page_num_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li')

    def elements_choice_page_num(self):
        return self.find_elements(self.choice_page_num_loc)

    def clicks_choice_num(self, n):
        self.clicks(self.choice_page_num_loc, n)

    # 页数
    page_loc = ('class name', 'ant-pagination-item')

    def elements_page(self):
        return self.find_elements(self.page_loc)

    # 添加音频
    add_audio_loc = ('xpath', '//div[@class="zent-design-component-columns1-editor-add-btn"]/a[2]')

    def click_add_audio(self):
        self.click(self.add_audio_loc)

    # 添加文章
    add_article_loc = ('xpath', '//div[@class="zent-design-component-columns1-editor-add-btn"]/a[3]')

    def click_add_article(self):
        self.click(self.add_article_loc)

    # 页面元素
    # 视频标题
    video_title_loc = ('class name', 'zent-design-component-column1-preview__video-title')

    def elements_video_title(self):
        return self.find_elements(self.video_title_loc)

    video_img_loc = ('class name', 'zent-design-component-column1-preview__video-img')

    def elements_video_img(self):
        return self.find_elements(self.video_img_loc)

    # 音频标题
    audio_title_loc = ('class name', 'zent-design-component-column1-preview__audio-title')

    def elements_audio_title(self):
        return self.find_elements(self.audio_title_loc)

    audio_img_loc = ('class name', 'zent-design-component-column1-preview__audio-img')

    def elements_audio_img(self):
        return self.find_elements(self.audio_img_loc)

    # 文章标题
    article_title_loc = ('class name', 'zent-design-component-column1-preview__article-title')

    def elements_article_title(self):
        return self.find_elements(self.article_title_loc)

    # 文章单图
    article_single_img_loc = ('class name', 'zent-design-component-column1-preview__audio-grid-1')

    def elements_article_single_img(self):
        return self.find_elements(self.article_single_img_loc)

    # 文章三个图片
    article_three_img_loc = ('class name', 'zent-design-component-column1-preview__article-img')

    def elements_article_three_img(self):
        return self.find_elements(self.article_three_img_loc)

    # 单列广告
    single_ad_img_loc = ('class name', 'zent-design-component-carousel-preview__image-img')

    def elements_single_ad_img(self):
        return self.find_elements(self.single_ad_img_loc)

    # 两列广告
    two_ad_img_loc = ('class name', 'zent-design-component-column2-preview_img')

    def elements_two_ad_img(self):
        return self.find_elements(self.two_ad_img_loc)

    # 三列广告
    three_ad_img_loc = ('class name', 'zent-design-component-column3-preview_img')

    def elements_three_ad_img(self):
        return self.find_elements(self.three_ad_img_loc)

    # 四列广告
    four_ad_img_loc = ('class name', 'zent-design-component-column4-preview_img')

    def elements_four_ad_img(self):
        return self.find_elements(self.four_ad_img_loc)

    # 广告
    add_ad_loc = ('xpath', '//div[@class="ant-upload ant-upload-select ant-upload-select-text"]/span/a')

    def click_add_ad(self):
        self.click(self.add_ad_loc)

    # 选择链接  //*[@id="mainContainer"]/div[3]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[2]/div[1]/ul/li[2]/div/div/div/div[2]/span/input
    #           //*[@id="mainContainer"]/div[3]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[2]/div[1]/ul/li[1]/div/div/div/div[2]/span/span/button
    #               //ul[@class="zent-design-component-image-ad-editor__entry-list"]/li/div/div/div/div[2]/input
    choice_link_loc = ('xpath',
                       '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[1]/div/div/div/div[2]/span/span/button')
    choice_link1_loc = ('xpath',
                        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[2]/div/div/div/div[2]/span/span/button')
    choice_link2_loc = ('xpath',
                        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[3]/div/div/div/div[2]/span/span/button')

    def click_choice_link(self):
        self.click(self.choice_link_loc)

    choice_link3_loc = ('xpath',
                        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[4]/div/div/div/div[2]/span/span/button')

    def click_choice_link3(self):
        self.click(self.choice_link3_loc)

    def click_choice_link2(self):
        self.click(self.choice_link2_loc)

    def click_choice_link1(self):
        self.click(self.choice_link1_loc)

    # 选择广告链接类型

    type_loc = ('class name', 'ant-radio-button-wrapper')

    def elements_type(self):
        return self.find_elements(self.type_loc)

    def clicks_type(self, n):
        self.clicks(self.type_loc, n)

    # 获取广告链接id  //*[@id="mainContainer"]/div[3]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[2]/div[1]/ul/li[2]/div/div/div/div[2]/span/input
    ad_link_id_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[1]/div/div/div/div[2]/span/input')
    ad_link_id1_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[2]/div/div/div/div[2]/span/input')
    ad_link_id2_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[3]/div/div/div/div[2]/span/input')
    ad_link_id3_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[4]/div/div/div/div[2]/span/input')

    def elements_ad_link_id(self):
        return self.find_elements(self.ad_link_id_loc)

    def elements_ad_link_id3(self):
        return self.find_elements(self.ad_link_id3_loc)

    def elements_ad_link_id2(self):
        return self.find_elements(self.ad_link_id2_loc)

    def elements_ad_link_id1(self):
        return self.find_elements(self.ad_link_id1_loc)

    # 是否分享
    ad_share_loc = ('xpath', '//label[@class="ant-radio-wrapper"]/span[1]')

    def click_ad_share(self):
        self.click(self.ad_share_loc)

    # 保存页面
    save_page_loc = ('xpath', '//div[@class="paper-create__actions"]/button[2]')

    def click_save_page(self):
        self.click(self.save_page_loc)

    # 保存成功提示
    success_save_btn_loc = ('xpath', '/html/body/div[2]/div/span/div/div/div/span')

    def text_success_save_btn(self):
        return self.get_text(self.success_save_btn_loc)

    # 两列

    # 广告
    two_add_ad_loc = ('xpath', '//div[@class="zent-design-component-columns1-editor-add-btn"]/span/div')

    def click_two_add_ad(self):
        self.click(self.two_add_ad_loc)

    # 图文广告
    two_add_img_ad_loc = ('xpath', '//div[@class="zent-design-component-columns1-editor-add-btn"]/a')

    def click_two_add_img_ad(self):
        self.click(self.two_add_img_ad_loc)

    # 添加图片
    two_add_img_loc = ('xpath',
                       '//div[@class="zent-design-component-image-ad-editor__image-entry-image-upload zent-design-component-image-ad-editor__image-entry-image-upload--no-image"]/a')

    def click_two_add_img(self):
        self.click(self.two_add_img_loc)

    # 显示文本
    two_text_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[1]/div/div/div/div[2]/input')

    def input_two_text(self, text):
        self.send_keys(self.two_text_loc, text)

    two_text1_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[2]/div/div/div/div[2]/input')

    def input_two_text1(self, text):
        self.send_keys(self.two_text1_loc, text)

    two_text2_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[3]/div/div/div/div[2]/input')

    def input_two_text2(self, text):
        self.send_keys(self.two_text2_loc, text)

    two_text3_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[4]/div/div/div/div[2]/input')

    def input_two_text3(self, text):
        self.send_keys(self.two_text3_loc, text)

    # 选择数据  click_choice_link1
    two_choice_data_loc = (
        'xpath',
        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[1]/div/div/div/div[3]/span/span/button')

    def click_two_choice_link(self):
        self.click(self.two_choice_data_loc)

    two_choice_data1_loc = (
        'xpath',
        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[2]/div/div/div/div[3]/span/span/button')

    def click_two_choice_link1(self):
        self.click(self.two_choice_data1_loc)

    two_choice_data2_loc = (
        'xpath',
        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[3]/div/div/div/div[3]/span/span/button')

    def click_two_choice_link2(self):
        self.click(self.two_choice_data2_loc)

    two_choice_data3_loc = (
        'xpath',
        '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[4]/div/div/div/div[3]/span/span/button')

    def click_two_choice_link3(self):
        self.click(self.two_choice_data3_loc)

    # 验证数据
    two_check_data_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[1]/div/div/div/div[3]/span/input')
    two_check_data1_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[2]/div/div/div/div[3]/span/input')

    def text_two_check_data(self):
        return self.get_attribute(self.two_check_data_loc, 'value')

    two_check_data2_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[3]/div/div/div/div[3]/span/input')

    def text_two_check_data2(self):
        return self.get_attribute(self.two_check_data2_loc, 'value')

    two_check_data3_loc = (
        'xpath', '//ul[@class="zent-design-component-image-ad-editor__entry-list"]/li[4]/div/div/div/div[3]/span/input')

    def text_two_check_data3(self):
        return self.get_attribute(self.two_check_data3_loc, 'value')

    def text_two_check_data1(self):
        return self.get_attribute(self.two_check_data1_loc, 'value')

    # 是否滚动到底部
    bottom_loc = ('class name', 'ant-layout-footer')

    def element_bottom(self):
        return self.find_element(self.bottom_loc)

    # 轮播
    carousel_ad_btn_loc = ('xpath', '//div[@class="ant-upload ant-upload-select ant-upload-select-text"]/span/a')

    def click_carousel_ad_btn(self):
        self.click(self.carousel_ad_btn_loc)

    # 空白
    blank_height_loc = (
        'xpath',
        '//div[@class="zent-design-component-image-ad-editor__image-entry-controls"]/div/div[3]/div/div[2]/input')

    def inputs_blank_height(self, n, text):
        self.sends_keys(self.blank_height_loc, n, text)

    # 颜色
    blank_color_btn_loc = ('class name', 'zent-color-picker__preview')

    def click_blank_color_btn(self):
        self.click(self.blank_color_btn_loc)

    blank_color_loc = ('xpath', '//div[@class="zent-colorpicker-colors"]/div/div')

    def clicks_blank_color(self, n):
        self.clicks(self.blank_color_loc, n)

    blank_color_check_loc = ('xpath', '//div[@class="zent-colorpicker-board"]/div[1]/div/div/div[1]')

    def click_blank_color_check(self):
        self.click(self.blank_color_check_loc)

    # 页面
    page_query_loc = ('id', 'queryString')

    def input_page_query(self, name):
        self.send_keys(self.page_query_loc, name)

    # test页面
    test_page_loc = ('xpath', '//label[@class="ant-radio-wrapper"]/span')

    def click_test_page(self):
        self.click(self.test_page_loc)

    # 新增文件夹
    new_folder_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/button[2]')

    def click_new_folder(self):
        self.click(self.new_folder_loc)

    # 确定按钮
    sure_folder_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_folder_btn(self):
        self.click(self.sure_folder_btn_loc)

    # 是否新建文件夹

    page_folder_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]')

    def elements_page_folder(self):
        return self.find_elements(self.page_folder_loc)

    # test文件夹
    test_folder_data_loc = ('xpath', '//div[@class="nodata___3qxxL"]')

    def element_test_folder_data(self):
        return self.find_element(self.test_folder_data_loc)

    # 复制删除
    options_btn_loc = ('xpath', '//div[@class="ant-menu-item ant-menu-item-selected"]/span[2]/button')

    options_copy_btn_loc = ('xpath',
                            '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[3]')

    def move_options_copy_btn(self):
        self.move(self.options_btn_loc, self.options_copy_btn_loc)

    copy_option_sure_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_copy_option_sure(self):
        self.click(self.copy_option_sure_loc)

    options_delete_btn_loc = ('xpath',
                              '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')

    def move_options_delete_btn(self):
        self.move(self.options_btn_loc, self.options_copy_btn_loc)
