#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
import scrapy
from ..items import LagouzpItem
import requests
from bs4 import BeautifulSoup
import json
import re


class Spider(scrapy.Spider):
    name = 'lagou'
    cookies = {
        'user_trace_token': '20170329220541-535dcc08aa394057884d3de6c06da2aa',
        'JSESSIONID': 'ABAAABAAAFCAAEG36FCE164D221C1CEB89E796234273C56',
        'PRE_UTM': '',
        'BAIDUID': '45A2EA96C0D623AADAE825E1A3DE41F8:FG=1',
        'PRE_SITE': '',
        'PRE_HOST': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'index_location_city': '%E5%8C%97%E4%BA%AC',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1491116405,1491116452,1493122880,1493122898',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1493123186',
        '_ga': 'GA1.2.1412866745.1489497427',
        'LGUID': '20170819003739-8cd023cd-8433-11e7-9d86-525400f775ce',
        'LGSID': '20170819002347-9caa6942-8431-11e7-8a38-5254005c3644',
        'TG-TRACK-CODE': 'index_search',
        'SEARCH_ID': 'b3638e10d2a5464598572ce7dfb66e1b'
    }
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }

    def start_requests(self):
        kd = ['运维开发']
        city = ['北京', '上海', '广州', '深圳', '杭州']
        urls_kd = ['https://www.lagou.com/jobs/list_{}?px=default&city='.format(one) for one in kd]
        for urls in urls_kd:
            urls_city = [urls + one for one in city]
            for url in urls_city:
                response = requests.get(url, headers=self.headers, cookies=self.cookies)
                location = url.split('&')[-1].split('=')[1]
                key = url.split('/')[-1].split('?')[0].split('_')[1]
                soup = BeautifulSoup(response.text, 'lxml')
                pages = soup.find('span', {'class': 'span totalNum'}).get_text()
                for i in range(1, int(pages) + 1):
                    url = "https://m.lagou.com/search.json?city={}&positionName={}&pageNo={}".format(location, key, i)
                    yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        content = data['content']
        positionResult = content['data']['page']['result']
        item = LagouzpItem()

        for one in positionResult:
                item['positionId'] = one['positionId']
                item['positionName']= one['positionName']
                item['city'] = one['city']
                item['createTime'] = one['createTime'].split(' ')[0]
                item['companyId'] = one['companyId']
                item['companyName'] = one['companyName']
                item['companyFullName'] = one['companyFullName']
                item['salary'] = one['salary']
                item['minsalary'] = re.split(r'(k|-|K)', one['salary'])[0]
                item['munsalary'] = (int(re.split(r'(k|-|K)', one['salary'])[0]) + int(re.split(r'(k|-|K)', one['salary'])[4])) / 2
                item['maxsalary'] = re.split(r'(k|-|K)', one['salary'])[4]
                yield item
