# Jace Sperry - Demo 3: Strings
my_name = "Jace Sperry"

length_of_my_name = len(my_name)
print(length_of_my_name)
print("First Letter: ", my_name[0])
print("Third Letter: ", my_name[2])
print("The Last Letter: ", my_name[-1])

# Let's Get a subString
print("\nSubeCode\n")

first_name = my_name[0:4]  # Takes char 0 - 4
last_name = my_name[5:]  # Takes everything from char 6 on
first_two_of_last = my_name[5:7]
print("First Name: ", first_name)
print("Last Name: ", last_name)
print(first_two_of_last)

print("\nESCAPE CHARACTERS\n")

print("There is a tab between tab ->\t<- tab this")
print("Double quotes! \" \" ")
print("Slash -> \\")
print("new line. \nthis text will be in the next line")

print("\nMore String Methods\n")

print("My name in upper case: ", my_name.upper())
print("My name in lower case: ", my_name.lower())
print("The state of my name: ", my_name)

my_name = my_name.lower()

print("The state of my name after overwrite: ", my_name)
print("My name, in proper (title) casing: ", my_name.title())
print("The state of my name: ", my_name)

long_messy_string = "                        some data                        "
print(long_messy_string)
# Strip removes the whitespace before and after the string
print(long_messy_string.strip())
print(long_messy_string.lstrip())  # Remove whitespace on the left

# replace substring
print(my_name.replace("jace", "chad"))  # Note: This is case sensitive
print("The state of my name: ", my_name)
print(my_name.replace("r", "💀"))
# Returns the first index of the searched string, or -1 f not found
print(my_name.find("r"))
print("ace" in my_name)
print("ace" not in my_name)
