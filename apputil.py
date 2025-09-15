import seaborn as sns
import pandas as pd


# update/add code below ...

# Exercise 1: Fibonacci Sequence Function
# Write a recursive function to compute the nth Fibonacci number in the series

def fib(n):
    ''' This function is responsible for returning the nth Fibonacci number in the series based on the input n.
        For example, if we were to call fib(3), the function would return 2. The function would first check if
        n is equal to 0 or 1, and if not, it essentially skips to the else statement, which returns the the sum of
        the two previous Fibonacci numbers, which are calculated by calling the function recursively with n-1 and n-2.
        So, in this example, the return statement would end up being fib(2) + fib(1), which is 1 + 1 = 2. Fib(2) holds 
        the value of 1 because it is calculated as fib(1) + fib(0), which is 1 + 0 = 1. Fib(1) is 1 because of the base case.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)