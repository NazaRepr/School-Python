# Jace Sperry

num1 = float(input("Choose a num: "))
num2 = float(input("Choose a num: "))
num3 = float(input("Choose a num: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
