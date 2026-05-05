import combat_styles

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

