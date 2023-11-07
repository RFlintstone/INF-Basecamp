a = 35
b = 146
c = 1736

for i in range(100000):
    result = (a - i) * (b - i) * (c - i)
    if result == 606029204:
        print(f"i = {i}")