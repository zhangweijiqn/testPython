# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector

from xiaoqu.items import XiaoquItem


class xiaoquSpider(Spider):
    name = "xiaoqu"
    allowed_domains = ["suqian.58.com"]
    start_urls = [
        "http://suqian.58.com/xiaoqu/?PGTID=0d011138-0092-edf9-b20d-0c8be377e105&ClickID=1"
        # or http://suqian.58.com/xiaoqu/xqlist_A_1/
    ]

    # 下面两个是根据业务定义的一个是对link处理，一个是对页面里提取内容的标签进行匹配
    link_extractor = {  # 页面link处理
                        'page_down': SgmlLinkExtractor(allow='/xiaoqu/(pn_\d/.+|xqlist_.+)'),
                        # 满足条件的继续递归的爬下去
                        'content': SgmlLinkExtractor(allow='/xiaoqu/[a-zA-Z0-9]+/'),  # 内容页面
                        }

    _x_query = {  # 元素提取
                  'name': '//h1[@class="xiaoquh1"]/text()',
                  'address': '//dl[@class="bhrInfo"]/dd/span[@class="ddinfo"]/text()',
                  }

    def parse(self, response):  # 自动调用+递归调用
        print response.url
        for link in self.link_extractor['content'].extract_links(response):
            yield Request(url=link.url, callback=self.parse_content)
        for link in self.link_extractor['page_down'].extract_links(response):
            yield Request(url=link.url, callback=self.parse)

    def parse_content(self, response):
        sel = Selector(response)
        print response.url
        pageItem = XiaoquItem()
        name = str(sel.xpath(self._x_query['name']).extract()[0]).strip()
        pageItem["name"] = name
        address = str(sel.xpath(self._x_query['address']).extract()[0]).strip()
        pageItem["address"] = address
        return pageItem
