
word = input()

length = len(word)
if length < 5:
    print("NO")

for i in range (0,length-1):
    if word[i]=="h":
        if word[i+1]=="e":
            if word[i+2]=="l":
                if word[i+3]=="l":
                    if word[i+4]=="o":
                        print("YES")
                        break
                    else:
                        print("NO") 
                        break           
                else:
                    print("NO")
                    break
            else:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("NO")
        break