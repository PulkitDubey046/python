import random

print("Wellcome to Guessing a number Game...")
num=random.randint(1,100)
chance=10
while chance>=0:
    guess=int(input("Guess the number hint it is between 1 to 100: "))
    if guess == num:
        print(f"Winner.. you have taken {11-chance} tries.")
        print(f"The number was: {num}")
        break
    elif guess>num:
        print(f"Your guess is Wrong.. \n Try lower. \n {chance} tries remaining..")
        chance-=1
    else:
        print(f"Your guess is Wrong.. \n Try higher. \n {chance} tries remaining..")
        chance-=1
else:
    print("Lost..")