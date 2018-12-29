import requests
from lxml import etree

class ProxySpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_url_list(self):  # 1. 构造url列表
        url_list = []
        # url_list.append("https://free-proxy-list.net/")
        url_list.append("https://www.xicidaili.com/nn/")
        return url_list

    def parse_url(self, url):  # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str):  # 保存html字符串
        file_path = "proxyIP.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)
            f.close()

    def deal_free_proxy_list(self, html):
        trs = html.xpath("//tbody/tr")
        file_path = "proxyIP2.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            for tr in trs:
                ip = tr.xpath("./td[1]/text()")[0]
                port = tr.xpath("./td[2]/text()")[0]
                code = tr.xpath("./td[3]/text()")[0]
                country = tr.xpath("./td[4]/text()")[0]
                https = tr.xpath("./td[7]/text()")[0]
                # print(https)
                if https == "yes":
                    f.write(ip + ":" + port + "\n")
        f.close()

    def deal_xici(self, html):
        trs = html.xpath("//table[@id='ip_list']/tr")
        print(len(trs))
        file_path = "proxyIP.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            for inx, tr in enumerate(trs):
                print(inx)
                if inx >0 and inx <=30 :
                    ip = tr.xpath("./td[2]/text()")[0]
                    port = tr.xpath("./td[3]/text()")[0]
                    https = tr.xpath("./td[6]/text()")[0]
                    print(https)
                    if https == "HTTPS":
                        f.write(ip + ":" + port + "\n")
        f.close()

    def run(self):  # 实现主要逻辑
        # 1. 构造url列表
        url_list = self.get_url_list()
        # 2. 遍历，发送请求，获取响应
        html_str = self.parse_url(url_list[0])
        self.save_html(html_str)
        html = etree.HTML(html_str)
        # self.deal_free_proxy_list(html)
        self.deal_xici(html)


if __name__ == '__main__':
    spider = ProxySpider()
    spider.run()
