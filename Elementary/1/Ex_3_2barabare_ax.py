number = int(input())
first = number%10
variable = number%100
second = variable//10
third = number//100
javab = 2*(first*100 + second*10 + third)
print(javab)