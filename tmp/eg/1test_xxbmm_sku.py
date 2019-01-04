import time
import unittest

from common.basics import open_app
from common.logger import Log
from tmp.eg.page_sku import XxbmmSkuPage


# from common import readConfig
# from common.connectDB import SqL


class TestXxbmm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.xxbmm_sku = XxbmmSkuPage(cls.driver)
        # cls.db = SqL()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def text_normal_goods(self):
        xxbmm_sku = self.xxbmm_sku
        xxbmm_sku.click_back_home()
        xxbmm_sku.click_sku_model()
        time.sleep(6)