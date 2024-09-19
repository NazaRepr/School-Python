# Jace Sperry

user_park_time = int(input("How many hours did you park today? "))
total = 0

if user_park_time <= 3:
    total = user_park_time * 2
elif user_park_time > 3:
    total = 6
    user_park_time -= 3
    total += user_park_time

print("Your total is $" + str(total))
