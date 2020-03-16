tedad_laptop = int(input())
i=0
list_laptpha = []

while i < tedad_laptop:
    voroodi = str(input())
    list_voroodi = voroodi.split()

    for j in range(0,2):
        list_voroodi[j] = int(list_voroodi[j])

    list_laptpha.append(list_voroodi)
    i=i+1

#print(list_laptpha)

for j in range(0,tedad_laptop-1):
    if list_laptpha[j][0] < list_laptpha[j+1][0] and list_laptpha[j][1] > list_laptpha[j+1][1]:
        print("happy irsa")
    elif list_laptpha[j][0] > list_laptpha[j+1][0] and list_laptpha[j][1] < list_laptpha[j+1][1]:
        print("happy irsa")
    else:
        print("poor irsa")
        break