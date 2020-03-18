initialAge = int(input())
secondAge = int(input())
age = 0

if initialAge > secondAge :
    FirstMaxAge = initialAge
    SecondMaxAge = secondAge
    tempAge = FirstMaxAge
else:
    FirstMaxAge = secondAge
    SecondMaxAge = initialAge
    tempAge = FirstMaxAge

while age !=-1 :
    age = int(input())

    if age > FirstMaxAge :
        FirstMaxAge = age
        SecondMaxAge = tempAge
        tempAge = FirstMaxAge

    elif FirstMaxAge > age :
        FirstMaxAge = FirstMaxAge
        tempAge = FirstMaxAge
        if age > SecondMaxAge :
            SecondMaxAge = age
        else:
            SecondMaxAge = SecondMaxAge

print(FirstMaxAge,'' ,SecondMaxAge)
    

