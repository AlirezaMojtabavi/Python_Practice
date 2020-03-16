from collections import OrderedDict
import operator

Iran = OrderedDict()
Spain = OrderedDict()
Portugal = OrderedDict()
Morocco = OrderedDict()
a = OrderedDict()
b = OrderedDict()

def draws_result(a,b):
    a["draws"]+=1
    b["draws"]+=1
    a['points']+=1
    b['points']+=1

def left_wins(a,b):
    a['wins']+=1
    b['loses']+=1
    a['points']+=3
    b['points']+=0
    a['goal difference']+=result[0]-result[2]
    b['goal difference']+=result[2]-result[0]

def right_wins(a,b):
    b['wins']+=1
    a['loses']+=1
    b['points']+=3
    a['points']+=0
    a['goal difference']+=result[0]-result[2]
    b['goal difference']+=result[2]-result[0]

Iran = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Spain = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Portugal = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}
Morocco = {'wins':0 , 'loses':0 , "draws":0 , 'goal difference':0 , 'points':0}

match = 1
n=0
while n<6:
    if match ==1 :
        m1 = Iran
        m2 = Spain
    elif match ==2 :
        m1 = Iran
        m2 = Portugal
    elif match ==3 :
        m1 = Iran
        m2 = Morocco
    elif match ==4 :
        m1 = Spain
        m2 = Portugal
    elif match ==5 :
        m1 = Spain
        m2 = Morocco
    elif match ==6 :
        m1 = Portugal
        m2 = Morocco
    
    result = list(input())
    result[0] = int(result[0])
    result[2] = int(result[2])
 
    if result[0] == result[2]:
        draws_result(m1,m2)

    elif result[0] > result[2]:
        left_wins(m1,m2)

    elif result[0] < result[2]:
        right_wins(m1,m2)
    n+=1
    match+=1

teams_dict = {'Iran':Iran,'Spain':Spain,'Portugal':Portugal,'Morocco':Morocco}
teams_dict =  OrderedDict(sorted(teams_dict.items(), key=lambda k: (-k[1]['points'],-k[1]['wins'],k[0])))

for item in teams_dict.keys():
    print("%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i" %(item, teams_dict[item]["wins"],teams_dict[item]["loses"],teams_dict[item]["draws"],teams_dict[item]["goal difference"],teams_dict[item]["points"]))