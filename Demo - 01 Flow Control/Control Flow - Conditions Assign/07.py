# Jace Sperry
num1 = float(input("First Num: "))
operator = input("Operator: ")
num2 = float(input("Second Num: "))

if operator == "+":
    print(f"{num1 + num2}")
elif operator == "-":
    print(f"{num1 - num2}")
elif operator == "*":
    print(f"{num1 * num2}")
elif operator == "/" and num1 != 0 and num2 != 0:
    print(f"{num1 / num2}")
else:
    print(f"Error")
