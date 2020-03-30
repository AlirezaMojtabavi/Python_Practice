from collections import OrderedDict
import operator

def DrawResult(a,b):
    a["draws"]+=1
    b["draws"]+=1
    a['points']+=1
    b['points']+=1

def LeftWins(a,b):
    a['wins']+=1
    b['loses']+=1
    a['points']+=3
    b['points']+=0
    a['goal difference']+=result[0]-result[2]
    b['goal difference']+=result[2]-result[0]

def RightWins(a,b):
    b['wins']+=1
    a['loses']+=1
    b['points']+=3
    a['points']+=0
    a['goal difference']+=result[0]-result[2]
    b['goal difference']+=result[2]-result[0]

# Initial teams as Dictionary
Iran = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Spain = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Portugal = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Morocco = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}

match = 1
while match <= 6:
    if match == 1 :  # iran - spain
        m1 = Iran
        m2 = Spain
    elif match == 2 : # iran - portugal
        m1 = Iran
        m2 = Portugal
    elif match == 3 : # iran - morocco
        m1 = Iran
        m2 = Morocco
    elif match == 4 : # spain - portugal
        m1 = Spain
        m2 = Portugal
    elif match == 5 :   # spain - morocco
        m1 = Spain
        m2 = Morocco
    elif match == 6 :   
        m1 = Portugal   # Portugal - Morocco
        m2 = Morocco
    
    result = list(input())
    result[0] = int(result[0])
    result[2] = int(result[2])
 
    if result[0] == result[2]:
        DrawResult(m1,m2)

    elif result[0] > result[2]:
        LeftWins(m1,m2)

    elif result[0] < result[2]:
        RightWins(m1,m2)
    match+=1

teams = {'Iran':Iran,'Spain':Spain,'Portugal':Portugal,'Morocco':Morocco}
teams =  OrderedDict(sorted(teams.items(), key=lambda k: (-k[1]['points'],-k[1]['wins'],k[0])))

for item in teams.keys():
    print("%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i" 
    %(item, teams[item]["wins"],teams[item]["loses"],teams[item]["draws"],teams[item]["goal difference"],teams[item]["points"]))