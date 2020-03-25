import csv
from statistics import mean
from collections import OrderedDict
import operator

##------------------------------------Task 1 (GPA of each person, sorted by input sequence)--------------------

def Calculate_Average(input_file, output_file):

    average = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            average[name] = mean(grades)
    f.close()

    with open(output_file, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in average.items()]
    fout.close() 

Calculate_Average('list_of_grades.csv', 'GPA.csv') # call function

##---------------------------------Task 2 (GPA of each person, sorted by ascending order)----------------------

def Calculate_Ascending_Average(input_file, output_file):

    ascendingAverage = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            ascendingAverage[name] = mean(grades)
    ascendingAverage = {k: v for k, v in sorted(ascendingAverage.items(), key=lambda item: item[1])}
    f.close()

    with open(output_file, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in ascendingAverage.items()]
    fout.close()

Calculate_Ascending_Average('list_of_grades.csv', 'GPA_by_ascending_order.csv') # call function


##------------------------------------task3(top 3 GPA)-------------------------------------

def Calculate_top_three_average(input_file, output_file):

    averages = OrderedDict()
    top_Three_Average = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            averages[name] = mean(grades)
    f.close()

    averages = {k: v for k, v in sorted(averages.items(), key=lambda item: item[1], reverse=True)}
  
    counter = 1
    for k, v in averages.items():
        if counter <= 3:
            top_Three_Average[k] = v
            counter += 1
        else:
            break

    with open(output_file, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in top_Three_Average.items()]
    fout.close()

Calculate_top_three_average('list_of_grades.csv', 'top_Three_GPA.csv') # call function

# #------------------------------------task4(3 minimum GPA)-------------------------------------

def Calculate_bottom_three_average(input_file, output_file):

    averages = OrderedDict()
    Three_minimum_GPA = OrderedDict()

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader :
            name = row[0]
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            averages[name] = mean(grades)
    f.close()

    averages = {k: v for k, v in sorted(averages.items(), key=lambda item: item[1])}

    counter = 1
    for k, v in averages.items():
        if counter <= 3:
            Three_minimum_GPA[k] = v
            counter += 1
        else:
            break

    with open(output_file, 'w') as fout:
        [fout.write('{0},{1}\n'.format(key, value)) for key, value in Three_minimum_GPA.items()]
    fout.close()

Calculate_bottom_three_average('list_of_grades.csv', 'Three_minimum_GPA.csv') # call function

# #-------------------------------Task5(Average Of GPAs)-----------------------------------------------------

def calculate_total_average(input_file, output_file):
    
    GPAs = list()
    
    with open (input_file,'r') as fin:
        reader = csv.reader(fin)
        for row in reader:
            grades = list()
            for grade in row[1 :]:
                grades.append(float(grade))
            result = mean(grades)
            GPAs.append(float(result))
        AverageOfGPAs = float(mean(GPAs))
    fin.close()
        
    with open(output_file, 'w') as fout: 
        fout.write (str(AverageOfGPAs))
    fout.close()

calculate_total_average('list_of_grades.csv', 'Average_of_GPAs.csv') # call function
