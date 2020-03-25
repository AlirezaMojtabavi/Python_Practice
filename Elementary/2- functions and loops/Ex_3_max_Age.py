initialAge = int(input())
age = 0
maxAge = initialAge

while (age != -1): 
    age = int(input())

    if maxAge > age:
        maxAge = maxAge      
    else : 
        maxAge = age      
print(maxAge)