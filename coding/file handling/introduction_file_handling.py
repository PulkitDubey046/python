# opening a file in python
# open(file_name, mode_to_open_file)
# modes: 'r' - read, 'w' - write, 'a' - append, 'b' - binary, 'x' - create, 't' - text, 'r+' - read and write
# default mode is 'r' - read

file_handler = open("practice.txt", "rt")  # opening a file in read mode 
print(file_handler)

# Reading from a file
content = file_handler.read()  # read the entire content of the file
print(content)

file_handler.close()  # closing the file
