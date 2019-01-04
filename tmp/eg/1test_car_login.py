import time
import unittest

from BeautifulReport import BeautifulReport

from common.basics import open_app
from common.logger import Log, img_path
from tmp.eg.page_car_login import CarLoginPage


# from common import readConfig
# from common.connectDB import SqL


class TestCarLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.car = CarLoginPage(cls.driver)
        # cls.img_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'report\img')
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_1app')
    def test_1app(self):
        """打开app测试用例"""
        car = self.car
        car.click_skip()  # 跳过广告
        self.assertEqual('首页', car.text_home(), '进入app出错！')
        self.log.info('进入app成功！')

    # @BeautifulReport.add_test_img('QQ登录')
    # def test_2qq(self):
    #     """QQ登录测试用例"""
    #     car = self.car
    #     if car.text_landed() == '我的':
    #         car.click_landed()
    #         self.sign_out()
    #     if car.text_landed() == '未登录':
    #         self.log.info('用户未登录，准备 QQ 用户登录中...')
    #         car.click_landed()
    #         self.assertEqual(car.text_common(), '常用功能', '未进入 未登录 页面！')
    #         self.log.info('选择 QQ 用户登录.')
    #         car.click_qq()
    #         time.sleep(2)
    #         car.click_grant_btn()
    #         time.sleep(2)
    #         self.assertEqual(car.text_personal_center(), '个人主页', 'QQ 用户登录失败！')
    #         self.log.info('QQ 用户登录成功！')
    #         self.save_img('QQ登录')
    #
    # @BeautifulReport.add_test_img('微信登录')
    # def test_2wechat(self):
    #     """微信登录测试用例"""
    #     car = self.car
    #     if car.text_landed() == '我的':
    #         car.click_landed()
    #         self.sign_out()
    #     if car.text_landed() == '未登录':
    #         self.log.info('用户未登录，准备 微信 用户登录中...')
    #         car.click_landed()
    #         self.assertEqual(car.text_common(), '常用功能', '未进入 未登录<我的> 页面！')
    #         self.log.info('选择 微信 用户登录.')
    #         car.click_wechat()
    #         time.sleep(2)
    #         if car.text_personal_center() == '个人主页':
    #             self.log.info('微信 用户登录成功！')
    #         else:
    #             car.click_confirm_wechat()
    #             time.sleep(2)
    #             self.assertEqual(car.text_personal_center(), '个人主页', '微信 用户登录失败！')
    #             self.log.info('微信 用户登录成功1！')
    #             self.save_img('微信登录')

    @BeautifulReport.add_test_img('编辑资料')
    def test_4update_user_info(self):
        """编辑用户资料"""
        car = self.car
        if car.text_landed() == '未登录':
            self.log.warning('未检测到用户登录，不能进行编辑资料操作！')
        elif car.text_landed() == '我的':
            self.log.info('用户已登录，准备进行 编辑资料 操作.')
            car.click_landed()
            car.click_update_user()
            self.assertEqual(car.text_common(), '编辑资料', '出现错误，没有进入 编辑资料 页面！')
            start_user = car.text_get_user_name()
            car.click_user_name()
            car.input_user('111')
            car.click_enter_btn()
            end_user = car.text_get_user_name()
            self.save_img('编辑资料')
            time.sleep(2)
            if start_user == end_user:
                self.log.info('用户名称未做修改.')
            else:
                self.log.info('修改用户名称成功！修改后的名称：{}'.format(end_user))

    # def test_3phone(self):
    #     """手机登录"""
    #     car = self.car
    #     if car.text_landed() == '我的':
    #         car.click_landed()
    #         self.sign_out()
    #     if car.text_landed() == '未登录':
    #         self.log.info('用户未登录，准备 手机 用户登录中...')
    #         car.click_landed()
    #         self.assertEqual(car.text_common(), '常用功能', '未进入 未登录<我的> 页面！')
    #         self.log.info('选择 手机 用户登录.')
    #         car.click_phone()
    #         self.assertEqual(car.text_phone_login(), '手机快捷登录', '进入 手机快捷登录 页面失败！')
    #         car.input_phone('18701137212')
    #         time.sleep(1)
    #         car.click_verification_code()
    #         time.sleep(2)
    #         car.input_verification('5556')
    #         car.click_into_btn()
    #         self.assertEqual(car.text_personal_center(), '个人主页', '手机 用户登录失败！')
    #         self.log.info('手机 用户登录成功！')

    @BeautifulReport.add_test_img('退出登录')
    def sign_out(self):
        """用户退出"""
        car = self.car
        if car.text_common() == '常用功能':
            self.assertEqual(car.text_personal_center(), '个人主页', '没有用户登录，无法退出！')
            self.log.info('正在执行用户退出登录操作.')
            car.click_set_up()
            self.assertEqual(car.text_common(), '设置', '进入设置页面失败！')
            self.log.info('进入设置页成功!')
            car.click_logout()
            self.assertEqual(car.text_logout_confirm(), '退出确认', '出现错误，没有发现退出确认弹框！')
            car.click_confirm_logout()
            if not car.element_logout():
                self.log.info('退出登录成功！')
                self.save_img('退出登录')
                car.back()
        else:
            self.log.info('当前不在 我的 页面，无法进行退出登录操作！')


if __name__ == '__main__':
    unittest.main()
