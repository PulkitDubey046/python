import random

# random.randint(a, b) returns a random integer N such that a <= N <= b
# random() returns a random float in the range [0.0, 1.0) 
print(random.randint(10,15))

# from random sequence
# choice(sequence) => returns a random items from the sequence

nums=[10, 4, 5, 2, 19, 7]
print(random.choice(nums))

# shuffle list
# shuffle(sequence) => returns the elements shuffled in random order

fruits=["Apple", "Mango", "Orange"]
random.shuffle(fruits)
print(fruits)
