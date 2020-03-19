def Standardization(name):
    firstLetter = name[0].upper()
    name = name.lower()
    modifiedName = firstLetter + name[1 :]
    return modifiedName

inputName = ["" for x in range(0,10)]
standardName = ["" for x in range(0,10)]

i=0
while i !=10 :
    inputName[i] = str(input())
    standardName[i] = Standardization(inputName[i])
    i+=1

for name in standardName:
    print(name)