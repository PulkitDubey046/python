# Calculate simple interest given principal, rate, and time

P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time in years: "))

SI = (P * R * T)/100
print("Simple Interest is ", SI)