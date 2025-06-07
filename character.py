import json
from pathlib import Path
DATA_FOLDER = Path("data")
from JSON_util import read_json, save_json

#------------------------------------------------------------------------------------------------   <---Dictionaries--->
# New Character Stats Dictionary----------------------------------------------------------------------------------------
new_character_stats = {
    "level": 1,
    "exp": 0,
    "next_level": 30,
    "hp": 100,
    "max_hp": 100,
    "atk": 5,
    "def": 2,
    "inventory": {
        "currency": {
            "coins": 0
        },
        "materials": {
            "twigs": 0,
            "stones": 0,
            "feathers": 0,
            "small hides": 0,
            "shellbug shells": 0,
            "berries": 5,
            "medicinal herbs": 0
        },
        "consumables": {
            "berries": 0,
            "eggs": 0
        }
    }
}

#-----------------------------------------------------------------------------------------   <---Character Functions--->
# <---Character Stats---> ----------------------------------------------------------------------------------------------
def display_characters_stats(player_name):
    data = read_json("saved_character.json")
    print(f"\n{player_name}'s characters current Stats:")
    print(f"Character Level = {data["level"]} \t Next Level at {data["next_level"]} points")
    print(f"Current Experience Points = {data["exp"]}")
    print(f"Health Points = {data["hp"]} \t Max Health = {data["max_hp"]}")
    print(f"Attack = {data["atk"]} \t \t \t \t Defense = {data["def"]}")

# <---Level Up---> -----------------------------------------------------------------------------------------------------
def level_up_check(player_name):
    data = read_json("saved_character.json")

    if data["exp"] >= data["next_level"]:
        data["level"] += 1
        data["next_level"] += int((data['next_level'] * 1.3 ))
        data["atk"] += 5
        data["def"] += 2
        data["max_hp"] += 10
        print("-------------------------------- Level Up ---------------------------------")
        print(f"Congratulations {player_name} you are now Level {data['level']}")
        print(f"Next level at {data['next_level']} exp")

    save_json("saved_character.json", data)


# # <---Player Profile---> -----------------------------------------------------------------------------------------------
# def player_profile(player_name):
#     print(f"")
#
# # <---Equipped Items---> -----------------------------------------------------------------------------------------------
# # Incomplete, need equipping as well
# # Weapon
# def equipped_weapon():
#     if equipped_gear:
#         character_stats["atk"] += equipped_gear["weapon"]
#
# # Armor
# def equipped_armor():
#     if equipped_gear:
#         character_stats["def"] += equipped_gear["head"] + equipped_gear["body"] + equipped_gear["feet"]
#
# # <---Equipping Items---> ----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------   <---Inventory Functions--->
# <---View Inventory---> -----------------------------------------------------------------------------------------------
def view_inventory():

    path = DATA_FOLDER / "player_inventory.json"
    with open(path, "r") as file:
        inventory = json.load(file)
        print("\nYour Inventory")
        for category, items in inventory.items():
            print(f"{category.capitalize()}")
            for item, quantity in items.items():
                print(f"{item}: {quantity}")

# <---Add Items to Inventory---> ---------------------------------------------------------------------------------------
def add_to_inventory(category, item, quantity):
    path = DATA_FOLDER / "player_inventory.json"
    with open(path, "r") as file:
        inventory = json.load(file)

        if item in inventory[category]:
            inventory[category][item] += quantity
        else:
            inventory[category][item] = quantity

    with path.open("w") as file:
        json.dump(inventory, file, indent=4)

# # <---Use Items from Inventory---> -------------------------------------------------------------------------------------
# def use_item():
#     item = input("What item would you like to use? ")
#     if item in inventory and inventory[item] > 0:
#         inventory[item] -= 1
#         print(f"You used 1 {item}")
#         return True
#     else:
#         print(f"You don't have any {item} in inventory")
#         return False
#
# #------------------------------------------------------------------------------------------   <---Crafting Functions--->
# # <---Open Crafting---> ------------------------------------------------------------------------------------------------
# def crafting():
#     craft = input("what would you like to craft? ")
