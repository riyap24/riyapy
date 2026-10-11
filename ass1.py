premium = 250000
total_discount_percent = 0

age = int(input("Enter your age:"))
gender = input("Enter your gender(Male/Female):").strip().lower()
ped = input("Do you have any pre-existing disease?(Yes/No):").strip() .lower()

# senior citizen
if age > 60:
    total_discount_percent += 5
    
    #discount based on gender
    if gender == "Male":
        if 35 < age < 45:
         total_discount_percent += 5
        if ped =="Yes":
            total_discount_percent += 3
            
elif gender == "Female":
    if 35 < age < 45:
        total_discount_percent += 10
    if ped =="Yes":
        total_discount_percent += 5
        
    #widow discount
    widow = input("Are you a widow?(Yes/No):").strip() .lower()
    if widow =="Yes":
        total_discount_percent += 3
else:
    print("Invalid input for gender. Pkease enter 'Male' or 'Female'")    
    exit()
    
discount_amount = premium * total_discount_percent/100
final_premium = premium - discount_amount

print("\n-------Insurance Premium Details-------")
print("Original premium: rs.",premium)
print("Total discount percent:","%")
print("Discount Amount: rs.",discount_amount)
print("Final premium to be paid: rs.",final_premium)
        