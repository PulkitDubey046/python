"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

If the file exists:

"""

try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        i=0;    
        for line in file:
            i += 1
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

print("Enter text to write to the file: ")
user_input = input()
with open('output.txt', 'w') as file:
    file.write(user_input)
    print("Data successfully written to output.txt.")
with open('output.txt', 'a') as file:
    print("Enter additional text to append to the file: ")
    user_input = input()
    file.write("\n" + user_input)
with open('output.txt', 'r') as file:
    print("Final content of the file:")
    for line in file:
        print(line.strip())