# Jace Sperry

grade = int(input("How many did you get correct? "))
total = int(input("How many total questions are there "))
percentage = (grade / total) * 100

if percentage >= 90:
    print(f"Your grade is an A")
elif percentage >= 80:
    print("Your grade is a B")
elif percentage >= 70:
    print("Your grade is a C")
elif percentage > 60:
    print("Your grade is a D")
elif percentage <= 60:
    print("Your grade is a F")
else:
    print("Error")
