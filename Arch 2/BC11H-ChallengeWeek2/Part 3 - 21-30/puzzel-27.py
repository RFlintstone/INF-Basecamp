def set_sequence(shift_instructions, sequence_length, shift_sequence=[7]):
    sequence_nrs = []
    print(shift_instructions)
    for i in range(1, sequence_length + 1):
        if len(sequence_nrs) == 0:
            sequence_nrs.append(shift_instructions[0])
        else:
            next_shift = shift_sequence[-1] + shift_instructions[1]
            shift_sequence.append(next_shift)
            sequence_nrs.append(shift_sequence[-1])

    # print(f"{len(sequence_nrs)}::{sequence_nrs}")

    return sequence_nrs


def decode_string(encoded_text, sequence):
    decoded_string = []
    for pos, letter in enumerate(encoded_text):
        shift = sequence[pos % len(sequence)]  # Use the sequence cyclically
        while shift > 26:
            shift -= 26  # Ensure the shift value is within the range 1 to 26
        decoded_char = chr((ord(letter) - shift - ord('A')) % 26 + ord('A'))
        decoded_string.append(decoded_char)
    return ''.join(decoded_string)

# Text we'll check on
encoded_text = "CIJLRMAQFUPVEKHSMUEZFULZGLYFWJOSVMJNFGAXWNARWQFOFGDXKFQ"
common_words = {"the", "and", "you", "that", "for", "with", "this", "not", "are", "but", "have", "what", "can", "your",
                "all", "when", "one", "they", "how", "from"}

# Convert  to uppercase
common_words = {word.upper() for word in common_words}
encoded_text = encoded_text.upper()  # Convert to uppercase once

# Store possible answers
possible_answer = []

# Decode string with ever-changing sequence
for x in range(0, 20):
    for y in range(0, 100):
        sequence = set_sequence([x, y], 100)
        result = decode_string(encoded_text, sequence)
        for word in common_words:
            if word.upper() in result:
                print(f"Common word found: '{word}' in the decoded text:")
                print(result)
                possible_answer.append([[x, y], result])
print(possible_answer)

# RESULT: SURPRISEPARTYATAQUARTERBEFORENOONATTHEUNIVERSITYLIBRARY
# ANSWER: 11:45 AM
# X: 10, Y: 30