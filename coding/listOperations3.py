"""
reverse()
sort()
count()
Membership operation
"""

days_of_week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
print(days_of_week)
# reverse()
days_of_week.reverse()
print(days_of_week)


nums = [4, 9, 0, 1, 2, 8]
print(nums)
# sort()
nums.sort()
print("Sorted list: ", nums)
nums.sort(reverse=True)  # decending order
print("Sorted list: ", nums)


# count()
numbers = [0, 1, 3, 4, 1, 0]
print(numbers.count(1)) 
# it will count the number of item persent in the above lists not whole item


numbers = [10, 4, 5.5, 7, 1]
print(numbers)

# Smallest number in the list
# min()
print(f"Smallest number: {min(numbers)}")

# Biggest number in the list
# max()
print(f"Biggest number: {max(numbers)}")


# List inside a list (Nested List)
l1 = [5, 1.5, "Python", [1, 2]]
print(l1)
print(l1[3]) # list inside list
print(l1[-1][-1])