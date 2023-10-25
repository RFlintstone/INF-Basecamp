# Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
#
# Criteria: The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples
# of 10 degrees Celsius. Include appropriate headings on your columns. The formula for converting between degrees
# Celsius and degrees Fahrenheit can be found on the internet . Input example: No input is given
#
# Output example:
# °C °F
# 10 50
# 20 68
# ...

min_temp = 0
max_temp = 100

def c_to_f(c):
    return (c * 1.8) + 32


if __name__ == '__main__':
    # print("°C °F")
    for i in range(min_temp+1, max_temp+1):
        f = c_to_f(i*10)
        print(f'{i*10} {int(f)}')
