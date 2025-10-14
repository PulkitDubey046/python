# Employee Management System (EMS)

# Step 1: Initialize employee data dictionary with sample data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000.0}
}

# Function to display the main menu and handle user choices
def main_menu():
    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Function to add a new employee to the dictionary
def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID (unique integer): "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a new ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for Employee ID.")
            
    name = input("Enter Employee Name: ").strip()
    age = input("Enter Employee Age: ").strip()
    department = input("Enter Employee Department: ").strip()
    salary = input("Enter Employee Salary: ").strip()
    
    # Basic validation for age and salary to be integers
    try:
        age = int(age)
        salary = float(salary)
    except ValueError:
        print("Invalid age or salary. Please enter numeric values for age and salary.")
        return
    
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} added successfully.")

# Function to view all employees in a table format
def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    print("\nAll Employees:")
    print("{:<10} {:<20} {:<5} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, info in employees.items():
        print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
            emp_id, info['name'], info['age'], info['department'], info['salary']
        ))

# Function to search employee by emp_id and display details
def search_employee():
    try:
        emp_id = int(input("Enter the Employee ID to search: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for Employee ID.")
        return
    
    if emp_id in employees:
        info = employees[emp_id]
        print(f"\nEmployee ID: {emp_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Department: {info['department']}")
        print(f"Salary: {info['salary']}")
    else:
        print("Employee not found.")

# Run the EMS program
if __name__ == "__main__":
    main_menu()
