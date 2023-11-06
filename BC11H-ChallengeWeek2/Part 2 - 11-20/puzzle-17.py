import math

string = "48467640804449446969669889640080046948496400080004\
404090404617323716400008000046378322387361211020112321146419\
424910020011234321522122510002000110203020110406040112124212\
112345432112568652152280822594206024910000200001102214122011\
2102420121123456543"

longest = "0"


def palindrome_squared(str):
    return math.sqrt(int(str)) % 2 == 0 and str == str[::-1]


for one in range(len(string) + 1):
    for two in range(one + 1, len(string) + 1):
        # print(f"Check: {string[one:two]}")

        if (palindrome_squared(string[one:two])
           and int(string[one:two]) > int(longest)):
            longest = string[one:two]

if longest == "0":
    print("Nothing found...")
else:
    # RESULT: 637
    print(f"longest = {longest}")
