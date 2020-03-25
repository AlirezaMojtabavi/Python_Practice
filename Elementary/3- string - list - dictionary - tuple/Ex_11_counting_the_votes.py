from collections import OrderedDict 

number = int(input())
dictOfVotes = OrderedDict()

i=0
while i < number :
    votes = str(input())
    dictOfVotes[votes] = dictOfVotes.get(votes,0) + 1  

    i+=1

for thisOne in sorted(dictOfVotes.keys()):
    print(thisOne," ",dictOfVotes[thisOne])