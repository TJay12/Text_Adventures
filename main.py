from menus import menu
import character

# new_character = input("Do you wish to start a new character (y/n): ").lower()
# if new_character == "y":
#     player_name = input("What is your name adventurer? ")
#     print(f"Welcome to the game {player_name}, hope you enjoy your adventure")
#
#     # Begining stats
#     player_level = 1
#     player_current_exp = 0
#     next_level = 30
#     player_hp = 100
#     player_max_hp = 100
#     player_atk = 5
#     player_def = 2
#     player_current_coin = 0
#     character.display_characters_stats(player_name)
# else:
#     player_name= input("What's your adventure's name? ")
#     print(f"Welcome back {player_name}, hope you are enjoying your adventure")
#     # Load character_stats logic here

player_name = input("What is your name adventurer? ")
print(f"Welcome to the game {player_name}, hope you enjoy your adventure")
menu(player_name)
