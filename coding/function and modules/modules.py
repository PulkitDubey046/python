# Python built-in Modules
# A module is a file containing Python code. It can define functions, classes, and variables.
# A module can also include runnable code.
# Grouping related code into a module makes the code easier to understand and use.
# It also makes the code logically organized.
# Python has a large standard library of built-in modules that you can use.

# To use a module, you need to import it using the import statement.
# Syntax:
# import module_name

# some commonly used built-in modules are:
# math module - provides mathematical functions
import math
print(math.sqrt(16))  # Output: 4.0

# random module - provides functions for generating random numbers
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

# datetime module - provides classes for manipulating dates and times
import datetime
print(datetime.datetime.now())  # Output: Current date and time

# os module - provides functions for interacting with the operating system
import os
print(os.getcwd())  # Output: Current working directory

# sys module - provides access to system-specific parameters and functions
import sys
print(sys.version)  # Output: Python version information

# You can also create your own modules by saving Python code in a .py file and importing it in another Python file.
# For example, if you have a file named my_module.py with the following code:
# def greet(name):
#     return f"Hello, {name}!"
# You can import and use it in another file like this:
# import my_module