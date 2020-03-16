number = int(input())
temp = list()
list_jomle = list()
motarjem = dict()

i=0
while i < number :
    string = str(input())
    temp = string.split()
    if not(temp[0] in motarjem) :
        motarjem[temp[0]]= temp[1]
    i+=1
#print("\nDictionary:\n")
for this in list(motarjem.keys()):
    print("%s be farsi mishe %s."% (this,motarjem[this]))

jomle = str(input())
list_jomle = jomle.split()

for letter in list_jomle:
    if letter in motarjem :
       list_jomle[list_jomle.index(letter)] = motarjem[letter]

result = " ".join(list_jomle)
print(result)
