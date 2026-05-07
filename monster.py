
import random
monster_list = [
    #monster_name, HP, Attack,Coins
    ("Slime", 10,60,random.randint(1,3)),
    ("Skeleton",20,10,random.randint(4,10)),
    ("Armoured Skeleton",40,15,random.randint(10,13))
    ]
   
    



def spawn_monster():
    monster_chance = random.randint(1,100)
    monster = random.choice(monster_list)
    return(monster)


        

def deal_damage(monster_damage,player_hp):
    new_hp = player_hp - monster_damage
    print(f"Monster Dealt {monster_damage} Damage!")
    if new_hp < 0:
        new_hp = 0
    return new_hp