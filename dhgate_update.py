# coding=utf-8
from json import loads, dump
from urllib.request import urlretrieve
from os.path import join
from os import remove
import requests


# 解析json文件
def parse_json(jsonfile):
    if 'http' in jsonfile:
        content = requests.get(jsonfile).json()
    else:
        with open(jsonfile, 'r', encoding='utf-8') as f:
            content = loads(f.read())
    return content


# 判断版本是否最新
def check_if_latest(old_version, new_version):
    latest = True
    if (old_version < new_version):
        latest = False
    return latest


# 下载
def download(download_url, appname):
    urlretrieve(download_url, join('./', appname))


# 删除旧版本
def del_app(appname):
    remove(appname)


# 制作版本名称
def make_name(info):
    return info['name'] + ' v' + str(info['version']) + '.exe'


# 更新版本信息
def update_local_version_info(version_file, old_version_info, new_version):
    old_version_info['version'] = new_version
    with open(version_file, 'w', encoding='utf-8') as f:
        dump(old_version_info, f, ensure_ascii=False)


if __name__ == "__main__":
    # # 获取旧版本信息，以便等会删除
    old_version_info = parse_json('update.json')
    old_appname = make_name(old_version_info)
    print(old_appname)

    # 获取新版本信息，以便等会命名
    new_version_info = parse_json(old_version_info['version_url'])
    # 新版本名称
    appname = make_name(new_version_info)
    print(appname)
    # 判断是否是最新
    if not check_if_latest(old_version_info['version'],
                           new_version_info['version']):
        try:
            # 下载最新版
            download(old_version_info['download_url'], appname)
        except RuntimeError:
            download(old_version_info['download_url'], appname)
        # 删除老版本
        del_app(old_appname)
        # 更新本地版本信息
        update_local_version_info('update_demo.json', old_version_info,
                                  new_version_info['version'])
