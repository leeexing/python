# encoding = 'utf-8
'''
爬虫豆瓣音乐
'''
import re, requests, time
from bs4 import BeautifulSoup
import json
import pymongo
# 修改默认编码方式

client = pymongo.MongoClient('localhost', 27017)
douban = client['myblog']['music']

nums = re.compile('\d+')

def get_music(url):
    ''' no '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.jianshu.com/p/410e0a3c28cd',
        'Upgrade-Insecure-Requests': '1'
    }
    content = requests.get(url, headers=headers).content
    print(content.decode('utf-8'))

def save_music(item):
    if douban.save(item):
        pass
    else:
        print('保存失败')
        
def main():
    # url = 'http://music.163.com/'
    url = 'http://music.163.com/api/playlist/detail?id=37880978&updateTime=-1'
    get_music(url)

if __name__ == "__main__":
    main()