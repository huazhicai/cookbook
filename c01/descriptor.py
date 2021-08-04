# -*- coding:utf-8 -*-
from datetime import datetime

import requests
import traceback


class Descriptor:
    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return 'desc'

    def __set__(self, instance, value):
        print(instance)
        print(value)

    def __delete__(self, instance):
        print(instance)


class A:
    a = Descriptor()


instance = A()

# del instance
# del instance.a

# print(instance.a)
# print(A.a)

# A().a = 5
# A.a = 5


from retrying import retry

# @retry(stop_max_attempt_number=5, stop_max_delay=1000, wait_random_min=1000, wait_random_max=5000)
# def run():
#     print('start')
#     raise NameError
#
# if __name__ == '__main__':
#     try:
#         run()
#     except BaseException as e:
#         print(e)
