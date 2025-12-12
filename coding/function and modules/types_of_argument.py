def add(a, b):
    return a + b

# positional agrument - passing the argument in order of their position
result = add(10, 4)
print(result)

# Default arguments
def sub(a, b=2):
    return a-b

result= sub(10, 5)
print(result)

result= sub(10)
print(result)

# keyword argument

def multi(a, b, c):
    print(f"a:{a}, b:{b}, c:{c}")
    return a*b*c

result= multi(a=1, c=4, b=5)
print(result)