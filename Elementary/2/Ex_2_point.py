count_match = 0
count_win = 0
count_drew = 0

for i in range(1,31):
    point = int(input())
    i = i + 1
    if point==0:
        count_match = count_match + 1

    elif point==1:
        count_match = count_match + 1
        count_drew = count_drew + 1

    elif point==3:
        count_match = count_match + 1
        count_win = count_win + 1
print((count_win*3) + (count_drew*1),' ', count_win)

