inputString = str(input())
tool = len(inputString)
count_3 = inputString.count('3')
count_2 = inputString.count('2')
count_1 = inputString.count('1')
regularWordage = '1' * count_1 + '2' * count_2 + '3' * count_3

for i in range(0,tool-1) :
    if i%2 == 0:
        pass
    else:
        regularWordage = regularWordage[: i] + '+' + regularWordage[i :]
        
print(regularWordage)