# Write a Python function to reverse a string without using slicing.

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))