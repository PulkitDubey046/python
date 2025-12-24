# fh= open("practice1.txt","rt")
# contents = fh.read()
# fh.close()
# print(contents)

"""
with open("practice.txt", "rt") as fh:
    contents = fh.read()

print(contents)
"""

with open("practice1.txt", "rt") as fh:
    fh.write("New file creation\n")
    fh.write("Bye")

