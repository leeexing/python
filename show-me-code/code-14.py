'''
## 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

student.xls

阅读资料 腾讯游戏开发 XML 和 Excel 内容相互转换
'''

import xlwt
import re

def main():
    fname = './dist/014/student.xls'
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('student', cell_overwrite_ok = True)
    info = re.compile(r'\"(\d+)\":\[\"(\w+)\",(\d+),(\d+),(\d+)\]')
    
    with open('./_assets/doc/student.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
    print(txt)
    print(info.findall(txt))
    data = info.findall(txt)
    for row_ind, line in enumerate(data):
        for col_ind, cell in enumerate(line):
            sheet.write(row_ind, col_ind, cell)
    
    book.save(fname)

if __name__ == '__main__':
    main()


# 学习

# python操作Excel读写

'''
处理excel文件是在工作中经常用到的，python为我们考虑到了这一点，python中本身就自带csv模块。
 
创建工作簿（workbook）和工作表（sheet）
import xlwt
workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("Sheet Name")

写单元格（cell）
sheet.write(0, 0, 'foobar') # row, column, value

对单元格应用样式（加粗为例）
style = xlwt.easyxf('font: bold 1')
sheet.write(0, 0, 'foobar', style)

设置列宽
sheet.col(0).width = 256 * (len(key) + 1) 
# set width.. 256 = 1 width of 0 character
'''