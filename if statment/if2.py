# WAP to check whether the number is divisible by 2 or not
# Divisible by 2 -> Divide the number by 2 and 
    #  check remainder (%)
    # if remainder is 0 -> Number is divisible by 2
    # if remainder is not 0 -> Number is not divisible by 2
# Input = 1, conditions = 2 (if else)

num=int(input("Enter a number:"))

remainder = num%2
if remainder == 0:
    print(f"Number = {num} is divisible by 2")
    print(f"Number = {num} is even")

else:
    print(f"Number = {num} is not divisible by 2")
    print(f"Number = {num} is odd")
