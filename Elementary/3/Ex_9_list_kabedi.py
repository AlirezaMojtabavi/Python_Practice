number = int(input())
tajrobe = ["" for x in range(0,number)]
#print(tajrobe)
voroodi = str(input())
list_vorodi = voroodi.split()
#print(list_vorodi)
for i in range (0,number):
    tajrobe[i] = int(list_vorodi[i])
#print(tajrobe)

count = 0
for i in range (0,number) :
    if 5 - tajrobe[i] >= 3:
        count = count + 1
result = count//3
print(result)