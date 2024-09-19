user_input = ""
while not user_input in ["1", "2"]:
    user_input = input("Enter a 1 or 2: ").split()
print("Thank You")
print(user_input)

num = 100

while num > 0:
    print(num)
    num //= 2
