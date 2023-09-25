# variables for possible directions and direction output (interchangeable between rooms)
directions = ["west", "east", "north", "south"]
move_to = ""


# use established command system to defin a new command.
def command(cmd_arg, act_arg):
    # lower cmd and arg to get easier standards
    cmd_arg = cmd_arg.lower()
    act_arg = act_arg.lower()

    # check for go command
    if cmd_arg == "go":
        # check if the direction is possible and give them individual outpust for ease of use
        if act_arg in directions:
            move_to = act_arg[0].upper()

        # extra print in case the user does not input a wind direction
        else:
            move_to = "Fail"

        print(move_to)


command("go","south")

