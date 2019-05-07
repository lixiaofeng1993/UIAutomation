#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 18:57
# @Author  : lixiaofeng
# @Site    : 
# @File    : 1test.py
# @Software: PyCharm
# import random
#
# text = random.uniform(1, 10)
#
# print(round(text, 2))

#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import threading
import schedule
import time

login_url = 'http://gongjiaoapi.xuechebu.com/Student/setbadingstuinfo?password=123456&jgid=124001&id_type=1&xybh=5101231040';
login_header = {
 'User-Agent': 'ios_gongjiao;v4.0.0'
}


request = requests.session()

response = requests.post(url=login_url,headers = login_header)

content = response.content.decode()
print(content)
print("================================")
cookies=response.cookies
#
# #预约



def yuyue():
 date = ['2019年5月11日', '2019年5月12日']
 dateTime = ['58', '58']
 for i in range(len(date)):
  #上午  812  下午  15
  jx_url = 'http://gongjiaoapi.xuechebu.com/KM2/ClYyAddByMutil?aaaaa=O-add-r6rABjQPweieXIxb593Di2oK6xFyoJXqpe4ZeSnCFZsfxtYb87NstyWcXuAsIdqXFMQVwcC3zQ9HbfXoG4Tbhe7jkBJIm2uvKxwUmUi7yAicKbZSYtQk6wyk8gnkFb8GcH-add-Dqb/fGZB4fzdIxqkCfxyAD8KhPWZfZSh9EiHjI=&' \
           'os=ios&version=2.6&xxzh=63512740&' \
           'params=4%E9%98%9F11%E7%BB%84.' \
           +date[i]+ '.' \
            +dateTime[i]+'..&' \
           'isJcsdYyMode=5&TrainType=2'
  yx_response = requests.get(url=jx_url, headers=login_header, cookies=cookies)
  yx_content = yx_response.content.decode()
  print(yx_content)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(1).seconds.do(run_threaded,yuyue)
while True:
    schedule.run_pending()
    time.sleep(1)