from time import time
import inspect
from datetime import datetime


def decorator_2_1(func):
    def wrap_func(*args, **kwargs):
        wrap_func.count += 1
        start_time = time()
        try:
            result = func(*args, **kwargs)
            end_time = time()
            print(f' {func.__name__} call {wrap_func.count} executed in {(end_time - start_time):.4f}s')

            print("Name: "+func.__name__)
            print("Type: "+ str(type(func)))
            print("Sign: "+str(inspect.signature(func)))

            print("Doc: " + str(func.__doc__))
            print("Source: "+inspect.getsource(func))
            return result
        except Exception as e:
            f = open(f'log_{func.__name__}.log', 'w')
            f.write(f'{datetime.strftime(datetime.now(), f"%y-%m-%d %H:%M:%S: ")}function {func.__name__} {e}')
            f.write(str(e))
            f.close()

    wrap_func.count = 0
    return wrap_func

