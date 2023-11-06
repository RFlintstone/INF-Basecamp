total = 1
base_count = 0
count = 0


for i in range(2, 501):
    if count == 0:
        base_count += 1
        count += base_count
        print("Entering count=0")
    
    if base_count % 2 != 0:
        #print("+")
        total += i
        
    elif base_count % 2 == 0:
        #print("-")
        total -= i
    #print(f"{i} = {total}")
    count -= 1

print(f"Final total result: {total}")

# RESULT: 6336