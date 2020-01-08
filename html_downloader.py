# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import requests

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None

        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            return None
        return resp.text


if __name__ == "__main__":
    downloader = HtmlDownloader()
    print(downloader.download('https://www.dhgate.com/w/women+dress/0.html'))
