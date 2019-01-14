#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildMessagePage(Crazy):
    """留言管理"""
    #                               //*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[2]/a
    message_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[5]/a')

    def click_message_manage(self):
        self.click(self.message_manage_loc)

    # 验证
    check_message_text_loc = ('xpath', '//span[@class="ant-breadcrumb-link"]')

    def text_check_message_text(self):
        return self.get_text(self.check_message_text_loc)

    # 有没有留言数据
    message_data_loc = ('xpath', '//div[@class="ant-table-placeholder"]')

    def text_message_data(self):
        return self.get_text(self.message_data_loc)

    # 留言内容
    message_info_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr/td[6]')

    def elements_message_info(self):
        return self.find_elements(self.message_info_loc)

    # 勾选留言
    choice_message_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr/td[1]/span/label/span')

    def elements_choice_message(self):
        return self.find_elements(self.choice_message_loc)

    # 勾选成功
    check_choice_message_loc = ('xpath', '//button[@class="ant-btn ant-btn-danger"]')

    def element_check_choice_message(self):
        return self.find_element(self.check_choice_message_loc)

    # 选择审核通过
    check_to_success_message_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def element_check_to_success_message(self):
        return self.find_element(self.check_to_success_message_loc)

    # 批量审核确定
    choice_sure_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary ant-btn-sm"]')

    def click_choice_sure_btn(self):
        self.click(self.choice_sure_btn_loc)

    # 留言网友
    net_user_message_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr/td[4]')

    def elements_net_user_message(self):
        return self.find_elements(self.net_user_message_loc)

    # 选择审核通过
    option_btn_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr[1]/td[10]/button')
    option_to_examine_loc = ('xpath',
                             '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')

    def move_option_to_examine(self):
        self.move(self.option_btn_loc, self.option_to_examine_loc)

    # 审核不通过
    option_to_not_examine_loc = ('xpath',
                                 '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')

    def move_option_to_not_examine(self):
        self.move(self.option_btn_loc, self.option_to_not_examine_loc)

    # 回复留言
    reply_message_loc = ('id', 'reply')

    def input_reply_message(self, reply):
        self.send_keys(self.reply_message_loc, reply)

    # 验证留言成功
    check_reply_message_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr[1]/td[9]')

    def text_check_reply_message(self):
        return self.get_text(self.check_reply_message_loc)

    # 审核不通过原因
    to_not_examine_reason_loc = ('id', 'content')

    def input_to_not_examine_reason(self, reason):
        self.send_keys(self.to_not_examine_reason_loc, reason)

    # 确定
    sure_btn_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 审核状态
    examine_status_loc = ('xpath', '//div[@class="ant-col-xs-24 ant-col-sm-12 ant-col-md-12 ant-col-xl-10"]/div/label')

    def elements_examine_status(self):
        return self.find_elements(self.examine_status_loc)

    # 确定按钮
    upload_sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_upload_sure_btn(self):
        self.click(self.upload_sure_btn_loc)

    # 留言数量
    message_num_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[1]')

    def text_message_num(self):
        return self.get_text(self.message_num_loc)

    # 点击下一页

    next_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last() - 1]')

    def click_next_page(self):
        self.click(self.next_page_loc)

    # 查询
    query_time_loc = ('xpath', '//span[@class="ant-calendar-picker-input ant-input"]/input[1]')

    def click_query_time(self):
        self.click(self.query_time_loc)

    # 选择年份
    query_click_select_year_loc = (
        'xpath', '//div[@class="ant-calendar-range-part ant-calendar-range-left"]/div[2]/div[1]/div/span/a[1]')

    def click_query_click_year(self):
        self.click(self.query_click_select_year_loc)

    # 选择年份
    query_select_year_loc = ('xpath', '//tbody[@class="ant-calendar-year-panel-tbody"]/tr[4]/td[1]/a')

    def click_query_select_year(self):
        self.click(self.query_select_year_loc)

    # 默认一月，选择日期
    query_select_day_loc = (
        'xpath', '//div[@class="ant-calendar-range-part ant-calendar-range-left"]/div[2]/div[2]/table/tbody/tr/td/div')

    def elements_query_select_day(self):
        return self.find_elements(self.query_select_day_loc)

    # 结束日期
    query_end_day_loc = (
        'xpath', '//div[@class="ant-calendar-range-part ant-calendar-range-right"]/div[2]/div[2]/table/tbody/tr/td/div')

    def elements_query_end_day(self):
        return self.find_elements(self.query_end_day_loc)

    # 查询按钮
    query_btn_loc = ('xpath', '//button[@class="ant-btn margin-right ant-btn-primary"]')

    def click_query_btn(self):
        self.click(self.query_btn_loc)

    # 验证留言日期
    check_message_time_loc = ('xpath', '//table[@class="ant-table-fixed"]/tbody/tr/td[7]')

    def elements_check_message_time(self):
        return self.find_elements(self.check_message_time_loc)
