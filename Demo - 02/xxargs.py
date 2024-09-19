def save_user(**user):
    print(user)  # note User is a dictionary based on the args
    print(user["id"])
    print(user["name"])


save_user(id=5, name="Tony", age=43)
