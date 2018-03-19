from PIL import Image, ImageFilter

def main():
    img1 = Image.open('./_assets/images/weixin_avatar1.png')
    # img2 = Image.open('./assets/images/weixin_avatar2.png')
    # img = Image.blend(img1, img2, 0.5)
    # img.show()
    img2 = img1.filter(ImageFilter.BLUR)
    img2.show()

if __name__ == '__main__':
    main()