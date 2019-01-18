#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildGoldPage(Crazy):
    """分类管理"""
    gold_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[7]/div/span')

    def click_gold_manage(self):
        self.click(self.gold_manage_loc)

    # 二级分类
    all_manage_loc = ('xpath', '//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li/a')

    def elements_all_manage(self):
        return self.find_elements(self.all_manage_loc)

    # 验证
    check_gold_text_loc = ('xpath', '//div[@class="bread___2EMeU"]/div/span[2]/span[1]/span')

    def text_check_gold_text(self):
        return self.get_text(self.check_gold_text_loc)

    # 添加按钮
    new_add_gold_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def click_new_add_gold_btn(self):
        self.click(self.new_add_gold_btn_loc)

    # 选择数据
    check_data_loc = ('class name', 'ant-modal-title')

    def text_check_data(self):
        return self.get_text(self.check_data_loc)

    # 选择添加内容类型
    new_add_type_loc = ('xpath', '//div[@class="ant-radio-group"]/label/span[2]')

    def elements_new_add_type(self):
        return self.find_elements(self.new_add_type_loc)

    # 选择页
    check_random_page_loc = ('xpath', '//div[@class="ant-modal-body"]/div/div/div/ul/li/a')

    def elements_check_random_page(self):
        return self.find_elements(self.check_random_page_loc)

    # 选择内容
    check_random_info_loc = (
        'xpath', '//div[@class="ant-modal-body"]/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label')

    def elements_check_random_info(self):
        return self.find_elements(self.check_random_info_loc)

    check_info_name_loc = ('xpath', '//div[@class="ant-modal-body"]/div/div/div/div/div/div/table/tbody/tr/td[3]')

    def elements_check_info_name(self):
        return self.find_elements(self.check_info_name_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 取消按钮
    cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    # 页面已有元素名称
    page_info_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[3]')

    def elements_page_info_name(self):
        return self.find_elements(self.page_info_name_loc)

    # 金币
    gold_num_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[5]')

    def elements_gold_num(self):
        return self.find_elements(self.gold_num_loc)

    # 标签数量
    tag_number_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[1]')

    def text_tag_number(self):
        return self.get_text(self.tag_number_loc)

    # 点击下一页
    next_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last()-1]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    # 编辑按钮
    edit_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[last()]/div/span/a[1]')

    def elements_edit_btn(self):
        return self.find_elements(self.edit_btn_loc)

    # 删除按钮
    delete_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[last()]/div/span/a[1]')

    def elements_delete_btn(self):
        return self.find_elements(self.delete_btn_loc)

    # 编辑日期
    edit_time_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[4]/div/div/div/span/span/div/input')

    def click_edit_time(self):
        self.click(self.edit_time_loc)

    # 选择此刻
    now_time_loc = ('xpath', '//span[@class="ant-calendar-footer-btn"]/a[1]')

    def click_now_time(self):
        self.click(self.now_time_loc)

    # 兑换金币
    gold_text_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[5]/div/div/div/span/div/div[2]/input')

    def input_gold_text(self, gold):
        self.send_keys(self.gold_text_loc, gold)

    # 添加重复记录
    new_add_error_loc = ('xpath', '//div[@class="ant-message-notice"]/div/div/span')

    def text_new_add_error(self):
        return self.get_text(self.new_add_error_loc)

    # 删除按钮
    delete_gold_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[last()]/div/span/a[2]')

    def elements_delete_gold_btn(self):
        return self.find_elements(self.delete_gold_btn_loc)

    # 删除确定按钮
    delete_gold_sure_btn_loc = (
        'xpath', '//div[@class="ant-popover ant-popover-placement-top"]/div/div[2]/div/div/div[2]/button[2]')

    def click_delete_gold_sure_btn(self):
        self.click(self.delete_gold_sure_btn_loc)

    # 翻页
    random_skip_page_loc = ('xpath', '//div[@class="ant-pagination-options-quick-jumper"]/input')

    def input_skip_page(self, num):
        self.send_keys(self.random_skip_page_loc, num)

    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)
