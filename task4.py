import contextlib
import inspect
import io
from time import time

function_list={}


class decorator_4:
    #function_list = {}
    def __init__(self, func):
        # global function_list
        self.function = func
        self.count = 0
        self.time = 0.0

    def __call__(self, *args, **kwargs):
        start_time = time()
        try:
            result = self.function(*args, **kwargs)
            end_time = time()
            self.time = end_time - start_time
            self.count += 1
            function_list[self.function.__name__] = self.time
            # print(f' {self.function.__name__} call {self.count} executed in {(self.time):.4f}s')
            f = open(f'{self.function.__name__}.txt', 'w')
            f.write('Name: \t' + self.function.__name__)
            f.write('Type: \t' + str(type(self.function)))
            f.write('Sign: \t' + str(inspect.signature(self.function)))
            # print("Args: "+str(inspect.getargs(func)))
            f.write('Doc: \t' + str(self.function.__doc__))
            # print("Name: "+ str(inspect.getargs(func)))
            # f.write("Source: " + inspect.getsource(self.function))

            f.write('Args: \t positional:' + str(args))
            f.write('Args: \t kwarg:' + str(kwargs))

            f.write('Source: ' + '\n')
            i = 0
            for l in inspect.getsourcelines(self.function)[0]:
                f.write('  ' if i == 0 else '\t' + str(l) + '\n')
                i += 1
            fn = io.StringIO()
            with contextlib.redirect_stdout(fn):
                self.function(*args, **kwargs)
            s = fn.getvalue()
            f.write('Output: \t')
            for l in s.splitlines():
                f.write('\t' + l)

            f.close()
            return result
        except Exception as e:
            f = open(f'log_{self.function.__name__}.log', 'w')
            f.write(str(e))
            f.close()




