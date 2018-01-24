'''
## 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
http://tieba.baidu.com/p/2166231880
'''
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def get_image_srcs(url):
    content = requests.get(url).content
    # print(content.decode('utf-8'))
    soup = BeautifulSoup(content, 'lxml')
    images = soup.select('.p_content img')
    print(len(images))
    img_srcs = []
    for img in images:
        src = img.attrs['src']
        img_srcs.append(src)
    return img_srcs

def get_image(index, url):
    bdwater = '杉本有美吧'
    img_r = requests.get(url, stream = True)
    if img_r.status_code == 200:
        with open('./dist/013/{}-{}.jpg'.format(bdwater, index), 'wb') as f:
            for chunk in img_r:
                f.write(chunk)

def get_img_by_uillib(index, url):
    '''这个方法更加简单，一部就可以搞定'''
    urlretrieve(url, './dist/013/杉本有美吧-{}.jpg'.format(index))

def main():
    url = 'http://tieba.baidu.com/p/2166231880'
    img_srcs = get_image_srcs(url)

    # 方法一
    # for index, src in enumerate(img_srcs, 1):
    #     get_image(index, src)

    # 方法二
    for index, src in enumerate(img_srcs[0:5], 1):
        get_img_by_uillib(index, src)

if __name__ == '__main__':
    main()


# 学习

# enumerate()使用
'''
enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得   索引和值    -- 重点
enumerate多用于在for循环中得到计数
'''