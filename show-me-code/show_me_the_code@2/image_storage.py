# -*- coding:utf-8 -*-
from qiniu import Auth, put_data, put_file, etag

# 需要填写你的 Access Key 和 Secret Key
access_key = 'q6QLur7zYpyj9rUAeUwkKA3g2BxiGRugfevdqW7r'
secret_key = 'l8AfWuWW4DfK1TrZyPzUsXc8WKa_YojUgCUG040u'

# #构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'python'

#上传到七牛后保存的文件名
key = 'my-python-logo.png';

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = r'E:/Leeing/python/python/show-me-code/_assets/images/weixin_avatar2.png'
ret, info = put_file(token, key, localfile)
print(info)

assert ret['key'] == key
assert ret['hash'] == etag(localfile)