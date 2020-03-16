voroodi = str(input())
voroodi_list = voroodi.split()
length = len(voroodi_list)

#print(voroodi_list)
minimum = float(voroodi_list[0])
maximum = float(voroodi_list[1])
center = float(voroodi_list[2])

for i in range(0,length):
    voroodi_list[i] = float(voroodi_list[i]) 
    if voroodi_list[i] > maximum:
        maximum = voroodi_list[i] 

for i in range(0,length):
    if voroodi_list[i] < minimum:
        minimum = voroodi_list[i] 

for i in range(0,length):
    if voroodi_list[i] != minimum and voroodi_list[i] != maximum:
        voroodi_list[i] = center

result = float((center - minimum) + (maximum-center))
result = str(result)

for letter in result:
    if letter == ".":
        result = result[: result.index(".")]

result = int(result)
print(result)

