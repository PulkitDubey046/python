# FOR LOOP
# Definition: Used to iterate over a sequence (list, string, range, etc.)
# Syntax:
#   for variable in sequence:
#       code block

print("FOR LOOP: range(5)")
for i in range(5):     # range(5) → 0 to 4
    print(i, end=' ')  

print("\nFOR LOOP: iterating through a list")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:   # loops over each item in the list
    print(fruit)

print("\nFOR LOOP: iterating through a string")
for char in "hello":   # loops through each character
    print(char)
