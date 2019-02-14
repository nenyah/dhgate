# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import re

from bs4 import BeautifulSoup
from numpy import mean


class HtmlParser(object):
    def _get_new_data(self, page_url, soup):
        items = soup.find_all("div", "listitem")
        datas = []
        for item in items:
            title = item.find("h3").find("a").text  # 标题
            price = item.find("li", "price").text  # 价格
            m = re.findall(r'(\d+\.*\d+)', price)
            price = mean(list(map(float, m)))  # 计算均价
            attribute = item.find("ul", "attribute").text
            min_order = re.findall(r'Min. Order: (\d+)', attribute)[0]  # 起订量
            order = re.findall(r'Sold: (\d+)', attribute)
            order = order[0] if len(order) > 0 else 0  # 订单量
            feedback = item.find("span", "reviewnum")
            feedback = re.findall(r"\d+", feedback.text)[0] if feedback else 0
            seller = list(item.find("span", "seller").stripped_strings)[-1]
            store_url = item.find("span", "seller").find("a")['href']
            store_feedback = item.find("li", "feedback")
            store_feedback = re.findall(
                r"\d+\.*\d+", store_feedback.text)[0] if store_feedback else 0
            data = {
                'page_url': page_url,
                'title': title,
                'price': round(price, 2),
                'min_order': min_order,
                'order': order,
                'feedback': feedback,
                'seller': seller,
                'store_url': store_url,
                'store_feedback': store_feedback
            }
            datas.append(data)
        return datas

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_data = self._get_new_data(page_url, soup)
        return new_data
