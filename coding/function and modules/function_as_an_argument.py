# In python we can pass a function as an argument to another function.

def add_1(number):
    return number+1

print(add_1(4))

def square(number):
    return number ** 2

print(square(4))

num=int(input("Enter a number: "))
res=square(add_1(num))
print(res)

