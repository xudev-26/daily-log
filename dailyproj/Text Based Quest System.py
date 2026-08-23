from array import array
import random


def display(strength, health, armor, level):
    print("=" * 25)
    print("Player Stats")
    print("=" * 25)
    print(f"Health {health[0]}")
    print(f"Strength {strength[0]}")
    print(f"Armor {armor[0]}")
    print(f"Level {level[0]}")


def info():
    player_information = {
        "experience": 0,
        "skills": None,
        "pet": [],
        "keys": None,
        "reputation": "weak",
        "class": input(
            "Enter your class "
            "(Dragon Tamer/ Warrior/ Mage/ Swordsman): "
        ),
        "status": "beginner",
        "potion_owned": None
    }

    return player_information


def player_stats():
    strength = array("i", [15])
    health = array("i", [100])
    armor = array("i", [100])
    level = array("i", [1])

    return strength, health, armor, level


def pet():
    common = [
        "Wolf", "Dog", "Cat", "Hawk",
        "Rabbit", "Fox", "Horse"
    ]

    magical = [
        "Dragon", "Phoenix", "Griffin",
        "Fairy", "Spirit Fox", "Moon Owl",
        "Crystal Serpent"
    ]

    creature = random.choice(common + magical)

    if creature in magical:
        pet_type = "magical"
    else:
        pet_type = "common"

    return creature, pet_type


def validate(strength, health, armor, player_info):
    creature, pet_type = pet()

    if pet_type == "magical":
        strength[0] += 45
        health[0] += 70
        armor[0] += 5
    else:
        health[0] += 50
        armor[0] += 2

    player_info["pet"].append(creature)

    print(f"\nYour pet is a {creature}!")
    print(f"It is a {pet_type} pet.")

    return player_info


def fight(
    enemy_name,
    enemy_strength,
    enemy_health,
    enemy_armor,
    enemy_exp,
    strength,
    health,
    armor,
    player_info
):
    print(f"\nA wild {enemy_name} appeared!")

    while enemy_health > 0 and health[0] > 0:

        print("\n1. Fight")
        print("2. Escape")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            damage = max(1, strength[0] - enemy_armor)
            enemy_health -= damage
            print(f"You dealt {damage} damage!")

            if enemy_health > 0:

                damage_taken = max(
                    1,
                    enemy_strength - armor[0]
                )

                health[0] -= damage_taken

                print(
                    f"The enemy dealt {damage_taken} damage!"
                )
                print(f"Your health: {health[0]}")

            else:
                print(f"You defeated the {enemy_name}!")

                player_info["experience"] += enemy_exp

                print(
                    f"You gained {enemy_exp} experience!"
                )

                
                return "won"

        elif choice == "2":

            print("You escaped!")
            return "escaped"

        else:
            print("Please enter 1 or 2.")


    if health[0] <= 0:
        return "lost"


def enemies(strength, health, armor, level, player_info):

    level1 = {
        "grimfang": [35, 8, 4, 15],
        "duskhound": [30, 9, 3, 12],
        "rotclaw": [42, 7, 6, 18],
        "ashling": [28, 10, 2, 14],
        "murkhide": [50, 6, 9, 20],
        "bloodrat": [20, 6, 2, 8],
        "vexling": [32, 11, 3, 16],
        "thornback": [45, 8, 8, 22],
        "gloomfang": [38, 10, 5, 19],
        "skarn": [55, 7, 10, 25]
    }

    level2 = {
        "ironclaw": [55, 12, 7, 25],
        "nightfang": [48, 14, 5, 22],
        "brambleback": [70, 10, 12, 30],
        "emberling": [45, 15, 4, 24],
        "rotmaw": [62, 13, 8, 28],
        "shadowrat": [38, 11, 4, 18],
        "venomfang": [52, 16, 6, 27],
        "stonehide": [80, 9, 15, 35],
        "dreadwing": [58, 15, 7, 32],
        "skullcrawler": [65, 14, 9, 30]
    }

    level3 = {
        "frostfang": [75, 18, 10, 38],
        "razorclaw": [68, 20, 8, 35],
        "thornmaw": [90, 16, 14, 42],
        "flamekin": [60, 22, 7, 40],
        "venomclaw": [80, 19, 11, 45],
        "darkrat": [50, 16, 6, 28],
        "gravelurker": [95, 15, 16, 48],
        "stormwing": [72, 21, 9, 44],
        "bloodfang": [85, 23, 10, 50],
        "ironhide": [110, 14, 20, 55]
    }

    level4 = {
        "icefang": [100, 24, 14, 55],
        "razorbeast": [90, 27, 12, 52],
        "thornhide": [120, 21, 19, 62],
        "flameclaw": [85, 29, 10, 58],
        "venommaw": [105, 25, 15, 65],
        "shadowfang": [75, 22, 9, 45],
        "rockcrawler": [135, 20, 22, 70],
        "stormclaw": [95, 28, 13, 68],
        "bloodmaw": [115, 30, 15, 75],
        "steelhide": [155, 18, 26, 82]
    }

    level5 = {
        "glacierfang": [130, 30, 18, 75],
        "dreadclaw": [115, 34, 15, 70],
        "thornbeast": [155, 27, 24, 85],
        "infernal": [105, 37, 13, 82],
        "venomfang": [140, 32, 20, 90],
        "nightstalker": [95, 29, 12, 65],
        "stonecrusher": [175, 25, 29, 100],
        "stormbeast": [125, 36, 17, 95],
        "bloodreaver": [150, 40, 19, 110],
        "ironmauler": [200, 23, 34, 125]
    }

    all_levels = [
        level1,
        level2,
        level3,
        level4,
        level5
    ]

    current_level_index = level[0] - 1

    while (
        health[0] > 0
        and current_level_index < len(all_levels)
    ):

        current_enemy_group = all_levels[current_level_index]

        print(
            f"\n===== LEVEL {current_level_index + 1} ====="
        )

        level_cleared = True

        for enemy_name, enemy_stats in current_enemy_group.items():

            (
                enemy_strength,
                enemy_health,
                enemy_armor,
                enemy_exp
            ) = enemy_stats

            result = fight(
                enemy_name,
                enemy_strength,
                enemy_health,
                enemy_armor,
                enemy_exp,
                strength,
                health,
                armor,
                player_info
            )

            if result == "lost":
                print(
                    "\nGame Over! "
                    "The horde overwhelmed you."
                )

                return

            if result == "escaped":
                level_cleared = False
                break

        if level_cleared and health[0] > 0:

            print(
                f"\nLevel {current_level_index + 1} Cleared!"
            )

            level[0] += 1
            strength[0] += 10
            armor[0] += 5

            current_level_index += 1

        else:
            break

    if level[0] > len(all_levels):
        print("\nCongratulations! You beat the entire game!")


def main():

    print("Welcome to Invented Game I Made for Fun!")

    strength, health, armor, level = player_stats()
    player_info = info()

    validate(
        strength,
        health,
        armor,
        player_info
    )

    while True:

        print("\n1. Proceed")
        print("2. Quit")

        choose = input("Pick your choice: ")

        if not choose.isdigit():
            print("Please enter a valid number.")
            continue

        transform = int(choose)

        
        if transform == 1:

            display(
                strength,
                health,
                armor,
                level
            )

            enemies(
                strength,
                health,
                armor,
                level,
                player_info
            )

            if health[0] <= 0:
                break

        elif transform == 2:

            print("Goodbye!")
            break

        else:
            print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()

# 1st bug.)
# I made the experience a list instead of a number. You can add a number
# to a list, but you can't combine the list with a number using arithmetic
# operators. For example, you can append a number to the list, but you
# can't directly add a number to the whole list


# 2nd bug fixed.)
# I added the player_info parameter to the validate() function so it can
# receive the data returned by the info() function and allow me to modify
# the player's information.


# 3rd bug fixed.)
# I have experience data in player_info, but I didn't add the enemy's
# experience to it when I defeated an enemy.


# 4th bug fixed.)
# I used the break statement instead of the return statement in the fight()
# function. Because of that, enemies() didn't know whether the player
# defeated the enemy, escaped, or lost. We used a word in the return
# statement, like "won", "escaped", or "lost", to act as a validation so
# the program knows what happened in the fight.


# 5th bug fixed.)
# I added an else statement so whenever the player inputs a number beyond
# 2, the loop will keep asking for a correct input instead of quitting
# the game.


# 6th bug fixed.)
# I removed the duplicate arrays in main() because I remembered that
# player_stats() already creates the strength, health, armor, and level
# arrays. I learned that I can call the function and receive those values
# instead of creating the same data again.


# 7th bug fixed.)
# I need to remember that Python executes the code in order. I displayed
# the stats before checking what the player entered, so the stats would
# be displayed even if the player chose to quit. I moved the display()
# call inside the if transform == 1 so it only displays when the player
# chooses to proceed