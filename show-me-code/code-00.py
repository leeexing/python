#!/usr/bin/env python
# encoding: utf-8
'''
## 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

def main():
    # text = '7'
    text = str(random.randint(0, 100))
    img = Image.open('./_assets/images/weixin_avatar1.png')
    img_w, img_h = img.size
    print('Original image size:{} -- {}'.format(img_w, img_h))

    # 缩放到50%. 函数内部需要是一个 元组
    img.thumbnail((img_w // 2, img_h // 2))

    dr = ImageDraw.Draw(img)
    font = ImageFont.truetype('./_assets/ttf/simhei.ttf', 34)

    dr.text((img.size[0]*0.5, img.size[1]*0.15), text, font=font, fill="#ff0000")

    img.rotate(45).show()
    # img.rotate(45).save('./dest/avarta_01.jpg', 'PNG')

def rand_char():
    return chr(random.randint(65, 90))

def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def app(n):
    '''随机生成验证码图片'''
    width = 60 *4
    height = 80
    img = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('./_assets/ttf/arialuni.ttf', 36)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill = rand_color())
    arr = []
    for t in range(4):
        rnd_chr = rand_char()
        arr.append(rnd_chr)
        draw.text((60*t + 10, 10), rnd_chr, font=font, fill=rand_color2())

    image = img.filter(ImageFilter.BLUR)
    print(arr)
    # image.show()
    image.save('./dist/QR-code/{}-{}.jpg'.format(''.join(arr), n), 'jpeg')

def factory(num=5):
    for i in range(num):
        app(i)


if __name__ == '__main__':
    # main()
    # app()
    factory(50)



