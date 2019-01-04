from common.basics import Crazy


class XxbmmSkuPage(Crazy):
    """元素定位"""
    # title
    xxbmm_text_loc = ('id', 'com.tencent.mm:id/kt')

    def text_xxbmm_text(self):
        return self.get_text(self.xxbmm_text_loc)

    back_home_loc = ('accessibility id', '首页')

    def click_back_home(self):
        self.click(self.back_home_loc)

    # sku模块
    sku_model_loc = ('accessibility id', 'SKU')

    def click_sku_model(self):
        self.click(self.sku_model_loc)

    # 单级型号多个拼团 商品
    model_collage_loc = ('accessibility id', '单级型号多个拼团')

    def click_model_collage(self):
        self.click(self.model_collage_loc)

    # 查看全部用户说 按钮    [27,657][1050,783]  [27,951][1050,1078] [0,621][1080,874] [27,748][1050,874]
    # all_user_said_loc = ('accessibility id', '查看全部用户说')
    all_user_said_loc = [(27,748), (1050,874)]

    def click_all_user_said(self):
        self.click_coordinate(self.all_user_said_loc)

    open_group_loc = ('accessibility id', '一键开团')

    def click_open_group(self):
        self.click(self.open_group_loc)

    check_norms_loc = ('accessibility id', '单级型号多个2')

    def click_check_norms(self):
        self.click(self.check_norms_loc)

    check_num_loc = ('accessibility id', '+')

    def click_check_num(self):
        self.click(self.check_num_loc)

    sure_btn_loc = ('accessibility id', '确定')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # [0,217][1080,343] [68,269][250,319]
    back_user_said_loc = [(68,269), (250,319)]

    def click_back_user_said(self):
        self.click_coordinate(self.all_user_said_loc)