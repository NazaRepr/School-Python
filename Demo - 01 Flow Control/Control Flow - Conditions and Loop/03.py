# Jace Sperry

age = int(input("How old are you? "))

if age < 12:
    print("Ticket is $5")
elif 12 <= age <= 64:
    print("Ticket is $10")
elif age > 64:
    print("Ticket is $7")
else:
    print("Error")
