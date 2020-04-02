import mysql.connector

flag = False
Email_password = str(input())

while (flag == False):
    try:
        Email_password = Email_password.split()
        len(Email_password) == 2
        Email = Email_password[0]
        password = Email_password[1]
        len(Email_password) == 2   
        separateEmail = Email.split(".")
        len(separateEmail) == 2
        separateEmail[1] is str 
        separateEmail[0] = str(separateEmail[0])
        firstPart = separateEmail[0].split("@")
        len(firstPart) == 2
        firstPart[1] is str 
        flag = True    
    except:
        print("Correct sample of Email is  \'expression@string.string\'")
        flag = False
        Email_password = str(input())

if flag == True:
    cnx = mysql.connector.connect(user = [type your user] , password = [type your password] ,
                                    host = [type your host]  , database = [type your database name] )
    cursor = cnx.cursor()
    cursor.execute('INSERT INTO [type your table's name] VALUES (\'%s\',\'%s\')' % (Email, password))
    cnx.commit()

    cnx.close()