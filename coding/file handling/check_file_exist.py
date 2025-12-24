# os.path.exists()
# import os
# file_path = 'example.txt'
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exists.")
# else:
#     print(f"The file '{file_path}' does not exist.")

# os.path.isfile()
# import os
# file_path = 'C:/Users/SILICON/Desktop/coding/python/coding/file handling/example.txt'
# # in file_path use forward slash(/) instead of the back slash(\). 
# if os.path.isfile(file_path):
#     print(f"'{file_path}' is a file.")
# else:
#     print(f"'{file_path}' is not a file.")


# pathlib.Path.exists()

from pathlib import Path
file_path = Path("C:/Users/SILICON/Desktop/coding/python/coding/file handling/example1.txt")
# in file_path use forward slash(/) instead of the back slash(\). 
if file_path.exists():
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

