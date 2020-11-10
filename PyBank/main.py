# Modules
import os
import csv
# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#List to iterate through each row and store data 

total_months = []
total_profit = []
monthly_pc = []

# Open the CSV
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

     #Reading the header row
    csv_header = next(csvreader)
    
    #Loop through every row
    for row in csvreader:

    #Appens the number of months to it's list 
     total_months.append(row[0])

     #Append the total to it's list
     total_profit.append(int(row[1]))

     #Calculate the differnce in PL and find average 
     for i in range(len(total_profit)-1):
         monthly_pc.append(total_profit[i+1]-total_profit[i])

#The maximum and minimum in the monthly change

#We obtain values for the max and min value
max_increase_value = max(monthly_pc)
max_decrease_value = min(monthly_pc)

# We use the month list and index and add +1 for the for the next month

max_increase_month = monthly_pc.index(max(monthly_pc)) + 1
max_decrease_month = monthly_pc.index(min(monthly_pc)) + 1 


#Printing above statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_pc)/len(monthly_pc),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")