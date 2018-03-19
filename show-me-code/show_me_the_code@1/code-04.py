'''
## 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
import re, collections

words = re.compile('[a-zA-Z]+')
def main():
    with open('./_assets/doc/english.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        obj = {}
        # print(words.findall(data))
        for word in words.findall(data):
            if word not in obj:
                obj[word] = 1
            else:
                obj[word] += 1
        # 统计
        method1(data)
        method2(obj)

def method1(data):
    '''使用包'''
    frequence_words = collections.Counter(words.findall(data))
    print(frequence_words)

def method2(data):
    '''对序列进行操作'''
    obj_set = list(data.items())
    obj_sort = sorted(obj_set, key=lambda x: x[1], reverse=True)
    print(obj_sort)

def method3():
    pass
        
if __name__ == '__main__':
    main()

# 学习 文件操作
'''
.readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。
.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。
'''

# 词频统计
'''
collections


    OrderedDict类：排序字典，是字典的子类。引入自2.7。
    namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
    Counter类：为hashable对象计数，是字典的子类。引入自2.7。
    deque：双向队列。引入自2.4。
    defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。


Counter类
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
collections.Counter(words_box)
'''
