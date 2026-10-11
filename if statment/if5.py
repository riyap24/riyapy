'''
5. WAP to check whether the number is less than 18 or not
    if less than 18 display 
    your age = {age} is below 18 you are not eligible for license
    if greater than or equal to 18 then display 
    your age = {age} is above or equal to 18 you are eligible for license
'''

age=int(input("Enter a number:"))

if age<=18:
    print(f"Your age = {age} is below 18 you are not eligible for lisense")
    
else:
    print(f"your age={age} is above or equal to 18 you are eligible")
    
