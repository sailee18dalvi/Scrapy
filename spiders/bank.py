#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:45:51 2018

@author: dalvi
"""

import scrapy

from example.items import NewItem

class bank(scrapy.Spider):
    name = "bank"
    allowed_domains = ["axis.com"]
    start_urls = (
            'https://www.axisbank.com/bank-smart/internet-banking',
    )
    
    def parse(self, response):
          item = NewItem()
          item['headline']=response.xpath('//body/div/div/div/div/div/h1/text()').extract()
          item['text']=response.xpath('//body/div/div/div/div/div/p/text()').extract()
          item['url']=response.xpath('//body/header/div/div/div/div/div/a').extract()
          item['img']=response.xpath('//body/header/div/div/div/div/div/a/img').extract()
        
          return item
        
        
        
        
        
