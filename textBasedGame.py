# John St Hilaire
# For use in Python 3
# Text-Based game for IT140 at SNHU
# 10/2023

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

class Room:
    def __init__(self, name, description, items, characters):
        self.name = name
        self.description = description
        self.items = items
        self.characters = characters

    def enter(self):
        print(self.description)
        # additional logic here

rooms = {
    "Plane Wreck": {"E": "Crash Site"},
    "Crash Site": {"E": "Jungle Path", "W": "Plane Wreck"},
    "Jungle Path": {"N": "Top of Temple Stairs", "W" : "Crash Site"},
    "Top of Temple Stairs": {"N" : "Temple Entrance", "S" : "Jungle Path"},
    "Temple Entrance": {"N" : "Treasure Room", "S" : "Top of Temple Stairs", "E" : "Demon's Lair", "W" : "Creepy Library"},
    "Creepy Library": {"N" : "Tomb", "E" : "Temple Entrance"},
    "Tomb": {"S" : "Creepy Library", "E" : "Treasure Room"},
    "Treasure Room": {"S" : "Temple Entrance", "W" : "Tomb"},
    "Demon's Lair": {"W" : "Temple Entrance"}
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
