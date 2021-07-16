# -*- coding:utf-8 -*-


class Foo:
    def __init__(self, item):
        self.item = item

    def __eq__(self, other):
        print('使用了equal函数对象的id', id(self))
        if isinstance(other, self.__class__):
            print(self.__dict__)
            return self.__dict__ == other.__dict__
        else:
            return False

    def __hash__(self):
        print('f' + str(self.item) + '使用了hash函数')
        return hash(self.item)


f1 = Foo(1)
f2 = Foo(2)
f3 = Foo(3)
fset = set([f1, f2, f3])
print(fset)
print()
f = Foo(3)
fset.add(f)
print('f3的id:', id(f3))
print('f的id:', id(f))
