from random import choice
monster_list = [
    #monster_name, HP, Attack
    ("Slime", 10,5),
    ("Skeleton",20,10),
    ("Armoured Skeleton",40,15)
    ]
   
    



def spawn_monster():
    monster = choice(monster_list)
    return(monster)


        

def deal_damage(monster_damage,player_hp):
    new_hp = player_hp - monster_damage
    print(f"Monster Dealt {monster_damage} Damage!")
    if new_hp < 0:
        new_hp = 0
    return new_hp