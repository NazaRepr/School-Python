# Jace Sperry

user_age = int(input("How old are you? "))

if user_age >= 18:
    print("Access Granted")
elif 13 <= user_age <= 17:
    print("Access with supervision")
else:
    print("Access Denied")
