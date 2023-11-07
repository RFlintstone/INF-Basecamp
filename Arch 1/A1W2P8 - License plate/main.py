# Consider a valid license plate in The Netherlands (see valid patterns below).
# Write a program that begins by reading a string of characters from the user.
# Then your program should display a message indicating whether the characters are representing a valid license plate.
#
# Valid patterns:
# ✓ XX-99-99
# ✓ 99-XX-XX
# ✓ 99-99-XX
# ✓ XX-XX-99
# ✓ 99-XX-99
# ✓ XX-99-XX
# ✓ 99-XXX-9
# ✓ XX-999-X
# ✓ 9-XXX-99
# ✓ X-999-XX
# ✓ XXX-99-X
# ✓ 9-XX-999

#
# Input examples:
# License: A-149-HH
# License: 149-A-HH
#
# Output examples:
# Valid
# Invalid

def validate_license(license):
    # Split into parts
    parts = license.split("-")
    print(parts)
    # print(parts[0])
    # print(parts[1])
    # print(parts[2])

    # Validate format
    if len(parts) != 3:
        return False

    if parts[2].isnumeric() != parts[0].isnumeric():
        return False

    # XX-99-99
    # 99-XX-XX
    if parts[1] == parts[2] and parts[0] != parts[1]:
        return True

    # 99-99-XX
    # XX-XX-99
    if parts[0] == parts[1] and parts[0] != parts[2]:
        return True

    # 99-XX-99
    # XX-99-XX
    if parts[0] == parts[2] and parts[0] != parts[1]:
        return True

    if parts[0] != parts[1] and parts[0] != parts[2]:
        # 99-XXX-9
        # XX-999-X
        # XXX-99-X
        if (len(parts[0]) + len(parts[1])) == 5 and len(parts[2]) == 1:
            return True

        # 9-XXX-99
        # X-999-XX
        # 9-XX-999
        if (len(parts[1]) + len(parts[2])) == 5 and len(parts[0]) == 1:
            return True


def _main_():
    license = input("License: ")
    if validate_license(license):
        print("Valid")
    else:
        print("Invalid")

_main_()