# Modules
import os
import csv
# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create list to iterate through each row and store data 

total_months = []
total_profit = []
monthly_change = []

# Open the CSV
with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")

     #Reading the header row
    csv_header = next(csvreader)
    
    #Loop through every row
    for row in csvreader:

    #Appens the number of months to it's list cal length when printing 
     total_months.append(row[0])

     #Append the total to it's list, cal sum when printing
     total_profit.append(int(row[1]))

        # Go through the row to have the monthly change
    for i in range(len(total_profit)-1):
        
        # To Calculate monthly change
        monthly_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min for the  monthly_profit_change
max_increase_value = max(monthly_change)
max_decrease_value = min(monthly_change)

# Use list and index from max and min monthly_fit_change
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1 

# Printing the above statements 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#output files as text files in below path
output_path = os.path.join('analysis',"output.txt")

#Printing/writing results as text file 
with open(output_path, "w") as file:
    
    #Printing the Analysis as a text file and add \n for new line
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
