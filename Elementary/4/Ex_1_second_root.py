from math import sqrt
from math import floor

number = int(input())
resultList = list()

i = 0
while i< number:

    inputNumber = input()
    inputNumber = float(inputNumber)
    secondRoot = float(sqrt(inputNumber))
    integerNumber = int(floor(secondRoot))
    Decimals = str(secondRoot - integerNumber)
    Decimals = Decimals[2 :]

    if len(Decimals) >= 4 :
        Decimals = Decimals[0 : 4]
    elif len(Decimals) == 3 :
        Decimals = Decimals + "0"
    elif len(Decimals) == 2 :
        Decimals = Decimals + "00"
    elif len(Decimals) == 1 :
        Decimals = Decimals + "000"
    elif len(Decimals) == 0 :
        Decimals = Decimals + "0000"
    
    result = str(integerNumber) + "." + Decimals
    resultList.append(result)
    i+=1

for finalResult in resultList :
    print(finalResult)