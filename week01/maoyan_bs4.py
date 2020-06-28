# 翻页的处理

import requests
import lxml.etree
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装

film_name = []
plan_date = []
film_type = []

def get_detail(url):
    global film_name, plan_date, film_type

    # 爬取页面详细信息

    # 电影详细页面
    # url = 'https://maoyan.com/films/1250952'

    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    # 声明为字典使用字典的语法赋值
    header = {
        "Host": "maoyan.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://maoyan.com/films?showType=3&offset=0",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": '__mta=50241049.1593284256092.1593330110604.1593330768171.4; uuid_n_v=v1; uuid=0EF7F890B8A811EAB11C23537EB4C64BFDEA2C384DAD474EABC0F4EAB433B826; _csrf=c3fdd9d7b87351897c22eb3c71021b17c3a3875a1e18601661cdd9b7aedb88d6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593284255; _lxsdk_cuid=172f7245de9c8-0dbad9557ac0b-31617402-fa000-172f7245de988; _lxsdk=0EF7F890B8A811EAB11C23537EB4C64BFDEA2C384DAD474EABC0F4EAB433B826; mojo-uuid=d53cc2faec9d5adfe92e896fd09151de; mojo-session-id={"id":"7ae61e7e450db2fbbf2dc4a9a54dcb9a","time":1593361668494}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593362363; __mta=50241049.1593284256092.1593330768171.1593362363397.5; mojo-trace-id=10; _lxsdk_s=172fbc199c3-1a7-56c-13a%7C%7C14'
    }

    response = requests.get(url, headers=header)

    # xml化处理
    selector = lxml.etree.HTML(response.text)

    # 电影名称
    movie_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    print(f'电影名称: {movie_name[0]}')
    film_name.append(movie_name[0])

    # 电影类型
    movie_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/*/text()')
    print(f'电影类型: {movie_type}')
    film_type.append(' / '.join(movie_type))

    # 上映日期
    release_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    release_date = re.sub(r'[^\d-]', "", release_date[0])
    print(f'上映时间：{release_date}')
    plan_date.append(release_date)

# url = 'https://maoyan.com/films/1250952'
# get_detail(url)

# Python 使用def定义函数，myurl是函数的参数
def get_list(myurl):
    header = {
        "Host": "maoyan.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://maoyan.com/films?showType=3&offset=0",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": '__mta=50241049.1593284256092.1593330110604.1593330768171.4; uuid_n_v=v1; uuid=0EF7F890B8A811EAB11C23537EB4C64BFDEA2C384DAD474EABC0F4EAB433B826; _csrf=c3fdd9d7b87351897c22eb3c71021b17c3a3875a1e18601661cdd9b7aedb88d6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593284255; _lxsdk_cuid=172f7245de9c8-0dbad9557ac0b-31617402-fa000-172f7245de988; _lxsdk=0EF7F890B8A811EAB11C23537EB4C64BFDEA2C384DAD474EABC0F4EAB433B826; mojo-uuid=d53cc2faec9d5adfe92e896fd09151de; mojo-session-id={"id":"7ae61e7e450db2fbbf2dc4a9a54dcb9a","time":1593361668494}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593362363; __mta=50241049.1593284256092.1593330768171.1593362363397.5; mojo-trace-id=10; _lxsdk_s=172fbc199c3-1a7-56c-13a%7C%7C14'
    }
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info)
    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    i = 1
    for tags in bs_info.find_all('div', attrs={'class': 'movie-item-title'})[0:10]:
        # print(tags)
        for atag in tags.find_all('a'):
            # print(i, '=======')
            # if i == 0:   # 当变量 i 等于 0 时退出循环
            #     break
            # i = i -1
            # 获取所有链接
            # print('https://maoyan.com' + atag.get('href'))
            # 获取电影名字
            # print(atag.get_text())
            url = 'https://maoyan.com' + atag.get('href')
            get_detail(url)


# 生成包含所有页面的元组
urls = tuple(f'https://maoyan.com/films?showType=3&offset={ page * 30 }' for page in range(1))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(3)

for page in urls:
    get_list(page)
    sleep(5)

mylist = {}
mylist = {'电影名称': film_name, '上映日期': plan_date, '电影类型': film_type}
movie = pd.DataFrame(data=mylist)

# windows需要使用gbk字符集
movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)