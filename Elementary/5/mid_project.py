import csv
from statistics import mean
from collections import OrderedDict
import operator

##------------------------------------Task 1 ------(moadele har fard be tartibe vorooodi va khorooji)--------------------

def Calculate_Average(input_file, output_file):
    grades_dic = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            grades_dic[name] = mean(grades)

           # print(grades)
        #print(grades_dic)

  #  with open(output_file, 'w') as fout:
 #           [fout.write('{0},{1}\n'.format(key, value)) for key, value in grades_dic.items()]   

#Calculate_Average('list_asli.csv', 'task11.csv') 

##---------------------------------Task 2 -------------(moadele afrad be tartibe soudi)-------------------------------

def Calculate_Ascending_Average(input_file, output_file):
    grades_dict2 = OrderedDict()
    sorted_grades_dict2 = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            grades_dict2[name] = mean(grades)
    sorted_grades_dict2 = sorted(grades_dict2.items(), key=operator.itemgetter(1))


           # print(grades)
    #print(sorted_grades_dict2)

  #  with open(output_file, 'w') as fout:
 #           [fout.write('{0},{1}\n'.format(key, value)) for key, value in sorted_grades_dict2.items()]   

#Calculate_Ascending_Average('list_asli.csv', 'task22.csv') 


#------------------------------------task3---------(3moadele bartar)-------------------------------------

def Calculate_top_three_average(input_file, output_file):
    grades_dict3 = OrderedDict()
    sorted_grades_dict3 = OrderedDict()
    top_3_ave = OrderedDict()
    counter = 0

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            grades_dict3[name] = mean(grades)
    #sorted_grades_dict3 = sorted(grades_dict3.items(), key=operator.itemgetter(1))
    sorted_grades_dict3 = sorted(grades_dict3.items(), key=lambda kv: kv[1], reverse=True)
    sorted_grades_dict3 = OrderedDict(sorted_grades_dict3)

    
    for k, v in sorted_grades_dict3.items():
        if counter <= 2:
            top_3_ave[k] = v
            counter = counter + 1
        else:
            break

           # print(grades)
   # print(top_3_ave)

    #with open(output_file, 'w') as fout:
     #       [fout.write('{0},{1}\n'.format(key, value)) for key, value in top_3_ave.items()]   

#Calculate_top_three_average('list_asli.csv', 'task33.csv') 

#------------------------------------task4---------(3moadele badtar)-------------------------------------

def Calculate_bottom_three_average(input_file, output_file):
    grades_dict4 = OrderedDict()
    sorted_grades_dict4 = OrderedDict()
    bottom_4_ave = OrderedDict()
    counter = 0
    unname_list = list()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            grades_dict4[name] = mean(grades)
    #sorted_grades_dict3 = sorted(grades_dict3.items(), key=operator.itemgetter(1))
    sorted_grades_dict4 = sorted(grades_dict4.items(), key=operator.itemgetter(1))
    sorted_grades_dict4 = OrderedDict(sorted_grades_dict4)

    
    for k, v in sorted_grades_dict4.items():
        if counter <= 2:
            bottom_4_ave[k] = v
            unname_list.append(v)
            counter = counter + 1
        else:
            break

           # print(grades)
    #print(unname_list)

    with open(output_file,'w') as fout:
        writer = csv.writer(fout)
        writer.writerow(unname_list) 
        fout.close()

#Calculate_bottom_three_average('list_asli.csv', 'task44.csv') 

#-------------------------------Task5-----------------------------------------------------

def calculate_total_average(input_file, output_file):
    
    averages = list()
    
    with open (input_file,'r') as fin:
        reader = csv.reader(fin)
        for row in reader:
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            result = mean(grades)
            averages.append(float(result))
        total_average = float(mean(averages))
        print(total_average)
        
    #with open(output_file,'wb') as fout:
    #   writer = csv.writer(fout)
    #   writer.writerow(str(total_average)) 
    #    fout.close()
    with open(output_file, 'w') as fout: 
        fout.write (str(total_average))

#calculate_total_average('list_asli.csv', 'task55.csv')
