# Common built-in functions in Python

# print() - outputs text to console
print("Hello, World!")

# len() - returns length of a sequence
text = "Python"
print(len(text))

# type() - returns the type of an object
print(type(42))
print(type("string"))

# int(), str(), float() - type conversions
print(int("10"))
print(str(100))
print(float("3.14"))

# range() - generates a sequence of numbers
for i in range(5):
    print(i)

# sum() - adds items in an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# max(), min() - returns largest/smallest value
print(max([3, 1, 4, 1, 5]))
print(min([3, 1, 4, 1, 5]))

# abs() - returns absolute value
print(abs(-10))

# round() - rounds to nearest integer
print(round(3.7))

# sorted() - returns sorted list
print(sorted([3, 1, 4, 1, 5]))

# all(), any() - checks conditions on iterables
print(all([True, True, True]))
print(any([False, False, True]))

# enumerate() - loops with index
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

# zip() - combines multiple iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))

# map() - applies function to all items
print(list(map(str.upper, ['hello', 'world'])))

# filter() - filters items based on condition
print(list(filter(lambda x: x > 2, [1, 2, 3, 4, 5])))