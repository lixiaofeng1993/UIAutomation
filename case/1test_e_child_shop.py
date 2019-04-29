#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:19
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_d_child_audio.py
# @Software: PyCharm
import random
import re
import time
import unittest
from unittest import skip
from BeautifulReport import BeautifulReport
from common import read_config
from common.basics import open_browser
from common.logger import Log, img_path
from common.random_upload import uploaded
from page.page_child_login import ChildLoginPage
from page.page_child_shop import ChildShopPage


class TestShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.shop = ChildShopPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径
        cls.two = False
        cls.img = False
        cls.three = False
        cls.four = False
        cls.left = False
        cls.make = False
        cls.single = False
        cls.test = False

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_shop')
    def test_a_shop(self):
        """进入店铺装修"""
        shop = self.shop
        shop.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        shop.click_shop_manage()
        self.assertEqual(shop.text_check_shop_manage(), '店铺装修', '进入店铺装修栏失败！')
        self.log.info('进入 店铺装修 成功.')
        self.save_img('店铺装修')

    @BeautifulReport.add_test_img('test_b_delete_page_data')
    def test_b_delete_page_data(self):
        """新建文件夹"""
        shop = self.shop
        self.assertEqual('店铺装修', shop.text_check_shop_manage(), '打开页面错误！')
        self.log.info('检查test文件夹是否存在.')
        self.check_folder_is_exist(shop)
        if self.make:
            return
        else:
            self.log.info('未发现test文件夹，新建中...')
            shop.click_new_folder()
            time.sleep(1)
            shop.input_page_name('test')
            shop.click_sure_folder_btn()
            time.sleep(1)
            self.check_folder_is_exist(shop)
            if self.make:
                self.log.info('test文件夹新建成功.')

    @BeautifulReport.add_test_img('test_b_new_page_shop')
    def test_b_new_page_shop(self):
        """新建页面"""
        shop = self.shop
        self.assertEqual(shop.text_check_shop_manage(), '店铺装修', '当前不在 店铺装修 页面，无法进行新建页面操作！')
        self.log.info('开始新建页面.')
        self.check_test_page(shop)
        if self.test:
            return
        self.test = False
        time.sleep(1)
        shop.click_new_page_btn()
        time.sleep(1)
        self.input_test_page_data(shop)
        time.sleep(1)
        self.check_test_page(shop, make=1)
        if self.test:
            self.log.info('新建 test 页面成功.')
        else:
            self.log.error('test 页面创建失败！')

    @BeautifulReport.add_test_img('test_c_video_shop')
    def test_c_video_shop(self):
        """装修页面-单列视频"""
        shop = self.shop
        self.title_list = []
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择视频进行店铺装修.')
        time.sleep(1)
        shop.click_single_model()  # 单列
        shop.click_add_video()
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        self.log.info('进行选择数据操作.')
        self.choice_data(shop)
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_d_audio_shop')
    def test_d_audio_shop(self):
        """装修页面-单列音频"""
        shop = self.shop
        self.title_list = []
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择音频进行店铺装修.')
        self.choice_page_data(shop)
        if self.check_already_ten(shop):
            shop.click_add_audio()
        else:
            self.log.error('选择模块数据已经有十条，无法继续添加.')
            return
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        self.log.info('进行选择数据操作.')
        self.choice_data(shop)
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_e_article_shop')
    def test_e_article_shop(self):
        """装修页面-单列文章"""
        shop = self.shop
        self.title_list = []
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择文章进行店铺装修.')
        self.choice_page_data(shop)
        self.check_bottom(shop)
        if self.check_already_ten(shop):
            shop.click_add_article()
        else:
            self.log.error('选择模块数据已经有十条，无法继续添加.')
            return
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        self.log.info('进行选择数据操作.')
        self.choice_data(shop, make=True)
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_f_single_ad_shop')
    def test_f_single_ad_shop(self):
        """装修页面-单列广告"""
        shop = self.shop
        self.title_list = []
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择广告进行店铺装修.')
        time.sleep(1)
        shop.click_single_model()  # 单列
        shop.click_add_ad()
        uploaded()
        time.sleep(1)
        shop.click_choice_link4()
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        n = random.randint(0, len(shop.elements_type()) - 1)
        shop.clicks_type(n)
        time.sleep(1)
        self.single = True
        self.choice_data(shop, type='ad', make=n, ad=True)
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_g_two_ad_shop')
    def test_g_two_ad_shop(self):
        """两列广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 两列 进行店铺装修.')
        shop.click_two_model()
        self.log.info('正在添加两列广告.')
        time.sleep(1)
        if self.two_ad_shop(shop, make=True):
            self.two = True
            self.two_ad_shop(shop, make=True)
        if self.two:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_g_two_img_ad_shop')
    def test_g_two_img_ad_shop(self):
        """两列图文广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 两列 进行店铺装修.')
        shop.click_two_model()
        self.log.info('正在添加两列图文广告.')
        if self.two_ad_shop(shop, img=True):
            self.img = True
            self.two_ad_shop(shop, img=True)
        if self.img:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_h_three_ad_shop')
    def test_h_three_ad_shop(self):
        """三列广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 三列 进行店铺装修.')
        shop.click_three_model()
        self.log.info('正在添加三列广告.')
        if self.two_ad_shop(shop, make=True):
            self.two = True
            if self.two_ad_shop(shop, make=True):
                self.three = True
                self.two_ad_shop(shop, make=True)
        if self.three:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_h_three_img_ad_shop')
    def test_h_three_img_ad_shop(self):
        """三列图文广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 三列 进行店铺装修.')
        shop.click_three_model()
        self.log.info('正在添加三列图文广告.')
        if self.two_ad_shop(shop, img=True):
            self.img = True
            if self.two_ad_shop(shop, img=True):
                self.three = True
                self.two_ad_shop(shop, img=True)
        if self.three:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_i_four_ad_shop')
    def test_i_four_ad_shop(self):
        """四列广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 四列 进行店铺装修.')
        shop.click_four_model()
        self.log.info('正在添加四列广告.')
        if self.two_ad_shop(shop, make=True):
            self.two = True
            if self.two_ad_shop(shop, make=True):
                self.three = True
                if self.two_ad_shop(shop, make=True):
                    self.four = True
                    self.two_ad_shop(shop, make=True)
        if self.four:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_i_four_img_ad_shop')
    def test_i_four_img_ad_shop(self):
        """四列图文广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 四列 进行店铺装修.')
        shop.click_four_model()
        self.log.info('正在添加四列图文广告.')
        if self.two_ad_shop(shop, img=True):
            self.img = True
            if self.two_ad_shop(shop, img=True):
                self.three = True
                if self.two_ad_shop(shop, img=True):
                    self.four = True
                    self.two_ad_shop(shop, img=True)
        if self.four:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_j_carousel_ad_shop')
    def test_j_carousel_ad_shop(self):
        """轮播广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 轮播 进行店铺装修.')
        shop.click_carousel_model()
        self.log.info('正在添加轮播广告.')
        if self.two_ad_shop(shop, make=True, carousel=True):
            self.two = True
            if self.two_ad_shop(shop, make=True, carousel=True):
                self.three = True
                if self.two_ad_shop(shop, make=True, carousel=True):
                    self.four = True
                    self.two_ad_shop(shop, make=True, carousel=True)
        if self.four:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_k_left_ad_shop')
    def test_k_left_ad_shop(self):
        """左滑广告"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 左滑 进行店铺装修.')
        shop.click_left_model()
        self.log.info('正在添加左滑广告.')
        if self.two_ad_shop(shop, make=True, left=True):
            self.two = True
            if self.two_ad_shop(shop, make=True, left=True):
                self.three = True
                if self.two_ad_shop(shop, make=True, left=True):
                    self.four = True
                    self.two_ad_shop(shop, make=True, left=True)
        if self.four:
            self.save_page(shop)

    @BeautifulReport.add_test_img('test_l_blank_ad_shop')
    def test_l_blank_ad_shop(self):
        """空白"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 空白 进行店铺装修.')
        shop.click_blank_model()
        self.log.info('正在添加空白.')
        height = random.randint(10, 50)
        shop.inputs_blank_height(0, height)
        self.log.info('设置空白高度:{}px'.format(height))
        left = random.randint(10, 300)
        shop.inputs_blank_height(1, left)
        self.log.info('设置左边长度:{}px'.format(left))
        shop.click_blank_color_btn()
        color = random.randint(0, 14)
        shop.clicks_blank_color(color)
        self.log.info('选择颜色值:{}'.format(color))
        shop.click_blank_color_check()
        self.log.info('空白添加成功.')
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_m_page_ad_shop')
    def test_m_page_ad_shop(self):
        """页面"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，选择 页面 进行店铺装修.')
        shop.click_blank_model()
        self.log.info('正在添加页面.')
        shop.click_page_model()
        shop.click_two_add_img_ad()
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        self.switch_data_page(shop)
        shop.input_page_query('test')
        shop.send_keys_enter()
        time.sleep(1)
        shop.click_test_page()
        page_name = shop.elements_choice_video_id()[0].text
        self.log.info('添加 {} 页面成功.'.format(page_name))
        shop.click_sure_data_btn()
        self.save_page(shop)

    @BeautifulReport.add_test_img('test_n_copy_page_shop')
    def test_n_copy_page_shop(self):
        """复制删除编辑"""
        shop = self.shop
        if shop.element_cancel_top():  # 返回顶部
            shop.click_cancel_top()
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，进行复制、删除、编辑操作.')
        shop.move_options_copy_btn()
        time.sleep(1)
        shop.click_copy_option_sure()
        self.test = False
        self.check_test_page(shop, make=2)
        if self.test:
            self.log.info('复制 test 页面成功.')
            self.check_test_page(shop, make=3)
            self.check_test_page(shop, make=4)
        else:
            self.log.info('复制 test 页面失败！')

    @BeautifulReport.add_test_img('test_o_element_shop')
    def test_o_element_shop(self):
        """元素功能"""
        shop = self.shop
        self.assertEqual('test', shop.text_page_title(), '打开页面错误！')
        self.log.info('已选中新建页面，验证 元素 功能.')
        try:
            video_name = shop.texts_video_title(0)
        except IndexError:
            self.log.error('test 页面没有元素！')
            return
        shop.click_element_btn()
        self.assertEqual('元素', shop.text_check_element(), '没有打开元素功能页面！')
        self.log.info('打开元素功能页面成功.')
        shop.click_element_delete_btn()
        time.sleep(1)
        shop.click_copy_option_sure()
        time.sleep(1)
        end_video_name = shop.texts_video_title(0)
        self.assertNotEqual(video_name, end_video_name, '元素删除失败！')
        self.log.info('元素删除成功.')
        time.sleep(1)
        shop.click_element_btn()

    def input_test_page_data(self, shop):
        """输入test页面内容"""
        shop.input_page_name('test')
        shop.input_page_share_name('这是一个测试页面.')
        shop.click_share_img()
        uploaded()
        shop.click_is_share()
        # shop.click_cancel_btn()
        time.sleep(1)
        shop.click_new_page_sure_btn()

    def delete_test_page(self, shop):
        """删除test页面"""
        self.test = False
        shop.move_options_delete_btn()
        time.sleep(1)
        shop.click_copy_option_sure()
        self.check_test_page(shop, make=1)
        if not self.test:
            self.log.info('test页面删除成功.')
        else:
            self.log.error('test页面删除失败！')

    def edit_test_page(self, shop):
        """编辑test页面"""
        self.test = False
        shop.move_options_edit_btn()
        time.sleep(1)
        self.input_test_page_data(shop)
        self.check_test_page(shop, make=4)
        if not self.test:
            self.log.error('test页面编辑失败！')
        else:
            self.log.info('test页面编辑成功.')

    def check_test_page(self, shop, make=0):
        """检查test页面是否存在
            make:   0   首次检测页面是否存在；
            make:   1   非首次检测页面是否存在；
            make    2   复制是否成功；
            make    3   删除原来页面；
            make    4   编辑复制页面；
        """
        if make == 0:
            shop.click_not_grouped()
        time.sleep(1)
        page_list = shop.elements_check_page_name()
        for element in page_list:
            if make in [0, 1, 3]:
                if element.text == 'test':
                    if not make:
                        self.test = True
                    element.click()
                    if make == 3:
                        self.delete_test_page(shop)
                        time.sleep(1)
            elif make in [2, 4]:
                if element.text == 'test 的副本':
                    self.test = True
                    element.click()
                    self.check_bottom(shop)  # 滚动到底部
                    if make == 4:
                        self.edit_test_page(shop)

    def check_folder_is_exist(self, shop):
        """检查test文件夹是否存在"""
        folder = shop.elements_page_folder()
        for element in folder:
            if element.text == 'test':
                # element.click()
                self.make = True

    def two_ad_shop(self, shop, make=False, img=False, carousel=False, left=False):
        """两列广告、图文广告操作"""
        if img:
            shop.click_two_add_img_ad()
            shop.click_two_add_img()
            uploaded()
            if self.img and self.three and self.four:
                shop.input_two_text3('test3')
                shop.click_two_choice_link3()
            elif self.img and self.three:
                shop.input_two_text2('test2')
                shop.click_two_choice_link2()
            else:
                try:
                    shop.input_two_text1('test1')
                    shop.click_two_choice_link1()
                except AttributeError:
                    shop.input_two_text('test')
                    shop.click_two_choice_link()
        if make:
            if carousel or left:
                shop.click_add_ad()
            else:
                shop.click_two_add_ad()
            uploaded()
            if self.two and self.three and self.four:
                time.sleep(1)
                shop.click_choice_link3()
            elif self.three and self.two:
                shop.click_choice_link2()
            elif self.two:
                shop.click_choice_link1()
            else:
                shop.click_choice_link()
        time.sleep(1)
        self.assertEqual('选择数据', shop.text_check_data(), '选择数据弹窗未弹出！')
        n = random.randint(0, len(shop.elements_type()) - 1)
        shop.clicks_type(n)
        time.sleep(1)
        if img:
            self.choice_data(shop, type='ad', make=n, ad=True, two=True, img=True)
            return True
        if make:
            self.choice_data(shop, type='ad', make=n, ad=True, two=True)
            return True

    def get_element_title(self, elements):
        """遍历元素，加到一个list中"""
        if elements:
            for i in elements:
                self.title_list.append(i)

    def choice_page_data(self, shop):
        """随机选择页面元素，点击"""
        data_list = []
        elements = []
        self.log.info('开始随机选择元素.')
        if shop.elements_video_img():
            data_list.append(shop.elements_video_img())
        if shop.elements_audio_img():
            data_list.append(shop.elements_audio_img())
        # if shop.elements_article_single_img():
        #     data_list.append(shop.elements_article_single_img())
        # if shop.elements_article_three_img():
        #     data_list.append(shop.elements_article_three_img())
        # if shop.elements_single_ad_img():
        #     data_list.append(shop.elements_single_ad_img())
        # if shop.elements_two_ad_img():
        #     data_list.append(shop.elements_two_ad_img())
        # if shop.elements_three_ad_img():
        #     data_list.append(shop.elements_three_ad_img())
        # if shop.elements_four_ad_img():
        #     data_list.append(shop.elements_four_ad_img())
        for datas in data_list:
            for data in datas:
                elements.append(data)
        elements = list(set(elements))
        n = random.randint(0, len(elements) - 1)
        elements[n].click()
        self.log.info('随机选择的元素是:{}.'.format(elements[n]))

    def switch_data_page(self, shop):
        """切换选择数据页面"""
        page_num = shop.text_page_num()
        nun = int(re.findall('(\d+)', page_num)[0])
        if nun > 10:
            page = int(random.randint(1, len(shop.elements_choice_page_num()) - 1))
            self.log.info('page=============>   ' + str(page))
            shop.clicks_choice_num(page)
            time.sleep(1)

    def choice_data(self, shop, type='', make=False, ad=False, two=False, img=False):
        """随机选择数据，添加到页面
            shop:   webdriver对象；
            type：   区分广告和非广告定位；
            make：   非广告定位中区别；
            ad：     广告定位中区别；
            two:    多列广告；
            img:    图文广告;
        """
        self.switch_data_page(shop)
        if ad:
            data = shop.element_choice_vaa()
        else:
            data = shop.element_choice_data()
        n = random.randint(0, len(data) - 1)
        self.log.info('n----------------------->' + str(n))
        data[n].click()
        time.sleep(1)
        if type != 'ad':
            if make:
                choice_video_name = shop.elements_choice_article_name()[n - 1].text
            else:
                choice_video_name = shop.elements_choice_video_name()[n - 1].text
        else:
            if two:
                if make in [0, 1]:
                    choice_video_name = shop.elements_choice_video_id()[n].text
                elif make in [2, 3]:
                    choice_video_name = shop.elements_choice_article_id()[n].text
                else:
                    raise ValueError('choice_video_name ERROR!')
            else:
                if make in [0, 1]:
                    choice_video_name = shop.elements_choice_video_id()[n - 1].text
                elif make in [2, 3]:
                    choice_video_name = shop.elements_choice_article_id()[n - 1].text
                else:
                    raise ValueError('choice_video_name ERROR!')
        self.log.info('选择数据名称/ID: {}'.format(choice_video_name))
        time.sleep(1)
        shop.click_sure_data_btn()
        self.check_bottom(shop)
        if type == 'ad':
            if self.two and self.three and self.four:
                link_list = shop.elements_ad_link_id3()
            elif self.three and self.two:
                link_list = shop.elements_ad_link_id2()
            elif self.two:
                link_list = shop.elements_ad_link_id1()
            elif self.single:
                link_list = shop.elements_ad_link_id4()
            elif img:
                if self.img and self.three and self.four:
                    link_list = shop.text_two_check_data3()
                elif self.img and self.three:
                    link_list = shop.text_two_check_data2()
                elif self.img:
                    link_list = shop.text_two_check_data1()
                else:
                    link_list = shop.text_two_check_data()
            else:
                link_list = shop.elements_ad_link_id()
            if link_list:
                if img:
                    value = link_list
                else:
                    value = link_list[0].get_attribute('value')
                id = value.split('id=')[1]
                if two:
                    self.assertEqual(id, choice_video_name, '验证失败，添加错误！')
                    self.log.info('广告添加数据验证成功.')
                else:
                    if id in link_list[0].get_attribute('value') and id == choice_video_name:
                        self.log.info('广告添加数据验证成功.')
                        link_list[-1].send_keys('test')
                        shop.click_ad_share()
            else:
                self.log.info('添加数据失败！')
        else:
            self.get_element_title(shop.elements_video_title())
            self.get_element_title(shop.elements_audio_title())
            self.get_element_title(shop.elements_article_title())
            for element in self.title_list:
                if element.text == choice_video_name:
                    self.log.info('添加数据验证成功.')

    def save_page(self, shop):
        """保存页面"""
        time.sleep(1)
        shop.click_save_page()
        time.sleep(1)
        if shop.text_success_save_btn() == '保存成功':
            self.log.info('页面保存成功.')
        else:
            self.log.warning('可能保存失败，没有检测到成功提示！')

    def check_bottom(self, shop):
        time.sleep(1)
        self.log.info('向下滑动页面.')
        while True:
            if not shop.element_bottom():
                shop.js_scroll_bottom()
                time.sleep(2)
            else:
                break

    def check_top(self, shop):
        time.sleep(1)
        self.log.info('向上滑动页面.')
        while True:
            if not shop.text_page_title():
                shop.js_scroll_top()
                time.sleep(2)
            else:
                break

    def check_already_ten(self, shop):
        """验证随机选择数据是否已经十条"""
        data_num = len(shop.elements_data_ten())
        if data_num < 10:
            return True
        else:
            return False


if __name__ == '__main__':
    unittest.main()
