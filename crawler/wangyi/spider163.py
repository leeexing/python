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

music_categories = ['古典', '轻音乐','电子', '民谣', '爵士', '流行', '说唱']

music_arr = []

def get_music(url, category):
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
    photoins = soup.select('.photoin')
    for photo in photoins:
        obj = {
            'type': category,
            'typeName': music_categories[category-1],
            'cover': photo.select('.artist-img .artist_photo img')[0].attrs['src'],
            'href': photo.select('.artist-img .artist_photo')[0].attrs['href'],
            'sides': json.loads(photo.select('.artist-img')[0].attrs['data-sids']),
            'name': photo.select('.ll a')[0].get_text(),
            'like': int(nums.findall(photo.select('.ll .pl')[0].get_text())[0])
        }
        music_arr.append(obj)

def save_music(item):
    if douban.save(item):
        pass
    else:
        print('保存失败')
        
def main():
    # urls = ['https://music.douban.com/artists/genre_page/{}/{}'.format(cate, indx) for cate in range(1, 2) for indx in range(1,2)]
    content = requests.get('http://124.202.164.16/files/3216000009F0694B/m10.music.126.net/20170324152218/0b9ee6cb89c65921ad956fe86768cc49/ymusic/513b/e87e/3360/b872f9d143b44d35a21ef404f75b884a.mp3').content
    http://124.202.164.4/files/420800000B0DD043/m7.music.126.net/20171130092709/1b2cb0e77d693e68916001587e64273d/ymusic/a623/a974/c01d/a5097d2488bff76ffe34d4d75791f4e7.mp3
    http://m10.music.126.net/20180129204057/6f3a8569d576c5d2b581fff3c5da8307/ymusic/a623/a974/c01d/a5097d2488bff76ffe34d4d75791f4e7.mp3
    # print(content)
    with open('1.mp3', 'wb') as f:
        f.write(content)

if __name__ == "__main__":
    main()