import random

class Human :
    def __init__(self,name):
        self.name = name   
    
    def GetName(self):
        return self.name

names = ["mohsen","hosein","maziyar","akbar","nima","mehdi","farhad","mohamad","khashayar","milad","mostafa","amin","said","pooya","pooria","reza","ali","behzad","soheil","shahrooz","saman","behrooz"]
randomNames = random.sample(names, 22)
listOfHumans = list() 

for name in randomNames :
    listOfHumans.append(Human(name))

class SoccerPlayer(Human) :
       def __init__(self,name,team):
        self.name = name 
        self.team = team
        

listOfSoccerPlayer = list()
A_count = 0
B_count = 0

for i in range(0,22):
    if random.randint(0,1) == 0 and A_count <= 11:
        listOfSoccerPlayer.append(SoccerPlayer(listOfHumans[i].GetName(),"A"))
        A_count += 1
    else:
        listOfSoccerPlayer.append(SoccerPlayer(listOfHumans[i].GetName(),"B"))
        B_count += 1
        
for item in listOfSoccerPlayer:
    print(item.name, item.team)