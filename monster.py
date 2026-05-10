
import random
import random

# The dictionary of dictionaries
monster_dict = {
    "Slime": {"HP": 10, "Attack": 60, "Coins": random.randint(1, 3)},
    "Skeleton": {"HP": 20, "Attack": 10, "Coins": random.randint(4, 10)},
    "Armoured Skeleton": {"HP": 40, "Attack": 15, "Coins": random.randint(10, 13)}
}

def spawn_monster():
    # To pick a random monster name from the dictionary keys
    monster_name = random.choice(list(monster_dict.keys()))
    
    # Get that specific monster's dictionary
    monster_stats = monster_dict[monster_name]
    
    # Returning the name and stats together
    return monster_name, monster_stats

        

def deal_damage(monster_damage,player_hp):
    new_hp = player_hp - monster_damage
    print(f"Monster Dealt {monster_damage} Damage!")
    if new_hp < 0:
        new_hp = 0
    return new_hp

