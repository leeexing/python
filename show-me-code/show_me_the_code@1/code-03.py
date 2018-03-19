'''
## 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''
import redis
import string, random
r = redis.Redis(host='localhost', port=6379, db=0)

forSelect = string.ascii_letters + '0123456789'
def main(count=100, length=23):
    '''生成激活码'''
    act_list = []
    for n in range(count):
        activation = ''
        for i in range(length):
            activation += random.choice(forSelect)
        # print(activation)
        act_list.append(activation)
    print(act_list)
    save_to_redis(act_list)

def save_to_redis(data):
    for item in data:
        r.sadd('activation:apple', item)

def get_activation():
    arr = r.smembers('activation:apple')
    print(arr)

if __name__ == '__main__':
    main(2)
    # get_activation()


# redis连接实例是线程安全的，可以直接将redis连接实例设置为一个全局变量，直接使用。
# 如果需要另一个Redis实例（or Redis数据库）时，就需要重新创建redis连接实例来获取一个新的连接。同理，python的redis没有实现select命令

'''
Redis 键命令的基本语法如下： COMMAND KEY_NAME

SET runoobkey redis   |  DEL runoobkey

1、Redis 字符串(String) ：set keyName keyValue   |   get keyName

2、Redis 哈希(Hash)：HMSET keyName keyValues    |   HGETALL runoobkey
    Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。
    **这个就有点像 dict 数据类型了啊**
    eg：
    HMSET runoobkey name "redis tutorial" description "redis basic commands for caching" likes 20 visitors 23000
    HGETALL runoobkey
    1) "name"
    2) "redis tutorial"
    3) "description"
    4) "redis basic commands for caching"
    5) "likes"
    6) "20"
    7) "visitors"
    8) "23000"

3、Redis 列表(List) ：LPUSH runoobkey redis、LPUSH runoobkey mongodb |   LRANGE runoobkey 0 10

4、Redis 集合(Set)：SADD runoobkey redis、SADD runoobkey mongodb   |   SMEMBERS runoobkey    //  "mysql" "mongodb"

5、Redis 有序集合(sorted set)：ZADD runoobkey 1 redis、ZADD runoobkey 2 mongodb、ZADD runoobkey 3 mysql  |  ZRANGE runoobkey 0 10 WITHSCORES
    // 1) "redis" 2) "1" 3) "mongodb" 4) "2" 5) "mysql" 6) "4"

6、Redis HyperLogLog
    Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。
'''