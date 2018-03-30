# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        resp = requests.get(url)
        if resp.status_code != 200:
            return None
        return resp.text
