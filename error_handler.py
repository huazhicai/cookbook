# -*- coding:utf-8 -*-
import functools


def error_handler(func):
    import traceback
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except:
            msg = traceback.format_exc()
            print(msg)
            return 'error'

    return wrapper
