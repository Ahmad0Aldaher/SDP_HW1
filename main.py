import random
from task1 import decorator_1
from task2 import decorator_2
#from task3 import decorator_3, function_list # uncomment when testing task3
from task4 import decorator_4, function_list #  uncomment when testing task4
from task4_1 import decorator_2_1 # task4 applied on function decorator

import cmath

# uncomment only the decorator you want to test

#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
#@decorator_2_1
def s_quad(a, b, c):
    """
    This function calculates the roots for quadratic equation
    :params a,b,c : the coefficients of the quadratic equation a^2*x+bx+c=0
    :output: the two roots of the equation
    """
    z = lambda a, b, c :((-b+cmath.sqrt((b**2-4*a*c)))/(2*a) , (-b-cmath.sqrt((b**2-4*a*c)))/(2*a))
    return z(a, b, c)


#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
#@decorator_2_1
def pascal(n):
    """
    This function draw pascal triangle
    :params n : the depth of pascal triangle
    :output: print pascal triangle
    """
    for i in range(n):
        print(' ' * (n - i), end='')
        print(' '.join(map(str, str(11 ** i))))


#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
#@decorator_2_1
def func():
    """
    This function for testing it just generate a random  number n and loop for 10*n
    """
    result = 0
    n = random.randint(10, 751)
    for i in range(n*10):
        result += (i ** 2)


#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
#@decorator_2_1
def funx(n=2, m=5):
    """
     This function for testing
    :param n: default value 2
    :param m: default value 5
     """
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(100000)]
    for i in res:
        if i > max_val:
            max_val = i


#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
#@decorator_2_1
def funh(bar1, bar2=""):
    """
    This function does something useful (just for testing)
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")
    # uncomment when testing error handling in the task4 and task4_1
    raise Exception("Sorry, some error happened")



if __name__ == "__main__":
    # demo for task 1, uncomment when testing task1
    '''
    func()
    funx()
    func()
    funx()
    func()
    '''

    # demo for task 2 , uncomment when testing task2 "remember to uncomment the raise command only for demos task4 and task4_1 "
    '''

    funh(None, bar2="")
    '''

    # demo for task 3 and task4 , uncomment when testing task3 or task4

    funx()
    funh(None, bar2="")
    func()
    s_quad(1, 1, 2)
    pascal(5)

    print("PROGRAM || RANK || TIME ELAPSED")
    sorted_funs=sorted(function_list.items(), key=lambda item: item[1])

    j=1
    for key,val in sorted_funs:
        print(key+ "\t\t" +  str(j) + "\t\t" + str(val)+"s")
        j+=1
