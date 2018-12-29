# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FreeProxyListNetSpider(CrawlSpider):
    name = 'free-proxy-list.net'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net/']

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
