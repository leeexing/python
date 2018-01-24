'''
## 第 0009 题： 一个HTML文件，找出里面的链接。
'''
import re, os
import requests
from bs4 import BeautifulSoup

path_file = r'./_assets/code'
def main():
    names = [os.path.join(path_file, item) for item in os.listdir(path_file) if item.endswith('.html')]
    print(names)
    for item in names[1:2]:
        with open(item, encoding='utf-8') as f:
            data = f.read()
            print(data) 

def app():
    url = 'http://www.leeeing.com/'
    content = requests.get(url).content
    # print(content.decode('utf-8'))
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.select('a')
    for item in links:
        print(item.get_text().strip())
    # print(link.get_text())

if __name__ == '__main__':
    # main()
    app()