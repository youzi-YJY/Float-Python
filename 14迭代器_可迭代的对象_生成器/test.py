# -*-coding:utf-8 -*-
import re
import reprlib

RE_WORD=re.compile('\w+')
text='"The time has come," the Walrus said'
words=RE_WORD.findall(text)
print(words)