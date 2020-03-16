number = int(input())
list_nahayi = list()

i= 0
while i<number:
    list_fard = list()
    str_input = str(input())
    
    
## hazfe "."
    for letter in str_input:
        if letter == ".":
            str_input = str_input[: str_input.index(letter)]+" "+str_input[str_input.index(letter)+1 :]

    result = str_input.lower()
    result = result[: 2]+result[2].upper()+result[3 :]
    tool = len(result)

    if result[-1]=="c":
        result= result[: tool-1] + "C"
    if str_input[-1]=="+":
        result= result[: tool-3]+ "C++"
    if str_input[-1]=="#":
        result= result[: tool-2]+ "C#"
    if str_input[-4 :] == "Java":
        result = result[: tool-4]+"Java"
    if str_input[-7 :] == "Android":
        result = result[: tool-7]+"Android"
    if str_input[-6 :] == "Python":
        result = result[: tool-6]+"Python"

    list_fard= "".join(result)
    list_nahayi.append(list_fard)
    i+=1

list_nahayi=sorted(list_nahayi, key=str.lower)
for item in list_nahayi:
    print(item)


