def octal_to_decimal(octal_str):
    decimal_value = 0
    base = 1
    while octal_str:
        last_digit = octal_str % 10
        octal_str = int(octal_str / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


a = 0
b = 0
c = 0

for a in range(8):
    for b in range(8):
        for c in range(8):
            result = (
                str(a)
                + str(c)
                + str(a)
                + str(b)
                + str(a)
                + str(c)
                + str(a)
                + str(a)
                + str(a)
                + str(c)
                + str(b)
                + str(b)
            )
            result_int = int(result, 8)
            # result = octal_to_decimal(octal_value)
            if str(result_int)[-3:] == "736":
                # print(f"a = {a}")
                # print(f"b = {b}")
                # print(f"c = {c}")
                print(f"result = {str(result_int)[:3]}")

# RESULT: 326
