from time import time
import inspect


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

            # print("Args: "+str(inspect.getargs(func)))

            print("Doc: " + str(func.__doc__))
            #print("Name: "+ str(inspect.getargs(func)))
            print("Source: "+inspect.getsource(func))
            return result
        except Exception as e:
            f = open(f'log_{func.__name__}.txt', 'w')
            f.write(str(e))
            f.close()

    wrap_func.count = 0
    return wrap_func

