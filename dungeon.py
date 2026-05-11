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
                "desc":"Room Filled with Treasure",
                "next":"Enemy Room",
                "type": "treasure",
                "items":{"Sword":{"Damage":5},
                    "Armour":{"HP":15}}
                    
                    
                
            },
            4:{
                "name":"Enemy Room",
                "desc":"Room ",
                "type": "enemy",
                "next":None
                
                
            },

    }



# room = get_rooms()

# room_num = 4

# print(room[room_num]["name"])
# print(f"You Encountered {room[room_num]["monster"]}")

