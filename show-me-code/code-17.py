'''
## 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

import xlrd, codecs
from lxml import etree
from collections import OrderedDict

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    print(table.nrows)
    c = OrderedDict()
    for idx in range(table.nrows):
        print(table.row_values(idx))
        print(table.cell(idx,0).value)
        c[table.cell(idx, 0).value] = table.row_values(idx)[1:]
    return c

def save_xml(data):
    output = codecs.open('student.xml', 'w', 'utf-8')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'student')
    student.text = str(data)
    student.append(etree.Comment('学生信息表\n\"id\": [名字， 数学，语文， 英语]'))
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()

def main():
    fname = './dist/014/student.xls'
    data = read_xls(fname)
    print(data)
    save_xml(data)
    

if __name__ == '__main__':
    main()

# 学习

# OrderedDict
# Python中的字典对象可以以“键：值”的方式存取数据。OrderedDict是它的一个子类，实现了对字典对象中元素的排序。
# 使用OrderedDict会根据放入元素的先后顺序进行排序。由于进行了排序，所以OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象
'''
一、首先明白创建 dict 的方式

1、传统的文字表达式：
>>> d={'name':'Allen','age':21,'gender':'male'}
>>> d
{'age': 21, 'name': 'Allen', 'gender': 'male'}

2.动态分配键值：
>>> d={}
>>> d['name']='Allen'
>>> d['age']=21
>>> d['gender']='male'
>>> d
{'age': 21, 'name': 'Allen', 'gender': 'male'}

3.字典键值表：
>>> c = dict(name='Allen', age=14, gender='male')
>>> c
{'gender': 'male', 'name': 'Allen', 'age': 14}

**注意**
因为这种形式语法简单，不易出错，所以非常流行。
这种形式所需的代码比常量少，但是键必须都是字符串才行，所以下列代码会报错
>>> c = dict(name='Allen', age=14, gender='male', 1='abcd')
SyntaxError: keyword can't be an expression

4.字典键值元组表
>>> obj = dict([('1', ['张三', '150', '120', '100']), ('name','Allen')])
>>> obj
{'1': ['张三', '150', '120', '100']}
    如果你需要在程序运行时把键和值逐步建成序列，那么这种方式比较有用。

# 这种数据格式就是和 obj.items() 返回的数据格式相同

5.所有键的值都相同或者赋予初始值：
>>> f=dict.fromkeys(['height','weight'],'normal')
>>> f
{'weight': 'normal', 'height': 'normal'}

二、collections.OrderedDict

dd = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
#按key排序
kd = collections.OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
print kd
#按照value排序
vd = collections.OrderedDict(sorted(dd.items(),key=lambda t:t[1]))
print vd

#输出
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
'''