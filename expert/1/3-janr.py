from collections import OrderedDict
import operator

number = int(input())
janr_list = list()
letter_dic = dict()

i=1
Horror = 0
Romance = 0
Comedy = 0
Action = 0
Adventure = 0
History = 0

while i<=number:
    srting_janr = str(input())
    janr_list = srting_janr.split(' ')

    for letter in janr_list:
        if letter == "Horror" :
            Horror=Horror+1
        if letter == "Romance"  :
            Romance=Romance+1
        if letter == "Comedy":
            Comedy=Comedy + 1
        if letter == "Action":
            Action= Action +1
        if letter == "Adventure":
            Adventure= Adventure +1
        if letter == "History":
            History= History +1
    i=i+1

letter_dic["Horror"] =  Horror  
letter_dic["Romance"] =  Romance 
letter_dic["Comedy"] =  Comedy  
letter_dic["Action"] =  Action  
letter_dic["Adventure"] =  Adventure  
letter_dic["History"] =  History 

#sorted_dict_dsc = sorted(letter_dic.items(), key=lambda kv: kv[1], reverse=True)
#sorted_dict_dsc= OrderedDict(sorted_dict_dsc)
sorted_dict = sorted(letter_dic.items(), key=lambda x: (-x[1], x[0]))

sorted_dict = OrderedDict(sorted_dict)
for key, value in sorted_dict.items():
    print(key , ":", value)
