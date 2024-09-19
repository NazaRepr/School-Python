# Jace Sperry

import random

num = int(input("Choose a number (1-10): "))
random_num = random.randint(1, 10)
attempt = 0

while True:
    num = int(input("Choose a number (1-10): "))
    if num == random_num:
        print("YOU GOT IT!")
        break
