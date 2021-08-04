# -*- coding:utf-8 -*-


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # 描述符赋值给类属性， cls.name=Typed(name, expected_type)
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# @typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name  # 赋值调用Stack.name.__set__('apple')
        self.shares = shares
        self.price = price


Stock = typeassert(name=str, shares=int, price=float)(Stock)
s = Stock('apple', 12, 13)


class D(object):
    def f(self, x):
        return x


d = D()
print(D.__dict__['f'])  # Stored internally as a function

print(D.f)  # Get from a class becomes an unbound method

print(d.f)
