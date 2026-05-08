import player
import combat_styles
import monster
#stores list for classes which came from function "get_class_data()" in combat_styles
class_list = combat_styles.get_class_data()
action_list = player.player_action_data()
player_data_list = player.player_create
mnstr_name,mnstr_hp,mnstr_dmg,mnstr_coin= monster.spawn_monster()

player
def display_action():
    for key,details in action_list.items():
     print(f"{key}: {details}")
def is_monster_dead(monster_hp):
    if monster_hp <= 0:
        print(f"Congrats! You Deafeated {mnstr_name}")
        exit()
def is_player_dead(player_hp):
    
    if player_hp <= 0:
        print("You have been defeated... Game Over.")
        exit()
#asks for players name
print("Welcome to Aincrad!")
print("Please State Your Name Traveller")
player_name = input(f'> ')

#stores and sends player input to player.player_create() for the players name
create_player = player.player_create(player_name)

#a for loop which loops thru items in create_player 
for key,values in create_player.items():
    print(f'{key}: {values}')
#asks player if player wants a class
wants_a_class = input("Do You want a class? [1] - Yes [2] - No ")
#if players wants class (input is 1)
if wants_a_class == "1":
    #prompts user to choose for class
    print(f"\nPlayer {player_name} Please Choose Your Combat Style!\n")
    #using the data from class_list it loops thru the classes name and damage
    for key,details in class_list.items():
        name = details["Name"]
        dmg = details["Stats"]["Damage"]
        print(f"Class {key}: {name} - Damage [{dmg}]")
        
    fighting_style_choice = input("> ")
    #sends player's input to combat_styles.select_character() for complete class info and updating player damage
    combat = combat_styles.select_class(fighting_style_choice)

    #checks if fighting_style_choice is in class_list (fighting_style_choice = 1 if true proceed)
    if fighting_style_choice in class_list:
        # Access the selected data
        #stores data from what the player choose
        selected_data = class_list[fighting_style_choice]
    
    # Update the player stats
    #selected_data["Stats"]["Damage"] is used from updating create_player["Damage"] to 
    #access deeper list value
        create_player["Damage"] = selected_data["Stats"]["Damage"]
        create_player["Class"] = selected_data["Name"]
        
    
        print(f"\nPower increased! You are now a {create_player['Class']} with {create_player['Damage']} Damage.")
    else:
        print("Invalid choice, the monsters of Aincrad won't be so forgiving!")

    print("\n--- Updated Player Profile ---")
    for key, value in create_player.items():
        print(f"{key}: {value}")
     
else:
    print("\n--- Player Profile ---")
    for key, value in create_player.items():
        print(f"{key}: {value}")
print()

#Combat

print("Room 1!")


while True:
    player.display_interface(mnstr_name,mnstr_hp,create_player["HP"],player_name)

    display_action()
    action_choice = input("> ")
    #Combat
       

    if action_choice == '1':
            

            mnstr_hp = player.deal_damage(create_player["Damage"],mnstr_hp)
            is_monster_dead(mnstr_hp)
            
            print('\n-----------------------------------\n')
        
            print(f"{mnstr_name}'s Turn!\n")
                    

            create_player["HP"] = monster.deal_damage(mnstr_dmg,create_player["HP"])
            is_player_dead(create_player["HP"])
                

            
    elif action_choice == '2':
            if wants_a_class == '1':
                print("Skills:")
                player_skill = combat["Skills"]
                
                print("\n--- Available Skills ---")
                combat_styles.display_skill_interface(combat["Skills"])
                skill_choice = input(">")
                
                chosen_skill_dmg = combat["Skills"][skill_choice]["Damage"]
                chosen_skill_uses = combat["Skills"][skill_choice]["uses"]
                chosen_skill_name = combat["Name"]

                mnstr_hp = combat_styles.skill_damage(chosen_skill_name,mnstr_name,chosen_skill_dmg,mnstr_hp)
                combat["Skills"][skill_choice]["uses"] = combat_styles.skill_used(chosen_skill_uses)
                print(f"Uses Left: {combat["Skills"][skill_choice]["uses"]}")
                is_monster_dead(mnstr_hp)
            elif wants_a_class == '2':
                print("You Don't Have a Skill!")
                continue
    elif action_choice == '3':
        pass

    elif action_choice == '4':
        print("You ran like a coward. Pathetic.")
        break
    else:
            print("Invalid Input! Try Again!\n")
            exit()