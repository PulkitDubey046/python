# User defined function in Python
# Syntax:
# def function_name(parameters):
#     """docstring"""
#     function_body
#     return value

# Example 1: Function without parameters and return value
def greet():
    """Function to greet the user"""
    print("Hello! Welcome to the Python world.")

greet()  # Calling the function

# Example 2: Function with parameters and return value
def add(a, b):
    """Function to add two numbers"""
    return a + b
result = add(5, 3)  # Calling the function with arguments
print(f"Sum: {result}")

# Example 3: Function with default parameter
def power(base, exponent=2):
    """Function to calculate power of a number"""
    return base ** exponent
print(f"Power: {power(4)}")        # Uses default exponent
print(f"Power: {power(2, 3)}")     # Uses provided exponent

# Example 4: Function with variable-length arguments
def multiply(*args):
    """Function to multiply multiple numbers"""
    result = 1
    for num in args:
        result *= num
    return result

print(f"Product: {multiply(2, 3, 4)}")  # Calling the function with multiple arguments