# Jace Sperry

int = int(input("Input a Number: "))

if int % 5 == 0 and int % 7 == 0:
    print("Divisible by Both")
elif int % 5 == 0 and int % 7 != 0:
    print("Devisable by 5")
elif int % 5 != 0 and int % 7 == 0:
    print("Divisible by 7")
elif int % 5 != 0 and int % 7 != 0:
    print("Not devisable by 5 or 7")
else:
    print("Error")
