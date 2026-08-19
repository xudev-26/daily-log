from array import array
import math
import re
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
        "experience": [],
        "skills": None,
        "pet": [],
        "keys": None,
        "reputation": "weak",
        "class": input("Enter your class(Dragon Tamer/ Warrior/ Mage/ Swordsman/): "),
        "status": "beginner",
        "potion_owned": None
    }

    return player_information


def player_stats():
    strength = array("i", [15])
    health = array("i", [100])
    armor = array("i", [100])
    level = array("i", [1])

    stats = strength, health, armor, level
    return stats


def pet():
    common = [
        "Wolf", "Dog", "Cat", "Hawk", "Rabbit", "Fox", "Horse"
    ]

    magical = [
        "Dragon", "Phoenix", "Griffin", "Fairy", "Spirit Fox", "Moon Owl", "Crystal Serpent"
    ]

    creature = random.choice(common + magical)

    if creature in magical:
        pet_type = "magical"
    else:
        pet_type = "common"

    return creature, pet_type


def validate(strength, health, armor):
    creature, pet_type = pet()

    player_info = info()

    if pet_type == "magical":
        strength[0] += 45
        health[0] += 70
        armor[0] += 5
    else:
        health[0] += 50
        armor[0] += 2

    player_info["pet"].append(creature)

    return player_info



def fight(enemy_strength, enemy_health, enemy_armor, enemy_exp, strength, health):

    while enemy_health > 0 and health[0] > 0:
        print("\n1 Attack")
        print("\n2 Escape")
        choice = input("Enter your choice(1/2): ")

        if choice == "1":
            enemy_health -= strength[0]


        print(f"You dealt {strength[0]} damage!")

        if enemy_health <= 0:
            print("You defeated the enemy")


def enemies(strength, health):
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

    level = [level1, level2, level3, level4, level5]

    for level_index, enemy_group in enumerate(level):
        for name, enemy_stats in enemy_group.items():
            enemy_strength, enemy_health, enemy_armor, enemy_exp = enemy_stats
            fight(enemy_strength, enemy_health, enemy_armor, enemy_exp, strength, health)