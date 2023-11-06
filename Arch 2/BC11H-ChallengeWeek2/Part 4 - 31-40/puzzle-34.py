from Challenge_Resources import passages

# 34.
# - 100 athletes run a race with 5 stages.
# - Every stage the passing order is registered in a list of the ‘rugnummers’.
# You can find this in the file passages.py.
# - If the runner passes first (s)he gets 100 points,
# second 99 points, etc. For each runner the scores of the 5 stages are summed up. How many points had the winner?

# Input
stages = [
    passages.stage1,
    passages.stage2,
    passages.stage3,
    passages.stage4,
    passages.stage5,
]

# Pairs - [rugnummer, point_amount]
pairs = []

# Give each runner the correct score
for i in range(0, len(stages)):
    # Length of input / Starting number
    start_num = len(stages[i])

    # Loop through input
    for value in stages[i]:
        # Check if we are at 0 thanks to decrementing start_num. If we are
        if start_num == 0:
            # Start at 100 because we can't give 0 points
            start_num = 100

        # Create pair - [rugnummer, point_amount]
        pair = [value, start_num]

        # Append to pair list
        pairs.append(pair)

        # Decrement start_num
        start_num -= 1


# Calculate the total score of each runner
def find_total(pairs, search_val):
    total = 0
    for pair in pairs:
        if pair[0] == search_val:
            total += pair[1]
    return total


# Add the total score of each runner to the score list
score = []
for i in range(99):
    total = find_total(pairs, i)
    score.append(total)

# Sort the score list from high to low
score.sort(reverse=True)

print("Winner's score:", score[0])

# RESULT: 406
