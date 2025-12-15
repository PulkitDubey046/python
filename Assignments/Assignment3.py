# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python

# Task 1: Calculate Factorial Using a Function

"""
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = factorial(num)
    print(f"Factorial of {num} is: {fact}")



# Task 2: Using the Math Module for Calculations
"""
Problem Statement: Write a Python program that:
    1.  Asks the user for a number as input.
    2.  Uses the math module to calculate the:
        a. Square root of the number
        b. Natural logarithm (log base e) of the number
        c. Sine of the number (in radians)
    3.  Displays the calculated results.
"""

import math

num = int(input("Enter a number: "))
print(f"Square root of {num}: {math.sqrt(num)} ")
print(f"Logrithm of {num}: {math.log(num)}")
print(f"Sine of {num}: {math.sin(num)}")