# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
from urllib.parse import quote_plus


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.site = 'http://www.dhgate.com/w/{0}/{1}.html'

    def build_url(self, key_word, page_num):
        key_word = quote_plus(key_word)
        for url in [self.site.format(key_word, page) for page in range(page_num)]:
            self.add_new_url(url)

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def show_urls(self):
        for url in self.new_urls:
            print(url)
