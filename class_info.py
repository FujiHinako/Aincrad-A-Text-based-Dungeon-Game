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

def display_skill_interface(player_skill):
    all_data = get_class_data()
    
    # Check if the choice exists in our data
   
    for key, skill_info in player_skill.items():
        name = skill_info["Name"]
        dmg = skill_info["Damage"]
        uses = skill_info  ["uses"]
        print(f"[{key}] {name} - Deals {dmg} Damage \n Uses: {uses}")