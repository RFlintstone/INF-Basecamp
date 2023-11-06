from util import bruteforce

items = [i for i in range(1000, 10000)]
items.reverse()

print(
    "result:",
    bruteforce.send_items(
        items,
        "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnx7862s000cod0ukp5u511h",
    ),
)

# RESULT: 7977
