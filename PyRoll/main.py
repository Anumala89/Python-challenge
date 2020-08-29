#import all the necessary dependencies
import os
import csv

#create a path for the csv file
Election_csv = os.path.join('Resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
Election_csv_output = os.path.join('Analysis', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data_analysis.txt')

#open the file as read and skip the header
with open(Election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    Election_list = list(csvreader)

    #get the total number of votes cast
    total = len(Election_list)

    #get a complete list of candidates who received votes
    list1 = list((Election_list[i][2]) for i in range(len(Election_list)))
    candidate_list = list([x for x in set(list1) if list1.count(x) >1])
    #print(candidate_list)
    
    #the total number of votes each candidate won
    candidate_one = list1.count(candidate_list[0])
    candidate_two = list1.count(candidate_list[1])
    candidate_three = list1.count(candidate_list[2])
    candidate_four = list1.count(candidate_list[3])
    
    #get the percentage of votes each candidate won
    candidate_one_percent ='{:.3%}'.format(candidate_one / total)
    candidate_two_percent ='{:.3%}'.format(candidate_two / total)
    candidate_three_percent = '{:.3%}'.format(candidate_three / total)
    candidate_four_percent = '{:.3%}'.format(candidate_four / total)
    
    #get the winner of the election based on popular vote
    winner = max(set(list1), key = list1.count)

    #print the result 
    print('Election Results')
    print('--------------------------')
    print(f'Total Votes: {total}')
    print('--------------------------')
    print(f'{candidate_list[0]} : {candidate_one_percent} ({candidate_one})')
    print(f'{candidate_list[1]} : {candidate_two_percent} ({candidate_two})')
    print(f'{candidate_list[2]} : {candidate_three_percent} ({candidate_three})')
    print(f'{candidate_list[3]} : {candidate_four_percent} ({candidate_four})')
    print('--------------------------')
    print(f'Winner : {winner}')
    print('--------------------------')


# Export the results to text file
with open(Election_csv_output, "w") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('------------------------------------\n')
    txtfile.write(f'Total Votes: {total}\n')
    txtfile.write('------------------------------------\n')
    txtfile.write(f'{candidate_list[0]} : {candidate_one_percent} ({candidate_one})\n')
    txtfile.write(f'{candidate_list[1]} : {candidate_two_percent} ({candidate_two})\n')
    txtfile.write(f'{candidate_list[2]} : {candidate_three_percent} ({candidate_three})\n')
    txtfile.write(f'{candidate_list[3]} : {candidate_four_percent} ({candidate_four})\n')
    txtfile.write('-------------------------------------\n')
    txtfile.write(f'Winner : {winner}\n')
    txtfile.write('-------------------------------------\n')




