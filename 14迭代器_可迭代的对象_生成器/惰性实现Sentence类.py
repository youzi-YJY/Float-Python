import re
import reprlib

RE_WORD=re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text=text

    def __repr__(self):
        return 'Sentencr(%s)' %reprlib.repr(self.text)

    def __next__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

'''
和前面的Sentence类进行对比，这般具有惰性，
体现在只在需要时才生成下一个单词
而前面的__init__方法急切地构建好了文本中的单词列表，并将其绑定到self.words上
re.finditer函数返回的不是列表，而是一个生成器，是re.findall函数的惰性版本。
'''