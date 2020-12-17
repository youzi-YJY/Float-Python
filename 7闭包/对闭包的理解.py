# -*- coding:utf-8 -*-
class Average:
    def __init__(self):
        self.series=[]

    def average(self,new_value):
        self.series.append(new_value)
        total=sum(self.series)
        return total/len(self.series)

#Average实例是可调用的对象，使用类来实现平均函数的功能。
#在Average类中存储历史值很明显:self.series实例属性

#下面使用高阶函数

def make_average():
    series=[]
    #闭包延伸
    def average(new_value):
        #调用实例的时候，average已经返回了，series是一个自由变量：
        #指未在本地作用域中绑定的变量
        series.append(new_value)
        totoal=sum(series)
        return totoal/len(series)
    return average

#闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时
#虽然定义作用域不可用了，但是仍能使用那些绑定。
#只有在嵌套其他函数中的函数才可能需要处理不在全局作用域中的外部变量

#计算移动平均值的高阶函数，不保存所有历史值，但有缺陷
def make_avager():
    count=0
    total=0
    def average(new_vaule):
        nonlocal  count,total
        count+=1
        total+=new_vaule
        return total/count
    return average
'''
UnboundLocalError:local variable 'count' referenced before assignment
'''
#对于数字、字符串、元组等不可变类型来说，只能读取，不能更新
#如果重新绑定：count+=1 会隐式创建局部变量，这样count就不能自由变量了
#也就无法保存在闭包中
#Python3引入了nonlocal声明，它的作用是将变量标记为自由变量，即使赋予新值，也会变为自由变量。
