#10. Find LCM of two numbers
import math

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a==0 or b==0:
    lcm = 0
else:
    lcm = abs(a*b) // math.gcd(a , b)
    
print("Lcm:", lcm)