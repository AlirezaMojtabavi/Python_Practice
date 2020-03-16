number = int(input())
first = number%10
temp = number%100
second = temp//10
third = number//100
javab = 2*(first*100 + second*10 + third)
print(javab)