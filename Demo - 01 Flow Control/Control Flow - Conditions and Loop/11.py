# Jace Sperry

temp = int(input("Temperature in Fahrenheit: "))

if temp > 90:
    print("Heat Warning!")
elif 32 <= temp <= 90:
    print("Temperature is Normal")
elif temp < 32:
    print("Freeze Warning!")
else:
    print("Error")
