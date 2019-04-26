#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:31
# @Author  : lixiaofeng
# @File    : page_zaojiao.py
# @Software: PyCharm
# @desc    :

from common.basics import Crazy


class Zaojiaopage(Crazy):
    """早教小程序"""

    zao_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cw" and @text="包妈优选"]')

    def click_zao(self):
        self.click(self.zao_btn_loc)

    def element_zao(self):
        return self.find_element(self.zao_btn_loc)

    find_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/d7b" and @text="发现"]')  # 发现按钮

    def click_find(self):
        self.click(self.find_loc)

    title_btn_loc = ('xpath', '//*[@resource-id="android:id/title" and @text="小程序"]')  # 发现页小程序按钮

    def click_title_btn(self):
        self.click(self.title_btn_loc)

    helper_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="小程序助手"]')  # 小程序助手

    def element_helper(self):
        return self.find_element(self.helper_loc)

    def click_helper(self):
        self.click(self.helper_loc)

    zaojiao_small_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="包妈优选"]')  # 包妈优选小程序

    def element_zaojiao_small_btn(self):
        return self.find_element(self.zaojiao_small_btn_loc)

    delete_small_btn_loc = ('xpath', '//*[contains(@text, "删除")]')  # 删除小程序按钮

    def click_delete_small_btn(self):
        self.click(self.delete_small_btn_loc)

    edition_btn_loc = ('xpath', '//*[contains(@text, "百宝福利Buy")]')

    def element_edition_btn(self):
        return self.find_element(self.edition_btn_loc)

    delete_small1_btn_loc = ('xpath', '//*[contains(@text, "拖动到此处删除")]')

    def element_delete_small1_btn(self):
        return self.find_element(self.delete_small1_btn_loc)

    version_btn_loc = ('xpath', '//*[contains(@text, "版本查看")]')  # 版本查看按钮

    def click_version_btn(self):
        self.click(self.version_btn_loc)

    experience_version_btn_loc = ('xpath', '//*[contains(@text, "1.1.497")]')  # 体验版

    def click_experience_version_btn(self):
        self.click(self.experience_version_btn_loc)

    audition_class_btn_loc = ('xpath', '//*[contains(@text, "0元领取7节试听课")]')  # 领取试听课

    def click_audition_class_btn(self):
        self.click(self.audition_class_btn_loc)

    month_btn_loc = ('xpath', '//*[contains(@text, "2018")]')  # 选择月份

    def click_mouth_btn(self):
        self.click(self.month_btn_loc)

    sure_btn_loc = ('xpath', '//*[contains(@text, "确定")]')  # 确定按钮

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    attend_lectures_btn_loc = ('xpath', '//*[contains(@text, "立即听课")]')  # 立即听课

    def click_attend_lectures_btn(self):
        self.click(self.attend_lectures_btn_loc)

    get_to_know_btn_loc = ('xpath', '//*[contains(@text, "立即了解正式课 ")]')  # 立即了解正式课

    def click_get_to_know_btn(self):
        self.click(self.get_to_know_btn_loc)

    sure_buy_btn_loc = ('xpath', '//*[contains(@text, "立即购买")]')  # 立即购买

    def click_sure_buy_btn(self):
        self.click(self.sure_buy_btn_loc)

    buy_password_loc = ('id', 'com.tencent.mm:id/cei')  # 输入支付密码

    def input_buy_password(self, paw):
        self.send_keys(self.buy_password_loc, paw)

    check_buy_money_loc = ('id', 'com.tencent.mm:id/dhz')  # 获取支付金额

    def text_buy_money(self):
        return self.get_text(self.check_buy_money_loc)

    success_btn_loc = ('id', 'com.tencent.mm:id/f1w')  # 完成按钮

    def click_success_btn(self):
        self.click(self.success_btn_loc)

    check_address_btn_loc = ('xpath', '//*[contains(@text, "收货地址：请选择地址")]')  # 选择收货地址

    def click_check_address_btn(self):
        self.click(self.check_address_btn_loc)

    add_address_btn_loc = ('xpath', '//*[contains(@text, "添加地址")]')  # 添加地址

    def click_add_address_btn(self):
        self.click(self.add_address_btn_loc)

    name_loc = ('xpath', '//*[contains(@text, "请输入你的姓名")]')  # 请输入你的姓名

    def input_name_btn(self, name):
        self.send_keys(self.name_loc, name)

    phone_btn_loc = ('xpath', '//*[contains(@text, "请填写收件人电话")]')  # 请填写收件人电话

    def input_phone_btn(self, phone):
        self.send_keys(self.phone_btn_loc, phone)

    region_btn_loc = ('xpath', '//*[contains(@text, "请输入你所在地区")]')  # 请输入你所在地区

    def click_region_btn(self):
        self.click(self.region_btn_loc)

    detailed_address_btn_loc = ('xpath', '//*[contains(@text, "请输入你的详细地址")]')  # 请输入你的详细地址

    def input_detailed_address_btn(self, address):
        self.send_keys(self.detailed_address_btn_loc, address)

    save_btn_loc = ('xpath', '//*[contains(@text, "保存")]')  # 保存

    def click_save_btn(self):
        self.click(self.save_btn_loc)

    receive_btn_loc = ('xpath', '//*[contains(@text, "立即领取")]')  # 立即领取

    def click_receive_btn(self):
        self.click(self.receive_btn_loc)

    addressee_loc = ('xpath', '//*[contains(@text, "收件人：")]')  # 地址列表是否有地址信息

    def elements_addressee(self):
        return self.find_elements(self.addressee_loc)

    def clicks_addressee(self):
        self.clicks(self.addressee_loc, 0)

    know_btn_loc = ('xpath', '//*[contains(@text, "知道了")]')  # 地址列表是否有地址信息

    def element_know(self):
        return self.find_element(self.know_btn_loc)

    def click_know(self):
        self.click(self.know_btn_loc)

    all_curriculum_btn_loc = ('xpath', '//*[contains(@text, "查看全部课程")]')  # 查看全部课程

    def element_all_curriculum_btn(self):
        return self.find_element(self.all_curriculum_btn_loc)

    def click_all_curriculum_btn(self):
        self.click(self.all_curriculum_btn_loc)

    curriculum_date_btn_loc = ('xpath', '//*[contains(@text, "2019-0")]')  # 历史推送

    def element_curriculum_date_btn(self):
        return self.find_element(self.curriculum_date_btn_loc)

    my_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cs" and @text="我的"]')  # 我的

    def click_my(self):
        self.click(self.my_btn_loc)

    my_baby_btn_loc = ('xpath', '//*[contains(@text, "我的宝宝")]')  # 我的宝宝

    def click_my_baby(self):
        self.click(self.my_baby_btn_loc)

    my_baby_title_loc = ('id', 'com.tencent.mm:id/oa')

    def text_my_baby_title(self):
        return self.get_text(self.my_baby_title_loc)

    new_baby_btn_loc = ('xpath', '//*[contains(@text, "新建宝宝")]')  # 新建宝宝

    def element_new_baby_btn(self):
        return self.find_element(self.new_baby_btn_loc)

    def click_new_baby_btn(self):
        self.click(self.new_baby_btn_loc)

    next_btn_loc = ('xpath', '//*[contains(@text, "下一步")]')  # 我的宝宝

    def click_next(self):
        self.click(self.next_btn_loc)

    baby_name_loc = ('xpath', '//*[contains(@text, "请输入宝宝姓名")]')  # 请输入宝宝姓名

    def input_baby_name(self, name):
        self.send_keys(self.baby_name_loc, name)

    baby_bir_btn_loc = ('xpath', '//*[contains(@text, "宝宝的生日:")]')  # 宝宝的生日

    def click_baby_bir_btn(self):
        self.click(self.baby_bir_btn_loc)

    finish_btn_loc = ('xpath', '//*[contains(@text, "完成")]')  # 完成按钮

    def click_finish_btn(self):
        self.click(self.finish_btn_loc)

    my_home_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cs" and @text="首页"]')  # 首页

    def click_my_home(self):
        self.click(self.my_home_loc)

    switch_btn_loc = ('xpath', '//*[contains(@text, "切换")]')  # 切换

    def click_switch_btn(self):
        self.click(self.switch_btn_loc)
