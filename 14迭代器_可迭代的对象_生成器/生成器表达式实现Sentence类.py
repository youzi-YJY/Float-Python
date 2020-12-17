import re
import reprlib

RE_WORD=re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text=text
    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


'''
生成器可以理解为列表推导的惰性版本：不会迫切的构建列表，而是返回一个生成器，
按需惰性生成元素
如果列表推导是制造列表的工厂，那么生成器表达式就是制造生成器的工厂
生成器表达式是语法糖：完全可以替换成生成器，不过有时使用生成器表达式更便利。
'''