# Jace Sperry

temp = int(input("Temperature in Fahrenheit: "))
celsius_temp = ((temp-32)*5)/9

if celsius_temp < 0:
    print("Below Freezing")
elif celsius_temp > 100:
    print("Very Hot")
else:
    print("Temperature is Moderate")
