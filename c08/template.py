# -*- coding:utf-8 -*-

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('-'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


# c = C()


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        print('get name')
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


p = Person('seven')
print(p.name)


class SubPerson(Person):
    """
    为了委托给之前定义的setter方法，
    需要将控制权传递给之前定义的name属性的 __set__() 方法。
    不过，获取这个方法的唯一途径是使用类变量而不是实例变量来访问它。
    这也是为什么我们要使用 super(SubPerson, SubPerson)
    """

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Guido')


# print(s.name)


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('getting name')
        return super().name


class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print('setting name to ', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)
