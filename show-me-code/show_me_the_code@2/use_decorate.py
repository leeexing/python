# -*- coding:utf-8 -*-
"""
2 道极好的 Python 算法题 | 带你透彻理解装饰器的妙用

1.斐波那契数列

2.爬楼梯
    比如我有7阶台阶，我们可以用两种爬发，一次一步或者两步，只能进不能退，算算有多少种爬法
"""
def fib(n):
    """斐波那契"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print([fib(n) for n in range(10)])

# 这里没有进行优化的情况下，打印n=40的时候需要 150s左右。所以我们考虑加一个缓存 cache

def fib(n, cache=None): # 为什么这里的cache不能直接设置为 {}。因为需要递归啊。会产生一个变量缓存不变的问题
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n is 0 or n is 1:
        return 1
    else:
        cache[n] = fib(n-2, cache) + fib(n-1, cache)
        return cache[n]


######################### 爬楼梯 #########################
"""
若只有一阶台阶，那么不管是一次选择一步还是两步，都只有一种爬法

若只有两阶台阶，选择一步or两步，会有两种爬法

若只有三阶台阶，选择一步然后一步然后一步，或者一步，两步，或者两步，一步，这样有3种爬法

若只有四阶台阶，选择一步，然后剩下3阶台阶的爬法，这3阶爬法可以直接取前面3阶台阶的计算结果
"""

def climb(n, steps):
    count = 0
    if n <= 1:
        count = 1
    else:
        for step in steps:
            count += climb(n-step, steps)
    return count

print(climb(7, [1, 2]))

# 此时不想再写一次 cache
# 使用 装饰器 的时候到了

def decorate(fn):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = fn(*args) # 很巧妙的使用 tuple 类型作为 dict 的键名
        return cache[args]
    return wrap

@decorate
def Fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fib(n-2) + Fib(n-1)

@decorate
def Climb(n, steps):
    count = 0
    if n <= 1:
        count = 1
    else:
        for step in steps:
            count += Climb(n-step, steps)
    return count

print(Climb(7, (1,2)))  # 注意，这里调用时传参发生了变化，不能使用 list 的形式了，只能用 tuple 的形式