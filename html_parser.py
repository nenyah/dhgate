'''
@Description: 解析器
@Author: Steven
@Date: 2018-09-18 10:15:44
@LastEditors  : Steven
@LastEditTime : 2020-01-09 10:35:21
'''
# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import re

from lxml import etree
from typing import List


class HtmlParser:
    def _get_new_data(self, page_url: str, tree: etree.Element) -> List:
        items = tree.xpath('//div[starts-with(@id,"product")]')
        datas = []
        for index, item in enumerate(items, 1):
            title = item.xpath('./h3/a/text()')[0]
            product_url = HtmlParser.format_str(item.xpath('./h3/a/@href')[0])
            price = item.xpath('.//*[@class="price"]/span/text()')[0]
            min_price, max_price = re.findall(r'(\d+\.*\d+)', price)  # 最低价，最高价
            min_order = item.xpath('./*[@class="min"]//text()')
            min_order = min_order[0] if len(min_order) > 0 else None
            min_order = re.findall(r'(\d+)',
                                   min_order)[0] if min_order else None  # 起订量
            order = item.xpath('.//*[@class="ordernum"]//text()')
            order = int(order[0].split()[0]) if len(order) > 0 else 0  # 订单量
            feedback = item.xpath('.//*[@class="reviewnum"]//text()')
            feedback = float(feedback[0]) if feedback else 0
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

    def parse(self, page_url: str, html_cont: str) -> List:
        if page_url is None or html_cont is None:
            return
        tree = etree.HTML(html_cont)
        new_data = self._get_new_data(page_url, tree)
        return new_data

    def format_str(text: str) -> str:
        return text.split("html")[0] + "html"
