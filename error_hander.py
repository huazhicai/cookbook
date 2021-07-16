import functools


def error_handler(func):
    import traceback
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            msg = traceback.format_exc()
            print(msg)
            return 'error'

    return wrapper
