'''
## 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
'''
from PIL import Image, ImageFont, ImageOps, ImageDraw
import string
import random

forSelect = string.ascii_letters + '0123456789'
 
def main():
    width = 60 * 4
    height = 60
    img = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('./_assets/ttf/arialuni.ttf', 50)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill = rand_color())
    for t in range(4):
        draw.text((60*t + 10, 0), random.choice(forSelect), font = font, fill = rand_color2())
    img.show()

def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

if __name__ == '__main__':
    main()