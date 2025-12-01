# Slicing Of Lists
l1 = [3,8,1,0,4,9,7,3,6]

print(l1[1:6:1])        # [8, 1, 0, 4, 9]
# starts from 1 and ends on 5. 6 is excluded

print(l1[2:7:2])        # [1, 4, 7]

"""
l1[2:7:1]
it means l1[startingIndex : endingIndex(excluded) : Steps/jumps]
"""

# Concatenation of Lists
l1 = [1, 7, 2]
l2 = [0, 5]

# concatination operator (+)
print(l1 + l2)      # [1, 7, 2, 0, 5]
print(l2 + l1)      # [0, 5, 1, 7, 2]

# Repetition of lists
l3 = [6, 3]

# using(*)
print (l3 * 3)      # [6, 3, 6, 3, 6, 3]

# append()
# adds as item to the end of list

fruits =["Mango", "Apple", "Orange"]
print(fruits)

# print(fruits.append("Banana"))     # None
# it will append but not return so the correct way is bellow

fruits.append("Banana")
print(fruits)

# insert
"""
Adds an element before the specified index
Syntax: list.insert(index,item)
"""

colours = ["Red", "Yellow", "Green"]
print(colours)      # ['Red', 'Yellow', 'Green']

colours.insert(2,"Blue")
print(colours)      # ['Red', 'Yellow', 'Blue', 'Green']