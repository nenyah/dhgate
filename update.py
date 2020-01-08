# coding=utf-8
import json
from os import path, remove, rename
from urllib.request import urlretrieve

import requests


def get_json(update_file):
    """获取本地版本信息
    :update_file 版本信息文件 url or json
    :return json
    """
    if 'http' in update_file:
        content = requests.get(update_file).json()
    else:
        with open(update_file, 'r', encoding='utf-8') as f:
            content = json.loads(f.read())
    return content


def check_exists(file):
    """检查文件是否存在
    :file 文件
    :return boolen
    """
    return path.exists(file)


def is_updated(old, new):
    """对比版本信息
    :old 老版本号 float
    :new 新版本号 new
    :return boolen
    """
    updated = False
    if old < new:
        updated = True
    return updated


def download(url, name):
    """下载文件
    :url 网址 str
    :name 存储名称 str
    """
    try:
        urlretrieve(url, name)
    except (RuntimeError, ConnectionError):
        urlretrieve(url, name)


def main():
    # 版本文件
    update_file = 'update.json'
    # 本地版本信息
    content = get_json(update_file)
    # 获取服务器版本信息
    r_content = get_json(content['version_url'])
    # 老版本号与新版本号
    old = content['version']
    new = r_content['version']
    # 零时名称
    appname = content['name'] + '_new.exe'
    # 是否有新版本
    updated = is_updated(old, new)
    # 有新版本并且没有下载好的文件
    if updated and not check_exists(appname):
        print("开始下载...")
        download(content['download_url'], appname)
        print("下载完成！")
    # 删除本地版本
    old_name = content['name'] + '.exe'
    if updated and check_exists(old_name):
        print("删除老版本")
        remove(old_name)
    # 更改新版本名称
    if updated and check_exists(appname) and not check_exists(old_name):
        print("更新名称")
        rename(appname, old_name)
    # 更新本地版本信息
    # 把远程版本号更新到本地
    if updated:
        content['version'] = r_content['version']
        with open(update_file, 'w', encoding='utf-8') as f:
            print("更新版本信息")
            json.dump(content, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
