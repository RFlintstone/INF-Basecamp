import commands as c

rooms = {
    'Start': {
        'description': 'You are in a small room with a wooden chest in the corner.',
        'exits': {'east': 'Hallway'},
        'items': ['small key'],
        'npcs': ['Bob']
    },

    'Hallway': {
        'description': 'You are in a long hallway.',
        'exits': {'west': 'Start', 'north': 'Dungeon'},
        'items': [],
        'npcs': []
    },

    'Dungeon': {
        'description': 'You are in a dark dungeon.',
        'exits': {},
        'items': ['torch'],
        'npcs': []
    }
}

# Add item to library
c.add_inv("small key")

stop_loop = False


def hallway1():
    # Set starting room
    current_room = 'Hallway'

    # Print current room description
    print(rooms[current_room]['description'])

    i = input("What do you want to do?").split(" ")
    print(i)

    # Call GO c.command
    go = c.command(i[0], i[1])

    if i[0].lower() == "go" and go == ("N" or "E" or "S" or "W"):
        current_room = rooms[current_room]['exits']['north']
        print(rooms[current_room]['description'])
        stop_loop = True

    # Call INSPECT c.command on chest
    if i[0].lower() == "inspect":
        inspect = c.command("inspect", "chest")
        print("INSPECT: " + str(inspect))

    # Call USE c.command on key
    if i[0].lower() == "use":
        use = c.command("use", "small key")
        print("USE: " + str(use))

    if i[0].lower() == "use" and use is True:
        print("Unlocked chest.")

    # Call TALK c.command
    if i[0].lower() == "talk":
        talk = c.command("talk", "bob")
        print("TALK: " + str(talk))

    if i[0].lower() == "talk" and talk is True:
        print("Dialog with Bob")


while stop_loop is False:
    hallway1()
