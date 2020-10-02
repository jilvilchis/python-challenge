#This is my first homework in Python so wish me luck
#We first import the functions we are going to use
import os
import csv 

#The follow line creates a path to the file regardless we are working with Mac or PC
budget_csv = os.path.join("..","Resources","budget_data.csv")
#budget_csv = "Resources/budget_data.csv"

#Read in the CSV file
with open(budget_csv, "r", encoding="UTF-8") as csvfile: 
    #Split the data using commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print (f"Header : {header}")
    print ("Financial Analysis")
    print ("-----------------------")
    t_months = 0 
    t_amount = 0
    PL = []
    date = []
    for line in csvreader:
        t_months = t_months + 1
        t_amount = t_amount + int(line[1])
        PL.append(line[1])
        date.append(line[0])
        #print(line)
    
    print (f"Total Months : {t_months}")
    print (f"Total : $ {t_amount}")
    #print (PL)
    #print(len(PL))
    
    avg_change = []
    for i in range(len(PL)):
        #print (PL[i])
        if i >= 1 :
            change = int(PL[i]) - int(PL[i-1])
            avg_change.append(change)
    #print(avg_change)
    
    key_day_max = (avg_change.index(max(avg_change))) + 1
    key_day_min = (avg_change.index(min(avg_change))) + 1   
    day_max = date[key_day_max]
    day_min = date[key_day_min]
    
    print (f"Average Change: ${sum(avg_change)/len(avg_change):.2f}")
    print (f"Greatest Increase in Profits: {day_max} (${max(avg_change)})")
    print (f"Greatest Decrease in Profits: {day_min} (${min(avg_change)})")

# to define what is the exit file
output_file = os.path.join ("..","analysis","PyBank_results.md")

#Do not forget to use newline='' to avoid spaces
with open(output_file,"w",newline='') as datafile:
    datafile.write ("Financial Analysis" + "\n")
    datafile.write ("-----------------------" + "\n")
    datafile.write (f"Total Months : {t_months}" + "\n")
    datafile.write (f"Total : $ {t_amount}" + "\n")
    datafile.write (f"Average Change: ${sum(avg_change)/len(avg_change):.2f}" + "\n")
    datafile.write (f"Greatest Increase in Profits: {day_max} (${max(avg_change)})" + "\n")
    datafile.write (f"Greatest Decrease in Profits: {day_min} (${min(avg_change)})" + "\n")

