def IsPrimeNumber(number): #the number is prime or not

    if number==2:
        return True

    if number == 1 :
        return False

    i=2    
    while i< number :
        divideRemaining = number%i
        if divideRemaining !=0 :
            pass
        else:
            return False
        i+=1

    return True

# --------------------------------------------------

def Divisor(number): # Divisors of number
    divisors = list()

    for i in range(1,number+1):
        if number%i==0:
            divisors.append(i)

    return divisors

#----------------------------------------------------

def NumberOfPrimeDivisors(divisorsList): # return the number of prime divisors

    divisorsList = Divisor(number)

    count=0
    for eleman in divisorsList :

        if IsPrimeNumber(eleman) == True:
            count+=1
        else:
            count = count
    
    return count
#--------------------------------------------------------


initCountOfPrimeDivisors = 2
numberOfMaxCount = 1
maxCount = initCountOfPrimeDivisors

i=1
while  i<=10:
    number = int(input())
    divisorsOfNumber = Divisor(number)
    countOfPrimeDivisors = NumberOfPrimeDivisors(divisorsOfNumber)

    if countOfPrimeDivisors > maxCount :
        maxCount = countOfPrimeDivisors
        numberOfMaxCount = number
        
    elif countOfPrimeDivisors < maxCount :
        maxCount = maxCount
        numberOfMaxCount = numberOfMaxCount

    elif  countOfPrimeDivisors == maxCount :
        if number > numberOfMaxCount :
            maxCount = countOfPrimeDivisors
            numberOfMaxCount = number
        else:
            maxCount = maxCount
            numberOfMaxCount = numberOfMaxCount

    i+=1

print(numberOfMaxCount," ",maxCount)