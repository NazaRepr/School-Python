# Jace Sperry

invetment = int(input("Enter investment amount: "))
years = int(input("Enter number of years: "))
annual_return = float(input("Enter annual return: "))

for i in range(years):
    invetment += invetment * annual_return / 100
    print(f"Year {i+1}: ${invetment:.2f}")
