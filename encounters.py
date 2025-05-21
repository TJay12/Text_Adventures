import random
from data.resources import resources
from data.creatures import creatures_stats
from character import character_stats
from character import add_to_inventory
from character import level_up_check

#-----------------------------------------------------------------------------------------   <---Encounter Functions--->
# Resource Encounter----------------------------------------------------------------------------------------------------
def encounter_resource(player_name):

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
def encounter_creature(biome, player_name):

    creature = random.choice(list(creatures_stats[biome].keys()))
    player_level = character_stats['level']
    (creature_level, creature_hp, creature_attack, creature_defence, creature_exp, creature_coins,
     creature_drops) = get_creature_stats(biome, creature, player_level)
    fight = input(f"You spot a level {creature_level} {creature} nearby, do you wish to fight? y/n ").lower()

    if fight == "n":
        print(f"{player_name} sneaks away from {creature}, crisis averted")
    elif fight == "y":
        if character_stats['hp'] <= 0:
                print(f"{player_name} is out of health, replenish health to battle again")
        else:
            print(f"Fighting level {creature_level} {creature} \nHP: {creature_hp} \t Attack: {creature_attack} \t "
                  f"Defence: {creature_defence}")
            battle_sequence(creature, creature_attack, creature_defence, creature_hp, creature_exp, creature_coins,
     creature_drops)
    else:
        print("Invalid Option")

#--------------------------------------------------------------------------------------------   <---Battle Functions--->
# Get Creature Stats----------------------------------------------------------------------------------------------------
def get_creature_stats(biome, creature, player_level):

    creature_data = creatures_stats[biome][creature]

    creature_level = max(1, random.randint(player_level - 2, player_level + 3))
    creature_hp = creature_data["hp"] * 0.5 * creature_level
    creature_attack = creature_data["atk"] * 0.5 * creature_level
    creature_defence = creature_data["def"]  * 0.5 * creature_level
    creature_exp = creature_data["exp"]  * 0.5 * creature_level
    creature_coins = creature_data["coins"]  * 0.5 * creature_level
    creature_base_drops = creature_data["loot"]

    return (creature_level, creature_hp, creature_attack, creature_defence, creature_exp, creature_coins,
            creature_base_drops)

# Battle Sequence-------------------------------------------------------------------------------------------------------
def battle_sequence(creature, creature_attack, creature_defence, creature_hp, creature_exp, creature_coins,
     creature_drops):
    player_name = "TJ"
    player_dmg = max(0, character_stats['atk'] - creature_defence)
    creature_dmg = max(0, creature_attack - character_stats['def'])

    while character_stats['hp'] > 0 and creature_hp > 0:
        print(f"{player_name} deals {player_dmg} to {creature}", end="\t")
        creature_hp -= player_dmg
        print(f"{creature} HP: {max(0, creature_hp)}", end="\t")
        if creature_hp <= 0:
            print(f"{player_name} has defeated {creature}")
            character_stats["exp"] += creature_exp
            level_up_check(player_name)
            add_to_inventory("currency", "coins", creature_coins)
            add_to_inventory("materials", creature_drops, 1)
        else:
            print(f"{creature} deals {creature_dmg} to {player_name}", end="\t")
            character_stats['hp'] -= creature_dmg
            print(f"{player_name} HP: {max(0, character_stats['hp'])}")
            if character_stats['hp'] <= 0:
                character_stats['hp'] = 0
                print(f"{creature} has defeated {player_name}")