'''
@Description: 主程序
@Author: Steven
@Date: 2018-09-18 10:15:44
@LastEditors  : Steven
@LastEditTime : 2020-01-09 13:17:24
'''
# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator

import url_manager
import html_downloader
import html_outputer
import html_parser
from typing import List


class SpiderMain:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, key_word: str, page_num: str) -> List:
        count = 1
        self.urls.build_url(key_word, int(page_num))
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(f"craw {count} : {new_url}")
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(new_url, html_cont)
                self.outputer.collect_data(new_data)
                count += 1
            except Exception as e:
                print("craw failed", e)
        # print(self.outputer.datas)
        # self.outputer.to_csv()
        return self.outputer.datas


if __name__ == "__main__":
    spider = SpiderMain()
    spider.craw("women dress", "2")
