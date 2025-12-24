# wt mode : "wt" and "w" behave the same in practice, because text mode is default.
# Text mode automatically handles newline conversion (\n ↔ platform-specific line endings).
# creates a new file if file does not exist 

f = open("example.txt", "wt")
f.write("Hello, universe\n")
f.close()