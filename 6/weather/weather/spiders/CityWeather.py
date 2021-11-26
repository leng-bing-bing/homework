import scrapy
from weather.items import WeatherItem

class CityweatherSpider(scrapy.Spider):
    name = 'CityWeather'
    allowed_domains = ['tianqi.com']
    start_urls = ['https://www.tianqi.com/tianqi/xiamen/20211031.html?qd=tq7']

    def parse(self, response):
        lists = response.xpath('/html/body/div[7]/div[1]/div[7]/div/ul/li')
        
               
        for i in lists:
            items = WeatherItem()
            items['date'] = i.xpath('./a/span[2]/text()').extract() 
            items['day'] = i.xpath('./a/span[1]/text()').extract()
            items['weather'] = i.xpath('./a/span[3]/text()').extract() 
            items['wind_direction'] = i.xpath('./a/span[6]/text()').extract()  #风向
            items['Minimum_temperature'] = i.xpath('./a/span[5]/span[1]/text()').extract() #最低温度 
            items['Maxmum_temperature'] = i.xpath('./a/span[5]/span[2]/text()').extract() #最高温度
            
            yield items
        
        pass
