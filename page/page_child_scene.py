#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildScenePage(Crazy):
    """情景互动"""
    #                               //*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[2]/a
    scene_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[6]/a')

    def click_scene_manage(self):
        self.click(self.scene_manage_loc)

    # 验证
    check_scene_text_loc = ('xpath', '//span[@class="ant-breadcrumb-link"]/span')

    def text_check_scene_text(self):
        return self.get_text(self.check_scene_text_loc)

    # 选择情景互动类型
    scene_type_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[1]/div/div/label/span[2]')

    def elements_scene_type(self):
        return self.find_elements(self.scene_type_loc)

    # 新增按钮
    scene_newly_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def click_scene_newly_btn(self):
        self.click(self.scene_newly_btn_loc)

    # 验证弹出
    check_newly_text_loc = ('xpath', '//div[@class="ant-modal-header"]/div')

    def text_check_newly_text(self):
        return self.get_text(self.check_newly_text_loc)

    # 使用场景
    description_loc = ('id', 'description')

    def input_description(self, description):
        self.send_keys(self.description_loc, description)

    # 弹窗中的标题
    popup_title_loc = ('id', 'title')

    def input_popup_title(self, title):
        self.send_keys(self.popup_title_loc, title)

    # 添加内容  /html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div[1]/div[2]/div/span/button
    add_type_info_loc = ('xpath', '//span[@class="ant-form-item-children"]/button')

    def click_add_type_info(self):
        self.click(self.add_type_info_loc)

    # 翻页按钮
    page_btn_loc = ('xpath', '//div[@class="ant-modal-content"]/div[2]/div/div/div/ul/li/a')

    def elements_page_btn(self):
        return self.find_elements(self.page_btn_loc)

    # 选择内容
    check_scene_info_loc = ('xpath', '//div[@class="ant-spin-container"]/div/div/div/table/tbody/tr/td/span/label')

    def elements_check_scene_info(self):
        return self.find_elements(self.check_scene_info_loc)

    # /html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[2]
    one_sure_btn_loc = ('xpath', '//body/div[last()]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_one_sure_btn(self):
        self.click(self.one_sure_btn_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 配置文案
    config_word_loc = ('xpath', '//div[@class="ant-modal-body"]/form/div[3]/div[2]/div[2]/div/span/input')

    def input_config_word(self, word):
        self.send_keys(self.config_word_loc, word)

    # 第二个配置文案
    second_config_word_loc = ('xpath', '//div[@class="ant-modal-body"]/form/div[4]/div[2]/div[2]/div/span/input')

    def input_second_config_word(self, word):
        self.send_keys(self.second_config_word_loc, word)

    # 上传图片按钮
    upload_img_btn_loc = ('xpath', '//div[@class="ant-upload ant-upload-select ant-upload-select-text"]/span/button')

    def click_upload_img_btn(self):
        self.click(self.upload_img_btn_loc)

    # 再次添加
    again_add_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[4]/div[2]/div/span/button')

    def click_again_add(self):
        self.click(self.again_add_loc)

    # 上下架 //div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label/span[2]
    is_upper_lower_loc = ('xpath', '//div[@id="upDownStatus"]/label/span[1]')

    def elements_is_upper_lower(self):
        return self.find_elements(self.is_upper_lower_loc)

    # 验证新增成功
    scene_page_info_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[2]')

    def elements_scene_page_info(self):
        return self.find_elements(self.scene_page_info_loc)

    # 上下架按钮切换
    upper_lower_btn_loc = ('xpath', '//div[@class="contentInner___3XSLP"]/div[1]/div[3]/div/div/label/span[2]')

    def elements_upper_lower_btn(self):
        return self.find_elements(self.upper_lower_btn_loc)

    # 重复添加内容
    repeat_add_info_error_loc = ('xpath', '//div[@class="ant-message-custom-content ant-message-error"]/span')

    def text_repeat_add_info_error(self):
        return self.get_text(self.repeat_add_info_error_loc)

    repeat_info_btn_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[4]/div/div[2]/div[1]/span[1]/button')

    def click_repeat_info_btn(self):
        self.click(self.repeat_info_btn_loc)

    # 添加商品
    add_goods_loc = ('id', 'productId')

    def input_add_goods(self, goods):
        self.send_keys(self.add_goods_loc, goods)

    # 添加按钮
    add_btn_loc = ('xpath', '//div[@class="ant-row ant-form-item"]/div[2]/div/span/button')

    def click_add_btn(self):
        self.click(self.add_btn_loc)

    # 删除商品
    delete_goods_btn_loc = (
        'xpath', '//button[@class="ant-btn ant-btn-danger ant-btn-circle ant-btn-sm ant-btn-icon-only"]')

    def elements_delete_goods_btn(self):
        return self.find_elements(self.delete_goods_btn_loc)

    # 删除确定
    delete_sure_btn_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_delete_sure_btn(self):
        self.click(self.delete_sure_btn_loc)

    option_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[last()]/td[last()]/button')
    # 编辑
    edit_scene_btn_loc = ('xpath',
                          '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[3]')
    # 查看
    look_scene_btn_loc = ('xpath',
                          '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')
    # 上架、下架
    upper_scene_btn_loc = ('xpath',
                           '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')
    # 删除
    delete_scene_btn_loc = ('xpath',
                            '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[4]')

    def move_edit_scene_btn(self):
        self.move(self.option_btn_loc, self.edit_scene_btn_loc)

    def move_look_scene_btn_loc(self):
        self.move(self.option_btn_loc, self.look_scene_btn_loc)

    def move_upper_scene_btn(self):
        self.move(self.option_btn_loc, self.upper_scene_btn_loc)

    def move_delete_scene_btn(self):
        self.move(self.option_btn_loc, self.delete_scene_btn_loc)

    # 点击x
    close_x_loc = ('xpath', '//span[@class="ant-modal-close-x"]')

    def click_close_x(self):
        self.click(self.close_x_loc)

    # 第一个情景互动名称
    scene_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]')

    def text_scene_name(self):
        return self.get_text(self.scene_name_loc)

    # 查询
    query_input_loc = ('id', 'queryString')

    def input_query_input(self, query):
        self