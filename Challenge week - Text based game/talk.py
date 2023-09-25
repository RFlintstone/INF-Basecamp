import speak as dialog

# Debugging True or False
DEBUG_MODE = False


# Create a method so we can execute 'commands'
def command(cmd_arg, action_arg):
    action_doable = False

    # Lower the command and action
    cmd_arg = cmd_arg.lower()
    action_arg = action_arg.lower()

    # If we are going to use an item
    if cmd_arg == "talk":
        if dialog.dialog_check(action_arg, "greeting", 0):
            action_doable = True
            dialog.dialog_trigger("user", "greeting", 0)
            dialog.dialog_trigger(action_arg, "greeting", 0)
        return action_doable


if __name__ == '__main__':
    talk = command("talk", "bob")
    print(talk)