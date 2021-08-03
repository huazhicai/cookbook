# -*- coding:utf-8 -*-

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# @timethis
# def countdown(n):
#     pass

def countdown(n):
    pass


countdown = timethis(countdown)

# 签名信息
from inspect import signature

print(signature(countdown))

# ====================section 02

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y
