
def get_class_data():
    return {
        "1": {
            "Name": "Warrior",
            "Stats": {"Damage": 25},
            "Skills": {
                "1": {"Name": "Sword Slash", "Damage": 30},
                "2": {"Name": "Excalibur", "Damage": 60}
            }
        },
        "2": {
            "Name": "Mage",
            "Stats": {"Damage": 20},
            "Skills": {
                "1": {"Name": "Fire-Ball", "Damage": 35},
                "2": {"Name": "Explosion", "Damage": 50}
            }
        }
    }

def select_character(choice):
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
            print(f"[{key}] {name} - Deals {dmg} Damage")
            
        
        return char # Return the specific dictionary for the game to use
    else:
        print("Invalid Choice!")
        return None