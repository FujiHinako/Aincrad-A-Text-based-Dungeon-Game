import player
import combat_styles
#

class_list = combat_styles.get_class_data()

print("Welcome to Aincrad!")
print("Please State Your Name Traveller")
player_name = input(f'> ')

create_player = player.player_create(player_name)

for key,values in create_player.items():
    print(f'{key}: {values}')
wants_a_class = input("Do You want a class? [1] - Yes [2] - No")
if wants_a_class == 1:
    print(f"\nPlayer {player_name} Please Choose Your Combat Style!\n")

    for key,details in class_list.items():
        print(f"{key}: {details['Name']}")
        print(f"{details['Stats']}")
    fighting_style_choice = input("> ")
    combat_styles.select_character(fighting_style_choice)


    if fighting_style_choice in class_list:
    # Access the selected data
        selected_data = class_list[fighting_style_choice]
    
    # Update the player stats
        create_player["Damage"] = selected_data["Stats"]["Damage"]
        create_player["Class"] = selected_data["Name"] # Useful to track class name!
    
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