name ="John"
age=20
percent =85.5

student = ["John", 20, 85.5]
print(type(student))    # <class 'list'>
print(student)          # ['John', 20, 85.5]

"""
Lists can contain anytype of data.
It is used when you want to store collection of data in a single variable.
Lists are always in a order similar to array.
"""

days_of_week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
# Posetive indexing : 0     1      2     3     4     5     6
# Negative indexing : -7    -6    -5    -4    -3    -2    -1

print(days_of_week[0])      # Mon
print(days_of_week[4])      # Fri

print(f"last day of the week is {days_of_week[6]}") #by posetive indexing
# last day of the week is Sun

print(f"last day of the week is {days_of_week[-1]}") #by negative indexing
# last day of the week is Sun

# Length of a list : The number of items/elements in the list
print(len(days_of_week))        # 7

# print(days_of_week[8])
# IndexError: list index out of range

