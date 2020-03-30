number = int(input())
finalList = list()

i= 0
while i<number:
    sexNameLanguage = str(input())
    
    for letter in sexNameLanguage: 
        if letter == ".": # Remove "."
            sexNameLanguage = sexNameLanguage[: sexNameLanguage.index(letter)]+" "+sexNameLanguage[sexNameLanguage.index(letter)+1 :]

    sexNameLanguage = sexNameLanguage.lower()
    sexNameLanguage = sexNameLanguage[: 2]+sexNameLanguage[2].upper()+sexNameLanguage[3 :] # make first letter of name capital
    length = len(sexNameLanguage)

    if sexNameLanguage[-1]=="c":
        sexNameLanguage= sexNameLanguage[: length-1] + "C"
    if sexNameLanguage[-1]=="+":
        sexNameLanguage= sexNameLanguage[: length-3]+ "C++"
    if sexNameLanguage[-1]=="#":
        sexNameLanguage= sexNameLanguage[: length-2]+ "C#"

    finalList.append(sexNameLanguage)
    i+=1

finalList = sorted(finalList, key=str.lower)
for item in finalList:
    print(item)