# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class SeleniumMiddleware(object):
    USER_AGENTS = [
        "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
    ]

    def __init__(self):
        # 进入浏览器设置
        options = webdriver.ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        # 更换头部 options.add_argument("user-agent="+random.choice(self.USER_AGENTS))
        options.add_argument("user-agent=" + random.choice(self.USER_AGENTS))
        # 设置代理ip options.add_argument('--proxy-server=http://ip:port')
        ip = []
        file = open("D:\Spiders\jianshu\jianshu\proxyIP.txt")
        for line in file.readlines():
            ip.append(line.strip('\n'))
        randomIP = random.choice(ip)
        print(randomIP)
        # options.add_argument('--proxy-server=https://'+random.choice(ip))
        self.driver = webdriver.Chrome(chrome_options=options,
                                       executable_path=r"E:\GitRepository\sinosoft\webmagic\spider-webmagic-demo\target\classes\chromedriver.exe")

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            while True:
                showMore = self.driver.find_element_by_class_name()
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass

        source = self.driver.page_source

        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response

class UserAgentDownloadMiddleware(object):
    USER_AGENTS = {

    }

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

