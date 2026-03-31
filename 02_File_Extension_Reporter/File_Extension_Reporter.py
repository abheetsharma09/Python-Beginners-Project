#Import the Module OS
import os
#All the Variables
ext_list = []
ext_set = set()
list_all_files = os.listdir()
result = {}

#Defining a Function for the the evaluation of files
def file_func():
#This loop adds all the uniques extensions to set and all extensions to list
    for files in list_all_files:
        if "." in files: #Filter Outs the folder and files without extentions
            files_list = files.split(".")
            ext_list.append(files_list[1])
            ext_set.add(files_list[1])

#This loop count how many times a extension have been repeated and store it in a Dictionary
    for ext in ext_list:
        result[ext] = ext_list.count(ext)

    return result #Returns the data in the Form of dictionary 

print(file_func())
