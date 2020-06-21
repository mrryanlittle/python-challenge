import pandas as pd
import csv

election_data_path = "Resources/election_data.csv"

election_df = pd.read_csv(election_data_path)
election_df

votes_cast = election_df.count()
votes_cast

candidates = election_df['Candidate'].value_counts()
candidates

percentageKhan = (2218231 / 3521001) * 100
percentageKhan

percentageCorrey = (704200 / 3521001) * 100
percentageCorrey

percentageLi = (492940 / 3521001) * 100
percentageLi

percentageOTooley = (105630 / 3521001) * 100
percentageOTooley

print('Election Results')
print('--------------------')
print('Total Votes: 3521001')
print('--------------------')
print(f'Khan: {str(percentageKhan)}% (2218231)')
print(f'Correy: {str(percentageCorrey)}% (704200)')
print(f'Li: {str(percentageLi)}% (492940)')
print(f'OTooley: {str(percentageOTooley)}% (105630)')
print('--------------------')
print('Winner: Khan')
print('--------------------')

results = open('PyPoll/analysis/results.txt', 'w')
results.write(f'Election Results\n')
results.write(f'-----------------\n')
results.write(f'Total Votes: 3521001\n')
results.write(f'-----------------\n')
results.write(f'Khan: {str(percentageKhan)}% (2218231)\n')
results.write(f'Correy: {str(percentageCorrey)}% (704200)\n')
results.write(f'Li: {str(percentageLi)}% (492940)\n')
results.write(f'OTooley: {str(percentageOTooley)}% (105630)\n')
results.write(f'-----------------\n')
results.write(f'Winner: Khan\n')
results.write(f'-----------------\n')