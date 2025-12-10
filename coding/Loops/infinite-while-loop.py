correct_password = "Python"


while True:     # infinite loop
    user_password = input("Enter your password: ")
    if user_password == "Python":
        print("Password is correct! Congress")
        break
    else:
        print("Wrong Password, try again..")

print("Logged in!!!")