#We first import the functions we are going to use
import os
import csv 
#The follow line creates a path to the file regardless we are working with Mac or PC
election_csv = os.path.join("..","Resources","election_data.csv")
#Read in the CSV file
with open(election_csv, "r", encoding="UTF-8") as csvfile: 
    #Split the data using commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print (f"Header : {header}")
    print ("Election Results")
    print ("-----------------------")

    t_votes = 0 
    Results = dict()
    for line in csvreader:
        t_votes = t_votes + 1
        if line[2] not in Results:
            Results[line[2]] = 1
        else:
            Results[line[2]] = Results[line[2]] + 1
    print (f"Total Votes : {t_votes}")
    print ("-----------------------")
    #print (Results)
    Khan_percent = "{:.2%}".format(Results.get('Khan',0) / t_votes)
    Correy_percent = "{:.2%}".format(Results.get('Correy',0) / t_votes) 
    Li_percent = "{:.2%}".format(Results.get('Li',0) / t_votes)
    Tooley_percent = "{:.2%}".format(Results.get("O'Tooley",0) / t_votes)
    print (f"Khan: {Khan_percent} ({Results.get('Khan',0)})")
    print (f"Correy: {Correy_percent} ({Results.get('Correy',0)})")
    print (f"Li: {Li_percent} ({Results.get('Li',0)})")
    # I struggled a little to print the O'Tooley name because of the ' in his name
    print ("O'Tooley: " + str(Tooley_percent) + " (" + str(Results.get("O'Tooley",0)) +")") 
    print ("-----------------------")
    Max = 0
    
    winner = max(Results, key=Results.get) #get key with max value
    print (f"Winner, winner chicken dinner for: {winner}")
    print ("-----------------------")
    
# to define what is the exit file
output_file = os.path.join ("..","analysis","PyPoll_results.md")

#Do not forget to use newline='' to avoid spaces
with open(output_file,"w",newline='') as datafile:
    datafile.write("Election Results" + "\n")
    datafile.write("-----------------------" + "\n")
    datafile.write(f"Total Votes : {t_votes}" + "\n")
    datafile.write ("-----------------------" + "\n")
    datafile.write (f"Khan: {Khan_percent} ({Results.get('Khan',0)})" + "\n")
    datafile.write (f"Correy: {Correy_percent} ({Results.get('Correy',0)})" + "\n")
    datafile.write (f"Li: {Li_percent} ({Results.get('Li',0)})" + "\n")
    datafile.write ("O'Tooley: " + str(Tooley_percent) + " (" + str(Results.get("O'Tooley",0)) +")" + "\n") 
    datafile.write ("-----------------------" + "\n")
    datafile.write (f"Winner, winner chicken dinner for: {winner}" + "\n")
    datafile.write ("-----------------------" + "\n")

