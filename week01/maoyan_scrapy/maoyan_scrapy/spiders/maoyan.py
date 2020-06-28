# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from bs4 import BeautifulSoup
from maoyan_scrapy.items import MaoyanScrapyItem


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 1):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('dl', attrs={'class': 'movie-list'})
        #for i in range(len(title_list)):
        # 在Python中应该这样写
        for i in title_list:
            # 在items.py定义
            item = MaoyanScrapyItem()
            title = i.find('a').get_text()
            link = i.find('a').get('href')
            link = 'https://maoyan.com' + link
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']

        # xml化处理
        selector = lxml.etree.HTML(response.text)

        # 电影名称
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        print(f'电影名称: {film_name}')

        # 电影类型
        movie_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        print(f'电影类型: {movie_type}')

        # 上映日期
        release_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        print(f'上映时间：{release_time}')
        
        item['movie_type'] = movie_type
        item['release_time'] = release_time
        yield item

