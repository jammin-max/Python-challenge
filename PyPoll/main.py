import os
import csv

# Path to collect data from the Resources folder
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)
budget_csv = os.path.join('Resources','election_data.csv')
#start to read my CSV file
with open(budget_csv, 'r',encoding="utf-8") as csvfile:

        # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)
    #print(f"header:{csv_header}")
    
    #creating lists to store data
    voter_id = []
    county = []
    candidate = []
    khan = []
    correy = []
    li = []
    otooley = []
    
    for row in csvreader:
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

    #VOTE COUNT
    total_votes = (len(voter_id))
    #print(total_votes)

    #Votes by canidate
    for candidate in candidate:
        if candidate == "Khan":
            khan.append(candidate)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidate)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidate)
            li_votes = len(li)
        else:
            otooley.append(candidate)
            otooley_votes = len(otooley)
    #print(khan_votes)
    #print(correy_votes)
    #print(li_votes)
    #print(otooley_votes)
    
    
    #Percentages for each canidate
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    #print(khan_percent)
    #print(correy_percent)
    #print(li_percent)
    #print(otooley_percent)
    
    #The winner is
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"
# Create TEXT File, and write results to TEXt file
    textoutput = os.path.join('Analysis', 'Poll_Analysis.txt')
with open (textoutput, 'w', newline='') as analysis:
    write = csv.writer(analysis)
    write.writerows([
        
        ["Election Results"],
        ["-------------------------------------"],
        ["Total Votes:" + str(total_votes)],
        ["-------------------------------------"],
        [f"Khan: {khan_percent}% ({khan_votes})"],
        [f"Correy: {correy_percent}% ({correy_votes})"],
        [f"Li: {li_percent}% ({li_votes})"],
        [f"O'Tooley: {otooley_percent}% ({otooley_votes})"],
        [f"-----------------------------------"],
        [f"Winner: {winner}"],
        [f"-----------------------------------"]
    ])



        #All print statements together now

print(f"Election Results" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Total Votes: {total_votes}" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Khan: {khan_percent}% ({khan_votes})" + "\n")
print(f"Correy: {correy_percent}% ({correy_votes})" + "\n")
print(f"Li: {li_percent}% ({li_votes})" + "\n")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Winner: {winner}" + "\n")
print(f"-----------------------------------")