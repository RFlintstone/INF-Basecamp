from numba import jit

from util import bruteforce


@jit(nopython=True)  # Set "nopython" mode for best performance, equivalent to @njit
def run():
    items = []

    for i in range(0x9AEA5, 0xD7449):
        # Hex logic without hex() call
        s = ""
        while i > 0:
            digit = i % 16
            if digit < 10:
                s = str(digit) + s
            else:
                s = chr(ord("a") + digit - 10) + s
            i //= 16

        if len(s) < 5:
            s = (5 - len(s)) * "0" + s

        items.append(s)

    items.reverse()
    return items


items = run()
result = bruteforce.send_items(
    items,
    "https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnx9zych000god0uunqh33j7",
)
print(result)
