import random

class human :
    def __init__(self,name):
        self.name = name   
    
    def get_name(self):
        return self.name

names = ["mohsen","hosein","maziyar","akbar","nima","mehdi","farhad","mohamad","khashayar","milad","mostafa","amin","said","pooya","pooria","reza","ali","behzad","soheil","shahrooz","saman","behrooz"]
random_names = random.sample(names, 22)
list_of_humans = list() 

for name in random_names :
    list_of_humans.append(human(name))


class footballist(human) :
       def __init__(self,name,team):
        self.name = name 
        self.team = team
        

list_of_footballists = list()
A_count=0
B_count=0

for i in range(0,22):
    if random.randint(0,1) == 0 and A_count <= 11:
        list_of_footballists.append(footballist(list_of_humans[i].get_name(),"A"))
        A_count += 1
    else:
        list_of_footballists.append(footballist(list_of_humans[i].get_name(),"B"))
        B_count += 1
        
for item in list_of_footballists:
    print(item.name, item.team)