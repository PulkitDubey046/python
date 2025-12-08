
marks=float(input("Enter your marks: "))
if marks>50:
    print("Congrats you have passed the exam!")
    if marks>90:
        print("Grade is A.")
    elif marks>=80 and marks<90:
        print("Grade is B")
    elif marks>=70 and marks<80:
        print("Grade is C")     
    elif marks>=60 and marks<70:
        print("Grade is D")
    elif marks>=50 and marks<60:
        print("Grade is E")
else:
    print("You have Failed, study Hard next time.")