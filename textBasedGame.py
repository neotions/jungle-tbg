# John St Hilaire
# For use in Python 3
# Text-Based game for IT140 at SNHU
# 10/2023

import os

# map of rooms 
roomsDirections = {
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

# old room map 
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

# room descriptions
roomDescriptions = {
    "Plane Wreck": " ",
    "Crash Site": " ",
    "Jungle Path": " ",
    "Top of Temple Stairs": " ",
    "Temple Entrance": " ",
    "Creepy Library": " ",
    "Tomb": " ",
    "Treasure Room": " ",
    "Demon's Lair": " "
}

# room items
roomItems = {
    "Plane Wreck": {},
    "Crash Site": {},
    "Jungle Path": {},
    "Top of Temple Stairs": {},
    "Temple Entrance": {},
    "Creepy Library": {},
    "Tomb": {},
    "Treasure Room": {},
    "Demon's Lair": {}
}

# Clear the screen based on the OS
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# class that contains methods for room logic 
class Room:
    def __init__(self, name):
        self.name = name
        self.rooms = roomsDirections[self.name]
        self.description = roomDescriptions[self.name]
        self.items = roomItems[self.name]

    def enter(self):
        print(self.description)
        # additional logic here

# room object declaration
rooms = ["Plane Wreck", "Crash Site", "Jungle Path", "Top of Temple Stairs", "Temple Entrance", "Creepy Library", "Tomb", "Treasure Room", "Demon's Lair"]
roomObjMap = {x : Room(x) for x in rooms}

# init starting room and game state
playing = True
currentRoom = 'Plane Wreck'

# game loop
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
