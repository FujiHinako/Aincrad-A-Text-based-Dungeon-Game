
def get_class_data():
    # Define all characters in one place
    return {
        "1": {
            "Name": "Warrior",
            "Stats": {"Damage": 25},
            "Skills": {"1": "Sword Slash", "2": "Excalibur"}
        },
        "2": {
            "Name": "Mage",
            "Stats": {"Damage": 20},
            "Skills": {"1": "Fire-Ball", "2": "Explosion"}
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
            
        # Loop through Skills
        print("Skills:")
        for skill_id, skill_name in char['Skills'].items():
            print(f"  [{skill_id}] {skill_name}")
            
        return char # Return the specific dictionary for the game to use
    else:
        print("Invalid Choice!")
        return None