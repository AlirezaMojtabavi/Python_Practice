
def addad_aval(addad): #aval boodan ya naboodane addad
    
    if addad==2:
        return True

    i=2    
    while i<addad :
        count=0
        baghi_mande = addad%i
        if baghi_mande!=0:
            count=0
        else:
            #print("gheyre_avval")
            return False
        i=i+1

    if count==0:
        #print("avval")
        return True



def maghsoom_elayh(addad):#maghsoom elayhaye addad
    count_maghsoom_elayh = 0
    maghsoom_elayh = list()

    for i in range(1,addad+1):
        if addad%i==0:
            maghsoom_elayh.append(i)
            count_maghsoom_elayh+=1

    return maghsoom_elayh[1 :]

i=1
temp = 0
temp_count = 0

while  i<=10:
    addad = int(input())
    count=0
    maghsoom = maghsoom_elayh(addad)
    for j in maghsoom:
        if addad_aval(j)==True:
            count+=1
        else:
            count = count
    if count> temp_count:
        javab = addad
        temp_addad = addad
        temp_count = count
    elif count == temp_count:
        if addad >= temp_addad:
            javab=addad
            temp_addad = addad
            temp_count = count
        else:
            javab = temp_addad
            temp_addad = temp_addad
            temp_count = temp_count
    else:
        javab = temp_addad
        temp_addad = temp_addad
        temp_count = temp_count
    i+=1

print(javab,' ',temp_count)






    





