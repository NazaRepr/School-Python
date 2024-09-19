# click the bug icon on the left
# f9 or click to the left to add BREAKPOINT
# f10 to step over function
# f11 to step line by line
# f5 to start debugging

def multiple(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print("Start")
print(multiple(2, 3, 4, 5))
