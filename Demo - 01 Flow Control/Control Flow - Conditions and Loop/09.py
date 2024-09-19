# Jace Sperry

percentage = int(input("What is your percentage? "))

if percentage < 50:
    print("You need to work harder!")
elif 50 <= percentage < 75:
    print("You're doing okay, but there's room for improvement")
elif percentage >= 75:
    print("Great job!")
else:
    print("Error")
