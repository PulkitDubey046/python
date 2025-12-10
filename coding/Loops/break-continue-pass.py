# CONTROL STATEMENTS INSIDE LOOPS
# break    = stops the loop immediately.
# continue = skips current iteration and jumps to next.
# pass     = does nothing (placeholder).
# ------------------------------------------------------------

print("\nBREAK example")
for i in range(10):
    if i == 5:
        break          # loop ends when i reaches 5
    print(i)

print("\nCONTINUE example")
for i in range(5):
    if i == 2:
        continue       # skips printing 2
    print(i)

print("\nPASS example")
for i in range(3):
    pass               # placeholder, no action
print("PASS loop finished")