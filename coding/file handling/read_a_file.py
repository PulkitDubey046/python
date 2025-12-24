# rt mode = Read text. File must exist.

fh = open("example.txt", "rt")

# read() => reads the content of the file as str
# content = fh.read()
# content = fh.read(10) # this reads first 10 characters of file

# readline() => reads single line
# line1 = fh.readline()
# line2 = fh.readline()
# line3 = fh.readline()
# line4 = fh.readline() # empty string

# readlines()
lines = fh.readlines()

fh.close()

# print(content)
# print(type(content))

# print(f"Line1: {line1} ")
# print(f"Line2: {line2} ")
# print(f"Line3: {line3} ")
# print(f"Line4: {line4} ")

# print(f"Lines: {lines}")
for line in lines:
    print(line.strip())  # to remove \n at the end of each line
