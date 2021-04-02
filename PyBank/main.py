import os
import csv
#set direct path
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)

budget_csv = os.path.join( "Resources", "budget_data.csv")
with open(budget_csv,"r", encoding="utf-8") as csvfile_whatever:    
    csvreader = csv.reader(csvfile_whatever, delimiter=',')
    next(csvreader) 
    #add row counter
    row_count = sum(1 for row in csvreader)
    print(f"total months in the data set : {row_count}")

    #total = 0
    #for row in csvreader(csvfile_whatever):
        #total = sum(int(row[1]))
    #print(total)

    
    

  
     
    
     #print(type(row))
        # this will print months
        #print row[1]
# this will print profit, and loss = sum this
        #print(row[1])
        #changes in profit,and losses, and find the the average of the changes
        # find maximum (Date included)
        #find minimum  (date included)
        #print
        #create txt file
        #write to the txt file
