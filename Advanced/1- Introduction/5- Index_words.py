indexWords = list()

def PreviouseWord(_list, _word):
    if _list[_list.index(_word)-1] :
        return _list[_list.index(_word)-1]
    else:
        return
        
phrase = str(input())
phraseList = phrase.split(" ")
length = len(phraseList)
for item in phraseList :
    item = item.strip()

if phrase != "" :
    for i in range(0, length-1) :
        lenghtOfWord = len(phraseList[i])
        if phraseList[i][0].isupper() :
            if PreviouseWord(phraseList, phraseList[i])[-1] != "." :
                if phraseList[i][-1]=="." or phraseList[i][-1]=="," :
                    indexWords.append(i + 1)
                    indexWords.append(phraseList[i][: lenghtOfWord-1]) 
                elif phraseList[i][-1]== "]" and phraseList[i][-2]== "'" :
                    indexWords.append(i + 1)
                    indexWords.append(phraseList[i][: lenghtOfWord-2])  
                else :
                    indexWords.append(i + 1)
                    indexWords.append(phraseList[i])
else:
    print("None")

lengthOfIndexWord = len(indexWords)

if lengthOfIndexWord == 0 :
    print("None")
else:
    for i in range(0, lengthOfIndexWord//2):
        print("%i:%s" %(indexWords[2*i],indexWords[(2*i)+1]))