# __name__.py
# The __name__ variable in Python is a special built-in variable that represents the name of the current module.
# When a Python file is run directly, the __name__ variable is set to "__main__".
# However, when the same file is imported as a module in another file, the __name__ variable is set to the name of the module.

def greet():
    print("Hello, universe")

if __name__ == "__main__":
    greet()
