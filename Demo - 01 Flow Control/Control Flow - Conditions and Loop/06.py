# Jace Sperry

user_password = input("Please enter your password: ")

if len(user_password) < 8:
    print("Password is too short")
elif 8 <= len(user_password) <= 16:
    print("Password is medium length")
elif len(user_password) > 16:
    print("Password is too long")
