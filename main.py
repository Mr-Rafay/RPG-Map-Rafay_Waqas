# ---------------------------------------------------------------------------
# Created By  : Rafay Waqas
# Created Date: 3/19/2024
# version = '1.0'
# ---------------------------------------------------------------------------
"""
Medieval Text-based map Game
----------------------------------
This program is a simple text-based map game set in a medieval
world. The player navigates through a map, using the commands 'walk' and 'run'.
The game map is representedusing a list of lists (array), and location descriptions are 
stored in a dictionary.
"""
# ---------------------------------------------------------------------------

# ----IMPORTS AND GLOBAL VARIABLES--------------------------------------------
# Define the game map using a list of lists (array)
game_map = [
    ['Courtyard', 'Enchanted Forest', 'Misty Mountains'],
    ['Raging River', 'Damp Dungeon', 'Guarded Castle'],
    ['Sandy Shore', 'Mysterious Island', 'Throne Room']
]

# Define the location descriptions using a dictionary
location_descriptions = {
    'Courtyard': 'You find yourself in the castle courtyard. The adventure begins!',
    'Enchanted Forest': 'You enter an enchanted forest filled with ancient trees and magical creatures.',
    'Misty Mountains': 'You reach the foot of the misty mountains. The peaks disappear into the clouds.',
    'Raging River': 'A raging river blocks your path. The water rushes by with great force.',
    'Damp Dungeon': 'You stumble upon a damp dungeon. The air is heavy with the scent of moss.',
    'Guarded Castle': 'You approach a heavily guarded castle. The drawbridge is raised.',
    'Sandy Shore': 'You arrive at a sandy shore. The waves gently lap against the coastline.',
    'Mysterious Island': 'You discover a mysterious island shrouded in mist.',
    'Throne Room': 'Congratulations! You have reached the Throne Room. Your quest is complete.'
}

# Define the valid actions and directions
valid_actions = ['walk', 'run']
valid_directions = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}

# ----FUNCTIONS--------------------------------------------------------------
def display_location_description(location):
    """Display the description of the given location."""
    print(location_descriptions[location])


def update_player_position(direction, position, steps):
    """Update the player's position based on the given direction and steps."""
    row_offset, col_offset = valid_directions[direction]
    position[0] += row_offset * steps
    position[1] += col_offset * steps
    return position


def is_valid_move(position):
    """Check if the given position is a valid move within the map boundaries."""
    row, col = position
    return 0 <= row < len(game_map) and 0 <= col < len(game_map[0])


def play_game():
    """Start the game."""
    player_position = [0, 0]  # Courtyard

    while True:
        current_location = game_map[player_position[0]][player_position[1]]
        display_location_description(current_location)

        print(f"What do you want to do? (Valid actions: {', '.join(valid_actions)})")
        action = input("> ").lower()

        if action in valid_actions:
            steps = 1 if action == 'walk' else 2
            print(f"Which direction do you want to go? (Valid directions: {', '.join(valid_directions)})")
            direction = input("> ").lower()

            if direction in valid_directions:
                new_position = update_player_position(direction, player_position.copy(), steps)

                if is_valid_move(new_position):
                    player_position = new_position
                else:
                    print("You cannot go that way. An invisible force stops you!")
            else:
                print("Invalid direction. Please choose a valid direction.")
        elif action == 'quit':
            print("Thank you for playing. Farewell, brave adventurer!")
            break
        else:
            print("Invalid action. Please choose a valid action.")


def display_main_menu():
    """Display the main menu."""
    print("==== Medieval Adventure Game ====")
    print("1. Start Game")
    print("2. Quit")


# ----MAIN-------------------------------------------------------------------
def main():
    """The main game loop."""
    while True:
        display_main_menu()
        choice = input("> ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("Thank you for playing. Farewell!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()