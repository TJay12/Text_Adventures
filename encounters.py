import json
from pathlib import Path
import random
from xml.etree.ElementTree import indent

from character import add_to_inventory
from character import level_up_check
from JSON_util import read_json, save_json
DATA_FOLDER = Path("data")

#-----------------------------------------------------------------------------------------   <---Encounter Functions--->
# Resource Encounter----------------------------------------------------------------------------------------------------
def encounter_resource(player_name):
    path = DATA_FOLDER / "resources_plains.json"
    with open(path, "r") as file:
        resources = json.load(file)

    encounter = random.choice(list(resources.keys()))
    resource = encounter
    for item in resources[resource]:
        loot = item
        loot_qty = random.randint(1, 3)
    collect = input(f"You spot a {resource} nearby, do you wish to gather? y/n ").lower()

    if collect == "n":
        print(f"{player_name} Doesn't need any more resources from {resource} right now")
    elif collect == "y":
        print(f"Found {loot_qty} x {loot} in {resource}")
        add_to_inventory("materials", loot, loot_qty)
    else:
        print("Invalid Option")

# Creature Encounter----------------------------------------------------------------------------------------------------
def encounter_creature(player_name):
    path = DATA_FOLDER / "creatures_plains.json"

    with open(path, "r") as file:
        creatures = json.load(file)
        character = read_json("saved_character.json")
        rand_creature = random.choice(list(creatures.keys()))
        player_level = character['level']
        (creature_level, creature_hp, creature_attack, creature_defence, creature_exp, creature_coins,
         loot_item, loot_qty) = get_creature_stats(creatures, rand_creature, player_level)
        fight = input(f"You spot a level {creature_level} {rand_creature} nearby, do you wish to fight? y/n ").lower()

        if fight == "n":
            print(f"{player_name} sneaks away from {rand_creature}, crisis averted")
        elif fight == "y":
            if character['hp'] <= 0:
                    print(f"{player_name} is out of health, replenish health to battle again")
            else:
                print(f"Fighting level {creature_level} {rand_creature} \nHP: {creature_hp} \t Attack: {creature_attack} \t "
                      f"Defence: {creature_defence}")
                battle_sequence(player_name, rand_creature, creature_attack, creature_defence, creature_hp,
                                creature_exp, creature_coins, loot_item, loot_qty)
        else:
            print("Invalid Option")

#--------------------------------------------------------------------------------------------   <---Battle Functions--->
# Get Creature Stats----------------------------------------------------------------------------------------------------
def get_creature_stats(creatures, rand_creature, player_level):
    creature = creatures[rand_creature]

    creature_level = max(1, random.randint(player_level - 2, player_level + 3))
    creature_hp = creature["hp"] * 0.5 * creature_level
    creature_attack = creature["atk"] * 0.5 * creature_level
    creature_defence = creature["def"]  * 0.5 * creature_level
    creature_exp = creature["exp"]  * 0.5 * creature_level
    creature_coins = creature["coins"]  * 0.5 * creature_level
    for item, value in creature["loot"].items():
        loot = item
        loot_qty = value

    return (creature_level, creature_hp, creature_attack, creature_defence, creature_exp, creature_coins,
            loot, loot_qty)

# Battle Sequence-------------------------------------------------------------------------------------------------------
def battle_sequence(player_name, rand_creature, creature_attack, creature_defence, creature_hp,
                    creature_exp, creature_coins, loot_item, loot_qty):

    character = read_json("saved_character.json")
    player_dmg = max(0, character['atk'] - creature_defence)
    creature_dmg = max(0, creature_attack - character['def'])

    while character['hp'] > 0 and creature_hp > 0:
        print(f"{player_name} deals {player_dmg} to {rand_creature}", end="\t")
        creature_hp -= player_dmg
        print(f"{rand_creature} HP: {max(0, creature_hp)}", end="\t")
        if creature_hp <= 0:
            print(f"{player_name} has defeated {rand_creature}")
            character["exp"] += creature_exp
            add_to_inventory("currency", "coins", creature_coins)
            add_to_inventory("materials", loot_item, loot_qty)
        else:
            print(f"{rand_creature} deals {creature_dmg} to {player_name}", end="\t")
            character['hp'] -= creature_dmg
            print(f"{player_name} HP: {max(0, character['hp'])}")
            if character['hp'] <= 0:
                character['hp'] = 0
                print(f"{rand_creature} has defeated {player_name}")
    save_json("saved_character.json", character)
    level_up_check(player_name)

# <--- === Testing Zone === --->
# for i in range(5):
#     encounter_resource("player_name")

# for i in range(10):
#     encounter_creature("player_name")

# path = DATA_FOLDER / "creatures_plains.json"
# with open(path, "r") as file:
#     creatures = json.load(file)
#     get_creature_stats(creatures, random.choice(list(creatures.keys())), 3)