# x mode => create a file
fh = open("file1.txt", "x")  # opening a file in create mode
# after creating one file we can't run this statement again
# if we try to do it again it will give us error

# writing some content to the file
# write(content)

fh.write("This file is created using the 'x' mode in Python.\n")
fh.write("Next line.")

# close the file
fh.close()

# after closing the file we can't write again this will give us error
# fh.write("I am the best")  # ValueError: I/O operation on closed file.