import mysql.connector

cnx = mysql.connector.connect(user = [type your user] , password = [type your password] ,
                                    host = [type your host]  , database = [type your database name] )
cursor = cnx.cursor()
query = 'SELECT * FROM [type your table's name] ;'
cursor.execute(query)

employeesList = list()
for row in cursor :
    employeesList.append(row)

cnx.close()

employeesList = list(sorted (employeesList, key = lambda x:( -x[1], x[2])))

for employee in employeesList :
    print("%s %i %i"%(employee[0], employee[1], employee[2]))