import json
import commands as c

# Add item to library
c.add_inv("small key")


def setup_room(my_room_name):
    with open('rooms.json') as f:
        rooms = json.load(f)

    # Set starting room
    current_room = my_room_name.capitalize()

    # Print current room description
    print(rooms[current_room]['description'])

    return rooms, current_room


def hallway1(rooms, current_room):
    stop_loop = False

    i = input("What do you want to do?").split(" ")
    # print(i)

    if len(i) < 2:
        print("You didn't specify an action")
        stop_loop = False
        return stop_loop
    else:
        # Call GO c.command
        go = c.command(i[0], i[1])

        if i[0].lower() == "go" and go == ("N" or "E" or "S" or "W"):
            current_room = rooms[current_room]['exits']['north']
            print(rooms[current_room]['description'])
            stop_loop = True

        # Call INSPECT c.command on chest
        if i[0].lower() == "inspect":
            inspect = c.command("inspect", i[1])
            print("INSPECT: " + str(inspect))

            if inspect == "room":
                print(rooms[current_room]['inspect_description'])

            if inspect == "exit" or inspect == "exits":
                d = rooms[current_room]['exits']
                print("You see exits on the following sides:")
                print(', '.join(d.keys()))

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

        print("\n")
        return stop_loop


stop_loop_ = False
room_json, room_name = setup_room("Hallway")

while stop_loop_ is False:
    stop_loop_ = hallway1(room_json, room_name)
