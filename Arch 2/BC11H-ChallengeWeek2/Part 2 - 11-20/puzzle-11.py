def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


prime_list = [2, 3]  # Start with the first two prime numbers
n = 5
while len(prime_list) < 100:
    if is_prime(n):
        prime_list.append(n)
    n += 2  # Check only odd numbers to optimize

# 101273
print(sum([int("1" + str(prime)) for prime in prime_list]))
