# Jace Sperry

attempt = 0

while True:
    if attempt >= 3:
        print("Card Locked")
        break

    user_pin = int(input("Enter your pin: "))

    if user_pin == 1234:
        print("Access Granted")
        break
    else:
        attempt += 1
        print("Access Denied")
