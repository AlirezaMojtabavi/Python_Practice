number = int(input())
numberOfExperience = str(input())
listOfExperience = numberOfExperience.split()

count = 0
for i in range (0,number):
    listOfExperience[i] = int(listOfExperience[i])
    if 5 - listOfExperience[i] >= 3:
        count += 1

result = count//3
print(result)