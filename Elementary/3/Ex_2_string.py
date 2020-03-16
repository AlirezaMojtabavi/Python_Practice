vorodi = str(input())
tool = len(vorodi)
count_3 = vorodi.count('3')
count_2 = vorodi.count('2')
count_1 = vorodi.count('1')

my_string = '1' * count_1 + '2' * count_2 + '3' * count_3
#print(my_string)
#tool = len(my_string)
for i in range(0,tool-1) :
    if i%2 == 0:
        my_string = my_string[: i] + my_string[i :]
    else:
        
        my_string = my_string[: i] + '+' + my_string[i :]
        
print(my_string)