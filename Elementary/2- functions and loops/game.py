from random import randint
a = 1
b = 99
hads = randint(a,b)
while True:
    print(hads)
    rahnamai = str(input())
    if rahnamai =="b":
        a = hads + 1
        hads = randint(a,b)
    elif rahnamai == 'k':
         b = hads - 1
         hads = randint(a,b)
    elif rahnamai =='d':
        break

print('hads = ' ,hads ,'afffarinn computer !!!!!!!')