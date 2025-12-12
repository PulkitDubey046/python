user = {
    "username": "my_user",
    "password": "my_password",
    "email": "my_email@example.com",
    "address": "123 Main St",
    "country": "USA"
}

sensetive_info = ["password", "address", "phone"]

# for i in user:
#     if i in sensetive_info:  # RuntimeError: dictionary changed size during iteration
#         user.pop(i)
# print(user)


for i in sensetive_info:
    if i in user:
        print(f"Deleted => Key: {i}, value:{user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")

print(user)



for key in list(user.keys()):
    if key in sensetive_info:
        user.pop(key)

print(user)
