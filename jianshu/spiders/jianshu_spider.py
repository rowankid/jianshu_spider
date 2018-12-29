# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem
from scrapy.http.response.html import HtmlResponse


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*", "")
        origin_url = response.url
        article_id = response.url.split("?")[0].split("/")[-1]
        content = response.xpath("//div[@class='show-content-free']").get().encode()
        word_count = response.xpath("//span[@class='wordage']/text()").get().split(" ")[-1]
        read_count = response.xpath("//span[@class='views-count']/text()").get().split(" ")[-1]
        like_count = response.xpath("//span[@class='likes-count']/text()").get().split(" ")[-1]
        comment_count = response.xpath("//span[@class='comments-count']/text()").get().split(" ")[-1]
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(
            title=title,
            avatar=avatar,
            pub_time=pub_time,
            origin_url=origin_url,
            article_id=article_id,
            author=author,
            content=content,
            word_count=word_count,
            read_count=read_count,
            like_count=like_count,
            subjects=subjects,
            comment_count=comment_count,
        )
        yield item
