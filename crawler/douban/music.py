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
    for cate in range(1, 8):
        for index in range(1, 6):
            get_music('https://music.douban.com/artists/genre_page/{}/{}'.format(cate, index), cate)
            time.sleep(1)
    # print(music_arr)
    for item in music_arr:
        save_music(item)
    

if __name__ == "__main__":
    main()