from data.inventory import inventory

#------------------------------------------------------------------------------------------------   <---Dictionaries--->
# Character Stats Dictionary--------------------------------------------------------------------------------------------
character_stats = {
    "level": 1,
    "exp": 0,
    "next_level": 30,
    "hp": 100,
    "max_hp": 100,
    "atk": 5,
    "def": 2,
}


#-----------------------------------------------------------------------------------------   <---Character Functions--->
# <---Character Stats---> ----------------------------------------------------------------------------------------------
def display_characters_stats(player_name):
    print(f"\n{player_name}'s characters current Stats:")
    print(f"Character Level = {character_stats["level"]} \t Next Level at {character_stats["next_level"]} points")
    print(f"Current Experience Points = {character_stats["exp"]}")
    print(f"Health Points = {character_stats["hp"]} \t Max Health = {character_stats["max_hp"]}")
    print(f"Attack = {character_stats["atk"]} \t \t \t \t Defense = {character_stats["def"]}")

# <---Level Up---> -----------------------------------------------------------------------------------------------------
def level_up_check(player_name):
    if character_stats["exp"] >= character_stats["next_level"]:
        character_stats["level"] += 1
        character_stats["exp"] -= character_stats["next_level"]
        character_stats["next_level"] += int((character_stats["next_level"] * 0.6 ))
        character_stats["atk"] += 5
        character_stats["def"] += 2
        character_stats["max_hp"] += 10
        print("-------------------------------- Level Up ---------------------------------")
        print(f"Congratulations {player_name} you are now Level {character_stats["level"]}")

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
    print("\nYour Inventory")
    for category, items in inventory.items():
        print(f"{category.capitalize()}")
        for item, quantity in items.items():
            print(f"{item}: {quantity}")

# <---Add Items to Inventory---> ---------------------------------------------------------------------------------------
def add_to_inventory(category, item, quantity):
    if item in inventory[category]:
        inventory[category][item] += quantity
    else:
        inventory[category][item] = quantity

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
