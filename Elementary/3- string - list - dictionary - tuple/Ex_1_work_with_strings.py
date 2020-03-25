string = str(input())
string = ' ' + string + ' '

for letter in string:
    if letter=='a' or letter=='A' or letter=='e' or letter=='E' or letter=='i' or letter=='I' or letter=='o' or letter=='O' or letter=='u' or letter=='U':
        string = string[: string.index(letter)] + string[string.index(letter)+1 :]

string = string.strip()

##--------------------------------------------------------------------------

if string[0]!=".":
    string = "." + string

tool = len(string)
for i in range(1,2*tool-2):
    if string[i]=="." or string[i-1]=='.':
        string = string[: i] + string[i :]
    elif string[i]!="." and string[i-1]!=".":
        string =string[: i] + "." + string[i :]

string = string.lower()
print(string)