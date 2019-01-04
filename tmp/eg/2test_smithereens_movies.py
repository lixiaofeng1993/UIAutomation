import time
import unittest

from page.page_login import LoginPage

from common import read_config
from common.basics import open_browser
from common.connect_db import SqL
from common.logger import Log
from tmp.eg.page_movies import MoviesPage


class TestSmithereensMovies(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.movie = MoviesPage(cls.driver)
        cls.url = read_config.url
        cls.db = SqL()

    @classmethod
    def tearDownClass(cls):
        cls.movie.close()
        cls.db.execute_sql("delete from movie_comment where netName = 'lixiaofeng'")
        cls.log.info('测试环境恢复成功！')

    def test_movies(self):
        """电影热门排行，发表短评未登录"""
        movie = self.movie
        movie.open(url=self.url, t='長情.主页')
        movie.click_movie_btn()
        self.assertEqual(movie.text_movie_title(), 'Smithereens. 电影', '进去电影模块失败!')
        self.log.info('进入电影模块成功!')
        movie.click_movie_top()
        movie.save_report_html()
        self.assertEqual(movie.text_note_movie(), '热门电影排行榜', '进入电影排行页面失败!')
        self.log.info('进入电影排行页面成功!')
        if len(movie.note_movies_elements()) < 1:
            self.log.info('电影排行界面没有显示电影.')
            return
        else:
            movie.click_note_movie_name()
            self.assertIn('No.', movie.text_movie_rank(), '进入电影信息界面失败!')
            self.log.info('进入电影信息界面成功!')
        movie.js_scroll_top()
        movie.click_comments_btn()
        self.assertIn('短评', movie.text_comments_title(), '进入短评界面失败!')
        self.log.info('进入短评界面成功!')
        movie.click_read_comments_btn()
        self.assertEqual(self.login.text_login_title(), '登录 Smithereens.')
        self.log.info('用户未登录!')

    def test_movies_user_login(self):
        """电影热门排行，发表短评"""
        movie = self.movie
        movie.open(url=self.url + 'login/', t='login')
        self.login.input_phone('18701137212')
        self.login.input_pass('123456')
        self.login.click_login_btn()
        self.assertIn('你好', self.login.check_login(), '登录成功!')
        movie.click_movie_btn()
        self.assertEqual(movie.text_movie_title(), 'Smithereens. 电影', '进去电影模块失败!')
        self.log.info('进入电影模块成功!')
        movie.click_movie_top()
        movie.save_report_html()
        self.assertEqual(movie.text_note_movie(), '热门电影排行榜', '进入电影排行页面失败!')
        self.log.info('进入电影排行页面成功!')
        if len(movie.note_movies_elements()) < 1:
            self.log.info('电影排行界面没有显示电影.')
            return
        else:
            movie.click_note_movie_name()
            self.assertIn('No.', movie.text_movie_rank(), '进入电影信息界面失败!')
            self.log.info('进入电影信息界面成功!')
            movie.js_scroll_top()
            movie.click_comments_btn()
            self.assertIn('短评', movie.text_comments_title(), '进入短评界面失败!')
            self.log.info('进入短评界面成功!')
            time.sleep(1)
            movie.click_read_comments_btn()
            self.assertIn('撰写', self.login.text_login_title(), '进入撰写短评界面失败!')
            self.log.info('正在编写短评!')
            movie.input_states('四星级')
            movie.input_content('你是谁是是是?')
            time.sleep(1)
            movie.click_read_submit()
            self.assertIn('短评', movie.text_comments_title(), '返回短评界面失败!')
            self.log.info('返回短评界面成功!')
            movie.js_scroll_top()
            time.sleep(1)
            self.assertEqual(movie.comments_content_elements()[-1].text, '你是谁是是是?', '添加短评失败!')
            self.assertEqual(movie.comments_states_elements()[-1].text, '四星级', '添加短评失败!')
            self.log.info('添加短评成功!')


if __name__ == '__main__':
    unittest.main()
