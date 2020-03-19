word = str(input())
word = word.lower()
lengthOfWord = len(word)

if lengthOfWord %2 == 0 :
    length = int(lengthOfWord/2)
    for i in range(0, length):
        if word[i] == word[-i-1]:
            print("palindrome")
            break
        else:
            print("not palindrome")
            break
else:
    length = int((lengthOfWord-1)/2)
    for i in range(0,length):
        if word[i] == word[-i-1]:
            print("palindrome")
            break
        else:
            print("not palindrome")
            break