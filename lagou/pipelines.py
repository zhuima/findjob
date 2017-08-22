# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class LagouPipeline(object):
    # def process_item(self, item, spider):
        # return item

#import MySQLdb
from db import Cursor
from utils import get_config


class LagouzpPipeline(object):
    def __init__(self):
        self.config = get_config("common")
        self.cursor = Cursor(self.config)

    def process_item(self, item, spider):
        data = {
            "positionId": item['positionId'],
            "positionName": item['positionName'],
            "city": item['city'],
            "createTime": item['createTime'],
            "companyId": item['companyId'],
            "companyName": item['companyName'],
            "companyFullName": item['companyFullName'],
            "salary": item['salary'],
            "minsalary": item['minsalary'],
            "munsalary": item['munsalary'],
            "maxsalary": item['maxsalary']
        }
        self.cursor.execute_insert_sql('jobinfo', data)
        return item
