def recaman_sequence(n):
    seq, seen = [0], set()
    for i in range(1, n):
        prev = seq[-1]
        if prev - i > 0 and prev - i not in seen:
            seq.append(prev - i)
        else:
            seq.append(prev + i)
        seen.add(seq[-1])
    return seq[n - 1]


print(recaman_sequence(1000))

# RESULT: 2686