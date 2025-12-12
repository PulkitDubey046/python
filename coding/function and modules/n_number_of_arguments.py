# *args - variale length positional arguments (0 to n)

def add(*args):
    print(args)
    return sum(args)

result=add(10,20,4,5)
print(result)

def s(*num):
    print(num)
    return sub(num)

result=s(10,20)
print(result)