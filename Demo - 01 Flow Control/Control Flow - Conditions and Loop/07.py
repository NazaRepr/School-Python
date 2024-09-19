# Jace Sperry

num_of_grocery_items = int(input("How many grocery items do you have? "))
total = 0

for i in range(num_of_grocery_items):
    item_price = float(
        input("Enter the price for item #" + str(i + 1) + ": "))

    total += item_price

print(f"Your total is ${total:.2f}")
