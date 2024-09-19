import random

# Ask user for their name
name = input("What is your name? ")

total_stat_points = 30

# Default stats
user_default_stats = {
    "health": 10,
    "strength": 0,
    "defense": 0,
    "agility": 0,
    "dexterity": 0,
    "intelligence": 0,
    "wisdom": 0
}

user_race = None
user_class = None
started = False
monster_here = False

# Class selection
while True:
    class_choice = input(
        "What class do you want to be? (Wizard, Warrior, Rogue, Cleric, Druid): ")
    user_class = class_choice

    if class_choice in ["Wizard", "Warrior", "Rogue", "Cleric", "Druid"]:
        break
    else:
        print("I don't recognize that class. Please try again.")

print("You have chosen: " + class_choice)

# Race selection with stat adjustments
while True:
    race_choice = input(
        "What race do you want to be? (Elf, Human, Orc, Half-Elf, Half-Orc): ")
    user_race = race_choice

    if race_choice == "Elf":
        user_default_stats["dexterity"] += 1
        user_default_stats["wisdom"] += 1
    elif race_choice == "Human":
        user_default_stats["strength"] += 1
        user_default_stats["intelligence"] += 1
    elif race_choice == "Orc":
        user_default_stats["strength"] += 1
        user_default_stats["defense"] += 1
    elif race_choice == "Half-Elf":
        user_default_stats["dexterity"] += 1
        user_default_stats["wisdom"] += 1
    elif race_choice == "Half-Orc":
        user_default_stats["strength"] += 1
        user_default_stats["defense"] += 1
    else:
        print("I don't recognize that race. Please try again.")
        continue
    break

print("You have chosen: " + race_choice)

# Stat allocation
while total_stat_points > 0:
    print("You have " + str(total_stat_points) + " stat points left.")
    print("1. Strength")
    print("2. Defense")
    print("3. Agility")
    print("4. Dexterity")
    print("5. Intelligence")
    print("6. Wisdom")

    stat_choice = input("What stat do you want to add? ")

    if stat_choice == "1":
        user_default_stats["strength"] += 1
        total_stat_points -= 1
    elif stat_choice == "2":
        user_default_stats["defense"] += 1
        total_stat_points -= 1
    elif stat_choice == "3":
        user_default_stats["agility"] += 1
        total_stat_points -= 1
    elif stat_choice == "4":
        user_default_stats["dexterity"] += 1
        total_stat_points -= 1
    elif stat_choice == "5":
        user_default_stats["intelligence"] += 1
        total_stat_points -= 1
    elif stat_choice == "6":
        user_default_stats["wisdom"] += 1
        total_stat_points -= 1
    else:
        print("I don't recognize that stat. Please try again.")

    print("Your new stats are: " + str(user_default_stats))

print("Your final stats are: " + str(user_default_stats))

# Helper functions


def choose_your_own_adventure():
    print("Choose Your Own Adventure")
    print("Type 'help' for help.")
    print("Type 'quit' to quit.")
    print("Type 'stats' to see your stats.")
    print("Type 'go' to start your adventure.")


def help():
    print("Commands: 'help', 'quit', 'stats', 'go', 'step', 'spell' (if applicable).")


def stats():
    print("Your stats are: " + str(user_default_stats))


def go():
    print("Starting the adventure...")
    print("Step into the room...")


def quit_game():
    print("Goodbye!")
    exit()


def roll_d20():
    return random.randint(1, 20)


# Combat system
monsters = {
    "Goblin": {"hp": 10, "attack": 3},
    "Orc": {"hp": 15, "attack": 5},
    "Troll": {"hp": 20, "attack": 7}
}


def combat(monster_name, monster):
    player_hp = user_default_stats["health"]
    monster_hp = monster["hp"]
    print(f"A {monster_name} appears with {monster_hp} HP!")

    while player_hp > 0 and monster_hp > 0:
        action = input("Do you want to (attack) or (flee)? ")
        if action == "attack":
            attack_roll = roll_d20() + user_default_stats["strength"]
            if attack_roll >= 12:  # Base AC for simplicity
                damage = random.randint(1, 8)
                monster_hp -= damage
                print(f"You hit the {monster_name} for {damage} damage!")
            else:
                print("You missed!")

            if monster_hp > 0:
                monster_attack = random.randint(1, monster["attack"])
                player_hp -= monster_attack
                print(f"The {monster_name} hit you for {
                      monster_attack} damage!")
        elif action == "flee":
            print("You flee from the battle!")
            return

    if player_hp <= 0:
        print("You have been defeated!")
        quit_game()
    else:
        print(f"You defeated the {monster_name}!")


# Spell system
spells = {
    "Fireball": {"damage": 10, "mana_cost": 5},
    "Heal": {"healing": 8, "mana_cost": 3}
}


def cast_spell(spell_name):
    if spell_name in spells:
        spell = spells[spell_name]
        if user_default_stats["intelligence"] >= spell["mana_cost"]:
            if "damage" in spell:
                print(f"You cast {spell_name} and deal {
                      spell['damage']} damage!")
            if "healing" in spell:
                print(f"You cast {spell_name} and heal for {
                      spell['healing']} HP!")
            user_default_stats["intelligence"] -= spell["mana_cost"]
        else:
            print("Not enough mana to cast the spell.")
    else:
        print(f"{spell_name} is not a known spell.")


# Dungeon exploration
dungeon_rooms = ["Empty room", "Treasure room", "Monster room", "Trap room"]


def explore_dungeon():
    print("You are exploring the dungeon...")
    room = random.choice(dungeon_rooms)
    print(f"You entered a {room}!")

    if room == "Monster room":
        monster = random.choice(list(monsters.keys()))
        combat(monster, monsters[monster])
    elif room == "Treasure room":
        print("You found a treasure chest with 100 gold!")
    elif room == "Trap room":
        print("You triggered a trap! You take 5 damage.")
        user_default_stats["health"] -= 5


# Main game loop
choose_your_own_adventure()

while not started and user_default_stats["health"] > 0:
    choice = input("> ")

    if choice == "help":
        help()
    elif choice == "stats":
        stats()
    elif choice == "go":
        go()
        started = True
    elif choice == "quit":
        quit_game()
    else:
        print("I don't recognize that command. Please try again.")

while started and user_default_stats["health"] > 0:
    choice = input("> ")

    if choice == "help":
        help()
    elif choice == "stats":
        stats()
    elif choice == "step":
        explore_dungeon()
    elif choice == "spell":
        if user_class == "Wizard":
            spell_choice = input(
                "Which spell do you want to cast? (Fireball, Heal): ")
            cast_spell(spell_choice)
        else:
            print("You don't know any spells!")
    elif choice == "quit":
        quit_game()
    else:
        print("I don't recognize that command. Please try again.")
print("Game over!")
