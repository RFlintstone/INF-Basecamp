from util import bruteforce

bits = [False for _ in range(8)]
items = []

while True:
    items.append("".join(["0" if bit else "1" for bit in bits]))
    for index, bit in enumerate(bits):
        if bit == False:
            bits[index] = True
            break
        else:
            bits[index] = False
    else:
        break

items = set(items)

print(
    "result:",
    bruteforce.send_items(
        items,
        "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnyhzo5p000kod0uqgornh1i",
    ),
)

# RESULT: 00101010
