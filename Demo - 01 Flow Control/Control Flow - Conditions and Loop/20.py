# Jace Sperry

while True:
    coffee = input(
        "What kind of coffee would you like? (latte, cappuccino, or espresso) ").lower().strip()
    if coffee == "latte":
        print(f"Preparing your coffee...")
        break
    elif coffee == "cappuccino":
        print(f"Preparing your coffee...")
        break
    elif coffee == "espresso":
        print(f"Preparing your coffee...")
        break
    else:
        print("Invalid section.")
print(f"Here is your {coffee} ☕")
