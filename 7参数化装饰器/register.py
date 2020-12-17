# -*-coding:utf-8 -*-
registry=[]
def register(active=True):
    def decorate(func):
        print('running register (active=%s)->decorate(%s)'
              %(active,func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func#装饰器必须返回一个函数
    return decorate#装饰器工厂函数，必须返回一个函数

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')


#如果不使用@句法，那就要像常规函数那样使用register
#若把f添加到registry中：register()(f)
#删除为：register(active=False)(f)