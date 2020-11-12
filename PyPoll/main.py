# Import Modules
import os
import csv
# Set path for file to use 
csvpath = os.path.join('Resources', 'election_data.csv')

#Create list to iterate through each row and store data 

total_votes_cast = 0
Khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
candidate = set()
winner = 0

# Open the CSV path where the file is located
with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")

     #Reading the header row to skip to the next line
    csv_header = next(csvreader)
    
    #Loop through every row
    for row in csvreader:

#To get the total number of vote cast
        total_votes_cast += 1
        candidate.add(row[2])

#To get the number of vote per candidate
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

#To get the percentage of votes for each candidate

khan_Percent = (Khan_votes/total_votes_cast) 
correy_percent = (correy_votes/total_votes_cast) 
li_percent = (li_votes/total_votes_cast) 
otooley_percent = (otooley_votes/total_votes_cast) 

#The winner of the election 
vote_total = [Khan_votes, correy_votes, li_votes, otooley_votes]

#Assign variables
winner_counts = max(vote_total)
winner_name = ""

#Use if statement to check winner
if winner_counts == Khan_votes :
    winner_name = "Khan"

elif winner_counts == correy_votes :
    winner_name = "Correy"   

elif winner_counts == li_votes :
    winner_name = "Li"

elif winner_counts == otooley_votes :
    winner_name = "O'Tooley"

else :
    winner_name = "No winner"



#Print the above statements
print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes_cast))
print("---------------------")
print("Khan: " + "{:.3%}".format(khan_Percent) + " " + (str(Khan_votes)))
print("Correy: " + "{:.3%}".format(correy_percent) + " " + (str(correy_votes)))
print("Li: " + "{:.3%}".format(li_percent) + " " + (str(li_votes)))
print("O'Tooley: " + "{:.3%}".format(otooley_percent) + " " + (str(otooley_votes)))
print("---------------------")
print("Winner: " +  winner_name)
print("---------------------")
print("----")