import math

string = """d72a72121175d8bef1c668619dfe6e652e1bf1d4c37ea01f50734a22c0c63768e1bddce0dafa2679137119f5a9e6942162f0c741cc42d0cc8942e64218c9a1ed499afacf904bbae3ffcea1179c2531045eb159da9dc94dba084a22b980ba81698acc2420471b31e4e6de857afbdc61025be017e9c8cc42f87b6452f081f495040fc21e6f8faa8dec9cd9f34546df254c96f27a054b1914571fd7660fdf94ca1fdd4352cdcf8c3d57e6af85675078215dcf3a409adca5f68f831887fe7f2d6cbaad8bfc204c0f14e418bfe6138d1740ed6b2f726bfd5f82205c31fa76d6418867160121894010711f7713f4dd96975e70beb37715aacf53b0ba9a"""


largest = "0"


hex_to_dec = lambda hex_num: int(hex_num, 16)

def meets_conditions(str):
    for m in str:
        if str.count(m) != 1 or m == "f":
            return False
    return True

count = 0

for i in range(len(string)-4):
    count += 1
    #print(f"Check: {string[i:i+5]}")
    if meets_conditions(string[i:i+5]) and hex_to_dec(string[i:i+5]) > hex_to_dec(largest):
        largest = string[i:i+5]
        
    #print(f"largest: {largest}")

    #print()



print(f"largest = {largest}")

print(f"largest as decimal = {hex_to_dec(largest)}")