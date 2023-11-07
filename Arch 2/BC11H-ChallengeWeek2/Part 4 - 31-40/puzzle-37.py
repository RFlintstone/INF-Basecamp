def bcs_decode(encoded_message, key):
    # Convert the key into a list of digits in reverse order
    key_digits = list(map(int, str(key)))[::-1]

    # Start with the encoded message
    message = encoded_message

    # Repeat the process for each digit in the key
    for digit in key_digits:
        # Split the message into groups of size 'digit'
        groups = [message[i : i + digit] for i in range(0, len(message), digit)]

        # Reverse each group
        reversed_groups = [group[::-1] for group in groups]

        # Combine the reversed groups into a single string
        message = "".join(reversed_groups)

    decoded_message = "".join(reversed_groups)

    return decoded_message


def bcs_encode(message, key):
    message = str(message).replace(" ", "")

    key_digits = list(map(int, str(key)))
    # Start with the encoded message
    encoded_message = message

    # Repeat the process for each digit in the key
    for digit in key_digits:
        # Split the message into groups of size 'digit'
        groups = [
            encoded_message[i : i + digit]
            for i in range(0, len(encoded_message), digit)
        ]

        # Reverse each group
        reversed_groups = [group[::-1] for group in groups]

        # Combine the reversed groups into a single string
        encoded_message = "".join(reversed_groups)

    return encoded_message


encoded_message = "TRIEHERTSUOSELCEHAOTHTESNRUIOEABWR"

all_things = {}
with open(
    "out.lst",
    "w",
) as file:
    for key in range(22222, 100000):
        if "0" in str(key):
            continue
        else:
            decoded = bcs_decode(encoded_message, key)
            if "WINE" in decoded:
                print(key, decoded)

# 29128 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 29182 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 29218 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 29281 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 29812 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 29821 RCETEITHSRUESSLOEEBOAATHTORHRWINEU
# 34643 TIRRSSETEOUHTCLOSHEEAETHBURARWINEO
# 43234 TIRRSSETEOUHTCLOSHEEAETHBURARWINEO

# 45283 THETREASUREISCLOSETOTHEWINEHARBOUR - not accepted
# 45823 THETREASUREISCLOSETOTHEWINEHARBOUR - accepted
