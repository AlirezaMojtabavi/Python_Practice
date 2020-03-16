import hashlib
import csv
from collections import OrderedDict
import operator

def hash_password_hack(input_file_name, output_file_name):
    letter_dic = OrderedDict()
    pass_dict = OrderedDict()


    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        for row in reader:
            flag = False
            letter_list = list()
            name = row[0]
            for letter in row[1 :]:
                letter_list.append(letter)
            letter_dic[name] = letter_list
            Pass_String = ''.join(letter_list)
  
            MyPassword = '1000' #initial pass , suppose password beteween 1000 and 9999
            while int(MyPassword)<=9999 :

                hash_object = hashlib.sha256(MyPassword.encode())
                hex_dig = hash_object.hexdigest()

                if hex_dig == Pass_String:
                    flag = True
                    pass_dict[name] = MyPassword
                    #print(MyPassword) 
                    break
                else:
                    MyPassword = int(MyPassword)
                    MyPassword = MyPassword+1 
                    MyPassword = str(MyPassword)

            if flag==False:##       then password is less than '1000'
                MyPassword = '0100' #initial pass

            while int(MyPassword)<=999 :

                hash_object = hashlib.sha256(MyPassword.encode())
                hex_dig = hash_object.hexdigest()

                if hex_dig == Pass_String:
                    flag = True
                    pass_dict[name] = MyPassword
                    #print(MyPassword) 
                    break
                else:
                    MyPassword = int(MyPassword)
                    MyPassword = MyPassword+1 
                    MyPassword = '0'+ str(MyPassword)


            if flag==False:##   then password is less than '0100'
                MyPassword = '0010' #initial pass

            while int(MyPassword)<=99 :

                hash_object = hashlib.sha256(MyPassword.encode())
                hex_dig = hash_object.hexdigest()

                if hex_dig == Pass_String:
                    flag = True
                    pass_dict[name] = MyPassword
                    #print(MyPassword) 
                    break
                else:
                    MyPassword = int(MyPassword)
                    MyPassword = MyPassword+1 
                    MyPassword = '00'+ str(MyPassword)


            if flag==False:##   then password is less than '0100'
                MyPassword = '0001' #initial pass

            while int(MyPassword)<=9 :

                hash_object = hashlib.sha256(MyPassword.encode())
                hex_dig = hash_object.hexdigest()

                if hex_dig == Pass_String:
                    flag = True
                    pass_dict[name] = MyPassword
                    #print(MyPassword) 
                    break
                else:
                    MyPassword = int(MyPassword)
                    MyPassword = MyPassword+1 
                    MyPassword = '000'+ str(MyPassword)


    with open(output_file_name, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in pass_dict.items()]  


hash_password_hack('D:/tamarin/python_temp/Moghadamati/final_project/final.csv', 'D:/tamarin/python_temp/Moghadamati/final_project/output_file_name.csv')