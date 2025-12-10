# LOOP WITH ELSE
# Definition: The else block runs ONLY if the loop finishes normally
# (not stopped by break).
# Syntax:
#   for/while loop:
#       ...
#   else:
#       ...


print("\nFOR LOOP with ELSE")
for i in range(3):
    print(i)
else:
    print("Loop ended without break")

print("\nWHILE LOOP with ELSE")
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While loop ended normally")
