#We first import the functions we are going to use
import os
import csv 
#The follow line creates a path to the file regardless we are working with Mac or PC
employee_csv = os.path.join("..","Resources","employee_data.csv")
#Read in the CSV file
empl_id = []
CompleteName = []
Name = []
Last = []
DOB = []
Yr = []
Mon = []
dy = []
newDOB = []
SSN = []
SSNbis = []
State = []
st = {
"Alabama": "AL",
"Alaska": "AK",
"Arizona": "AZ",
"Arkansas": "AR",
"California": "CA",
"Colorado": "CO",
"Connecticut": "CT",
"Delaware": "DE",
"Florida": "FL",
"Georgia": "GA",
"Hawaii": "HI",
"Idaho": "ID",
"Illinois": "IL",
"Indiana": "IN",
"Iowa": "IA",
"Kansas": "KS",
"Kentucky": "KY",
"Louisiana": "LA",
"Maine": "ME",
"Maryland": "MD",
"Massachusetts": "MA",
"Michigan": "MI",
"Minnesota": "MN",
"Mississippi": "MS",
"Missouri": "MO",
"Montana": "MT",
"Nebraska": "NE",
"Nevada": "NV",
"New Hampshire": "NH",
"New Jersey": "NJ",
"New Mexico": "NM",
"New York": "NY",
"North Carolina": "NC",
"North Dakota": "ND",
"Ohio": "OH",
"Oklahoma": "OK",
"Oregon": "OR",
"Pennsylvania": "PA",
"Rhode Island": "RI",
"South Carolina": "SC",
"South Dakota": "SD",
"Tennessee": "TN",
"Texas": "TX",
"Utah": "UT",
"Vermont": "VT",
"Virginia": "VA",
"Washington": "WA",
"West Virginia": "WV",
"Wisconsin": "WI",
"Wyoming": "WY"
}
with open(employee_csv, "r", encoding="UTF-8") as csvfile: 
    #Split the data using commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print (f"Header : {header}")
    c = 0
    for row in csvreader:
        empl_id.append(row[0])
        
        #to split the comple name into Name & Last using split method
        CompleteName.append(row[1].split()) 
        Name.append(CompleteName[c][0])
        Last.append(CompleteName[c][1])

        #to split DOB into Yr,Mon,dy to rearrange them in different format
        DOB.append(row[2].split('-'))
        Yr.append(DOB[c][0])
        Mon.append(DOB[c][1])
        dy.append(DOB[c][2])
        newDOB.append(Mon[c] + "/" + dy[c] + "/" + Yr[c])
        
        #to split SSN into 3 sections to rearrange them in different format
        SSN.append(row[3].split('-'))
        SSNbis.append("***-**-" + SSN[c][2])

        #to populate the list State using the dictionary st
        State.append(st.get(row[4],0))
        
        c = c + 1

print ("-----------------------")  

#diferent print scenarios for testing
#print (State)
#print (st)
#print (Mon)
#print (DOB)
#print (CompleteName[1][1])

#to create a zip
cleaned_csv = zip(empl_id, Name, Last, newDOB, SSNbis, State)
# to define what is the exit file
output_file = os.path.join ("..","analysis","new_employee_data.csv")

#Do not forget to use newline='' to avoid spaces
with open(output_file,"w",newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(cleaned_csv)
