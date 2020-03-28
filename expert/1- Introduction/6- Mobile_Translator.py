from functools import reduce # these two library make list flat (between [......])
from operator import concat

number = int(input())
listOfWords = list()
listOfSentence = list()
translateList = list()

n=1
while n <= number:
    words = str(input())
    listOfWords.append(words.split())
    n+=1
flatWords = reduce(concat, listOfWords)

sentence = str(input())
listOfSentence.append(sentence.split())
flatSentence = reduce(concat, listOfSentence)

for letter in flatSentence:
    for item in flatWords:
        if letter == item :
            tempVariable = (flatWords.index(item))%4
            indexOfTranslate = flatWords.index(item) - tempVariable
            translateList.append(flatWords[indexOfTranslate]+ " ")
            flatTranslator = reduce(concat, translateList)
        elif (letter not in flatWords) and (letter not in flatTranslator) :
            translateList.append(letter + " ")
            flatTranslator = reduce(concat, translateList)

print(flatTranslator)