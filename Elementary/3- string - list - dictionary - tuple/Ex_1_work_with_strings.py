string = str(input())
string = ' ' + string + ' '

vowels = ["a","A","e","E","i","I","o","O","u","U"]

for letter in string:
    if letter in vowels:
        string = string[: string.index(letter)] + string[string.index(letter)+1 :]

string = string.strip()

##--------------------------------------------------------------------------



tool = len(string)
for i in range(0,2*tool-1):
    if i%2 !=0:
        pass
    else:
        string =string[: i] + "." + string[i :]

string = string.lower()
print(string)