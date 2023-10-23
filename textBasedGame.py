# John St Hilaire
# For use in Python 3
# Text-Based game for IT140: Intro to Scripting, at SNHU
# 10/2023

import os
import time

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
        "Strange Note" : {
            "examine" : lambda: printNote()
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

artifacts = ["Blue Artifact","Red Artifact", "Green Artifact"]

############  functions and classes ##############
# clear the screen based on the OS
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def beginning_of_game():
    # ASCII Art of a Plane
    plane_art = """
        __|__|__|__
       |--|--|--|--|
       |__|__|__|__|
       |||||||||||||
       |||||||||||||
    """
    
    print(plane_art)
    time.sleep(2)
    
    print("\nOn your way by airplane to hike a remote mountain in the Andes, your plane experiences an odd")
    time.sleep(2)
    print("weather phenomena and is forced to crash land.")
    time.sleep(2)
    print("When you come to, you peer around and notice a demon looking through the wreckage.")
    time.sleep(2)
    print("To your horror, the demon becomes fixated on your radio, snatches it, and flees into the depths of the jungle.")
    time.sleep(2)
    print("You know you must retrieve it if you have any hope of being saved.")



def allowedInBossRoom(inventory):
    global artifacts
    return all(x in inventory for x in artifacts)

def printNote():
    print("To vanquish the demon, heed this clue you've been given,")
    print("Start with the heat where fiery passions are driven,")
    print("Then to the woods where silent promises are sworn,")
    print("And finally to depths, where deep blues are born.")
    print("Arrange in this sequence, and the demon will be torn.")

# move between rooms
def moveRoom():
    global currentRoom
    global inventory
    global roomItems
    clear_screen()
    print(f"{'Direction':<15}{'Room':<25}")
    print('-' * 40)

    for direction, room in currentRoom.directions.items():
        print(f"{direction:<15}{room:<25}")
    print()

    newDirection = input("Which direction would you like to go?\n").capitalize()

    while True:
        if newDirection not in currentRoom.directions:
            print("Invalid direction.")
        elif currentRoom.directions[newDirection] == "Demon's Lair" and not allowedInBossRoom(inventory):  # Ensure the right inventory variable is used
            print("You are not allowed in the boss room.")
        else:
            break
        newDirection = input("Which direction would you like to go?\n").capitalize()

    if newDirection != "Exit":
        currentRoom = roomObjMap[currentRoom.directions[newDirection]]


# exits game
def leave():
    global playing
    clear_screen()
    leaveInput = input('Are you sure? (y or n)')
    while leaveInput not in ['y', 'n']:
        print('Invalid input')
        leaveInput = input('Are you sure you want to quit? (y or n)\n')
    if leaveInput == 'y':
        playing = False


# manage inventory prompts
def useInventory(inventory):
    global itemDescriptions
    if len(inventory) == 0:
        print("You don't have any items yet!")
    else:
        print('You currently have: ')
        for item in inventory:
            print(f'- {item}')
        use = input('Would you like to use an item? (yes/no)\n').lower()
        if use == 'yes':
            useWhich = input('Which item would you like to use?\n').lower()
            if useWhich in inventory:
                print(itemDescriptions[useWhich])
            else:
                print('You do not have that item.')
        else:
            print('You chose not to use an item.')

def bossRoom():
    global roomItems

    # Assuming these are available in the global scope
    global artifacts, clear_screen, printNote, playing

    print("As you step into the chamber, the temperature spikes and an overwhelming sense of dread washes over you. Your eyes are immediately drawn to a grotesque figure—a Jungle Demon, bound by enchanted chains that seem to struggle against its immense strength. Its eyes lock onto yours, and for a brief moment, it feels like it's peering into your soul.\n")
    time.sleep(2)
    print("Your attention shifts momentarily, and you notice the radio lying haphazardly on the ground near the demon. It's old and battered, but you can't shake the feeling that it might be important.\n")
    time.sleep(2)
    print("Lastly, your gaze wanders to a large monument on the wall. Intricately carved runes adorn its surface, and a sense of familiarity strikes you; it closely resembles the monument described in that strange note you found earlier. The weight of the room seems to press on you even more, as if urging you to act quickly.")
    time.sleep(2)
    print("You frantically pull out the strange note you found in the temple entrance and read it...")

    printNote()

    answers = []

    for _ in range(3):
        for i, x in enumerate(artifacts):
            print(f"{i+1}.{x}")
        ans = int(input(f'What artifact goes in the slot?')) - 1
        answers.append(artifacts[ans])
        artifacts.pop(ans)
        clear_screen()
        printNote()

    if answers == ["Red Artifact", "Green Artifact", "Blue Artifact"]:
        print("A blinding light fills the chamber as the artifacts resonate with the monument.")
        time.sleep(2)
        print("The chains around the Jungle Demon glow red hot and start to disintegrate into ashes.")
        time.sleep(2)
        print("The demon lets out an ear-piercing roar as it struggles against the energy, but it's too late.")
        time.sleep(2)
        print("With a final cry, the demon disintegrates into a cloud of dark smoke, leaving the chamber in silence.")
        time.sleep(2)
        print("You feel a surge of relief and triumph. The Jungle Demon is vanquished!")
        time.sleep(2)
        print("You walk over to the Demon and find your radio! It still has battery!")
        time.sleep(2)
        print("Time to find a high place so I can call for some help! I think I'll eat that chocolate bar now....")
        time.sleep(2)
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
        print(self.description)

    # search room for items and user choice to pick up item
    def search(self, inventory):
        clear_screen()
        if self.items:
            for key, value in self.items.items():
                print(f'You picked up a {key}')
                inventory.append(key)
            self.items.clear()
        else:
            print("There's nothing of use you can find in here.")



############  init  ##############
# room object declaration
rooms = ["Plane Wreck", "Crash Site", "Jungle Path", "Top of Temple Stairs", "Temple Entrance", "Creepy Library", "Tomb", "Treasure Room", "Demon's Lair"]

# dictionary with all room objects
roomObjMap = {x : Room(x) for x in rooms}

# init starting room, game states, and inventory
playing = True
complete = False
currentRoom = roomObjMap['Crash Site']
inventory = []

############  game  ##############

clear_screen()

beginning_of_game()

while playing:

    if currentRoom.name == "Demon's Lair":
        bossRoom()
    else:
        # Display current room
        print(f"You are in {currentRoom.name}.")
        print(" ")

        print(currentRoom.description)
        
        print(" ")

        # ask user what to do
        print("1. Move to another room")
        print("2. Check Inventory")
        print("3. Search Room")
        print("4. Exit Game")
        command = int(input('What would you like to do? (enter a number)\n'))

        # check if input is valid
        while command not in [1,2,3,4]:
            print('invalid input... (pick a number 1-4)')
            command = int(input('What would you like to do? (enter a number)\n'))
        # command cases
        if command == 1:
            moveRoom()
        elif command == 2:
            useInventory(inventory)
        elif command == 3:
            currentRoom.search(inventory)
        elif command == 4:
            leave()
        else:
            print("Not too sure how you got here.... that's a bug")

        # clear the screen
        #clear_screen()
print(" ")
print("Thanks for Playing!!")
print(" ")



