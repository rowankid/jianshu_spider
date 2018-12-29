from scrapy import cmdline


# scrapy genspider -t crawl wxminiapp_spider "wxapp-union.com"

spider_name = "free-proxy-list.net"
domain = "free-proxy-list.net"

command = [
    "scrapy",
    "genspider",
    "-t",
    "crawl",
    spider_name,
    domain,
]
cmdline.execute(command)
