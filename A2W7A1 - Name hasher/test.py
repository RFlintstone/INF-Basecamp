import json

key = str({'a': '@', 'b': '.', 'c': '>', 'd': '#', 'e': 'A'})

# Remove outer quotes
key = key.replace("'", '"')

# Parse string as JSON directly
dict_key = json.loads(key)

print(dict_key)