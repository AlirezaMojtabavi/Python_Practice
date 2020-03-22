number = int(input())
onlineDictionary = dict()

i=0
while i < number :
    words = str(input())
    translatorList = words.split()
    onlineDictionary[translatorList[0]] = translatorList[1]
    i+=1

sentence = str(input())
sentence = sentence.split()

for letter in sentence:
    if letter in onlineDictionary :
       sentence[sentence.index(letter)] = onlineDictionary[letter]

result = " ".join(sentence)
print(result)