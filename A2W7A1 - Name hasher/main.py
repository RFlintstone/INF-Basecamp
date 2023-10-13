import json

dict_key_value = {}
encoded_values = []
decoded_values = []


# create a function that given the input string converts it to the encoded equivalent based on the provided or
# already set key/hashmap make sure to only convert values that are in the key, if the value is not present,
# use its own value
def encode_string(data: str, key: str = None) -> str:
    # a@b.c>d#eA
    # Check if data is a string
    if not isinstance(data, str):
        raise TypeError("data must be a string")

    # Check if key is a string
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
    for letter in data:
        encoded_values.append(key.get(letter))

    # Return the encoded string
    return ''.join(encoded_values)


# create a function that given the input string converts it to the decoded equivalent based on the provided or
# already set key/hashmap make sure to only decode values that are in the key, if the value is not present,
# use its own value
def decode_string(data: str, key: str = None) -> str:
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
        raise ValueError("Unable to convert key to JSON")

    # 'decode' the data
    for letter in data:
        decoded_values.append(reverse_key.get(letter))

    # Return the encoded string
    return ''.join(decoded_values)


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the
# key/hashmap you can use the already created encode function when looping through the list tip! make use of the map
# function within python with a lambda to call the internal function with all elements as a return value, you should
# return a list with Tuples containing the decoded value as first value and the encode value as second value
def encode_list(data: list, key: str = None) -> list:
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
    encoded = []
    for word in data:
        for letter in word:
            if letter != " ":
                encoded.append(key.get(letter))
            else:
                encoded.append("\n")

    encoded_values.extend(encoded)

    return encoded_values


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the
# key/hashmap you can use the already created decode function when looping through the list tip! make use of the map
# function within python with a lambda to call the internal function with all elements as a return value, you should
# return a list with Tuples containing the decoded value as first value and the encode value as second value
def decode_list(data: list, key: str = None) -> list:
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
    decoded = []
    for word in data:
        for letter in word:
            if letter != " ":
                decoded.append(reverse_key.get(letter))
            else:
                decoded.append("\n")

    decoded_values.extend(decoded)

    return decoded_values


# create a function that given an encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    # Check if encoded is a string
    if not isinstance(encoded, str):
        raise TypeError("encoded must be a string")

    # Check if decoded is a string
    if not isinstance(decoded, str):
        raise TypeError("decoded must be a string")

    # Check if key is a string
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    print("")
    return False


# give the option to input a hashvalue to be used/converted to a key
# each uneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
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
        dict_key_value.update(key_dict)


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    # Setup key dictionary
    encode_str = ""
    decode_str = ""
    set_dict_key(input("key?: "))

    if len(dict_key_value) != 0:
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

        while True:
            action = input("Please input a command ").upper()

            if action == "E":
                # Encode
                encoded_values.clear()
                input_data = input("TO ENCODE: ")  # Needs to be an input
                input_data = input_data.split(",")
                if len(input_data) == 1:
                    encode_str = encode_string(input_data[0], str(dict_key_value))
                else:
                    encode_str = encode_list(input_data, str(dict_key_value))
                    encode_str = "".join(encode_str)

            elif action == "D":
                # Decode
                decoded_values.clear()
                input_data = input("TO DECODE: ")  # Needs to be an input
                input_data = input_data.split(",")
                if len(input_data) == 1:
                    decode_str = decode_string(input_data[0], str(dict_key_value))
                else:
                    decode_str = decode_list(input_data, str(dict_key_value))
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


# Create an unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    (lambda x: print(x))("=" * 70)
    main()
