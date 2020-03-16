import csv
# For the average
from statistics import mean 
from collections import OrderedDict
import operator


def calculate_averages(input_file_name, output_file_name):   
        grades_dic = OrderedDict()

        with open(input_file_name, 'r') as fin:
                reader = csv.reader(fin)
                for row in reader:
                        grades_list = list()
                        name = row[0]
                        for grade in row[1 :]:
                                grades_list.append(float(grade))

                        grades_dic[name]= mean(grades_list)

        with open(output_file_name, 'w') as fout:
                [fout.write('{0},{1}\n'.format(key, value)) for key, value in grades_dic.items()]   

#calculate_averages('project_miyani_1.csv', 'project_miyani_11.csv')            



def calculate_sorted_averages(input_file_name, output_file_name):
        grades_dic = OrderedDict()

        with open(input_file_name) as fin:
                reader = csv.reader(fin)
                for row in reader:
                        grades_list = list()
                        name = row[0]
                        for grade in row[1 :]:
                                grade = float(grade)
                                grades_list.append((grade))

                        grades_dic[name]= mean(grades_list)

        sorted_grades_dic = sorted(grades_dic.items(), key=operator.itemgetter(1)) 
        sorted_grades_dic= OrderedDict(sorted_grades_dic)#Sorted dictionary

        with open(output_file_name, 'w') as fout:
                [fout.write('{0},{1}\n'.format(key, value)) for key, value in sorted_grades_dic.items()]
        
#calculate_sorted_averages('project_miyani_1.csv', 'project_miyani_12.csv')

  

def calculate_three_best(input_file_name, output_file_name):
        My_List = list()
        grades_dic = OrderedDict()
        three_best = list()

        with open(input_file_name,'r') as fin:
                reader = csv.reader(fin)
                for row in reader:
                        grades_list = list()
                        name = row[0]
                        for grade in row[1 :]:
                                grades_list.append(float(grade))
                        grades_dic[name]= mean(grades_list)

        sorted_grades_dic = sorted(grades_dic.items(), key=operator.itemgetter(1)) 
        sorted_grades_dic= OrderedDict(sorted_grades_dic)#Sorted dictionary

        My_List = list(sorted_grades_dic.items())
       
        i = -1
        while i>-4:
                three_best.append(My_List[i])
                i=i-1
        
        three_best = OrderedDict(three_best)

        with open(output_file_name, 'w') as fout:
                [fout.write('{0},{1}\n'.format(key, value)) for key, value in three_best.items()]
        
     
#calculate_three_best('project_miyani_1.csv', 'project_miyani_13.csv')
    


def calculate_three_worst(input_file_name, output_file_name):
        My_List = list()
        grades_dic = OrderedDict()
        three_worst = list()

        with open(input_file_name,'r') as fin:
                reader = csv.reader(fin)
                for row in reader:
                        grades_list = list()
                        name = row[0]
                        for grade in row[1 :]:
                                grades_list.append(float(grade))
                        grades_dic[name]= mean(grades_list)

        sorted_grades_dic = sorted(grades_dic.items(), key=operator.itemgetter(1)) 
        sorted_grades_dic= OrderedDict(sorted_grades_dic)#Sorted dictionary

        My_List = list(sorted_grades_dic.values())
        three_worst = My_List[: 3]

        with open(output_file_name, 'w') as fout: 
                for grade in three_worst:
                        fout.write(str(grade))
                        fout.write("\n")


#calculate_three_worst('project_miyani_1.csv', 'project_miyani_14.csv')


def calculate_average_of_averages(input_file_name, output_file_name):
        grades_dic = OrderedDict()

        with open(input_file_name,'r') as fin:
                reader = csv.reader(fin)
                for row in reader:
                        grades_list = list()
                        name = row[0]
                        for grade in row[1 :]:
                                grades_list.append(float(grade))
                        grades_dic[name]= mean(grades_list)
        
        grade_list = grades_dic.values()
        with open(output_file_name, 'w') as fout: 
                fout.write (str(mean(grade_list)))


#calculate_average_of_averages('project_miyani_1.csv', 'project_miyani_15.csv')                