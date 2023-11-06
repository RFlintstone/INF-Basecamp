list = []

for i in range(1, 1001):
    if len(str(i)) == 1:
        list.append(i)
    else:
        for l in str(i):
            list.append(int(l))

total = 0

for i in range(1000):
    total += list[i]

print(total)

# RESULT: 3738
