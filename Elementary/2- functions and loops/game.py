import random
a = 1
b = 99
hads = random.randint(a,b)
while True:
    print(hads)
    rahnamai = str(input())
    if rahnamai =="b":
        a = hads + 1
        hads = random.randint(a,b)
    elif rahnamai == 'k':
         b = hads - 1
         hads = random.randint(a,b)
    elif rahnamai =='d':
        break

print('hads = ' ,hads ,'afffarinn computer !!!!!!!')