# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeatherPipeline(object):
    def open_spider(self,spider):
        # 首先用写入的方式创建或者打开一个普通文件用于存储爬取到的数据
        self.f = open(r"result.txt","wb")
        
    def process_item(self, item, spider):
        line = str(item['date'] + item['day'] + item['weather'] + item['Minimum_temperature'] + item['Maxmum_temperature'] + item['wind_direction']) + "\n"
        
        
        line = line.replace('\'','')
        line = line.replace('[','')
        line = line.replace(']','')
        line = line.encode()
        self.f.write(line)
        return item
    
    
    def close_spider(self,spider):        
        #关闭文件         
        print("文件关闭")  
        self.f.close()
      
  


