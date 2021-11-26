# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class StockstarPipeline(object):
    
    def open_spider(self,spider):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = '沪深股票消息'
        self.ws.append(['代码','名称','涨跌额','成交量','成交额','最高','最低','今开','昨收' ])
    

    def process_item(self, item, spider):
        line = [item['code'], item['name'], item['Limitamount'], item['Turnover'], item['Volume'], item['highest'], item['lowest'], item['Open'], item['PrevClose']]
        print(line)
        self.ws.append(line)
        return item
    
    def close_spider(self,spider):        
        #关闭文件  
        self.wb.save('result.xlsx')
        print("完成")  
        
    
        