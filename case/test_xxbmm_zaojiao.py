#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:22
# @Author  : lixiaofeng
# @File    : test_xxbmm_zaojiao.py
# @Software: PyCharm
# @desc    :

import time
import unittest, random
from faker import Faker
from BeautifulReport import BeautifulReport
from appium.webdriver.common.touch_action import TouchAction
from common.basics import open_app
from common.logger import Log, img_path
from page.page_zaojiao import Zaojiaopage
from common import read_config
from common.api import clear_user


# from common import readConfig
# from common.connectDB import SqL


class TestXbu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.zao = Zaojiaopage(cls.driver)
        cls.t = TouchAction(cls.driver)
        cls.faker = Faker('zh_CN')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_1first_baby')
    def test_1first_baby(self):
        """第一个宝宝的购买和领课流程"""
        z = self.zao
        time.sleep(2)
        self.delete_applet(z)
        self.log.info('第一个宝宝开始进行操作...')
        self.buy_class(z, n=1)
        self.leading_class(z, n=1)
        self.create_baby(z)
        self.my_page_operation(z, n=1)
        self.operation_game_class(z, n=1)
        self.log.info('第一个宝宝操作完成！\n')

    @BeautifulReport.add_test_img('test_2second_baby')
    def test_2second_baby(self):
        """第二个宝宝的购买和领课流程"""
        z = self.zao
        self.log.info('第二个宝宝开始进行操作...')
        self.buy_class(z)
        self.leading_class(z, n=2)
        self.create_baby(z)
        self.my_page_operation(z, n=2)
        self.operation_game_class(z, n=2)
        self.log.info('第二个宝宝操作完成！\n')

    @BeautifulReport.add_test_img('test_3last_baby')
    def test_3last_baby(self):
        """第三个宝宝的购买和领课流程"""
        z = self.zao
        self.log.info('第三个宝宝开始进行操作...')
        self.buy_class(z)
        self.leading_class(z, n=3)
        self.my_page_operation(z, n=3)
        self.operation_game_class(z, n=3)
        # self.clock_card(z)
        self.log.info('第三个宝宝操作完成！\n')

    def delete_applet(self, z):
        z.swipeDown(n=2)
        if not z.element_zao():
            self.log.error('被测小程序不存在！')
        else:
            self.log.info('删除被测小程序.')
            element_obj = self.t.long_press(z.element_zao()).perform()
            element_obj.move_to(z.element_delete_small1_btn()).wait(1000).release().perform()
            time.sleep(2)
        z.click_small_help_btn()
        self.log.info('点击小程序助手，查找被测小程序.')
        if not z.element_small_name():
            z.click_switching_applet_btn()
            if z.element_small_name():
                z.click_small_name()
            else:
                self.log.error('没有发现要测试的小程序')
                return
        z.click_version_btn()
        self.log.info('正在进入被测小程序...')
        z.clicks_experience_version_btn()
        while True:
            if z.element_audition_class_btn():
                self.log.info('点击按钮，进行授权!')
                z.click_audition_class_btn()
                break
            else:
                self.log.info('未发现0元领取10节试听课按钮，等待中...')
                time.sleep(3)
        self.log.info('正在进行授权操作.')
        z.click_wechat_grant_btn()
        z.click_allow_btn()
        while True:
            if z.element_wechat_grant_btn():
                z.click_wechat_grant_btn()
                time.sleep(1)
            else:
                self.log.info('授权成功！')
                break

    def clock_card(self, z):
        """打卡"""
        if not z.element_my_btn():
            self.log.error('当前位置不在首页，无法点击 首页 按钮！')
            return
        z.click_my_home()
        if not z.element_clock_btn():
            self.log.error('没有发现打卡按钮！')
            return
        z.click_clock_btn()
        self.log.info(z.elements_title()[-1].text + '=====>页面title')
        self.assertEqual(z.elements_title()[-1].text, '打卡攻略', '进入打卡首页失败！')
        self.log.info('进入打卡页面成功！')
        if not z.element_no_clock_btn():
            self.log.warning('打卡界面没有发现未打卡标志，退出！')
            # return
        z.click_get_card_btn()
        i = 1
        while True:
            if z.element_generated_loading():
                self.log.info('等待海报生成中...{}'.format(i))
                i += 1
                time.sleep(1)
            else:
                self.log.info('生成海报成功！')
                break
        self.log.info(z.elements_title()[-1].text + '=====>1')
        z.click_save_img_btn()
        self.log.info(z.elements_title()[-1].text + '=====>2')
        z.click_copy_text_btn()
        if z.element_copy_format_btn():
            z.click_know()
        z.click_card_go_btn()
        self.log.info(z.elements_title()[-1].text + '=====>4')
        z.swipeUp(n=1)
        try:
            z.click_upload_card_btn()
        except AttributeError:
            z.click_again_upload_card_btn()
            z.click_reset_img_btn()
        z.clicks_choice_album(0)
        z.click_complete_btn()
        self.log.info(z.elements_title()[-1].text + '=====>5')
        z.click_upload_btn()
        if z.element_today_card_btn():
            self.log.info('上传打卡成功！')
        else:
            self.log.error('上传打卡失败！')

    def click_reply_8_img(self, z, buy=False, type=5):
        """点击回复 8 进群banner"""
        self.log.info('发现的元素数量：{}, buy: {}, type: {}'.format(len(z.elements_reply_8()), buy, type))
        if type == 8:
            if buy:
                i = 33
            else:
                i = 17
        elif type == 5:
            i = 1
        while True:
            self.log.info('尝试点击image元素.')
            if type == 5:
                z.elements_reply_8()[i].click()
            else:
                z.elements_reply_8()[i].click()
            i += 1
            if i > len(z.elements_reply_8()):
                self.log.error('遍历完成，没有发现正确的页面！')
                break
            if z.element_parent_btn():
                self.log.info('成功进入回复{}页面！'.format(type))
                break
            else:
                self.log.info(z.elements_title()[-1].text + '=====>页面title')
                if type == 5:
                    if z.elements_title()[-1].text == '在家早教课':
                        if z.element_get_set() and not z.element_collection_btn():
                            self.log.info('点击失败，还在当前页面！点击次数：{}'.format(i - 1))
                        else:
                            self.log.info('第{}次返回...'.format(i - 1))
                            time.sleep(1)
                            z.back()
                    else:
                        self.log.info('第{}次返回...'.format(i - 1))
                        time.sleep(1)
                        z.back()
                elif type == 8:
                    if z.elements_title()[-1].text == '早教核心课':
                        if z.element_get_set() and not z.element_collection_btn():
                            if buy:
                                self.log.info('点击失败，还在当前页面！点击次数：{}'.format(i - 33))
                            else:
                                self.log.info('点击失败，还在当前页面！点击次数：{}'.format(i - 17))
                        else:
                            if buy:
                                self.log.info('第{}次返回...'.format(i - 33))
                            else:
                                self.log.info('第{}次返回...'.format(i - 17))
                            time.sleep(1)
                            z.back()
                    else:
                        if buy:
                            self.log.info('第{}次返回...'.format(i - 33))
                        else:
                            self.log.info('第{}次返回...'.format(i - 17))
                        time.sleep(1)
                        z.back()

    def add_group(self, z, make=False, buy=False):
        """进群流程"""
        self.log.info('点击进群banner，进行进群流程验证...make：{}'.format(make))
        if make:
            self.log.info('查找回复8进群banner中...')
            self.click_reply_8_img(z, buy=buy, type=8)
            if not self.long_code_fun(z, '8'):
                return
            self.log.info('跳转到公众号，点击推送信息，长按识别二维码进群！')
            if not z.text_class_group():
                time.sleep(3)
            self.assertIn('小小包早教课学习群', z.text_class_group(), '回复8，扫码识别错误！')
            self.log.info('回复8，识别进群码成功！')
            time.sleep(1)
            z.click_x_btn()
            time.sleep(1)
            z.click_zao()
            time.sleep(3)
            z.back()
        else:
            self.log.info('点击回复5进群banner.')
            # z.elements_reply_5()[0].click()
            self.click_reply_8_img(z, type=5)
            time.sleep(1)
            if not self.long_code_fun(z, '5'):
                return
            if not z.text_class_group():
                time.sleep(3)
            self.assertIn('小小包早教训练', z.text_class_group(), '回复5，扫码识别错误！')
            self.log.info('回复5，识别进群码成功！')
            time.sleep(3)
            z.click_x_btn()
            z.click_long_code()
            time.sleep(1)
            z.back()
            time.sleep(1)
            z.back()
            time.sleep(1)

    def long_code_fun(self, z, n):
        """发现二维码并长按"""
        z.click_add_to_btn()
        z.input_reply_5(n)
        z.click_send()
        time.sleep(3)  # 等待服务器返回二维码
        self.log.info('发送 {} ，并长按返回二维码.'.format(n))
        i = 0
        while True:
            z.clicks_reply_code(-1)
            if z.element_long_code():
                self.log.info('长按二维码.')
                z.long_press(z.element_long_code())
                self.log.info('识别进群码操作.')
                z.click_discern_code()
                if n == '8':
                    z.clicks_info_btn(-1)
                    z.long_press(z.elements_reply_8()[0])
                    z.click_discern_code()
                break
            else:
                i += 1
                if z.elements_reply_code():
                    self.log.info('未发现可长按二维码，继续点击的次数{}'.format(i))
                    # z.clicks_reply_code(-1)
                else:
                    self.log.error('长按二维码出现错误！')
                    return False
        return True

    def buy_class(self, z, n=0):
        """购买流程"""
        time.sleep(1)
        if n:
            if z.element_attend_lectures_btn():
                z.click_attend_lectures_btn()
            else:
                z.click_audition_class_btn()
                time.sleep(1)
                z.click_sure_btn()
                # z.class_info_btn()
        else:
            z.click_attend_lectures_btn()
        time.sleep(1)
        self.log.info('进行购买核心课操作...')
        self.add_group(z)
        z.click_get_to_know_btn()
        z.click_sure_buy_btn()
        self.payment_window(z)

    def payment_window(self, z):
        """支付弹窗"""
        # self.assertEqual(z.text_payment(), '请输入支付密码', '调用微信支付失败！')
        if z.text_payment() not in ['请输入支付密码', '请验证指纹']:
            self.log.error('调用微信支付失败!')
            return
        self.log.info('调用微信支付成功，弹出输入密码弹窗！')
        buy_money = float(z.text_buy_money().replace('¥', ''))
        self.log.info('支付金额是：{} 元'.format(buy_money))
        if buy_money != 0.01:
            self.log.error('支付金额不是0.01元！{} 元'.format(buy_money))
            return
        i = 0
        while True:
            if i > len(read_config.payment_password):
                self.log.error('配置文件中的支付密码没有正确的！')
                break
            if z.element_usd_password():
                self.log.info('从指纹支付切换到输入密码支付！')
                z.click_usd_password()
            z.input_buy_password(read_config.payment_password[i])
            if z.element_password_error():
                i += 1
                self.log.warning('密码输入错误，进行重试...{}次'.format(i))
                z.click_again_btn()
            else:
                break
        if z.text_start_fingerprint_buy():
            self.log.info('弹出开启指纹支付的提示，正在处理该弹窗！')
            z.click_no_more_reminder_btn()
            z.click_cancel_btn()
        z.click_success_btn()
        self.log.info('支付完成，进行领取核心课操作...')

    def leading_class(self, z, n):
        """领取已购买课程，并查看历史推送"""
        buy = False
        if not self.receive_curriculum(z):
            self.log.info('没有发现购买未领取的课程.')
            z.click_attend_lectures_btn()
        else:
            self.choice_moth(z, n)
            time.sleep(1)
            z.click_receive_btn()
            buy = True
            self.log.info('领取课程成功！')
        if z.element_know():
            self.log.info('存在我知道了弹层，正常点击中.')
            z.click_know()
        if z.element_know():
            self.log.info('存在我知道了弹层，正常点击中.')
            z.click_know()
        if z.element_get_to_know_btn():
            self.log.warning('该宝宝还未购买核心课！')
            return
        self.add_group(z, make=True, buy=buy)
        z.swipeUp(n=5)
        z.click_all_curriculum_btn()
        time.sleep(2)
        if z.element_curriculum_date_btn():
            self.log.info('查看历史推送成功！')
        else:
            self.log.error('查看历史推送失败！')
            return
        self.release_record(z, n)
        self._back(z)

    def choice_moth(self, z, n):
        """区别三个宝宝，选择不同的月份"""
        if n == 1:
            pass
        elif n == 2:
            z.click_baby_bri()
            time.sleep(1)
            z.click_mouth_btn()
            z.click_sure_btn()
        else:
            z.click_baby_bri()
            time.sleep(1)
            z.click_mouth_btn()
            time.sleep(1)
            z.click_mouth_btn()
            time.sleep(1)
            z.click_mouth_btn()
            z.click_sure_btn()

    def release_record(self, z, n=1, make=False):
        """发布记录操作"""
        self.log.info('选择指定课程.{n}--->{make}'.format(n=n, make=make))
        if not make:
            z.swipeUp(n=5)
            z.clicks_class_name(-1)
        else:
            z.clicks_class2_name(-1)
            if z.element_reminder_btn():
                z.click_know()
        z.swipeUp(n=5)
        time.sleep(2)
        try:
            z.clicks_collection_btn(-1)
        except IndexError:
            try:
                z.click_collection_btn()
            except AttributeError:
                self.log.warning('收藏按钮点击失败了......')
                pass
        self.log.info('点击收藏按钮.')
        self.log.info('进行发布记录操作...')
        try:
            z.clicks_write_record_btn(-1)
        except IndexError:
            try:
                z.click_write_record_btn()
            except AttributeError:
                self.log.error('无法点击写记录按钮！')
                return

        if z.element_typewriting_finish_btn():
            z.click_typewriting_finish_btn()

        self.log.info('输入记录文本.')
        data = self.faker.text(max_nb_chars=200)
        try:
            z.inputs_write_text(data, -1)
        except IndexError:
            try:
                z.input_write_text(data)
            except AttributeError:
                self.log.error('无法点击记录输入框！')
                return
        time.sleep(1)
        self.log.info('选择记录配图或者小视频.')
        if z.element_typewriting_finish_btn():
            z.click_typewriting_finish_btn()
        if n == 1:
            self.log.info('选择图片中...')
            z.click_album_btn()
            for i in range(3):
                self.log.info('选择第{}张图片中...'.format(i))
                z.clicks_choice_album(i)
                # z.clicks_choice_album(0)
        else:
            self.log.info('选择视频中...')
            z.click_small_video_btn()
            if z.element_typewriting_finish_btn():
                z.click_typewriting_finish_btn()
            # num = random.randint(0, len(z.elements_choice_album()))
            # z.clicks_choice_album(num)
            z.clicks_choice_album(0)
        z.click_complete_btn()
        self.log.info('选择图片或视频成功！')
        time.sleep(2)
        self.log.info('记录发布状态：{}'.format(z.element_record_info(data)))
        self.assertTrue(z.element_record_info(data), '发布记录失败了呢！')
        if z.element_typewriting_finish_btn():
            z.click_typewriting_finish_btn()
        z.clicks_release_btn(-1)
        self.log.info('记录：{} 发布成功'.format(data))

    def create_baby(self, z):
        """创建宝宝，并返回首页切换最新创建的宝宝"""
        if not z.element_my_btn():
            self.log.error('当前位置不在首页，无法点击 我的 按钮！')
            return
        z.click_my()
        self.log.info(z.text_my_baby_title() + '=====>页面title')
        self.assertEqual(z.text_my_baby_title(), '个人中心', '进入个人中心失败！')
        self.log.info('进入个人中心成功，开始进行新建宝宝操作...')
        z.click_my_baby()
        if z.element_typewriting_finish_btn():
            z.click_typewriting_finish_btn()
        if not z.element_new_baby_btn():
            self.log.error('无法创建宝宝，请检查原因！')
            return
        z.clicks_new_baby_btn(-1)
        time.sleep(1)
        z.click_next()
        baby_name = self.faker.last_name()
        z.inputs_baby_name(baby_name, -1)
        if z.element_typewriting_finish_btn():
            z.click_typewriting_finish_btn()
        z.click_baby_bir_btn()
        time.sleep(1)
        z.click_sure_btn()
        z.clicks_finish_btn(-1)
        if z.element_new_baby_btn():
            self.log.error('创建宝宝失败，请检查原因！')
            return
        self.log.info('创建宝宝: {} 成功！'.format(baby_name))
        self._back(z)

    def my_page_operation(self, z, n):
        """我的页面其他功能操作"""
        if not z.element_my_btn():
            self.log.error('当前位置不在首页，无法点击 我的 按钮！')
            return
        z.click_my()
        z.click_my_collection_btn()
        if z.elements_my_collection_english_course_btn() or z.elements_my_collection_game_course_btn():
            self.log.info('在课程详情页添加收藏成功，共 {} 条！'.format(
                len(z.elements_my_collection_english_course_btn()) + len(z.elements_my_collection_game_course_btn())))
        else:
            self.log.warning('在课程详情页添加收藏存在失败的情况，请查明原因！')
        time.sleep(1)
        z.back()
        z.click_my_course_btn()
        if z.elements_my_course_buy_btn():
            if n == len(z.elements_my_course_buy_btn()):
                self.log.info('成功购买 {} 节早教核心课！'.format(n))
            else:
                self.log.warning('购买早教核心课数量出现错误！')
        else:
            self.log.error('当前未检测到购买的课程！')
        time.sleep(1)
        z.back()
        z.click_my_order_btn()
        if z.elements_my_order_card_btn():
            for i in z.elements_my_order_card_btn():
                self.log.info('获取到的订单编号有： {}'.format(i.text.replace('订单编号：', '')))
        else:
            self.log.warning('未发现订单，请检查原因！')
        time.sleep(1)
        z.back()
        z.click_my_record_btn()
        if z.elements_my_record_class_btn():
            self.log.info('成长记录添加成功，共 {} 条！'.format(n))
        else:
            self.log.warning('成长记录添加存在失败的情况，请查看原因！')
        time.sleep(1)
        z.back()
        z.click_my_home()
        self.log.info('切换宝宝操作.')
        z.click_switch_btn()

    def operation_game_class(self, z, n):
        """操作游戏课程"""
        if not z.element_my_home():
            self.log.error('当前位置不在首页，无法点击 首页 按钮！')
            return
        z.click_my_home()
        while True:
            try:
                z.element_look_all_btn()[-1].click()
            except IndexError:
                try:
                    z.click_look_all_btn()
                except AttributeError:
                    self.log.warning('没有找到 查看全部 按钮......')
                    return
            time.sleep(1)
            self.log.info(z.elements_title()[-1].text + '=====>页面title')
            if z.elements_title()[-1].text == '游戏百宝箱':
                self.log.info('进入游戏主页成功！')
                break
            else:
                self.log.warning('到哪了这是？')
                self._back(z)
        # self.assertEqual(z.elements_title()[-1].text, '游戏百宝箱', '进入游戏首页失败！')
        z.element_look_all_btn()[-1].click()

        self.log.info(z.elements_title()[-1].text + '=====>页面title')
        if z.elements_title()[-1].text == '宝宝游戏箱':
            self.log.info('进入宝宝游戏箱成功！')
        else:
            self.log.warning('到哪了这是 +1')
        # self.assertEqual(z.elements_title()[-1].text, '宝宝游戏箱', '进入宝宝游戏箱失败！')
        self.release_record(z, n, make=True)
        self._back(z)
        z.swipeDown(n=2)  # 返回首页顶部

    def receive_curriculum(self, z):
        """选择地址信息"""
        if not z.element_check_address_btn():
            self.log.info('选择收货地址按钮不存在！')
            return False
        z.click_check_address_btn()
        if z.elements_addressee():
            self.log.info('地址信息已存在，默认选择第一个地址信息.')
            z.clicks_addressee()
            return True
        else:
            self.log.info('地址信息不存在，进行添加地址信息操作...')
            z.click_add_address_btn()
            z.input_name_btn(self.faker.name())
            z.input_phone_btn(self.faker.phone_number())
            z.click_region_btn()
            z.click_sure_btn()
            z.input_detailed_address_btn(self.faker.address())
            time.sleep(1)
            z.click_save_btn()
            self.log.info('添加收货地址完成！')
            return True

    def delete_test_small_program(self, z):
        """发现-小程序-判断小程序是否存在并删除"""
        test_small_program = z.element_zaojiao_small_btn()
        if not test_small_program:
            self.log.error('不存在被测试的小程序！')
            return False
        else:
            while True:
                time.sleep(0.5)
                if z.element_zaojiao_small_btn():
                    z.long_press(z.element_zaojiao_small_btn())
                    z.click_delete_small_btn()
                else:
                    self.log.info('测试小程序删除成功！')
                    break
            return True

    def _back(self, z):
        """返回按钮"""
        n = 0
        while True:
            if z.element_back_btn():
                z.click_back_btn()
                self.log.info('连续点击返回操作次数: {}'.format(n))
                n += 1
                if n > 5:
                    z.back()
                    break
            else:
                break


if __name__ == '__main__':
    unittest.main()
