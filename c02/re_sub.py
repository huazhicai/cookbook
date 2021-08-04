# -*- coding:utf-8 -*-
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# \3 指向前面模式的捕获组号
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 相同的模式做多次替换
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)


# re.IGNORECASE

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


text2 = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text2, flags=re.IGNORECASE))
print(re.sub('python', matchcase('snake'), text2, flags=re.IGNORECASE))

# .*? 非贪婪模式
