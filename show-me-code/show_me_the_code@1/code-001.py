# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import string
import random

KEY_LEN = 20
KEY_ALL = 200

KEY_STRING = string.ascii_letters + string.digits

def key_gen():
    keylists = [random.choice(KEY_STRING) for _ in range(KEY_LEN)]
    return ''.join(keylists)

def key_num(num, result=None):
    if result is None:
        result = []
    for _ in range(num):
        result.append(key_gen())
    return result

def main():
    print(key_num(10))

if __name__ == '__main__':
    main()