# Create our inventory
inv = list()

# For testing purposes we do something in our inventory
inv.append("wrench")


def command(cmd_arg, action_arg):
    # Lower the command and action
    cmd_arg = cmd_arg.lower()
    action_arg = action_arg.lower()

    # If we are going to use an item
    if cmd_arg == "use":
        # Check if we have the item
        if action_arg.lower() in inv:
            # Print the inventory
            print(inv)
            # Print that we are using the item
            print("Using item: " + action_arg)
            # Remove the item from our inventory
            inv.remove(action_arg)
            # Print our (updated) inventory
            print(inv)
        # If we don't have the item we are trying to use
        else:
            # Print that we don't have the item
            print("You don't have a(n) " + action_arg + " in your inventory")


if __name__ == '__main__':
    # Set "cmd_arg" as "use" and "action_arg" as the item you want to use.
    command("use", "WRENCH")
