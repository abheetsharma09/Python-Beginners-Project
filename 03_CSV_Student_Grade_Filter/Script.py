#import csv module
import csv

#Opens and read the CSV File and process the data
with open("students.csv" , "r") as csv_data:
    csv_students_data = csv.reader(csv_data)
    for data_in_csv in csv_students_data:
        #Filter the data of the passed students
        if int(data_in_csv[1]) >= 40:
            with open("Passed_Students.txt" , "a") as pass_stu: #writes in the passed.txt file
                pass_stu.write(f'{data_in_csv[0]} Passed \n')
        #Filter the data of the failed students
        else:
            with open("Failed_Students.txt" , "a") as pass_stu: #writes in the failed.txt
                pass_stu.write(f'{data_in_csv[0]} Failed \n')
