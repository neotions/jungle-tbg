# Your Name
# ModuleSixMilestone.py

import os

# Clear the screen based on the OS
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

playing = True
currentRoom = 'Great Hall'

while playing:
    # Display current room
    print(f"You are in {currentRoom}.")

    # Display available directions
    for direction, room in rooms[currentRoom].items():
        print(f"Direction: {direction}, Room: {room}")

    # Get player input
    newDirection = input("Which direction would you like to go? Type 'exit' to exit the game.\n").capitalize()

    # Check if direction is valid
    if newDirection in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][newDirection]
    elif newDirection == 'Exit':
        playing = False
    else:
        print("You cannot go that way.")

    # Clear the screen
    clear_screen()
