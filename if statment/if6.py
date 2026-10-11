# WAP to accept 3 sides of triangle and check whether the triangle is
# 1. Equilateral : All sides are equal -> and
# 2. Isoceles: Any 2 sides are equal -> or
# 3. Scalene: No sides are equal -> else

s1 =int(input("Enter the side 1:"))
s2 =int(input("Enter the side 2: "))
s3 =int(input("Enter the side 3:"))

if s1==s2 and s2==s3:
    print("Equilateral Triangle")
    
elif s1==s2 or s2==s3 or s1==s3:
    print(" Isoceles Triangle")
else:
    print(("Scalene Triangle"))