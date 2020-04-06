import requests
import re
from bs4 import BeautifulSoup
import mysql.connector

inputCar = str(input()) ## for example "MG"
pageNumber = 1          ## each page has 30 cars, so I don't need to change pageNumber
listOfCars = list()
count = 0

while (count < 20):

    url = 'https://bama.ir/car/'
    url = url + inputCar + '/all-models/all-trims?page=' + str(pageNumber)
    getURL = requests.get(url)
    soup = BeautifulSoup(getURL.text,'html.parser')
    listOfData = soup.find_all('div', attrs = {'class':'listdata'})

    for item in listOfData:
        count += 1
        if count > 20 :
            break
        mileage = item.find_all('p', attrs = {'class':'price hidden-xs'})
        if mileage[0].text != "-":
            mileage = re.findall(r'کارکرد (.*)', mileage[0].text)[0].strip()
            if mileage == 'صفر' :
                mileage = '0'
        else:
            mileage = "-"

        price = item.find_all('span', attrs = {'itemprop':'price'})
        
        try:
            if price[0].text == " توافقی ":
                listOfCars.append((count, mileage, 'agreemental'))
            else : 
                listOfCars.append((count, mileage,price[0].text.strip() ))

        except:
            listOfCars.append((count, mileage,"Please Call"))
            
    if count > 20:
        break

length = len(listOfCars)

##/////////////////////////// INSERT IN TO DATABASE ////////////////////////////////////////////

cnx = mysql.connector.connect(user = [type your user] , password = [type your password] ,
                                host = [type your host]  , database = [type your database name] )
cursor = cnx.cursor()
for i in range(1,length+1):
    cursor.execute('INSERT INTO [type your table's name] VALUES (\'%i\',\'%s\',\'%s\',\'%s\')' 
                            % (i, inputCar, listOfCars[i-1][1], listOfCars[i-1][2]))
        
cnx.commit()

cnx.close()                                    