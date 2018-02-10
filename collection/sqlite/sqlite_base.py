'''
sqlite 增删改查的封装
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候连接对象会自动创建数据库文件；
如果数据库文件已经存在，则连接对象不会再创建数据库文件，而是直接打开该数据库文件。

连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库执行完任何操作后，都不需要提交事务的(commit)

        创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
        创建在内存上面： conn = sqlite3.connect('"memory:')

其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

        commit()            --事务提交              --该方法提交当前的事务。如果您未调用该方法，那么自您上一次调用 commit() 以来所做的任何动作对其他数据库连接来说是不可见的。
        rollback()          --事务回滚              --该方法回滚自上一次调用 commit() 以来对数据库所做的更改。
        close()             --关闭一个数据库链接     --该方法关闭数据库连接。请注意，这不会自动调用 commit()。如果您之前未调用 commit() 方法，就直接关闭数据库连接，您所做的所有更改将全部丢失！
        cursor()            --创建一个游标

cu = conn.cursor()
这样我们就创建了一个游标对象：cu
在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成

对于游标对象cu，具有以下具体操作：

        execute()           --执行一条sql语句         -- cursor.execute(sql [, optional parameters])  |   cursor.execute("insert into people values (?, ?)", (who, age))  占位符：问号和命名占位符（命名样式）
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录     --该方法获取查询结果集中的下一行，返回一个单一的序列，当没有更多可用的数据时，则返回 None。
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录     --该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
        scroll()            --游标滚动

使用体会：
crate table 只能创建一次，如果创建了在创建，程序会报错
如果创建了表格，那就直接 insert 或者 update 数据即可

execute(sql, data)
这个 data 必须是 tuple 数据类型
'''
import sqlite3
import os

# 数据库文件绝对路径
DB_FILE_PATH= r'E:\Leeing\DB\sqlite'
# 表名称
TABLE_NAME = ''
# 是否打印 sql
SHOW_SQL = True

def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面：【{}】'.format(path))
        return conn
    else:
        conn = None
        print('内存上面：【memory:】')
        return sqlite3.connect('memory:')

def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

##########################################
###       创建 | 删除表操作    START
##########################################

def drop_table(conn, table):
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('执行sql：【{}】'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('删除数据表【{}】成功'.format(table))
        close_all(conn, cu)
    else:
        print('the {} is empty or equal None!'.format(sql))

def create_table(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql：【{}】'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('创建数据表成功')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def close_all(conn, cu):
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()

##########################################
###        数据库操作 CRUD    START
##########################################

def save(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql: 【{}】, 参数： 【{}】'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchall(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql：【{}】'.format(sql))
        cu.execute(sql)
        result = cu.fetchall()
        if len(result) > 0:
            for index in range(len(result)):
                print(result[index])
        else:
            print('>>>> 哎呦~，一点数据都木有了 *_*')
        return result
    else:
        print('the 【{}】 is empty or equal None!'.format(sql))

def fetchone(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            d = (data, )
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('执行sql: 【{}】, 参数： 【{}】'.format(sql, d))
            cu.execute(sql, d)
            ret = cu.fetchall()
            if len(ret) > 0:
                for index in range(len(ret)):
                    print(ret[index])
            else:
                print('>>>> 嘿嘿~，你要的数据没有 #_#')
        else:
            print('the [{}] equal None'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def update(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql: 【{}】, 参数： 【{}】'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def delete(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql: 【{}】, 参数： 【{}】'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


##########################################
###         测试操作    START
##########################################

def drop_table_test():
    '''删除数据库表测试'''
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)

def create_table_test():
    '''创建数据库表测试'''
    print('创建数据库表测试...')
    create_table_sql = '''CREATE TABLE `student` (
                        `id` int(11) NOT NULL,
                        `name` varchar(20) NOT NULL,
                        `gender` varchar(4) DEFAULT NULL,
                        `age` int(11) DEFAULT NULL,
                        `address` varchar(200) DEFAULT NULL,
                        `phone` varchar(20) DEFAULT NULL,
                        PRIMARY KEY (`id`)
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)

def save_test():
    '''保存数据测试...'''
    print('保存数据测试...')
    save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
            (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
            (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
            (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)

def fetchall_test():
    '''查询所有数据...'''
    print('查询所有数据...')
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)

def fetchone_test():
    '''查询一条数据...'''
    print('查询一条数据...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = 1
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, data)

def update_test():
    '''更新数据...'''
    print('更新数据...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)

def delete_test():
    '''删除数据...'''
    print('删除数据...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)