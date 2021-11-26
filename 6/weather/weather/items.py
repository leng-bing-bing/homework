# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json

class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field() #日期
    day = scrapy.Field() #星期
    weather = scrapy.Field() #天气
    wind_direction = scrapy.Field() #风向
    Minimum_temperature = scrapy.Field() #最低温度 
    Maxmum_temperature = scrapy.Field() #最高温度
    
    pass
