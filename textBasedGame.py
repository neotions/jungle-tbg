# John St Hilaire
# For use in Python 3
# Text-Based game for IT140: Intro to Scripting, at SNHU
# 10/2023

import os

############  all game data ##############
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

itemDescriptions = {
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
    "Plane Wreck": {
        "Chocolate Bar" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Crash Site": {
        "Chocolate Bar" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Jungle Path": {
        "Radio" : {
            "examine" : "I found the radio... this won't be too helpful if I don't know where I am"
        }
    },
    "Top of Temple Stairs": {
        "Chocolate Bar" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Temple Entrance": {
        "Strange note" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Creepy Library": {
        "Blue Artifact" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Tomb": {
        "Green Artifact" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Treasure Room": {
        "Red Artifact" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Demon's Lair": {
        "GPS Device" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    }
}

############  functions and classes ##############
# clear the screen based on the OS
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# move between rooms
def moveRoom():
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

# manage inventory prompts
def useInventory(inventory):
    if len(inventory == 0):
        print("You don't have any items yet!")
    else:
        # table header
        print(f"{'Item':<15}{'Description':<25}")
        print('-' * 40)

    # List available directions and rooms
    for item in inventory:
        print(f"{item:<15}{itemDescriptions[item]:<25}")
    print()

# exits game
def leave():
    input('Are you sure? (y or n)')
    while input not in ['y','n']:
        print('Invalid input')
        input('Are you sure you want to quit? (y or n)\n')
    if input == 'y':
        playing = False

# class that contains methods for room logic 
class Room:
    def __init__(self, name):
        self.name = name
        self.directions = roomsDirections[self.name]
        self.description = roomDescriptions[self.name]
        self.items = roomItems[self.name]

    def enter(self):
        print(self.description)
    
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


############  init  ##############
# room object declaration
rooms = ["Plane Wreck", "Crash Site", "Jungle Path", "Top of Temple Stairs", "Temple Entrance", "Creepy Library", "Tomb", "Treasure Room", "Demon's Lair"]

# dictionary with all room objects
roomObjMap = {x : Room(x) for x in rooms}

# init starting room, game states, and inventory
playing = True
complete = False
currentRoom = roomObjMap['Plane Wreck']
inventory = []

############  game  ##############
while playing:
    # Display current room
    print(f"You are in {currentRoom.name}.")
    print(" ")

    # ask user what to do
    print("1. Move to another room")
    print("2. Check Inventory")
    print("3. Search Room")
    print("4. Exit Game")
    command = input('What would you like to do? (enter a number)\n')

    # check if input is valid
    while command not in [1,2,3,4]:
        print('invalid input... (pick a number 1-4)')
        command = int(input('What would you like to do? (enter a number)\n'))
    # command cases
    if command == 1:
        moveRoom(currentRoom)
    elif command == 2:
        useInventory(inventory)
    elif command == 3:
        currentRoom.search()
    elif command == 4:
        leave()
    else:
        print("Not too sure how you got here.... that's a bug")

    # clear the screen
    clear_screen()

print("Thanks for Playing!!")
print(" ")
