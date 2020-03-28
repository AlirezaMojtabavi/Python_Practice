from collections import OrderedDict
import operator

number = int(input())
genresDict = OrderedDict()

Horror = 0
Romance = 0
Comedy = 0
Action = 0
Adventure = 0
History = 0

i=1
while i<=number:
    faveGenres = str(input())
    faveGenres = faveGenres.split(' ')

    for letter in faveGenres:
        if letter == "Horror" :
            Horror+=1
        if letter == "Romance"  :
            Romance+=1
        if letter == "Comedy":
            Comedy+=1
        if letter == "Action":
            Action+=1
        if letter == "Adventure":
            Adventure+=1
        if letter == "History":
            History+=1
    i+=1

genresDict["Horror"] =  Horror  
genresDict["Romance"] =  Romance 
genresDict["Comedy"] =  Comedy  
genresDict["Action"] =  Action  
genresDict["Adventure"] =  Adventure  
genresDict["History"] =  History 

genresDict = OrderedDict(sorted(genresDict.items(), key=lambda x: (-x[1], x[0])))

for key, value in genresDict.items():
    print(key , ":", value)