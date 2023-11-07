string = "12345678987654321"

for one in range(len(string)):
    
    for two in range(len(string)):
        
        temp_list = list(string)
        if int(string[one]) % 2 == 0 and int(string[two]) % 2 == 0 and one != two:
            
            temp_list[one] = "+"
            temp_list[two] = "*"

            temp_string = "".join(map(str,temp_list))

            if str(eval(temp_string))[-3:] == "132":
                
                print("Success!!")
                
                print(temp_string)
                print(eval(temp_string))