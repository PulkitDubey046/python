from pathlib import Path
file_path = Path("C:/Users/SILICON/Desktop/coding/python/coding/file handling/example-1.txt")
# in file_path use forward slash(/) instead of the back slash(\). 
if file_path.exists():
    print("The file exists. Cannot create!")
else:
    print("The file does not exist, creating it")
    fh= open(file_path,'xt')
    fh.write("Some Content")
    fh.close()
