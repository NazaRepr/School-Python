# Jace Sperry

total_correct = 0

question_01 = input("What is my favorite Language? ")
question_02 = input("What is my favorite Package Manager? ")
question_03 = input("What is my favorite Package? ")

if question_01 == "Javascript":
    print("Correct")
    total_correct += 1
else:
    print("Incorrect")

if question_02 == "NPM":
    print("Correct")
    total_correct += 1
else:
    print("Incorrect")

if question_03 == "TailwindCSS":
    print("Correct")
    total_correct += 1
else:
    print("Incorrect")

print(f"You got {total_correct} correct")
