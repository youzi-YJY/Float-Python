# -*-coding:utf-8 -*-
class HauntBus:
    '''
    备受幽灵乘客折磨的校车
    '''
    def __init__(self,passenger=[]):
        self.passenger=passenger
        #除非这个方法确实想修改通过参数传入的对象
        #否则在类中直接把参数赋值给实例变量之前一定要三思
        #这样会为参数对象创建别名
        #不确定时，就创建副本。-
        '''
        def __init__(self,passenger=None):
            if passenger is None:
                self.passenger=[]
            else:
                self.passenger=list(passenger)
                #让乘客销声匿迹的校车
                self.passenger=passenger
                
        '''

    def pick(self,new):
        self.passenger.append(new)

    def drop(self,new):
        self.passenger.remove(new)

'''
会出现的情况是：
没有指定初始乘客的HauntBus实例会共享同一个乘客列表
结果就是：
登上一辆Bus的乘客也出现了在另一辆Bus中。
问题的根源是:
默认值在定义函数时计算(通常在加载模块时)，默认值变成了函数对象的属性
如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响
'''
