'''
WAP to accept marks of 5 subject  display sum and average
based on average display grades
1. average between 100 and 90 -> A Grade
2. average between 89 and 70 -> B Grade
3. average between 69 and 50 -> C Grade
4. average between 49 and 35 -> D Grade
5. Below 35 -> Fail
'''
s1=int(input("Enter the marks of s1:"))
s2=int(input("Enter the marks of s2:"))
s3=int(input("Enter the marks of s3:"))
s4=int(input("Enter the marks of s4:"))
s5=int(input("Enter the marks of s5:"))

sum= s1+s2+s3+s4+s5
print(f"{sum} is")
average = sum /5
print(f"{average}")

if 90>= average <=100:
    print("A Grade")
elif 70>= average<=89:
    print("B Grade")
elif 50>= average<= 69:
    print("C Grade")
elif 35>= average<=49:
    print("D Grade")
else:
    print("Fail!!!")