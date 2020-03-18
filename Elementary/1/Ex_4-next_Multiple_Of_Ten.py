first = int(input())
rest  = first % 10

if rest !=0 :
    nextMultipleOfTen = first + (10-rest)
else :
    nextMultipleOfTen = first + 10

print(nextMultipleOfTen)