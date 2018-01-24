'''
## 第 0008 题： 一个HTML文件，找出里面的正文。
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
    body = soup.select('body')[0]
    print(body.get_text())

if __name__ == '__main__':
    # main()
    app()