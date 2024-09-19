# Jace Sperry

monthly_income = float(input("Enter your monthly income: "))
monthly_rent = float(input("Enter your monthly rent: "))
monthly_grocery = float(input("Enter your monthly grocery bill: "))

if (monthly_grocery + monthly_rent) < monthly_income:
    print("You are saving money")
elif (monthly_grocery + monthly_rent) > monthly_income:
    print("You are not saving money")
