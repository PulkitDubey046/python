# Lamda Function
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not going to be reused elsewhere.
# They are defined using the lambda keyword instead of the def keyword.
# Syntax:
# lambda arguments: expression


"""
def add(a):
    return a+1

res = add(1)
print(res)
"""

fun = lambda a : a+1
res = fun(2)
print(res)

fun1 = lambda a, b : a+b
res = fun1(2, 3)
print(res)