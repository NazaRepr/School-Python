# write a function that prompts the user for a 1 or 2
# if the user types anything else, report the error and ask again.
# once you have a 1 or 2, return the value.

# eg.
# choice = get_one_or_two()

def get_one_or_two():
    choice = input("1 or 2: ").strip()
    if choice == "1":
        print(f"{choice}")
        return 1
    elif choice == "2":
        print(f"{choice}")
        return 2
    else:
        print(f"Error: '{choice}' is not 1 or 2")
        return get_one_or_two()


get_one_or_two()
