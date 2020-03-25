from hashlib import sha256
import csv
from collections import OrderedDict
import operator

def hash_password_hack(input_file_name, output_file_name):

    passDictionary = OrderedDict()

    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        for row in reader:
            flag = False
            listOfHash = list()
            name = row[0]
            for letter in row[1 :]: # or row[1]
                listOfHash.append(letter)
            stringOfHash = ''.join(listOfHash)
  
            password = '1000' #initial pass , assumed that password is beteween 1000 and 9999
            while int(password)<=9999 :

                hashObject = sha256(password.encode())
                hexDig = hashObject.hexdigest()

                if hexDig == stringOfHash:
                    flag = True
                    passDictionary[name] = password
                    break
                else:
                    password = int(password)
                    password +=1 
                    password = str(password)

            if flag==False: ##       then password is less than '1000'
                password = '0100' #initial pass
            while int(password)<=999 :

                hashObject = sha256(password.encode())
                hexDig = hashObject.hexdigest()

                if hexDig == stringOfHash:
                    flag = True
                    passDictionary[name] = password
                    break
                else:
                    password = int(password)
                    password += 1 
                    password = '0'+ str(password)

            if flag==False:##   then password is less than '0100'
                password = '0010' #initial pass
            while int(password)<=99 :

                hashObject = sha256(password.encode())
                hexDig = hashObject.hexdigest()

                if hexDig == stringOfHash:
                    flag = True
                    passDictionary[name] = password
                    break
                else:
                    password = int(password)
                    password += 1 
                    password = '00'+ str(password)

            if flag==False:##   then password is less than '0100'
                password = '0001' #initial pass
            while int(password)<=9 :

                hashObject = sha256(password.encode())
                hexDig = hashObject.hexdigest()

                if hexDig == stringOfHash:
                    flag = True
                    passDictionary[name] = password
                    break
                else:
                    password = int(password)
                    password += 1
                    password = '000'+ str(password)
    fin.close()   

    with open(output_file_name, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in passDictionary.items()]
    fout.close()

hash_password_hack('hash_file.csv', 'hack_file.csv') # Call Function