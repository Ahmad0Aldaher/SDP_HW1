from time import time


def decorator_1(func):
    def wrap_func(*args, **kwargs):
        wrap_func.count += 1
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f' {func.__name__} call {wrap_func.count} executed in {(end_time-start_time):.4f}s')
        return result
    wrap_func.count = 0
    return wrap_func
