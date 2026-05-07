
deafult_hp = 100
deafult_dmg = 10
deafult_class = "Classless"
def player_create(name):
    return {
            "Name" : name,
            "HP" : deafult_hp,
            "Damage" : deafult_dmg, 
            "Class" : deafult_class
            }

def deal_damage(player_damage,enemy_hp):
    new_hp = enemy_hp - player_damage
    if new_hp < 0:
        new_hp = 0
    print(f"You Dealt {player_damage}!")
    return new_hp

def player_action_data():
    return {
            "1" : "Attack",
            "2" : "Skill",
            "3" : "Items", 
            "4" : "Run"
            }

def player_use_skill(player_dmg,monster_hp,uses):
    
        monster_hp -= player_dmg
        uses -= 1
        return monster_hp,uses



def display_interface(mnstr_name,mnstr_hp,player_hp,player_name):
    print(f"You've Encountered {mnstr_name}")
    print(f"Current Monster hp: {mnstr_hp}")
    print(f"Current Hp: {player_hp}")
    print(f"What will {player_name} do? ")
        

