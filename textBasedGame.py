# John St Hilaire
# For use in Python 3
# Text-Based game for IT140: Intro to Scripting, at SNHU
# 10/2023

import os
import random

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
    "Plane Wreck" : "Placeholder room description",
    "Crash Site" : "Placeholder room description",
    "Jungle Path" : "Placeholder room description",
    "Top of Temple Stairs" : "Placeholder room description",
    "Temple Entrance" : "Placeholder room description",
    "Creepy Library" : "Placeholder room description",
    "Tomb": "Placeholder room description",
    "Treasure Room" : "Placeholder room description",
    "Demon's Lair" : "Placeholder room description"
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
        self.directions = roomsDirections[self.name]
        self.description = roomDescriptions[self.name]
        self.items = roomItems[self.name]

    def enter(self):
        print(self.description)
        # additional logic here
    
    # prints description of room
    def examine(self):
        print(self.discription)

    # search room for items and user choice to pick up item
    def search(self):
        print(f"You search the room and find:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")
            
        itemSelection = int(input("Enter the number of the item you would like to pick up"))
        if itemSelection - 1 <= len(self.items):
            inventory.append(self.items[itemSelection - 1])
            self.items.pop(itemSelection - 1)
        else:
            print("Enter a number listed")
        

# room object declaration
rooms = ["Plane Wreck", "Crash Site", "Jungle Path", "Top of Temple Stairs", "Temple Entrance", "Creepy Library", "Tomb", "Treasure Room", "Demon's Lair"]

# dictionary with all room objects
roomObjMap = {x : Room(x) for x in rooms}

# init starting room game state, and inventory
playing = True
currentRoom = roomObjMap['Plane Wreck']
inventory = []

# game loop
while playing:
    # Display current room
    print(f"You are in {currentRoom.name}.")
    print(" ")
    # table header
    print(f"{'Direction':<15}{'Room':<25}")
    print('-' * 40)

    # List available directions and rooms
    for direction, room in currentRoom.directions.items():
        print(f"{direction:<15}{room:<25}")
    print()

    # Get player input
    newDirection = input("Which direction would you like to go? Type 'exit' to exit the game.\n").capitalize()

    while newDirection not in currentRoom.directions and newDirection != "Exit":
        print("You cannot go that way.")
        newDirection = input("Which direction would you like to go? Type 'exit' to exit the game.\n").capitalize()

    if newDirection == "Exit":
        playing = False
    else:
        currentRoom = roomObjMap[currentRoom.directions[newDirection]]

    # Clear the screen
    clear_screen()

print("Thanks for Playing!!")
print(" ")
