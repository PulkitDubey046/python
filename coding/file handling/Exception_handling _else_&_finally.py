try:
    fh= open('example10.txt', 'rt')
    data = fh.read()
    fh.close()
except FileNotFoundError as file_error:
    print("File not found. Please check the file path.")
    print(file_error)

else:
    print("File read successfully.\n")
    print(data)

finally:
    print("\nExecution completed. This block runs regardless of exceptions.")