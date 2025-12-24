# 'a' mode => Append mode: Open the file for writing, but does not overwrite existing content.
# If the file does not exist, it creates a new file.

fh = open("practice.txt", "at")
fh.write("\nJai shree ram.")
fh.write("\nRadhe Radhe !!!")

fh.close()