# Consider a valid license plate in The Netherlands (see valid patterns below).
# Write a program that begins by reading a string of characters from the user.
# Then your program should display a message indicating whether the characters are representing a valid license plate.
#
# Valid patterns:
# ✓ XX-99-99
# ✓ 99-99-XX
# - 99-XX-99
# - XX-99-XX
# ✓ XX-XX-99
# ✓ 99-XX-XX
# - 99-XXX-9
# - 9-XXX-99
# - XX-999-X
# - X-999-XX
# - XXX-99-X
# - 9-XX-999
#
# Input examples:
# License: A-149-HH
# License: 149-A-HH
#
# Output examples:
# Valid
# Invalid

license_plate = input()
license_plate_length = len(license_plate)

good = 0

print(license_plate_length)

# XX-99-99
# 9-XXX-99
# XXX-99-X
if license_plate_length == 8:
    if license_plate[2] == "-" and license_plate[5] == "-":
        if (license_plate[0] + license_plate[1]) == (license_plate[3] + license_plate[4]):
            if (license_plate[6] + license_plate[7]) != (license_plate[3] + license_plate[4]):
                good = 1
        if (license_plate[3] + license_plate[4]) == (license_plate[6] + license_plate[7]):
            if (license_plate[0] + license_plate[1]) != (license_plate[3] + license_plate[4]):
                good = 1

    if license_plate[2] == "-" and license_plate[5] == "-":


    if good:
        print("Valid")
    else:
        print("Not Valid")

else:
    print("Lince plate length is NOT correct!")
