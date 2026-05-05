
def monster_data():
    return {
            "1":
                {
                    "Name":"Slime",
                    "Stats": {"HP": 25,"Damage": 5}
                },
            "2":
                {
                    "Name":"Skeleton",
                    "Stats": {"HP": 50,"Damage": 15}
                },
            "3":
                {
                    "Name":"Armoured Skeleton",
                    "Stats": {"HP": 75,"Damage": 20}
                }
            
            }
def select_monster(choice):
    monster = monster_data()
    
    # Check if the choice exists in our data
    if str(choice) in monster:
        char = monster[str(choice)]
        
        print(f"\n--- {char['Name']} ---")
        
        # Loop through Stats
        for key, value in char['Stats'].items():
            print(f"{key}: {value}")
            
        
        return char # Return the specific dictionary for the game to use
    else:
        print("Invalid Choice!")
        return None
def deal_damage(monster_damage,player_hp):
    new_hp = player_hp - monster_damage
    if new_hp < 0:
        new_hp = 0
    return new_hp