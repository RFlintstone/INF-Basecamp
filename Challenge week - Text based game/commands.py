import json

import dialog_trigger as dialog

# Debugging True or False
DEBUG_MODE = False

# Create our inventory
inv = list()
# Room
current_room = ""

if DEBUG_MODE:
    inv.append("wrench")

# Create a method so we can execute 'commands'
def command(cmd_arg, action_arg):
    action_doable = False

    # Lower the command and action
    cmd_arg = cmd_arg.lower()
    action_arg = action_arg.lower()

    # check for go command
    if cmd_arg == "go":
        # variables for possible directions and direction output (interchangeable between rooms)
        directions = ["west", "east", "north", "south"]

        # check if the direction is possible and give them individual outpust for ease of use
        if action_arg in directions:
            move_to = action_arg

        # extra print in case the user does not input a wind direction
        else:
            move_to = None

        return move_to

    # If we are going to use an item
    if cmd_arg == "use":
        # Check if we have the item
        if action_arg in inv:
            # Print that we are using the item
            print("Using item: " + action_arg)
            # Remove the item from our inventory
            inv.remove(action_arg)
            # Make us able to return the item we just used
            action_doable = "u_" + action_arg
        # If we don't have the item we are trying to use
        else:
            # Print that we don't have the item
            print("You don't have a(n) " + action_arg + " in your inventory")
            action_doable = "not_in_inv"

    # check for the inspect command
    if cmd_arg == "inspect":
        if action_arg == "inv" or action_arg == "inventory":
            print(inv)

        if action_arg.lower() in interactable:
            action_doable = "i_" + action_arg
        else:
            print("There is nothing like that in this room.")

    # If we want to talk
    if cmd_arg == "talk":
        if dialog.dialog_check(action_arg, "greeting", 0):
            action_doable = True
            dialog.dialog_trigger("user", "greeting", 0)
            dialog.dialog_trigger(action_arg, "greeting", 0)
        return action_doable

    return action_doable


def add_inv(item):
    inv.append(item)


if __name__ == '__main__':
    # Return N, E, S, W or None
    # Set "cmd_arg" as "go" and "action_arg" as the direction you want to walk in.
    go = command("go", "north")
    print("GO: " + go)

    # Return True or False
    # Set "cmd_arg" as "use" and "action_arg" as the item you want to use.
    use = command("use", "wrench")
    print("USE: " + str(use))

    # Return item which is inspected
    # Set "cmd_arg" as "inspect" and "action_arg" as the item you want to inspect.
    inspect = command("inspect", "chest")
    print("INSPECT: " + str(inspect))

    inspect = command("inspect", "inv")
    print("INSPECT: " + str(inspect))

    # Return True or False
    # Set "cmd_arg" as "talk" and "action_arg" as the person you want to talk to.
    talk = command("talk", "bob")
    print("TALK: " + str(talk))
