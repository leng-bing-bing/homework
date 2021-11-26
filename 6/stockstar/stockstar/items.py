# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockstarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field() #代码
    name = scrapy.Field() #名称
    highest = scrapy.Field() #最高
    lowest = scrapy.Field()  #最低
    Volume = scrapy.Field() #成交额
    Turnover = scrapy.Field() #成交量
    PrevClose = scrapy.Field() #昨收
    Limitamount = scrapy.Field() #涨停额
    Open = scrapy.Field() #今开

