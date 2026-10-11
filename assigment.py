premium = 25000
total_discount_percent = 0

age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")
ped = input("Do you have PED? (Yes/No): ")
marital_status = input("Enter marital status (Married/Widowed/Single): ")


if age > 60:
    total_discount_percent = total_discount_percent + 5


if gender.lower() == "male":
    total_discount_percent = total_discount_percent + 5

elif gender.lower() == "female":
    total_discount_percent = total_discount_percent + 10


if age > 35 and age < 45:
    total_discount_percent = total_discount_percent + 5


if ped.lower() == "yes":
    total_discount_percent = total_discount_percent + 3


if marital_status.lower() == "widowed":
    total_discount_percent = total_discount_percent + 3


discount_amount = premium * total_discount_percent / 100
final_premium = premium - discount_amount

print("\n----- Insurance Premium Details -----")
print("Original Premium = Rs.", premium)
print("Total Discount =", total_discount_percent, "%")
print("Discount Amount = Rs.", discount_amount)
print("Final Premium to be Paid = Rs.", final_premium)