voroodi = str(input())
voroodi = voroodi.lower()
length = len(voroodi)

if length%2 == 0 :
    tool = int(length/2)
    for i in range(0, tool):
        if voroodi[i] == voroodi[-i-1]:
            print("palindrome")
            break
        else:
            print("not palindrome")
            break
else:
    tool = length-1
    tool = int(tool/2)
    for i in range(0,tool):
        if voroodi[i] == voroodi[-i-1]:
            print("palindrome")
            break
        else:
            print("not palindrome")
            break
            