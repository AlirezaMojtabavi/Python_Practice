from statistics import mean

class School :
    def __init__(self,name):
        self.name = name
    
    age = list()
    height = list()
    weight = list()
    
    def MeanOfAge(self ,age) :
       return (float(mean(age)))
    def MeanOfHeight(self ,height) :
       return (float(mean(height)))
    def MeanOfWeight(self ,weight) :
       return (float(mean(weight)))

#/////////////////////////////////////////#

A = School('A')
A_number = int(input())

A_ages = str(input())
A.age = list(map(float,A_ages.split()))
A_averegeOfAges = A.MeanOfAge(A.age)

A_height = str(input())
A.height = list(map(float,A_height.split()))
A_averegeOfHeights = A.MeanOfHeight(A.height)

A_weight = str(input())
A.weight = list(map(float,A_weight.split()))
A_averageOfWeights = A.MeanOfWeight(A.weight)

#/////////////////////////////////////////////

B = School('B')
B_number = int(input())

B_ages = str(input())
B.age = list(map(float,B_ages.split()))
B_averegeOfAges = B.MeanOfAge(B.age)

B_height = str(input())
B.height = list(map(float,B_height.split()))
B_averageOfHeights = B.MeanOfHeight(B.height)

B_weight = str(input())
B.weight = list(map(float,B_weight.split()))
B_averageOfWeights = B.MeanOfWeight(B.weight)

#////////////////    OUTPUT    //////////////////////

print(A_averegeOfAges)
print(A_averegeOfHeights)
print(A_averageOfWeights)

print(B_averegeOfAges)
print(B_averageOfHeights)
print(B_averageOfWeights)

if A_averegeOfHeights > B_averageOfHeights :
    print(A.name)
elif A_averegeOfHeights < B_averageOfHeights :
    print(B.name)
elif (A_averegeOfHeights == B_averageOfHeights) and (A_averageOfWeights < B_averageOfWeights):
    print(A.name)
elif (A_averegeOfHeights == B_averageOfHeights) and (A_averageOfWeights > B_averageOfWeights):
    print(B.name)
elif (A_averegeOfHeights == B_averageOfHeights) and (A_averageOfWeights == B_averageOfWeights):
    print('Same')