# Lists are data strucutures that contains an ordered list of elements.
# order means they can accessed by an index

# use square brackets for lists
games = ["Rocket League", "Titanfall 2", "Rainbow 6", "Halo 3", "keanu's blackjack",
         "that stupid terraria", "roblox - a bunch", "mario party", "Mario kart (SNES)"]
high_scores = [2, 7, 5, 9]
mixed_list = ["Mr. Klins", 43, True]
list_of_lists = [["Rocket League", 2],
                 ["Titanfall 2", 7],
                 ["Rainbow 6", 5],
                 ["Halo 3", 9]]
# access element by index
print(games[2])
# access element from back list
print(games[-1])

# changing values in a list:
games[-1] = "Garfield Kart"
print(games)

# slicing lists:
# a slice os a subset of a list
first_four = games[:4]  # same as first_four = games[0:4]
print(first_four)

last_four = games[-4:]
print(last_four)

middle_slice = games[4:6]
print(middle_slice)

# create a list of numbers:
numbers = list(range(10))
print(numbers)
# print every other number
print(numbers[::2])
print(numbers[1:7:2])

# reverse a list
print(numbers[::-1])

# combine lists
combined = games + high_scores
print(combined)

# repeated lists
repeated = [5] * 10
print(repeated)
dublicated_high_scores = high_scores * 2
print(dublicated_high_scores)

# find the length of a list
print(len(high_scores))
print(len(dublicated_high_scores))

# unpacking lists:
name, age, likes_teaching = mixed_list
print(f"{name} is {age} and likes {likes_teaching}")

# unpacking with remainders * {first, middle_chunk, last}
game1, *other_games, game2 = games
print(game1)
print(other_games)
print(game2)

for i in games:
    print(i)

# iterate through a list, but also know the index USE ENUMERATE!
for index, game in enumerate(games):
    print(index, game)

# adding items to a list
# append method
games.append("Odie Role Play")
print(games)
games.insert(1, "John Arbuckles's night on the town")
print(games)

# removing elements from a list
games.remove("Halo 3")
print(games)

# remove last element
games.pop(3)
print(games)

# find the index of an element
print(games.index("John Arbuckles's night on the town"))

# note, you'll get an error if the element doesn't exist:
# print(games.index("Odie Role Play"))
# ValueError: 'Odie Role Play' is not in list

# to advoid value error
if "Odie Role Play" in games:
    print(games.index("Odie Role Play"))
else:
    print("What have you done? Where's Odie")

# sort a list
nums_to_sort = [6, 4, 3, 1, 9]
print(nums_to_sort)
nums_to_sort.sort()  # sorting in place - updating order of list
print(nums_to_sort)
# nums_to_sort.sort(reverse=True) # sorting in reverse
nums_to_sort.reverse()  # so will this
print(nums_to_sort)

# create a new sorted list without editing the existing one:
new_sorted_list = sorted(nums_to_sort)
print(nums_to_sort)
print(new_sorted_list)
