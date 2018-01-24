'''
## 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''
import os

path_file = r'./_assets/doc'

word_filter = set()

def main():
    global word_filter
    with open(os.path.join(path_file, 'filter_words.txt'), 'r', encoding='utf-8') as f:
        data = f.readlines()
        for item in data:
            if item.strip() != '':
                word_filter |= {item.strip('\n')}
        print(word_filter)
    please_input()


def please_input():
    '''这是一个输入交互'''
    while True:
        s = input()
        if s == 'exit':
            break
        elif s in word_filter:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    main()

# 学习
# set   ：   是一个无序不重复元素集。 
# **注意**：是无序的。顺序是无可预知！！
'''
集合支持一系列标准操作，包括并集、交集、差集和对称差集，例如：

a = t | s          # t 和 s的并集     # 相当于 s.update(t)
  
b = t & s          # t 和 s的交集  
  
c = t – s          # 求差集（项在t中，但不在s中）  
  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中） 

基本操作：

t.add('x')            # 添加一项  
  
s.update([10,37,42])  # 在s中添加多项 

使用remove()可以删除一项：  
t.remove('H')  

s.discard(x)  
如果在 set “s”中存在元素 x, 则删除

s.pop()  
删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError  
  
s.clear()  
删除 set “s”中的所有元素  

len(s)  
set 的长度  
  
x in s  
测试 x 是否是 s 的成员  

s.issubset(t)  
s <= t  
测试是否 s 中的每一个元素都在 t 中  
  
s.issuperset(t)  
s >= t  
测试是否 t 中的每一个元素都在 s 中  
  
s.union(t)  
s | t  
返回一个新的 set 包含 s 和 t 中的每一个元素 

hash(s)  
返回 s 的 hash 值

s.copy()  
返回 set “s”的一个浅复制  

'''