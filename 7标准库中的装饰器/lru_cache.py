# -*- coding:utf-8 -*-
import functools
from clockdeco import clock
import time


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)
'''
[0.00000058s] fibonacci(0) -> 0
[0.00000065s] fibonacci(1) -> 1
[0.00006516s] fibonacci(2) -> 1
[0.00000041s] fibonacci(1) -> 1
[0.00000055s] fibonacci(0) -> 0
[0.00000044s] fibonacci(1) -> 1
[0.00001363s] fibonacci(2) -> 1
[0.00002591s] fibonacci(3) -> 2
[0.00010353s] fibonacci(4) -> 3
[0.00000036s] fibonacci(1) -> 1
[0.00000036s] fibonacci(0) -> 0
[0.00000040s] fibonacci(1) -> 1
[0.00001270s] fibonacci(2) -> 1
[0.00002495s] fibonacci(3) -> 2
[0.00000036s] fibonacci(0) -> 0
[0.00000041s] fibonacci(1) -> 1
[0.00001248s] fibonacci(2) -> 1
[0.00000035s] fibonacci(1) -> 1
[0.00000044s] fibonacci(0) -> 0
[0.00000035s] fibonacci(1) -> 1
[0.00001267s] fibonacci(2) -> 1
[0.00002483s] fibonacci(3) -> 2
[0.00005073s] fibonacci(4) -> 3
[0.00008731s] fibonacci(5) -> 5
[0.00020422s] fibonacci(6) -> 8
8
'''

@functools.lru_cache()
@clock
def fibonacci(n):
    t0=time.time()
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))

'''
[0.00000095s] fibonacci(0) -> 0
[0.00000235s] fibonacci(1) -> 1
[0.00016627s] fibonacci(2) -> 1
[0.00000457s] fibonacci(3) -> 2
[0.00029642s] fibonacci(4) -> 3
[0.00000257s] fibonacci(5) -> 5
[0.00035774s] fibonacci(6) -> 8
8
'''
#需要注意的点：
#1.必须像调用函数那样来使用lru_cache装饰器，带括号：@functools.lru_cache()
#2.叠放了装饰器，@lru_cache()应用到@clock返回的函数上。
'''
@d1
@d2
def f():
    printf('f')
等同于：
def f():
    printf('f')
f=d1(d2(f))
'''
#3.lru_cache可以使用两个可选的参数来配置，签名为：functools.lru_cache(maxsize=128,type=False)
#maxsize参数指定存储多少个调用的结果，最好设置为2的幂。
#type参数如果设置为True，把不同参数类型得到的结果分开保存。
#lru_cache使用字典存储结果，而且间根据调用时传入的定位参数和关键字参数创建，所以要求参数都必须是可散列的。