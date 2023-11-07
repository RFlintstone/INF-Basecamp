# 4. Alice is in a very strange elevator: when you press UP, the elevator goes from x to 3x+1 and when you press
# DOWN and the number is even, it goes to x//2 otherwise the lift goes to x+1. So if you are at 13 and press UP,
# DOWN, DOWN you are at 10. After UP, DOWN you are at 32.
# Alice starts at 1 and presses:
# UUUUUUUUUUUUDDDDDDDDDDDDDDDDDDDDDDDDUDUDUDUDUDUDUDUDUDUDDDD
# DDDDDDDDDDDDDUDUDUDUDUDDDUUUUUUDDDDUDUDUDUDUDDDDDDDDDUUDDDU
# DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

# UP: x = 3*x+1
# DOWN:
#   - Even: x = x//2
#   - Else: x += 1

instructions = "UUUUUUUUUUUUDDDDDDDDDDDDDDDDDDDDDDDDUDUDUDUDUDUDUDUDUDUDDDDDDDDDDDDDDDDDUDUDUDUDUDDDUUUUUUDDDDUDUDUDUDUDDDDDDDDDUUDDDUDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
instructions = list(instructions)


def up(x_value):
    x_value = 3 * x_value + 1
    print("UP", x_value)
    return x_value


def down(x_value):
    if x_value % 2 == 0:
        x_value = x_value // 2
    else:
        x_value += 1
    print("DOWN", x_value)
    return x_value


x = 1
for i in instructions:
    if i.upper() == "U":
        x = up(x)
    if i.upper() == "D":
        x = down(x)
print(x)

# RESULT: 53
