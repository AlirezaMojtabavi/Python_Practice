def Standard(name):
    first_letter = str(name[0])
    first_letter = first_letter.upper()
    name = first_letter + str(name[1 :]).lower()
    return name

voroodi = ["" for x in range(0,10)]
pasokh = ["" for x in range(0,10)]

i=0
while i <=5 :
    voroodi[i] = input()
    pasokh[i] = Standard(voroodi[i])
    i=i+1

i=0
while i <=5 :
    print(pasokh[i])
    i=i+1