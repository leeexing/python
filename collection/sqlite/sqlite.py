'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。
由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成

在使用SQLite前，我们先要搞清楚几个概念：
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
'''
import sqlite3

#  连接到SQLite数据库
# 数据库文件是leeing.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('leeing.db')
# 创建一个Cursor:
cursor = conn.cursor()

def close_sqlite():
    cursor.close()
    conn.close

def create_db():
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user(id, name) values ("1", "leeing")')

    # 通过rowcount获得插入的行数:
    rowNum = cursor.rowcount
    print(rowNum)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

def get_db():
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)
    close_sqlite()

def insert_db():
    
    cursor.execute('insert into')

def main():
    # create_db()
    get_db()

if __name__ == '__main__':
    main()