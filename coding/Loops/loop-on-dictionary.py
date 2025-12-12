# LOOPING THROUGH A DICTIONARY
# Definition: items() returns key-value pairs.
# Syntax:
#   for key, value in dictionary.items():


print("\nDICTIONARY LOOP example")
person = {"name": "Alice", "age": 25, "city": "Paris"}

# for only key
for key in person:
    print(key)

# for only values
for value in person.values():
    print(value)


# for both key and value
for key, value in person.items():
    print(key, ":", value)





    