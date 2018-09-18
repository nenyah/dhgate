# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import sys
import url_manager
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, key_word, page_num):
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
            except:
                print("craw failed")
        self.outputer.output_html()
        self.outputer.output_csv()


if __name__ == '__main__':
    key_word, page_num = sys.argv[1:3]
    obj_spider = SpiderMain()
    obj_spider.craw(key_word, page_num)
