def CountOfDivisor(inputNumber):
    count = 0
    for i in range(1,inputNumber+1):
        if inputNumber % i == 0:
            count+=1
    return count

initNumber = 1
codOfNumber = 1
maxCOD = codOfNumber
maxNumberOfCOD = initNumber

i = 0
while i !=20:

    number = int(input())
    codOfNumber = CountOfDivisor(number)
    if codOfNumber > maxCOD :
        maxCOD = codOfNumber
        maxNumberOfCOD = number

    elif codOfNumber < maxCOD :
        pass

    elif codOfNumber == maxCOD :
        if number < maxNumberOfCOD:
            maxNumberOfCOD = maxNumberOfCOD
        else :
            maxNumberOfCOD = number
    i+=1
    
print(maxNumberOfCOD,'',maxCOD)