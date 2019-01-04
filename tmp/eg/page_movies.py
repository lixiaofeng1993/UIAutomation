from common.basics import Crazy


class MoviesPage(Crazy):
    """movies模块元素封装"""

    movie_btn_loc = ('xpath', '/html/body/header/span[2]/a')

    def click_movie_btn(self):
        self.click(self.movie_btn_loc)

    movie_title_loc = ('xpath', '/html/body/div/div[1]/a/span')

    def text_movie_title(self):
        return self.get_text(self.movie_title_loc)

    movie_top_loc = ('xpath', '/html/body/div/div[1]/span/a')

    def click_movie_top(self):
        self.click(self.movie_top_loc)

    note_movie_loc = ('xpath', '/html/body/div/div/div[1]/span')

    def text_note_movie(self):
        return self.get_text(self.note_movie_loc)

    note_movies_list_loc = ('xpath', '/html/body/div/div/div[2]/ol/li')

    def note_movies_elements(self):
        return self.find_elements(self.note_movies_list_loc)

    note_movie_name_loc = ('xpath', '/html/body/div/div/div[2]/ol/li[1]/a')

    def click_note_movie_name(self):
        self.click(self.note_movie_name_loc)

    movie_rank_loc = ('xpath', '//*[@id="content"]/span[1]')

    def text_movie_rank(self):
        return self.get_text(self.movie_rank_loc)

    comments_btn_loc = ('xpath', '/html/body/div/div/div[3]/p[2]/a')

    def click_comments_btn(self):
        self.click(self.comments_btn_loc)

    comments_title = ('xpath', '/html/body/div/div[1]/div[1]/p')

    def text_comments_title(self):
        return self.get_text(self.comments_title)

    read_comments_btn = ('xpath', '/html/body/div/div[1]/div[2]/p/a')

    def click_read_comments_btn(self):
        self.click(self.read_comments_btn)

    read_states_loc = ('xpath', '/html/body/div/div/form/div/input[1]')

    def input_states(self, states):
        self.send_keys(self.read_states_loc, states)

    read_content_loc = ('xpath', '/html/body/div/div/form/div/textarea')

    def input_content(self, content):
        self.send_keys(self.read_content_loc, content)

    read_submit_loc = ('xpath', '/html/body/div/div/form/div/input[2]')

    def click_read_submit(self):
        self.click(self.read_submit_loc)

    comments_content_loc = ('xpath', '/html/body/div/div[2]/div/div[2]/p')

    def comments_content_elements(self):
        return self.find_elements(self.comments_content_loc)

    comments_states_loc = ('xpath', '/html/body/div/div[2]/div/div[2]/span[2]')

    def comments_states_elements(self):
        return self.find_elements(self.comments_states_loc)
