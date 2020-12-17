# -*-coding:utf-8 -*-
import re
import reprlib

RE_WORD=re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return
'''
不需要单独定义一个迭代器类
迭代器其实是生成器对象，每次调用__iter__方法都会自动创建，因为这里__iter__
方法是生成器函数
Attention：所有生成器都是迭代器，因为生成器完全实现了迭代器接口。
'''