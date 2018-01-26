'''
## 第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 ## 第 0005 题的代码是否可以复用
'''
from PIL import Image
import os

path_file = './_assets/images'

def self_adaption(files, width, height):
    for fname in files:
        img = Image.open(os.path.join(path_file, fname))
        print('{} 图像的原始宽：{} - 高：{} - 类型：{}'.format(fname, img.size[0], img.size[1], img.mode))
        img.thumbnail((width, height))
        print('{} 图像缩放后的宽高：{} - {} - {}'.format(fname, img.size[0], img.size[1], img.mode))
        print('='*20)
        # img.show()
        img.save(os.path.join('./dist/022', fname))

def main():
    files = [fs for fs in os.listdir(path_file) if os.path.isfile(os.path.join(path_file, fs)) and fs.endswith('.jpg')]
    PHONE = {
        'iphone5': (1136, 640),
        'iphone6': (1134,750),
        'iphone6P': (2208, 1242)
    }
    width, height = PHONE['iphone6']
    print(files)
    self_adaption(files, width, height)

if __name__ == '__main__':
    main()

# 学习