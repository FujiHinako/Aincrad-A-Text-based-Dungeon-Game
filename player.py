
deafult_hp = 100
deafult_dmg = 10
deafult_class = "Classless"
def player_create(name):
    return {
            "Player:" : name,
            "HP" : deafult_hp,
            "Damage" : deafult_dmg, 
            "Class" : deafult_class
            }

def deal_damage(player_damage,enemy_hp):
    new_hp = enemy_hp - player_damage
    if new_hp < 0:
        new_hp = 0
    return new_hp

def player_action_data():
    return {
            "1" : "Attack",
            "2" : "Skill",
            "3" : "Items", 
            "4" : "Run"
            }

