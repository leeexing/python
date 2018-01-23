'''
## 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
from PIL import Image, ImageOps
import os
import os.path as path

file_abs_path = r'./_assets/images'

def main():
    l = os.listdir(file_abs_path)
    lists = [item for item in l if path.isfile(path.join(file_abs_path,item)) and is_img(item)]
    print(lists)
    for filename in lists:
        filter_img_size(filename)

def filter_img_size(filename):
    img = Image.open(path.join(file_abs_path, filename))
    width, height = img.size
    print(width, height)
    height = height * 500 // width
    width = 500
    img = ImageOps.fit(img, (width, height))
    w, h = img.size
    print(w, h)
    img.save(path.join(r'./dist/05', filename))

def is_img(string):
    string = string.lower()
    return string.endswith('.jpg') or string.endswith('png') or string.endswith('.jpeg')


if __name__ == '__main__':
    main()


# 学习
# 注意：
# 当我使用os.path.isdir(目录的绝对路径)的时候，返回的才是true，也就是说，python的isdir()并不像php的is_dir()那样，可以使用当前工作目录的相对路径，
'''
        l = os.listdir('./_assets/images')
        lists = [item for item in l if os.path.isfile(item)]
        print(lists) // []
'''

# 额外知识

'''
python os 命令

os.sep 可以取代操作系统特定的路径分割符。
os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
os.listdir()返回指定目录下的所有文件和目录名。
os.remove()函数用来删除一个文件。
os.system()函数用来运行shell命令。

os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

os.path.split()函数返回一个路径的目录名和文件名。

os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。

os.path.existe()函数用来检验给出的路径是否真地存在

os和os.path模块
os.listdir(dirname)：列出dirname下的目录和文件
os.getcwd()：获得当前工作目录
os.curdir:返回但前目录（'.')
os.chdir(dirname):改变工作目录到dirname
'''

# ImageOps模块的函数

'''
Image.new(mode,size,color)中，可以填“L”或者‘RGB’等，那么mode这个参数是什么意思呢？
new方法用于创建一幅给定模式（mode）和尺寸（size）的图片。'RGB'是指的RGB彩色图像，‘L’是指的灰度图像。
mode 代表如何对图像矩阵进行解析（色彩空间）
“L”：灰度显示，8bit每像素（区别于1）
“RGB”：红绿蓝三通道


'''

'''
Autocontrast
定义：ImageOps.autocontrast(image, cutoff=0)? image
含义：最大图像对比度。这个函数计算一个输入图像的直方图，从这个直方图中去除最亮和最暗的百分之cutoff，然后重新映射图像，以便保留的最暗像素变为黑色，即0，最亮的变为白色，即255。
>>> im02 = Image.open("D:\\Code\\Python\\test\\img\\test02.jpg")
>>> im = ImageOps.autocontrast(im02, 20)
在图像im02中，去掉了原来直方图中最暗和最亮的各20%，剩下的像素值然后再映射到[0，255]的颜色空间上。


Colorize
ImageOps.colorize(image, black, white)? image
含义：使得灰色图像变成彩色图像。变量black和white应该是RGB元组或者颜色名称。这个函数会计算出一个颜色值，使得源图像中的所有黑色变成第一种颜色，所有白色变成第二种颜色。
变量image的模式必须为“L”。
eg: 
    im_r = ImageOps.colorize(r, "green", "blue")

Crop
ImageOps.crop(image, border=0)? image
含义：从图像的四个边去掉变量border定义的四元组对应的行/列。这个函数对所有图像模式有效。

Fit
ImageOps.fit(image, size, method, bleed, centering)? image
含义：返回一个指定大小的裁剪过的图像。该图像被裁剪到指定的宽高比和尺寸。变量size是要求的输出尺寸，以像素为单位，是一个（宽，高）元组。
变量method是用于重采样的方法。默认值为Image.NEAREST。
变量bleed允许用户去掉图像的边界（图像四个边界）。这个值是一个百分比数（0.01表示百分之一）。默认值是0（没有边界）。
变量centering用于控制裁剪位置。(0.5,0.5)是裁剪中心（例如，如果裁剪宽度，裁掉左侧50%（右侧50%），顶/底一样）

Flip
定义：ImageOps.flip(image)? image
含义：输出图像为输入图像在垂直方向的镜像（顶部跟底部对调）。
>>> im02= Image.open("D:\\Code\\Python\\test\\img\\test02.jpg")
>>> im= ImageOps.flip(im02)

Grayscale
定义：ImageOps.grayscale(image)? image
含义：将输入图像转换为灰色图像。
>>>im02 = Image.open("D:\\Code\\Python\\test\\img\\test02.jpg")
>>> im= ImageOps.grayscale(im02)
>>>im.mode
'L'

Invert
定义：ImageOps.invert(image)? image
含义：将输入图像转换为反色图像。
>>>im02 = Image.open("D:\\Code\\Python\\test\\img\\test02.jpg")
>>> im= ImageOps.invert(im02)

Mirror
定义：ImageOps.mirror(image)? image
含义：输出图像为输入图像水平方向的镜像。

Posterize
定义：ImageOps.posterize(image,bits)? image
含义：将每个颜色通道上变量bits对应的低(8-bits)个bit置0。变量bits的取值范围为[0，8]。
'''