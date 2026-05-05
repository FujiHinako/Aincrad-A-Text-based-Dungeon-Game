import player
import combat_styles
import monster
#stores list for classes which came from function "get_class_data()" in combat_styles
class_list = combat_styles.get_class_data()
monster_list = monster.monster_data()
action_list = player.player_action_data()
player_data_list = player.player_create

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
    combat_styles.select_character(fighting_style_choice)

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

#Combat
#player will choose which to fight for now
while True:
    print("Room 1!")
    for key,details in monster_list.items():
        print(f"{key}: {details['Name']}")
    monster_choice = input("> ")

    selected_monster = monster.select_monster(monster_choice)

    #Combat
    while create_player['HP']>0 and selected_monster["Stats"]["HP"]>0:
        print(f"Current Hp: {create_player['HP']}")
        print(f"{selected_monster["Name"]} Spawned, What will {player_name} do? ")
        for key,details in action_list.items():
            print(f"{key}: {details}")
        action_choice = input("> ")

        if action_choice == '1':
            monster_hp = selected_monster["Stats"]["HP"]
            player_hp = create_player['HP']
            player_dmg = create_player['Damage']
            monster_dmg = selected_monster['Stats']['Damage']

            selected_monster["Stats"]["HP"] = player.deal_damage(player_dmg,monster_hp)
            print(f"You Dealt {player_dmg}, {selected_monster["Name"]} has {selected_monster["Stats"]["HP"]} left!")
            create_player['HP'] = monster.deal_damage(monster_dmg,player_hp)
            print(create_player['HP'])
            
            
            
            if selected_monster["Stats"]["HP"] == 0:
                print(f"Congrats! You Deafeated {selected_monster['Name']}")
                break
            
            print('\n-----------------------------------\n')
            
            print(f"{selected_monster['Name']}'s Turn!\n")
            
            print(f"{selected_monster['Name']} Dealt {monster_dmg}, to {create_player["Name"]}!\n")
            
            print(f"{create_player['Name']} now has {create_player["HP"]}")

            if create_player["HP"] <= 0:
                print("You have been defeated... Game Over.")
                exit()
        elif action_choice == '2':
            print("Skills:")
            player_skills = class_list[fighting_style_choice]['Skills']
            
            print("\n--- Available Skills ---")
            for key, skill_info in player_skills.items():
                print(f"[{key}] {skill_info['Name']} - Deals {skill_info['Damage']} Damage")
            skill_choice = input(">")

            



   


