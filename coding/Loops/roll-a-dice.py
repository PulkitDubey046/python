import random

print("Welcome to the game of rolling a dice.")
while True:
    choice = input("Press 'Enter' to roll a dice or q to quit.")
    if choice=='q':
        print("Thankyou for playing the game.")
    elif choice=='':
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll} .")
    else:
        print("Invalid input!!")