dict_key_value = {}
encoded_values = []
decoded_values = []


# create a function that given the input string converts it to the encoded equivalent based on the provided or
# already set key/hashmap make sure to only convert values that are in the key, if the value is not present,
# use its own value
def encode_string(data: str, key: str = None) -> str:
    print("")
    return ""


# create a function that given the input string converts it to the decoded equivalent based on the provided or
# already set key/hashmap make sure to only decode values that are in the key, if the value is not present,
# use its own value
def decode_string(data: str, key: str = None) -> str:
    print("")
    return ""


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the
# key/hashmap you can use the already created encode function when looping through the list tip! make use of the map
# function within python with a lambda to call the internal function with all elements as a return value, you should
# return a list with Tuples containing the decoded value as first value and the encode value as second value
def encode_list(data: list, key: str = None) -> list:
    print("")
    return []


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the
# key/hashmap you can use the already created decode function when looping through the list tip! make use of the map
# function within python with a lambda to call the internal function with all elements as a return value, you should
# return a list with Tuples containing the decoded value as first value and the encode value as second value
def decode_list(data: list, key: str = None) -> list:
    print("")
    return []


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    print("")
    return True


# give the option to input a hashvalue to be used/converted to a key
# each uneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    # Define lambda function to check if value is even
    even = lambda x: x % 2 == 0

    # Define necessary variables
    key_char = ""
    dict = {}

    # Check if the provided key is uneven (not valid)
    if not even(len(key)):
        print("Invalid hashvalue input")
    else:
        # Fill the key dictionary
        for i, k in enumerate(key):
            # Use all even values as keys
            if even(i):
                key_char = k
                dict[key_char] = i
            # Use all uneven values as values
            else:
                dict[key_char] = key[i]
        # Print dictionary key
        print(dict)

# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    set_dict_key("a@b.c>d#eA")


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
