import json
import commands as c

# Add item to library
c.add_inv("key")

"""
Setup/load a new room.
Usage: room_json, room_name = setup_room("ROOM_NAME")
Returns: tuple (the whole json and the room name)
Prints: room description from json 
"""


def setup_room(my_room_name):
    # Load json content from rooms.json
    with open('rooms.json') as f:
        rooms = json.load(f)

    # Set starting room
    current_room = my_room_name.lower()

    # Print current room description
    print(rooms[current_room]['description'])

    return rooms, current_room

def ask_room(action, rooms, current_room):
  # Going into another room
    if action in ["west", "east", "north", "south"]:
        direction = action

    if direction not in rooms[current_room]['exits']:
        print("There is no exit here. Maybe use your compass?")

    if direction in rooms[current_room]['exits']:
        current_room = rooms[current_room]['exits'][direction]
        print(rooms[current_room]['description'])
        setup_room(current_room)


def start_room():
    # Getting an input from the player
    i = input("What do you want to do?").split(" ")

    # Check if we give both an action and an argument
    if len(i) < 2:
        print("You didn't specify an action")
    else:
        # Execute command
        action = c.command(i[0], i[1])
        print(action)

        if i[0] == "go":
            room_json, room_name = setup_room("start")
            ask_room(action, room_json, room_name)


def hallway():

    # Getting an input from the player

    i = input("What do you want to do?").split(" ")

    if len(i) < 2:
        print("You didn't specify an action")
    else:
        action = c.command(i[0], i[1])

        if i[0] == "go":
            room_json, room_name = setup_room("hallway")
            ask_room(action, room_json, room_name)


def dungeon():

    # Getting an input from the player

    i = input("What do you want to do?").split(" ")

    if len(i) < 2:
        print("You didn't specify an action")
    else:
        action = c.command(i[0], i[1])

        if i[0] == "go":
            room_json, room_name = setup_room("dungeon")
            ask_room(action, room_json, room_name)

room_name = "start"

# Ensure that the right room_function runs based on room_name
not_finished = True
while not_finished:
    if room_name == "start":
        start_room()
    if room_name == "hallway":
        hallway()
    if room_name == "dungeon":
        dungeon()
    not_finished = True

else:
    print("yay you won")
