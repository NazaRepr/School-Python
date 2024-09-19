# Jace Sperry

num1 = int(input("Choose a number: "))  # 5
num2 = int(input("Choose a number: "))  # 7
num3 = int(input("Choose a number: "))  # 3

if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 < num2 or num3 < num1 and num3 > num2:
    print(num3)
else:
    print("Error")
