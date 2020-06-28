# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
class MaoyanScrapyPipeline:
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        release_time = item['release_time']
        output = f'|{title}|\t|{movie_type}|\t|{release_time}|\n\n'
        with open('./maoyan.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item