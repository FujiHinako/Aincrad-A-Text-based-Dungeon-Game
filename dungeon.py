import player
import monster
monster_name,monster_stat = monster.spawn_monster()
def get_rooms():
    return {
            1:{
                "name":"Entrance",
                "desc":"A cold dark cave",
                "type": "peaceful",
                "next":"Hall Way"
            },
            2:{
                "name":"Hallway",
                "desc":"A dark Hallway",
                "next":"Treasure Room",
                "type": "peaceful",
                

            },
            3:{
                "name":"Treasure Room",
                "desc":"A cold dark cave",
                "next":"Enemy Room",
                "type": "treasure",
                "items":[("Sword",5),
                    ("Armour",10)]
                    
                    
                
            },
            4:{
                "name":"Enemy Room",
                "desc":"A cold dark cave",
                "type": "enemy",
                "next":None
                
                
            },

    }



# room = get_rooms()

# room_num = 4

# print(room[room_num]["name"])
# print(f"You Encountered {room[room_num]["monster"]}")

