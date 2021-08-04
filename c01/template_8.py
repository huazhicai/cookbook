# -*- coding:utf-8 -*-


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []
        self.sock = None

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


from functools import partial

# conn = LazyConnection(('www.python.org', 80))
# with conn as s:
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 8192), b''))
# print(resp)

import math


# 调用父类被覆盖的方法
class A:
    def spam(self):
        print("A.spam")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.y = 1

    def spam(self):
        print('B.span')
        super().spam()


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print("getting name")
        return super().name()

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
