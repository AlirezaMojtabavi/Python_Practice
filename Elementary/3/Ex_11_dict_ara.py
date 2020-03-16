import collections

number = int(input())
ara_dict = collections.OrderedDict()

i=0
while i < number :
    string = str(input())

    if string in ara_dict :
        ara_dict[string] += 1
    else:
        ara_dict[string] = 1

    #ara_dict[string] = ara_dict.get(string,0) + 1  

    i+=1

#ara_dict.keys() = sorted(ara_dict.items(), key=lambda x: x[0])

for this_one in sorted(ara_dict.keys()):
    print(this_one," ",ara_dict[this_one])