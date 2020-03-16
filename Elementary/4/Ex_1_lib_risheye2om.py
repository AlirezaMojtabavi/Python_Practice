from math import sqrt
from math import floor

number = int(input())
final_list = list()
i = 0
while i< number:

    voroodi = float(input())
    sqrt_result = float(sqrt(voroodi))
    adad = int(floor(sqrt_result))
    ashar = sqrt_result - adad
    string_ashar = str(ashar) 
    #print(string_ashar)
    string_ashar = string_ashar[2 :]
    #print(string_ashar)
    len_string_ashar = len(string_ashar)
    #print(len_string_ashar)

    if ashar == 0 :
        strintg_result = str(sqrt_result)+"000"
        final_list.append(strintg_result)
    
    if len_string_ashar > 4 and ashar != 0:
        final_result = str(adad) + "." + string_ashar[: 4] 
        final_list.append(final_result)

    elif len_string_ashar < 4 and ashar != 0 :
        if len_string_ashar == 3 :
            final_result = str(adad) + "." + string_ashar + "0"
            final_list.append(final_result)
        elif len_string_ashar == 2 :
            final_result = str(adad) + "." + string_ashar + "00"
            final_list.append(final_result)
        elif len_string_ashar == 1 :
            final_result = str(adad) + "." + string_ashar + "000"
            final_list.append(final_result)
    i+=1

for letter in final_list :
    print(letter)