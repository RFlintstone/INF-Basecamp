def juggler_sequence_count(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = int(n**0.5)
        else:
            n = int(n**1.5)
        count += 1
    return count


def find_smallest_n(processed_count):
    n = 1
    while True:
        if juggler_sequence_count(n) == processed_count:
            return n
        n += 1


smallest_n = find_smallest_n(51)

print(smallest_n)

# RESULT: 7795
