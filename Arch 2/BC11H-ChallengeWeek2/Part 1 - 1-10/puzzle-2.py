from util import bruteforce

items = [i for i in range(1000, 10000)]

print(
    "result:",
    bruteforce.send_items(
        items,
        "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnx9tkno000eod0uw64boukk",
    ),
)

# RESULT: 2704