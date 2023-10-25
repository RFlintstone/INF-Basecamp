# A string is a palindrome if it is identical forward and backward.
# For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.
# Write a program that reads a string from the user and uses a loop to determines whether it is a palindrome.
# Display the result, including a meaningful output message.
#
# Extra (additional challenge):
# Extend your solution so that is also ignores punctuation marks (like , . ? ! ;)
# Extend your solution so that it treats uppercase and lowercase letters as equivalent.
#
# Input example:
# String: anna
# String: hannah
# String: lepels
#
# Output example:
# "anna" is a palindrome
# "hannah" is a palindrome
# "lepels" is not a palindrome

# Ask for user input
i = input()

# characters to filter.
punct_marks = ",.?!;"

# Remove all characters listed in 'puct_marks'.
count = 0
for p in punct_marks:
    i = i.replace(p, "")
    count += 1

# Reverse filtered input
reversed_i = list(i)
reversed_i.reverse()
reversed_i = ''.join(reversed_i)

# Check if the input is the same as the reversed input
result = ""
result = f'{i} is '
if i == reversed_i:
    result += "a palindrome"
else:
    result += "not a palindrome"

# Print if the input is a palindrome or not
print(result)