string = str(input())
length = len(string)
string = string.upper()
flag = 0

for i in range(0,length):
    if string[i]== "A" and string[i+1]== "B":
        flag = 1
        break
    else:
        flag=0
        break

if flag == 1 :
    for i in range(0,length):
        if string[i]== "B" and string[i+1]== "A":
            flag = 2
            break
        else:
            flag = 0
            break
else:
    flag = 0


if flag == 2:
    print("YES")  
else:
    print("NO")          