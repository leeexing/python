#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
获取某个 RSS 的相关新闻 & 获取某地的天气；通过 index.html 展现出来gti
"""

import datetime
import requests
import feedparser
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed"}

DEFAULTS = {
    'city': '北京',
    'publication': 'songshuhui'
}

WEATHERS = {
    "北京": 101010100,
    "上海": 101020100,
    "广州": 101280101,
    "深圳": 101280601
}

def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]

@app.route('/')
def index():
    print('cookie信息 {}'.format(request.cookies())
    publication = get_value_with_fallback('publication')
    city = get_value_with_fallback('city')
    print('='*30)
    print(city)

    weather = get_weather(city)
    articles = get_news(publication)

    response = make_response(render_template('index.html', articles = articles, weather = weather))

    expires = datetime.datetime.now() + datetime.timedelta(days = 365)
    response.set_cookie('publication', publication, expires = expires)
    response.set_cookie('city', city, expires = expires)

    return response


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    # print(feed)
    return feed['entries']

def get_weather(city):
    code = WEATHERS.get(city, '101010100')
    url = "http://www.weather.com.cn/data/sk/{0}.html".format(code)

    r = requests.get(url)
    r.encoding = 'utf-8'
    print('*'*20)
    print(r.json())

    data = r.json()['weatherinfo']
    return dict(city=data['city'], temperature=data['temp'], description=data['WD'])



if __name__ == '__main__':
    app.run(debug=True)



""""
Response.set_cookie(
    key, //键
    value='', //值
    max_age=None, //秒为单位的cookie寿命，None表示http-only
    expires=None, //失效时间，datetime对象或unix时间戳
    path='/', //cookie的有效路径
    domain=None, //cookie的有效域
    secure=None, 
    httponly=False)

"""