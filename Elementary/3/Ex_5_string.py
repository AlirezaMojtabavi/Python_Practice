voroodi = str(input())
length = len(voroodi)
count_small = 0
count_capital = 0

for letter in voroodi:
    if str(letter) == str(letter).upper():
        count_capital = count_capital + 1
    else:
        count_small = count_small + 1

if count_capital > count_small:
    voroodi = voroodi.upper()
else:
    voroodi = voroodi.lower()

print(voroodi)