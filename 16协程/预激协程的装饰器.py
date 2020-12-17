from functools import wraps

def coroutine(func):
    '''
    装饰器：向前执行到第一个'yield'表达式，预激'func'
    '''
    @wraps(func)
    def primer(*args,**kwargs):
        gen=func(*args,**kwargs)
        next(gen)
        return gen
    return primer

'''
from coroutil import coroutine

@corotine
def averager():
    total=0.0
    count=0
    average=None
    while True:
        term=yield average
        total+=term
        count+=1
        average=total/count
'''

#让协程返回值
#namedtuple:不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，
#所以在这里引入了 collections.namedtuple 这个工厂函数，来构造一个带字段名的元组。

from collections import namedtuple
result=namedtuple('Result','count average')

def average():
    total=0.0
    count=0
    average=None
    while True:
        term=yield
        if term is None:
            break
        total+=term
        count+=1
        average=total/count
    return result(count,average)

#这一版不产出值，发送None会终止循环，导致协程结束，返回结果
#一如既往的，生成器对象会抛出StopIteration异常，异常对象的value属性保存着返回的值