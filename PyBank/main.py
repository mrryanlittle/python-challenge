import csv

budget_csv = "Resources/budget_data.csv"

with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    TotalMonths = 0
    NetProfitLoss = 0
    previousvalue = 0
    for month in reader:
        TotalMonths = TotalMonths + 1
        NetProfitLoss = NetProfitLoss + int(month[1])
        difference = int(month[1]) - previousvalue
        previousvalue = int(month[1])
        
    GreatestIncrease = max(month[1])
    GreatestDecrease = min(month[1])

    AvgChange = NetProfitLoss / TotalMonths
    print("Total Months:")
    print(TotalMonths)
    print("Net Profit/Loss:")
    print(NetProfitLoss)
    print("Average Change in Profit/Loss:")
    print(AvgChange)

    output = open("PyBank/analysisFinAnalysis.txt", 'w')
    output.write("Financial Analysis\n")
    output.write("------------------\n")
    output.write("Total Months: 86\n")
    output.write("Total: $38,356,388\n")