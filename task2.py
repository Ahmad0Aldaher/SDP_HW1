import contextlib
from time import time
import inspect
import io

def decorator_2(func):
    def wrap_func(*args, **kwargs):
        wrap_func.count += 1
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f' {func.__name__} call {wrap_func.count} executed in {(end_time-start_time):.4f}s')
        print('Name: \t ' + func.__name__)
        print('Type: \t' + str(type(func)))
        print('Sign: " \t' + str(inspect.signature(func)))

        print('Args: \t positional:', args)
        print('Args: \t kwarg:', kwargs)

        print('Doc: \t' + str(func.__doc__))
        print('Source: ',end='')
        i=0
        for l in inspect.getsourcelines(func)[0]:
            print('  ' if i==0 else '\t'+str(l), end='')
            i +=1
        print()
        fn= io.StringIO()
        with contextlib.redirect_stdout(fn):
            func(*args,**kwargs)
        s=fn.getvalue()
        print('Output: \t')
        for l in s.splitlines():
            print('\t'+l)

        return result
    wrap_func.count = 0
    return wrap_func


