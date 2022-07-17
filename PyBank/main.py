import csv
import os

budget_csvfile = os.path.join("Resources", "budget_data.csv")

#Variables for 
total_profLoss = float
profLossChange = float
Gincrease = float
Gdecrease = float
monthList = []

with open(budget_csvfile) as budcsvfile:

    budgetReader = csv.reader(budcsvfile, delimiter=',')
    #print(budgetReader)
    csvHeader = next(budgetReader)
    #print(f"CSV Header: {csvHeader}")
    for row in budgetReader:
        monthList.append(row[0])
        
        #print(monthList)
        #print(row)
    print("Financial Analysis")
    print("-"*30)
    print(f'Total Number of Months: {len(monthList)}')