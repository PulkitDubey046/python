# scope of variable

n=1 # global variable
def func():
    n=2 # local variable
    print("inside function:",n)

func()
print("outside function:",n)