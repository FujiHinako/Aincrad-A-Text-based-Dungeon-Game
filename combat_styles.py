
def get_class_data():
    return {
        "1": {
            "Name": "Warrior",
            "Stats": {"Damage": 25},
            "Skills": {
                "1": {"Name": "Sword Slash", "Damage": 30,"uses":5},
                "2": {"Name": "Excalibur", "Damage": 60,"uses":1}
            }
        },
        "2": {
            "Name": "Mage",
            "Stats": {"Damage": 20},
            "Skills": {
                "1": {"Name": "Fire-Ball", "Damage": 35,"uses":5},
                "2": {"Name": "Explosion", "Damage": 50,"uses":2}
            }
        }
    }

def select_class(choice):
    all_data = get_class_data()
    
    # Check if the choice exists in our data
    if str(choice) in all_data:
        char = all_data[str(choice)]
        
        print(f"\n--- {char['Name']} ---")
        
        # Loop through Stats
        for key, value in char['Stats'].items():
            print(f"{key}: {value}")

        print("\nSkills Available:")
        for key, skill_info in char['Skills'].items():
            name = skill_info["Name"]
            dmg = skill_info["Damage"]
            uses = skill_info["uses"]
            print(f"[{key}] {name} - Deals {dmg} Damage - Uses: {uses}")
            
        
        return char # Return the specific dictionary for the game to use
    else:
        print("Invalid Choice!")
        return None
    
def display_skill_interface(player_skill):
    for key, skill_info in player_skill.items():
                name = skill_info["Name"]
                dmg = skill_info["Damage"]
                uses = skill_info["uses"]
                print(f"[{key}] {name} - Deals {dmg} Damage \n Uses: {uses}")

def skill_damage(skill_name,monster_name,skill_dmg,monster_hp):
     
    monster_hp -= skill_dmg
    if monster_hp <0:
        monster_hp = 0
    print(f"{skill_name} Inflicted {monster_name} {skill_dmg} Damage!")
    print(f"{monster_name} now has {monster_hp}")

    return monster_hp
        





