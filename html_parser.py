# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import re

from lxml import etree


class HtmlParser:
    def _get_new_data(self, page_url, tree):
        items = tree.xpath('//div[starts-with(@id,"product")]')
        datas = []
        for item in items:
            title = item.xpath('./h3/a/text()')[0]
            product_url = HtmlParser.format_str(item.xpath('./h3/a/@href')[0])
            price = item.xpath('.//*[@class="price"]/span/text()')[0]
            min_price, max_price = re.findall(r'(\d+\.*\d+)', price)  # 最低价，最高价
            min_order = item.xpath('./*[@class="min"]//text()')
            min_order = min_order[0] if len(min_order) > 0 else None
            min_order = re.findall(r'Min. Order: (\d+)',
                                   min_order)[0] if min_order else 0  # 起订量
            order = item.xpath('.//*[@class="ordernum"]//text()')
            order = order[0] if len(order) > 0 else None
            order = re.findall(r'(\d+) Orders',
                               order)[0] if order else 0  # 订单量
            feedback = item.xpath('.//*[@class="reviewnum"]//text()')
            feedback = feedback[0] if feedback else 0
            seller = item.xpath('.//*[@class="seller-name"]/text()')[0]
            store_url = item.xpath('.//*[@class="seller-name"]/@href')[0]

            data = {
                'page_url': page_url,
                'title': title,
                'product_url': 'http:' + product_url,
                'min_price': min_price,
                'max_price': max_price,
                'min_order': min_order,
                'order': order,
                'feedback': feedback,
                'seller': seller,
                'store_url': store_url
            }
            datas.append(data)
        return datas

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        tree = etree.HTML(html_cont)
        new_data = self._get_new_data(page_url, tree)
        return new_data

    def format_str(text):
        return text.split("html")[0] + "html"
