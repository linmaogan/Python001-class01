# 翻页的处理

import requests
import lxml.etree
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装

def get_detail(url):
    # 爬取页面详细信息

    # 电影详细页面
    # url = 'https://maoyan.com/films/1250952'

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    # 声明为字典使用字典的语法赋值
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)

    # xml化处理
    selector = lxml.etree.HTML(response.text)

    # 电影名称
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    print(f'电影名称: {film_name}')

    # 电影类型
    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
    print(f'电影类型: {film_type}')

    # 上映日期
    plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    print(f'上映时间：{plan_date}')

    mylist = [film_name, plan_date, plan_date]


    import pandas as pd

    movie1 = pd.DataFrame(data = mylist)

    # windows需要使用gbk字符集
    movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

# url = 'https://maoyan.com/films/1250952'
# get_detail(url)

# Python 使用def定义函数，myurl是函数的参数
def get_list(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':user_agent}
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    
    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for tags in bs_info.find_all('dl', attrs={'class': 'movie-list'}):
        for atag in tags.find_all('a'):
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

sleep(10)

for page in urls:
    get_list(page)
    sleep(5)


