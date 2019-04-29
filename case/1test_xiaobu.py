import time
import unittest

from common.basics import open_app
from common.logger import Log
from tmp.eg.page_sku import XbuPage
from common.operation_excel import Write_excel


# from common import readConfig
# from common.connectDB import SqL


class TestXbu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.x = XbuPage(cls.driver)
        cls.write = Write_excel('G:\\UIAutomation\data\demo_api.xlsx')
        # cls.db = SqL()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_normal_goods(self):
        x = self.x
        time.sleep(10)
        x.click_all()
        while True:
            if x.element_curriculum():
                x.click_curriculum()
                break
            else:
                x.swipeUp()
                time.sleep(1)
        x.click_record()
        num = 0
        while True:
            if x.text_desc():
                print(num, '            2222222222222222222222222222222222222222222')
                try:
                    if num == 3:
                        break
                    print(x.text_desc())
                    data = x.text_desc()
                    self.write.write(num + 1, 1, data)
                    num += 1
                    print(num, '            333333333333333333333333333333333333333333')
                    x.swipeUp()
                    time.sleep(1)
                    while True:
                        try:
                            data1 = x.text_desc()
                            if data == data1:
                                x.swipeUp()
                                time.sleep(1)
                            else:
                                break
                        except Exception:
                            x.swipeUp()
                            time.sleep(1)

                except Exception:
                    x.swipeUp()
                    time.sleep(1)

            else:
                x.swipeUp()
                time.sleep(1)


if __name__ == '__main__':
    unittest.main()
