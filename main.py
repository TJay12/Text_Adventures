from JSON_util import read_json, save_json
from menus import menu
from character import new_character_stats, new_character_inventory

new_character = input("Do you wish to start a new character (y/n): ").lower()
if new_character == "y":
    data = new_character_stats
    inventory = new_character_inventory
    player_name = input("What is your name adventurer? ")
    data['name'] = player_name
    save_json("saved_character.json", data)
    save_json("player_inventory.json", inventory)
    print(f"Welcome to the game {player_name}, hope you enjoy your adventure")
    menu(player_name)

elif new_character == "n":
    data = read_json("saved_character.json")
    player_name = data['name']
    print(f"Welcome back {player_name}, hope you are enjoying your adventure")
    menu(player_name)

else:
    print("Invalid Option")


