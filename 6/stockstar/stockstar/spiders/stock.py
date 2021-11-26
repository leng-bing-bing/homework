import scrapy
import re
from stockstar.items import StockstarItem

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://38.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124031919791489639804_1635831226996&pn=1&pz=4701&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f4,f5,f6,f12,f14,f15,f16,f17,f18&_=1635831226997']
    #f4涨跌额，f5成交量，f6成交额，f12代码，f14名字，f15最高，f16最低，f17今开，f18昨收

    def parse(self, response):
        pat = "\"diff\":\[(.*?)\]"
        data = re.compile(pat,re.S).findall(response.text)
         #将数据里面无用信息去除
        datas =             data[0].replace('"',"").replace('f4','').replace('f5','').replace('f6','').replace('f12','').replace('f14','').replace('f15','').replace('f16','').replace('f17','').replace('f18','').replace(':','').replace('{','').replace('}','').replace('[','').replace(']','').split(",")
         
        #for i in range(0,9):
     #        print(datas[i])
         
           #提取数据
        for i in range(0,len(datas),9):
            items = StockstarItem()
  
            items['Limitamount'] = datas[i]
            
            items['Turnover'] = datas[i+1]
            
            items['Volume'] = datas[i+2]
            
            items['code'] = datas[i+3]
            
            items['name'] = datas[i+4]
            
            items['highest'] = datas[i+5]
           
            items['lowest'] = datas[i+6]
           
            items['Open'] = datas[i+7]
           
            items['PrevClose'] = datas[i+8]
   #         print(items)
#             print(datas[i])
        
        
        
            yield items
        

        pass
