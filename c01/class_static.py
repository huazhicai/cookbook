# -*- coding:utf-8 -*-

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month < 13 and year <= 3000


class ClassMethod(object):

    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner=None):
        print(instance)
        print(owner)
        if owner is None:
            owner = type(instance)

        def newfunc(*args):
            return self.f(owner, *args)

        return newfunc


class F(object):
    def f(cls, x):
        return cls.__name__, x

    f = ClassMethod(f)


# F.f -> call F.f.__get__(instance, F) -> newfunc

print(F.f(3))
instance = F()


# print(instance.f(3))


class StaticMethod(object):
    # 为了使用一个描述器，需要将这个描述器的实例作为类属性放到一个类定义中
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner=None):
        print(obj)
        return self.f


class E(object):
    # @staticmethod
    def f(x):
        print(x)

    # 静态方法
    f = StaticMethod(f)


# print(E.f(4))
# print(E().f(5))


class Property(object):

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class C(object):
    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = Property(getx, setx, delx, "i'm the x property.")
