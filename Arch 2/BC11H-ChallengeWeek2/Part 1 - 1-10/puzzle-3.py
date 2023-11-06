from util import bruteforce

items = [hex(i).strip("0x") for i in range(0x28BFF, 0xF8B72)]
items = [item + ("0" * (5 - len(item))) for item in items]
# voor de andere kant op
items.reverse()

# result: higher than 0x28bff, lower than 0xf8b72

print(
    "result:",
    bruteforce.send_items(
        items,
        "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnx9zych000god0uunqh33j7",
    ),
)
