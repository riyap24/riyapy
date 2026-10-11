#4. WAP to check whether the number is divisible by 5 or not

num =int(input("Enter the number:"))

remainder =num % 5
if remainder==0:
    print(f"The {num} is divisible by 5")
    
else:
    print(f"The {num} is not divisible by 5")
