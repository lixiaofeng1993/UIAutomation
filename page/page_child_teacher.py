#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildTeacherPage(Crazy):
    """老师管理"""
    #                               //*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[2]/a
    teacher_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[8]/a')

    def click_teacher_manage(self):
        self.click(self.teacher_manage_loc)

    # 验证
    check_teacher_text_loc = ('xpath', '//span[@class="ant-breadcrumb-link"]/span')

    def text_check_teacher_text(self):
        return self.get_text(self.check_teacher_text_loc)

    # 添加老师按钮

    new_add_teacher_btn_loc = (
        'xpath', '//button[@class="ant-btn margin-right ant-btn-primary"]/following-sibling::button')

    def click_new_add_teacher_btn(self):
        self.click(self.new_add_teacher_btn_loc)

    # 验证
    new_add_teacher_loc = ('xpath', '//div[@class="ant-modal-header"]/div')

    def text_new_add_teacher(self):
        return self.get_text(self.new_add_teacher_loc)

    # 老师姓名
    teacher_name_loc = ('id', 'name')

    def input_teacher_name(self, name):
        self.send_keys(self.teacher_name_loc, name)

    # 手机号
    teacher_phone_loc = ('id', 'phone')

    def input_teacher_phone(self, phone):
        self.send_keys(self.teacher_phone_loc, phone)

    # 社会职称
    teacher_socialTitle_loc = ('id', 'socialTitle')

    def input_tsocialTitle_phone(self, phone):
        self.send_keys(self.teacher_socialTitle_loc, phone)

    # 性别
    teacher_sex_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[4]/div[2]/div/span/div/label/span[1]')

    def elements_teacher_sex(self):
        return self.find_elements(self.teacher_sex_loc)

    # 上传头像
    upload_teacher_img_loc = (
        'xpath', '//div[@class="ant-upload ant-upload-select ant-upload-select-text"]/span/button')

    def click_upload_teacher_img(self):
        self.click(self.upload_teacher_img_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 取消按钮
    cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    # 页面老师名称
    page_teacher_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[3]')

    def elements_page_teacher_name(self):
        return self.find_elements(self.page_teacher_name_loc)

    # 老师数量
    tag_number_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[1]')

    def text_tag_number(self):
        return self.get_text(self.tag_number_loc)

    # 点击下一页
    next_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last()-1]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    # 操作
    option_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[last()]/button')

    def elements_option_btn(self):
        return self.find_elements(self.option_btn_loc)

    # 确定
    delete_sure_btn_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_delete_sure_btn(self):
        self.click(self.delete_sure_btn_loc)

    # 翻页
    random_skip_page_loc = ('xpath', '//div[@class="ant-pagination-options-quick-jumper"]/input')

    def input_skip_page(self, num):
        self.send_keys(self.random_skip_page_loc, num)

    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)

    # 查询
    query_text_loc = ('id', 'queryString')

    def input_text(self, text):
        self.send_keys(self.query_text_loc, text)

    # 查询按钮
    query_btn_loc = ('xpath', '//button[@class="ant-btn margin-right ant-btn-primary"]')

    def click_query_btn(self):
        self.click(self.query_btn_loc)
