# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouzpItem(scrapy.Item):
    positionId = scrapy.Field()
    positionName= scrapy.Field()
    city= scrapy.Field()
    createTime= scrapy.Field()
    companyId= scrapy.Field()
    companyName= scrapy.Field()
    companyFullName= scrapy.Field()
    salary= scrapy.Field()
    minsalary = scrapy.Field()
    munsalary = scrapy.Field()
    maxsalary = scrapy.Field()
