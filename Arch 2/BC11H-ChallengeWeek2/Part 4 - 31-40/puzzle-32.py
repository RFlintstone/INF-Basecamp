from util import bruteforce

print(
    "result: ",
    bruteforce.send_items(
        [i for i in range(10000)],
        "https://api.codehunt.nl/categories/clnx70w23000aod0ux45tp5jm/exercises/clo05dtca000sp40uhqm6pk3m",
    ),
)

# RESULT: 744
