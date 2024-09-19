# a function with a variable number of arguments
def multiple(message, *numbers):
    product = 1
    print(f"{message}: {numbers}")
    for num in numbers:
        product *= num
    return product


print(multiple("I'm multiplying", 2, 3, 4, 5))
