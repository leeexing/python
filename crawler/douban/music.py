'''
爬虫豆瓣音乐
'''
import re, requests, time
from bs4 import BeautifulSoup
import io, sys
import pymongo
# 修改默认编码方式
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

def get_music(url):
    ''' no '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'host': 'music.douban.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.jianshu.com/p/410e0a3c28cd',
        'Upgrade-Insecure-Requests': '1'
    }
    content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(content, 'lxml')


def main():
    urls = ['https://music.douban.com/artists/genre_page/6/{}'.format(url) for url in range(1,6)]
    for url in urls:
        get_music(url)
        time.sleep(1)    

if __name__ == "__main__":
    main()