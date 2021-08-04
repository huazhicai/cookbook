# -*- coding:utf-8 -*-
"""
当一个描述器被放入一个类的定义时， 每次访问属性时它的 __get__() 、__set__() 和 __delete__() 方法就会被触发。
"""
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)  # 缓存值
            return value


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    # area = lazyproperty(area)  # 类属性area指向一描述符

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.area)  # call Circle.area.__get__(c, Circle）  area=lazyproperty(area)
print(c.area)
