string = str(input())
length = len(string)
string = string.upper()
flag = True

for i in range(0,length):
    if (string[i]== "A") and (string[i+1]== "B"):
        string = string[: string.index('A')] + string[string.index('B')+1 :]
        break
    elif (string[i]== "B") and (string[i+1]== "A"):
        string = string[: string.index('B')] + string[string.index('A')+1 :]
        break
    else:
        flag = False
        break

length = len(string)

if flag != False :
    for i in range(0,length):
        if (string[i]== "B") and (string[i+1]== "A"):
            break
        elif (string[i]== "A") and (string[i+1]== "B"):
            break
        else:
            flag = False
            break
else:
    flag = False

if flag == True:
    print("YES")  
else:
    print("NO")          