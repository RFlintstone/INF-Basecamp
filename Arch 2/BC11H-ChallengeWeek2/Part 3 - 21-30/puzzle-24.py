def UP(num):
    return (3 * num) + 1
    
def DOWN(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num + 1

list = ["U", "D"]

x = 10

for one in list:
    x = 10
    for two in list:
        x = 10
        for three in list:
            x = 10
            for four in list:
                x = 10
                for five in list:
                    x = 10
                    for six in list:
                        x = 10
                        for seven in list:
                            x = 10
                            for eight in list:
                                x = 10
                                for nine in list:
                                    x = 10
                                    for ten in list:
                                        x = 10
                                        
                                        if one == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if two == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if three == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if four == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if five == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if six == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if seven == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if eight == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if nine == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if ten == "U":
                                            x = UP(x)
                                        else:
                                            x = DOWN(x)
                                        
                                        if x == 60:
                                            print("Success!!")
                                            
                                            print(f"The result is {one+two+three+four+five+six+seven+eight+nine+ten}")
                                            
                                            