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
    "Plane Wreck" : "The twisted metal and debris of the plane lie scattered around you. The scent of fuel fills the air, and the remnants of passenger belongings are strewn about. It's a grim reminder of how you got here.",
    "Crash Site" : "Just beyond the wreckage, trees are knocked over, forming a path of destruction through the dense jungle. Smoke rises lazily into the sky, making it easier for anyone—or anything—to find you.",
    "Jungle Path" : "You are surrounded by towering trees, their leaves forming a natural canopy that filters the sunlight. The path is narrow and overgrown, and you can hear the distant sounds of wildlife. The air is thick and humid.",
    "Top of Temple Stairs" : "You stand at the top of a grand staircase, each step worn from years of use. You can see the surrounding jungle stretching out below you, a sea of green. The entrance to the temple beckons.",
    "Temple Entrance" : "Ornate carvings decorate the stone walls, telling stories of gods and warriors. A sense of awe washes over you as you step into the dimly lit entrance. It's both foreboding and inviting.",
    "Creepy Library" : "Rows of ancient books line the walls, their spines cracked and faded. Cobwebs hang from the ceiling, and a sense of forgotten knowledge fills the air. A lone artifact glows on a pedestal in the center.",
    "Tomb" : "You are now in a dim chamber, lit only by the glow of an artifact. Hieroglyphics cover the walls, and a sarcophagus sits in the middle of the room. The air is stale, filled with the weight of centuries.",
    "Treasure Room" : "Your eyes widen as they fall upon heaps of gold, jewels, and artifacts of untold value. The room is richly decorated, and a red artifact pulsates mysteriously on a lavish pedestal.",
    "Demon's Lair" : "The atmosphere changes drastically, the air becoming hot and sulfurous. Flames flicker on the walls, casting grotesque shadows. A sense of malevolence hangs heavy, as if you're being watched by unseen eyes."
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
        "GPS device" : {
            "examine" : "My GPS Device! Now if I can find my radio I can call for some help.."
        }
    },
    "Top of Temple Stairs": {
    },
    "Temple Entrance": {
        "Strange note" : {
            "examine" : "It's not much but it will have to do for now..."
        }
    },
    "Creepy Library": {
        "Blue Artifact" : {
            "examine" : "This blue artifact glows with an eerie light, illuminating the dust-covered books around it. An aura of arcane power emanates from it, suggesting that it holds secrets yet to be unlocked."
        }
    },
    "Tomb": {
        "Green Artifact" : {
            "examine" : "The green artifact is embedded in a stone pedestal. Its glow pierces through the darkness of the tomb. You can feel it humming, as if vibrating to an otherworldly rhythm. It's both unsettling and fascinating."
        }
    },
    "Treasure Room": {
        "Red Artifact" : {
            "examine" : "Surrounded by piles of gold and jewels, the red artifact steals your attention. It pulses like a heart, and warmth radiates from it, as though it's alive. It feels as if it's beckoning you to wield its mysterious power."
        }
    },
    "Demon's Lair": {
        "GPS Device" : {
            "examine" : "Finally I can call for some help!"
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
