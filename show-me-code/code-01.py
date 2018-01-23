'''
## 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import random, string
import pymongo

client = pymongo.MongoClient('localhost', 27017)
python_QR_db = client['python']['QR_code']

def main(count=100, length=20):
    # count = 100
    # length = 20
    forSelect = string.ascii_letters + '0123456789'
    qr_data = []
    for x in range(count):
        re = ''
        for y in range(length):
            re += random.choice(forSelect)
        # print(re)
        obj = {
            'type': 'discount' if x > 50 else 'activation',
            'qr_code': re
        }
        qr_data.append(obj)
    # print(qr_data)
    save_qr_to_db(qr_data)

def save_qr_to_db(data):
    '''将激活码保存到 mongodb 中'''
    for item in data:
        # python_QR_db.insert_one(item)
        python_QR_db.save(item)

if __name__ == '__main__':
    main()





# 学习
# string.ascii_letters  // 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# random.choice从序列中获取一个随机元素
'''
random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。
参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
'''
# random.shuffle  random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱