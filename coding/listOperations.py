"""
extend()
remove()
pop()
"""

# extend
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.extend(["Banana", "Grapes"])
print(fruits)
print(len(fruits))


# remove()
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.remove("Mango")
print(fruits)

"""
fruits.remove("Banana")
ERROR: list.remove(x): x not in list
"""

# Pop
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.pop(1) # if you not give the index last index will be deleted
print(fruits)
