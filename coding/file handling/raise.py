# raise

salary = float(input("Enter your current salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative")
else:
    print(f"Your salary is {salary}")



age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")