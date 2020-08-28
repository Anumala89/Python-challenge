#import all the necessary dependencies
import os
import csv

#create a path for the csv file
Budget_csv = os.path.join('Resources','02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
Budget_csv_output = os.path.join('Analysis', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data_analysis.txt')

#print the header
print('Fiancial Analysis')

print('------------------------------------')

#open the csv file
with open(Budget_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    Budget_list = list(csvreader)
    
    #get the total number of months
    Months = len(Budget_list)
    print(f'Total months : {Months}')

    #get the net total amount of 'Profit/Losses' over he entire period
    Total = sum(int(Budget_list[i][1]) for i in range(len(Budget_list)))
    print(f'Total : ${Total}')

    #get the average of the changes in "Profit/Losses" over the entire period
    Change_list = list(int(Budget_list[i][1]) for i in range(len(Budget_list)))
    Average_change_list = list((Change_list[j]-Change_list[j-1]) for j in range(1,len(Change_list)))
    Average_change = round(sum(Average_change_list) / len(Average_change_list),2)
    print(f'Average_change : ${Average_change}')
    
    #get the greatest increase in profits (date and amount) over the entire period
    date = list((Budget_list[i][0]) for i in range(1,len(Budget_list)))
    greatest_increase = max(Average_change_list)
    increase_date = date[Average_change_list.index(max(Average_change_list))]
    print(f'Greatest Increase in Profits : {increase_date} (${greatest_increase})')

    # get the greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(Average_change_list)
    decrease_date = date[Average_change_list.index(min(Average_change_list))]
    print(f'Greatest Decrease in Profits : {decrease_date} (${greatest_decrease})')

# Export the results to text file
with open(Budget_csv_output, "w") as txtfile:
    txtfile.write('Fiancial Analysis\n')
    txtfile.write('------------------------------------\n')
    txtfile.write(f'Total months : {Months}\n')
    txtfile.write(f'Total :  ${Total}\n')
    txtfile.write(f'Average_change : ${Average_change}\n')
    txtfile.write(f'Greatest Increase in Profits : {increase_date} (${greatest_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits : {decrease_date} (${greatest_decrease})\n')
