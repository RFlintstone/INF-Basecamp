import json
from typing import List

hashmap_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, key: str = None) -> str:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    # Check if data is a string
    if not isinstance(data, str):
        raise TypeError("data must be a string")

    # Check if key is a string
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Replace single quotes with double quotes so the json can be parsed correctly
    key = key.replace("'", '"')

    # Convert the key to lower case for a case-insensitive comparison
    key = key.lower()

    # Parse string as JSON directly
    key = json.loads(key)

    # Verify if the key was converted to dict
    if not isinstance(key, dict):
        raise ValueError("Unable to convert key to JSON")

    # Initialize an empty list to store encoded values
    encoded_values = []

    # 'Encode' the data
    for letter in data:
        # Convert the letter to lower case
        letter_lower = letter.lower()
        encoded_value = key.get(letter_lower)
        # If the encoded value is None, it means the letter was not found in the key.
        if encoded_value is None:
            # Append the original letter (not converted to lower case) to the encoded_values list.
            encoded_values.append(letter)
        else:
            encoded_values.append(encoded_value)

    # Return the encoded string
    return ''.join(encoded_values)


def decode_string(data: str, key: str = None) -> str:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    if not isinstance(data, str):
        raise TypeError("data must be a string")

    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Replace single quotes with double quotes so the json can be parsed correctly
    key = key.replace("'", '"')

    # Parse string as JSON directly
    key = json.loads(key)

    # Reverse JSON key/value
    reverse_key = {v: k for k, v in key.items()}

    # Verify if the key was converted to dict
    if not isinstance(reverse_key, dict):
        raise ValueError("Unable to convert key to dict")

    # 'decode' the data
    decoded_values = []
    for letter in data:
        decoded_letter = reverse_key.get(letter)

        # if letter doesn't exist in dictionary, append original letter
        if decoded_letter is None:
            decoded_values.append(letter)
        else:
            decoded_values.append(decoded_letter)

    # Return the encoded string
    return ''.join(decoded_values)


def encode_list(data: List[str], key: str = None) -> List[str]:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Replace single quotes with double quotes so the json can be parsed correctly
    key = key.replace("'", '"')

    # Parse string as JSON directly
    key = json.loads(key)

    # Verify if the key was converted to dict
    if not isinstance(key, dict):
        raise ValueError("Unable to convert key to JSON")

    # 'Encode' the data
    encoded_values = []
    for word in data:
        encoded_word = []
        for letter in word:
            if letter != " ":
                encoded_word.append(key.get(letter))
            else:
                encoded_word.append("\n")
        encoded_values.append(''.join(encoded_word))

    return encoded_values


def decode_list(data: List[str], key: str = None) -> List[str]:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    # Check if data is a list
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    # Check if key is a string
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Replace single quotes with double quotes so the json can be parsed correctly
    key = key.replace("'", '"')

    # Parse string as JSON directly
    key = json.loads(key)

    # Reverse JSON key/value
    reverse_key = {v: k for k, v in key.items()}

    # Verify if the key was converted to dict
    if not isinstance(reverse_key, dict):
        raise ValueError("Unable to convert key to JSON")

    # 'Encode' the data
    decoded_values = []
    for word in data:
        decoded_word = ''
        for letter in word:
            if letter != " ":
                decoded_word += reverse_key.get(letter)
            else:
                decoded_word += ' '
        decoded_values.append(decoded_word)

    return decoded_values


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    # Check if encoded and decoded are both strings
    if not all(isinstance(item, str) for item in (encoded, decoded)):
        raise TypeError("Both `encoded` and `decoded` must be strings")

    # If key is provided, check if it's a string
    if key and not isinstance(key, str):
        raise TypeError("`key` must be a string")

        # Use the decoding function
    resolved = decode_string(encoded, key)

    # Return True if the decoded value matches the given decoded string, False otherwise
    return resolved == decoded


# create a function that given a key, converts to a key_hashmap (Dict) to be used for converting
# * each oneven character is the Key of the Dict, each even character is the coresponding Value
# * you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# * example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_hashmap(key: str) -> None:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    # Check if the key is a string
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Define necessary variables
    key_char = ""
    key_dict = {}

    # Check if the provided key is uneven (not valid)
    if not len(key) % 2 == 0:
        print("Invalid hashvalue input")
    else:
        # Fill the key dictionary
        for i, k in enumerate(key):
            # Use all even values as keys
            if i % 2 == 0:
                key_char = k
                key_dict[key_char] = i
            # Use all uneven values as values
            else:
                key_dict[key_char] = key[i]
        # Update dictionary
        hashmap_key_value.update(key_dict)


def run_main():
    menu_text = '''
    [E] Encode value to hashed value
    [D] Decode hashed value to normal value
    [P] Print all encoded/decoded values
    [V] Validate 2 values against eachother
    [Q] Quit program
    '''
    menu_lines = menu_text.splitlines()
    menu_stripped = [line.lstrip() for line in menu_lines]
    menu_text = '\n'.join(menu_stripped)
    print(menu_text)

    # Setup key dictionary
    encode_str = ""
    decode_str = ""
    set_hashmap(input("key?: "))

    if len(hashmap_key_value) != 0:
        while True:
            action = input("Please input a command ").upper()

            if action == "E":
                # Encode
                encoded_values.clear()
                input_data = input("TO ENCODE: ")  # Needs to be an input
                if input_data != type(list):
                    input_data = input_data.split(",")

                if len(input_data) == 1:
                    encode_str = encode_string(input_data[0], str(hashmap_key_value))
                else:
                    encode_str = encode_list(input_data, str(hashmap_key_value))
                    encode_str = "".join(encode_str)

            elif action == "D":
                # Decode
                decoded_values.clear()
                input_data = input("TO DECODE: ")  # Needs to be an input
                input_data = input_data.split(",")
                if len(input_data) == 1:
                    decode_str = decode_string(input_data[0], str(hashmap_key_value))
                else:
                    decode_str = decode_list(input_data, str(hashmap_key_value))
                    decode_str = "".join(decode_str)

            elif action == "P":
                # Prints @..@ with key: a@b.c>d#eA and input_data: abba
                print(f"Encoded String: {encode_str}")
                print(f"Decoded String: {decode_str}")

            elif action == "V":
                # Validate 2 values against eachother
                print("Validate 2 values against eachother")

            elif action == "Q":
                return


if __name__ == "__main__":
    run_main()
