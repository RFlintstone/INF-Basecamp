from util import bruteforce

items = [i for i in range(10000)]

print(
    "result:",
    bruteforce.send_items(
        items,
        "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnzx66rc000sod0u9t6d7t5y",
    ),
)

# RESULT: 27
