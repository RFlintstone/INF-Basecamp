# Debugging True or False
DEBUG_MODE = False

# Create our inventory
inv = list()

# For testing purposes we do something in our inventory
inv.append("wrench")


# Create a method so we can execute 'commands'
def command(cmd_arg, action_arg):
    # Lower the command and action
    cmd_arg = cmd_arg.lower()
    action_arg = action_arg.lower()

    # If we are going to use an item
    if cmd_arg == "use":
        # Check if we have the item
        if action_arg in inv:
            # Print the inventory if debug mode is on
            if DEBUG_MODE:
                print(inv)
            # Print that we are using the item
            print("Using item: " + action_arg)
            # Remove the item from our inventory
            inv.remove(action_arg)
            # Print our (updated) inventory if debug mode is on
            if DEBUG_MODE:
                print(inv)
        # If we don't have the item we are trying to use
        else:
            # Print that we don't have the item
            print("You don't have a(n) " + action_arg + " in your inventory")


if __name__ == '__main__':
    # Set "cmd_arg" as "use" and "action_arg" as the item you want to use.
    command("use", "WRENCH")


