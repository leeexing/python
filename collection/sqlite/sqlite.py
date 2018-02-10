'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。
由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成

在使用SQLite前，我们先要搞清楚几个概念：
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
'''
import random
import string
from sqlite_base import *

Letters = string.ascii_letters
Num = '123456789'

DB_FILE_PATH = r'E:\Leeing\DB\sqlite\leeing.db'

def save_data():
    ''''''
    create_sql = '''CREATE TABLE COMPANY 
                (ID INT PRIMARY KEY NOT NULL,
                NAME    TEXT    NOT NULL,
                GENDER  VARCHAR(4)  DEFAULT NULL,
                AGE     INT     NOT NULL,
                ADDRESS CHAR(50),
                PHONE   VARCHAR(20)    DEFAULT NULL
                );'''
    # table_name = 'COMPANY'
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_sql)
    
    save_sql = '''INSERT INTO COMPANY values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
            (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
            (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
            (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
    save(conn, save_sql, data)

def get_data(from_table='COMPANY'):
    '''获取全部数据'''
    fetchall_sql = 'SELECT * FROM {}'.format(from_table)
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)

def get_one_data(cond=1):
    '''获取一条数据'''
    fetchone_sql = 'select * from account where id=?'
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, cond)

def update_data():
    '''更新数据'''
    conn = get_conn(DB_FILE_PATH)
    data = []
    for index in range(1,4):
        s = list()
        s.append(''.join(random.sample(Letters, 5)))
        s.append(index)
        data.append(tuple(s))
    print('{:=^30}'.format('更新前的数据'))
    get_data('account')
    updata_sql_account = 'update account set name = ? where id = ?'
    update(conn, updata_sql_account, data)
    print('{:+^30}'.format('更新后的数据'))
    get_data('account')

def delete_data():
    '''删除数据'''
    conn = get_conn(DB_FILE_PATH)
    print('{:=^30}'.format('删除数据前的数据'))
    get_data('account')
    delete_sql_account = 'delete from account where id = ?'
    data = ['1', '2', '3']
    delete(conn, delete_sql_account, data)
    print('{:+^30}'.format('删除数后的还有数据吗？'))
    get_data('account')


def test():
    ''''''
    create_sql = '''CREATE TABLE account 
                (ID INT PRIMARY KEY NOT NULL,
                NAME    TEXT    NOT NULL,
                AGE     INT     NOT NULL
                )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_sql)

def insert_data():
    ''''''
    if not table_is_exist('account'):
        test()
    data = []
    for index in range(1,4):
        s = list()
        s.append(index)
        s.append(''.join(random.sample(Letters, 5)))
        s.append(random.randint(10, 50))
        data.append(tuple(s))
    conn = get_conn(DB_FILE_PATH)
    save_sql = 'insert into account values (?, ?, ?)'
    save(conn, save_sql, data)
        

def table_is_exist(table_name):
    ''''''
    is_exist = False
    conn = get_conn(DB_FILE_PATH)
    cu = get_cursor(conn)
    sql = '''select count(*) from sqlite_master where type='table' and name= '{}' '''.format(table_name)
    n = cu.execute(sql)
    print(sql)
    # print(list(n))
    if list(n)[0][0] > 0:
        is_exist = True
    return is_exist

def leeing():
    '''demo'''
    pass

def main():
    # pass
    # save_data()
    # get_data('account')
    # test()
    # table_is_exist('account')
    # insert_data()
    # get_data()
    # get_one_data(4)
    # update_data()
    delete_data()

if __name__ == '__main__':
    main()