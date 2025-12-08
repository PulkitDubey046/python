"""
>=90         grade A
80 and 89    grade B
70 and 79    grade C
60 and 69    grade D
50 and 59    grade E    
<50          grade F
"""

# if-elif-else

marks=float(input("Enter your marks: "))
if marks>90:
    print("Grade is A")
elif marks>=80 and marks<90:
    print("Grade is B")
elif marks>=70 and marks<80:
    print("Grade is C")     
elif marks>=60 and marks<70:
    print("Grade is D")
elif marks>=50 and marks<60:
    print("Grade is E")
else:
    print("Grade is F")