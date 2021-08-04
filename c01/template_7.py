# -*- coding:utf-8 -*-
from queue import Queue


def avg(first, *rest):
    # rest 由所有其他位置的元素组成
    # 然后我们在代码中把它当成`一个序列`来进行后续的计算
    print(type(rest))
    print(rest)
    # * 号解析元组内的元素
    print(*rest)
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
# 剩下的元素组合成元组传递进去
# avg(1, 2)  # 1.5， （2，）
# avg(1, 2, 3, 4)  # 2.5   (2, 3, 4)

import html


def make_element(name, value, **attrs):
    # attr是一个包含所有被传进来的关键字参数的`字典`
    print(attrs)
    # print(**attrs)
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    print(keyvals)
    attr_str = ''.join(keyvals)
    element = f'<{name}{attr_str}>{html.escape(value)}</{name}>'
    print(element)
    return element


def anyargs(*args, **kwargs):
    # 接受任意数量的位置参数和关键字参数
    print(args)  # A tuple
    print(kwargs)  # A dict


# 一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数
# make_element('item', 'Albatross', size='large', quantity=6)


def add(x: int, y: int) -> int:
    # 注解函数
    return x + y


# print(add.__annotations__)


def myfunc():
    # 为了能返回多个值，函数直接return一个元组就行了
    # 实际上我们使用逗号来生成一个元组的，而不是用括号
    a = 2,
    print(type(a))
    b = 1, 2
    print(type(b))
    return 1, 2, 3


# myfunc()

def spam(a, b=None):
    if b is None:
        b = []


_no_value = object()


def _spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
'''
这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，
这跟函数的默认值参数定义是不同的。 因此，在调用这个lambda表达式的时候，x的值是执行时的值。
'''
funcs = [lambda x, n=n: x + n for n in range(5)]


# for f in funcs:
#     print(f(0))
# print(sorted(names, key=lambda name: name.split()[-1].lower()))

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


import logging
from multiprocessing import Pool
from functools import partial, wraps

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

# p = Pool()
# # partial()传递额外的参数
# p.apply_async(add, (3,4), callback=partial(output_result, log=log))
# p.close()
# p.join()

from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


# serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED'))
# serv.serve_forever()


from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
print('start')


# for line in yahoo.open(names='IBM,APPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


print_result = lambda x: print('Got:', x)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_hand():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{} Got: {}'.format(sequence, result))


# handler = make_hand()
# next(handler)
# apply_async(add, (2, 3), callback=handler.send)
# apply_async(add, ('helloworld', 'world'), callback=handler.send)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


@inlined_async
def test():
    print('wait')
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func

# f = sample()
# f()
