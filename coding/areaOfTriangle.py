# Find the area of a triangle given side lengths a, b, and c using Heron's formula

import math
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))    
c = float(input("Enter length of side c: "))
s = (a + b + c) / 2  # semi-perimeter

area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("The area of the triangle is:", round(area, 2))