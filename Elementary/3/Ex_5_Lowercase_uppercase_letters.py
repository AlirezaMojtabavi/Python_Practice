word = str(input())
length = len(word)
countUppercase = 0
countLowercase = 0

for letter in word:
    if str(letter) == str(letter).upper():
        countUppercase += 1
    else:
        countLowercase += 1

if countUppercase > countLowercase:
    word = word.upper()
else:
    word = word.lower()

print(word)