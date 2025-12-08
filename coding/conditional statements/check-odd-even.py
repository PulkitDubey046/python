# Print if a number(int) is odd or EvenPrint if a number(int) is odd or Even
# Even - when the number is divisible by 2. remainder is 0
# Odd - when the number is not divisible by 2. remainder is not 0.

num = int(input("Enter number to check even or odd: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")