# Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
#
# Input example:
# 3141
#
# Output example:
# 3+1+4+1=9

input = input()
input_to_str = str(input)
input_to_array = [char for char in input_to_str]

sum = 0
sum_str = ""
counter = 0
for c in input_to_array:
    if len(sum_str) % 2:
        sum_str += "+" + input_to_array[counter]
    else:
        sum_str += input_to_array[counter]
    sum += int(input_to_array[counter])
    counter += 1
print(sum_str + "=" + str(sum))