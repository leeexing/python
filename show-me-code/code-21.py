'''
## 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
'''
import hashlib
from collections import defaultdict

# db = {}
db = defaultdict(lambda: 'N/A')

def get_md5(password):
    a = hashlib.md5()
    a.update(password.encode('utf-8'))
    return (a.hexdigest())

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    b = get_md5(password + username + 'the-Salt')
    print(b)
    if b == db[username]:
        return True
    else:
        return False

def app():
    a = input('注册输入用户名：')
    b = input('注册输入密码：')
    register(a, b)

    while True:
        c = input('登陆输入用户名：')
        if c == 'exit':
            break
        d = input('登陆输入密码：')
        if login(c, d):
            print('{:+^20}'.format('登陆成功'))
        else:
            print('{:=^20}'.format('登陆失败'))

def main():
    app()

if __name__ == '__main__':
    main()

# 学习

# defaultdict

'''
用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'

注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。