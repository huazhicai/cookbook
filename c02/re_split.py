# -*- coding:utf-8 -*-
"""
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
"""
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s*', line)
values = fields[1::2]
delimiters = fields[1::2] + ['']
print(values)
print(re.split(r'(?:,|;|\s)\s*', line))

# ==============================
import os

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.py', '.h'))])
print(any(name.endswith('.h') for name in filenames))
if any(name.endswith(('.c', '.h')) for name in os.listdir('.')):
    pass

# ===============================compile
# 同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
if datepat.match(text2):
    print('yes')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

#  r'(\d+)/(\d+)/(\d+)' 。 这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。
#  如果不这样做的话，你必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)'
m = datepat.match('11/27/2012abcdef')
print(m.group())
