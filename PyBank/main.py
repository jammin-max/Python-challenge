import os
import csv

# 2 list's to represent my columns


# Path to collect data from the Resources folder
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

os.chdir(dir_path)
budget_csv = os.path.join('Resources','budget_data.csv')

#start to read my CSV file

with open(budget_csv, 'r',encoding="utf-8") as csvfile:

        # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)
    print(f"header:{csv_header}")
    # created lists to store column data
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []

# to collect the total months
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month)
# to collect total revenue
  



    
    #months = []
    #net_profit_loss = []
    
    #for row in csvreader:
        #total_months.append(row[0])
        
        #net_profit_loss.append(row[1])
        
        #row_count = sum(1 for row[0] in csvreader)

        #average =0
        #average = average(net_profit_loss)
        #net_profit_loss.append(average)
        #print (f'the total months in this data set is:  {row_count}')
        #print(net_profit_loss)
        
        #for row in csvreader:
            #print(row)
            #total =0
            #total += int(row[1])
            #net_profit_loss.append(total)

        
        #print(row)
        
        
        #row_count = sum(1 for row in csvreader)

        
        

        #total =0
        #total += range(row[1]
        
        
        #profit_loss.append(row[1])
        
        #total =0
        #total += range(row[1]
        
        
        
        
        #print(total)

        

    #print(analysis(month_year))

   
        # Loop through the data
    #for row in csvreader:
        #month_year = str(row[1])
        #profit_loss = int(table_data[1])
        #row_count = sum(1 for row in csvreader)
        #sum =range(int([1]))
        #total = sum(int([1]))
        #profit_loss += for row[1] in csvreader
        #print(f'the total months in this data set is:  {row_count}')
        
        #print(table_data[0])

    

    

       





