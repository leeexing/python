'''
使用最初的 requests 方法去获取
'''
import re, time, requests
from bs4 import BeautifulSoup
import io, sys
## 修改默认编码格式
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'host': 'www.jianshu.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.jianshu.com/'
    }
    content = requests.get(url, headers=headers).content
    print(content.decode('utf-8'))

def main():
    url = 'https://www.jianshu.com/'
    get_data(url)

if __name__ == '__main__':
    main()