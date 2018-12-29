# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UseragentstringSpiderSpider(CrawlSpider):
    name = 'useragentstring_spider'
    allowed_domains = ['useragentstring.com']
    start_urls = ['http://www.useragentstring.com/pages/useragentstring.php?typ=Browser']

    def parse_item(self, response):
        response.xpath("//ul/li/a/text()").getall()
