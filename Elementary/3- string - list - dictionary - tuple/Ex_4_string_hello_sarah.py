word = str(input())
length = len(word)
flag = True

for letter1 in word:
    if letter1 == "h":
        word = word[word.index(letter1)+1 :]
        break
    else:
        word = word

if (len(word) != length) and (len(word)>=len("ello")):
    length = len(word)
    for letter2 in word:
        if letter2 == "e":
            word = word[word.index(letter2)+1 :]
            break
        else:
            word = word
else:
    flag = False

if (len(word) != length) and (len(word)>=len("llo")):
    length = len(word)
    for letter3 in word:
        if letter3 == "l":
            word = word[word.index(letter3)+1 :]
            break
        else:
            word = word
else:
    flag = False

if (len(word) != length) and (len(word)>=len("lo")):
    length = len(word)
    for letter4 in word:
        if letter4 == "l":
            word = word[word.index(letter4)+1 :]
            break
        else :
            word = word
else:
    flag = False

if (len(word) != length) and (len(word)>=len("o")):
    length = len(word)
    for letter5 in word:
        if letter5 == "o":
            word = word[word.index(letter5)+1 :]
            break
        else:
            word = word
else:
    flag = False

if flag == True :
    print("YES")

else :
    print("NO")