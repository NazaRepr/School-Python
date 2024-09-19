import webbrowser
import random
# There are 2 times of functions:
# 1: performs a task
# 2: runs some calculations are returns a value

# performs a task:


def who_is_john_lennon():
    print("He was a Beatle, a member of the greatest band ever")
    print("...other then Perry Gripp")

# perfoms a task:


def who_is_perry_gripp():
    imprint("Perry Gripp is a God of Music")
    webbrowser.open("https://www.youtube.com/watch?v=EiO9_PJ0h8Q")


# returns a value:
def get_awsome_song_link():
    links = ["https://www.youtube.com/watch?v=npjF032TDDQ",
             "https://www.youtube.com/watch?v=EiO9_PJ0h8Q", "https://www.youtube.com/watch?v=jcaej-i3QQo"]
    return random.choice(links)


# who_is_perry_gripp()
webbrowser.open(get_awsome_song_link())
