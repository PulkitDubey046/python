def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add, sub, mul = arithmetic_operations(num1, num2)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")