# from util.bruteforce import send_items

original = "IF YOU COPY THIS SENTENCE TWO HUNDRED TIMES AND REMOVE ALL WORDS WITH EXACTLY ONE LETTER E IN IT WHAT WILL BE THE THOUSANDTH WORD FOLLOWED BY THE HUNDREDTH WORD "


original = original * 200
words = original.split()

words = [word for word in words if word.count("E") != 1]

print(words[999] + words[99])

# WORDWORD
