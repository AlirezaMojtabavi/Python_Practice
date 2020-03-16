from statistics import mean

class school :
    def __init__(self,name):
        self.name = name
    
    sen = list()
    ghad = list()
    vazn = list()
    
    def mean_sen(self ,sen) :
       return (float(mean(sen)))
    def mean_ghad(self ,ghad) :
       return (float(mean(ghad)))
    def mean_vazn(self ,vazn) :
       return (float(mean(vazn)))

#/////////////////////////////////////////#


A = school('A')
number_A = int(input())

#ages_A = ["" for x in range (0,2*number_A-1)]
ages_A = str(input())
A.sen = list(map(float,ages_A.split()))
average_sen_A = A.mean_sen(A.sen)

#height_A = ["" for x in range (0,2*number_A-1)]
height_A = str(input())
A.ghad = list(map(float,height_A.split()))
average_ghad_A = A.mean_ghad(A.ghad)

#weight_B = ["" for x in range (0,2*number_A-1)]
weight_A = str(input())
A.vazn = list(map(float,weight_A.split()))
average_vazn_A = A.mean_vazn(A.vazn)

#/////////////////////////////////////////////

B = school('B')
number_B = int(input())

#ages_B = ["" for x in range (0,2 * number_B-1)]
ages_B = str(input())
B.sen = list(map(float,ages_B.split()))
average_sen_B = B.mean_sen(B.sen)

#height_B = ["" for x in range (0,2*number_B-1)]
height_B = str(input())
B.ghad = list(map(float,height_B.split()))
average_ghad_B = B.mean_ghad(B.ghad)

#weight_B = ["" for x in range (0,2*number_B-1)]
weight_B = str(input())
B.vazn = list(map(float,weight_B.split()))
average_vazn_B = B.mean_vazn(B.vazn)

#////////////////    OUTPUT    //////////////////////
print(average_sen_A)
print(average_ghad_A)
print(average_vazn_A)

print(average_sen_B)
print(average_ghad_B)
print(average_vazn_B)


if average_ghad_A > average_ghad_B :
    print(A.name)
elif average_ghad_A < average_ghad_B :
    print(B.name)
elif (average_ghad_A == average_ghad_B) and (average_vazn_A < average_vazn_B):
    print(A.name)
elif (average_ghad_A == average_ghad_B) and (average_vazn_A > average_vazn_B):
    print(B.name)
elif (average_ghad_A == average_ghad_B) and (average_vazn_A == average_vazn_B):
    print('Same')