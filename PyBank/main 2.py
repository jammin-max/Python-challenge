import os
import csv

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
    #print(f"header:{csv_header}")
    # created lists to store column data
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []

# to collect the total months
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    #print(f'total months:{len(month)}')

#to collect total revenue over all months
    revenue_total =map(int,revenue)
    total_revenue = (sum(revenue_total))
    #print(f'total:{total_revenue}')

# to calculate average change
    x = 0
    for x in range(len(revenue) -1):
        profit_loss = int(revenue[x+1]) -int(revenue[x])
        revenue_change.append(profit_loss)
    total=sum(revenue_change)

#find monthly changes
    monthly_change = round (total / len(revenue_change),2)

#to print average changes
    #print(f"average change: {monthly_change}")

#to find the greatest increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    H = revenue_change.index(profit_increase)
    month_increase =month[H+1]
    #print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

#to find the greatest decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    I = revenue_change.index(profit_decrease)
    month_decrease = month[I+1]
    #print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
    

#all the print statements together now
    print(f'Financial Analysis'+'\n')
    print(f'----------------------------'+'\n')


    print("Total number of months: " + str(len(month)))

    print("Total Revenue in period: $ " + str(total_revenue))
      
    print("Average monthly change in Revenue : $" + str(monthly_change))

    print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

    print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
  
     
    
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