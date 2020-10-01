#This is my first homework in Python so wish me luck

#We first import the functions we are going to use
import os
import csv 

#The follow line creates a path to the file regardless we are working with Mac or PC
#handle_csv = os.path.join("..","Resources","PyBank_Resources_budget_data.csv")
handle_csv = "../Resources/PyBank_Resources_budget_data.csv"


#Read in the CSV file
with open(handle_csv, "r", encoding="UTF-8") as csvfile:
    #Split the data using commas
    csvreader = csv.reader(handle_csv, delimiter=",")
    header = next(csvreader)
    print (f"Header : {header}")
    print ("-----------------------")

