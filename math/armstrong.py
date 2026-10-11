#8. Check Armstrong number
num = int(input("Enter a number:"))
digits = str(num)
total = 0

for digit in digits:
    total += int(digit)** len(digits)
    
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")