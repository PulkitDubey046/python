# without recursion

def fact(num):
    factorial = 1
    while num>1:
        factorial *= num
        num-=1
    return factorial

print(fact(4))  # Output: 24


# Recursion
"""
Recursion is a process in which a function calls itself till a certain condition is met.

There are two part of recursive function:
1. Base/terminal condition
2. Recursive condition

Factorial of a number can also be calculated using recursion.
Factorial of n => n * (n-1) * (n-2) * ... * 1
"""

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))  # Output: 24