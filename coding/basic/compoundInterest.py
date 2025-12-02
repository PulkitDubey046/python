""" 
Calculate the Compound Interest
Amount = P(1+ R/100) ** T
CI = Amount - P
"""
    
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interese rate: "))
time = float(input("Enter time: "))
# amount1 = principal * (1 + rate/100) ** time 
amount = principal * pow((1 + rate/100),time)
print("Amount is ", round(amount))
ci = amount - principal
print("Compound Interest is ", round(ci))