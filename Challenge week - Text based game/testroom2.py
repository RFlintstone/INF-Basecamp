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


room_json, room_name = setup_room("hallway")


def start_room():
    print("Hallway")
    setup_room("dungeon")


def hallway():
    print("Hallway")
    setup_room("dungeon")


def dungeon():
    print("Dungeon")


while True:
    if room_name == "start":
        start_room()
    if room_name == "hallway":
        hallway()
    if room_name == "dungeon":
        dungeon()
