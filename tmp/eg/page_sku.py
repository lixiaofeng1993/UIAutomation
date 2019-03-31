from common.basics import Crazy


class XbuPage(Crazy):
    """元素定位"""
    # title
    all_loc = ('id', 'com.xiaobu121.xiaobu.xiaobu_android:id/tv_title')

    def click_all(self):
        self.clicks(self.all_loc, 1)

    def click_record(self):
        self.clicks(self.all_loc, 2)

    curriculum_btn_loc = ('id', 'com.xiaobu121.xiaobu.xiaobu_android:id/tv_age_tag')

    def element_curriculum(self):
        return self.find_element(self.curriculum_btn_loc)

    def click_curriculum(self):
        self.click(self.curriculum_btn_loc)

    desc_loc = ('id', 'com.xiaobu121.xiaobu.xiaobu_android:id/expandable_text')

    def text_desc(self):
        return self.get_text(self.desc_loc)