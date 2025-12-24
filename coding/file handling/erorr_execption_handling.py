"""
1. Compile time Error Exception => Syntax error & Indentation error
2. Execeptions =>  errors during execution
"""

# age = 22
# if age>=18:
# print("You are an adult ") # Indentation error

# print(10/0)

# x=100
# result=x+y


# How to handle exception? => try-except block


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
    print(result)

except ZeroDivisionError:
    print("You cannot divide a number by zero")

except ValueError:
    print("Input should be digits.")