numberOfLaptops = int(input())
listOfLaptops = list()

i = 0
while i < numberOfLaptops:
    specificationsOfLaptops = str(input())
    laptops = specificationsOfLaptops.split()

    for j in range(0,2):
        laptops[j] = int(laptops[j])

    listOfLaptops.append(laptops)
    i+=1

for j in range(0,numberOfLaptops-1):
    if (listOfLaptops[j][0] <= listOfLaptops[j+1][0]) and (listOfLaptops[j][1] >= listOfLaptops[j+1][1]):
        print("happy irsa")
    elif (listOfLaptops[j][0] >= listOfLaptops[j+1][0]) and (listOfLaptops[j][1] <= listOfLaptops[j+1][1]):
        print("happy irsa")
    else:
        print("poor irsa")
        break