# WAP to understand arithmetic operators
n1=11
n2=3

result = n1**n2 # 11 to the power 3 (11 cube)
print("1. ** -> Raise to(Exponent/Power)")
print(n1,"raise to",n2,"=",result)
# formatted string -> fstring ->open only quote 1 time
print(f"{n1} raise to {n2} ={result}")

print()
print("2.* -> Multiplication")
result = n1*n2
print(f"{n1}*{n2}={result}")

print()
print("3. /-> Decimal quotient")
result = n1/n2
print(f"{n1}/{n2}={result}")

print()
print("4. //-> Integer quotient")
result = n1//n2
print(f"{n1}//{n2}={result}")

print()
print("5. %-> Modulus Remainder")
result = n1%n2
print(f"{n1}%{n2}={result}")

print()
print("6. /-> Adition")
result = n1+n2
print(f"{n1}+{n2}={result}")

print()
print("7. - ->  Substraction")
result = n1-n2
print(f"{n1}-{n2}={result}")


