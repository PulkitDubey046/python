# range() - built-in function used to generate a sequence of numbers.
# Syntax: 
# 1. range(start, stop, step)
#         - start: starting number (inclusive, default is 0)
#         - stop: ending number (exclusive)
#         - step: increment (default is 1)

# 2. range(stop) 
#         - starts from 0 to stop-1

# 3. range(start, stop)
#         - starts from start to stop-1



print("RANGE FUNCTION examples")
print("range(5):", list(range(5)))          # 0 to 4
print("range(2, 7):", list(range(2, 7)))    # 2 to 6
print("range(1, 10, 2):", list(range(1, 10, 2)))  # odd numbers from 1 to 9 

# range with loops
# Syntax:
# for i in range(start, end, step):
#       // loop statements

for i in range(1,11):
    print(i, end=' ')