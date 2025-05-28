import random
import character
import shop
import encounters
from JSON_util import read_json

# ------------------------------------------------------------------------------------------------------   <---Menus--->
# Main Menu ------------------------------------------------------------------------------------------------------------
def menu(player_name):
    while True:
        print("\n(C)haracter\t(E)xplore\t(Q)uit")
        menu_choice = input("What wold you like to do? ").lower()

        if menu_choice == "c":
            character_menu(player_name)
        elif menu_choice == "e":
            exploring("plains", player_name)
        # elif menu_choice == "s":
        #     shop_menu("biome")
        elif menu_choice == "q":
            print(f"Thanks for Playing! Hope you had fun today {player_name}")
            return
        else:
            print("Invalid Option")

# Character Menu -------------------------------------------------------------------------------------------------------
def character_menu(player_name):
    while True:
        print("\n(S)tats\t(I)nventory\t(E)xit")
        menu_choice = input("What wold you like to do? ").lower()

        # if menu_choice == "p":
        #     character.player_profile(player_name)
        if menu_choice == "s":
            character.display_characters_stats(player_name)
        elif menu_choice == "i":
            character.view_inventory()
            # inventory_menu(player_name)
        # elif menu_choice == "g":
        #     character.game_stats
        elif menu_choice == "e":
            return
        else:
            print("Invalid Option")

# # Inventory Menu -------------------------------------------------------------------------------------------------------
# def inventory_menu(player_name):
#     while True:
#         print("\n(U)se Item\t(C)raft Item\t(E)xit")
#         menu_choice = input("What wold you like to do? ").lower()
#
#         if menu_choice == "u":
#             character.use_item()
#         elif menu_choice == "c":
#             character.display_characters_stats(player_name)
#         elif menu_choice == "e":
#             print(f"Thanks for Playing! Hope you had fun today {player_name}")
#             break
#         else:
#             print("Invalid Option")

# Explore Menu ---------------------------------------------------------------------------------------------------------
def exploring(biome, player_name):
    print(f"Exploring exploring in the {biome}...")
    explore_event = random.choice(["creature", "resource", "nothing"])

    if explore_event == "creature":
        encounters.encounter_creature(player_name)
        data = read_json("player_inventory.json")
        ch_data = read_json("saved_character.json")
        print(f"You now have {data["currency"]["coins"]} coins and {ch_data["exp"]} exp")
    elif explore_event == "resource":
        encounters.encounter_resource(biome)
    else:
        print("nothing here")
# # Shop Menu ------------------------------------------------------------------------------------------------------------
# def shop_menu(biome):
#
#     shop_choice = input("Would you like to (V)iew (B)uy or (S)ell today? ").lower()
#
#     if shop_choice == "v":
#         shop.view_shop()
#     elif shop_choice == "b":
#         shop.buy_items()
#     elif shop_choice == "s":
#         shop.sell_items()
#     else:
#         print("Invalid Option")