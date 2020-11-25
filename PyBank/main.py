# import dependencies
import csv

# grab files
budget_csv = "PyBank/Resources/budget_data.csv"

# define variables
TotalMonths = []
TotalAmount = []
MonthlyChangeProfit = []

MonthlyChange = 0
MonthlyChangeTotal = 0
InitialProfitCounter = 0

# open files to use
with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

# for loop
    for row in reader:
        TotalMonths.append(row[0])
        SumMonths = len(TotalMonths)
        TotalAmount.append(float(row[1]))
        ProfitForMonth = int(row[1])
        MonthlyChange = float(ProfitForMonth)
        MonthlyChangeTotal = MonthlyChangeTotal + MonthlyChange
        InitialProfitCounter = int(row[1])
        MonthlyChangeProfit.append(MonthlyChange)
        MaxProfit = max(MonthlyChangeProfit)
        MaxIndex = MonthlyChangeProfit.index(MaxProfit)
        MinProfit = min(MonthlyChangeProfit)
        MinIndex = MonthlyChangeProfit.index(MinProfit)
        AvgChangeProfit = round(MonthlyChangeTotal/SumMonths)
        SumAmount = sum(TotalAmount)

# print to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {SumMonths}')
print(f'Total Amount: ${SumAmount}')
print(f'Average Monthly Change: ${SumAmount}')
print(f'Greatest Increase in Profits: {TotalMonths[MaxIndex]} ${MaxProfit}')
print(f'Greatest Decrease in Profits: {TotalMonths[MinIndex]} ${MinProfit}')

# output to file
output = open("PyBank/FinancialAnalysis.txt", 'w')
output.write(f'''
Financial Analysis
------------------
Total Months: {SumMonths}
Total: ${SumAmount}
Average Monthly Change: ${AvgChangeProfit}
Greatest Increase in Profits: {TotalMonths[MaxIndex]} (${MaxProfit})
Greatest Decrease in Profits: {TotalMonths[MinIndex]} (${MinProfit})''')