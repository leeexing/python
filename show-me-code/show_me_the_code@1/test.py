# 

from PIL import Image
import os

os.chdir(r'C:\Users\lixing1\Desktop')

img = Image.open(r'haha.jpg')
new_img = img.resize((144, 256), Image.BILINEAR)
new_img.save('link.png')
new_img.show()
