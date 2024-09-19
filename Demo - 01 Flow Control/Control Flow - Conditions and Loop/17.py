# Jace Sperry

age = int(input("How old are you? "))
valid_driver_license = input("Do you have a valid driver's license? (y/n)")
has_insurance = input("Do you have insurance? (y/n)")
get_insurance = False

if valid_driver_license == "n":
    valid_driver_license = False
elif valid_driver_license == "y":
    valid_driver_license = True

if has_insurance == "n":
    get_insurance = input("Do you agree to get insurance? (y/n)")
    if get_insurance == "y":
        get_insurance = True
    elif get_insurance == "n":
        get_insurance = False

if age >= 21 and valid_driver_license and (has_insurance or get_insurance):
    print("You can get a car")
elif age < 18:
    print("You're too young to get a car")
