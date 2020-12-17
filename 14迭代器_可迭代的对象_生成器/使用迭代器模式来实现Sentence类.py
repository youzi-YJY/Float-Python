# -*-coding:utf-8 -*-
import re
import reprlib

'''
迭代器模式可以用来：
1.访问一个聚合对象的内容而无需暴露它的内部表示
2.支持聚合对象的多种遍历
3.为遍历不同的聚合结构提供一个统一的接口
为支持"多种遍历"，必须能从一个可迭代的实例中获取多个独立的迭代器，而且
各个迭代器要能维护自身的内部状态
正确是的实现方式是：每次调用iter(my_iterable)都新建一个独立的迭代器，
这就是为什么要定义SentenceIterator类。
'''

#compile用于生成一个正则表达式对象，供match 和 search函数使用
#\w 匹配字母数字下划线
RE_WORD=re.compile('\w+')



#Sentence类第二版：14迭代器_可迭代的对象_生成器
class Sentence:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.recursive_repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self,words):
        self.words=words
        self.index=0

    def __next__(self):
        try:
            word=self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return word

    def __iter__(self):
        return self

'''
Attention：
要知道
可迭代的对象有个__iter__方法，每次都实例化一个新的迭代器
而迭代器要实现__next__方法，返回单个元素，此外还要实现__iter__方法，返回迭代器本身
'''