import csv
import os

budget_csvfile = os.path.join("Resources", "budget_data.csv")

#Variables declared
total = 0
changeTotal = 0
Gincrease = float
Gdecrease = float
monthList = []

with open(budget_csvfile) as budcsvfile:

    budgetReader = csv.reader(budcsvfile, delimiter=',')
    #print(budgetReader)
    csvHeader = next(budgetReader)
    print(f"CSV Header: {csvHeader}")
    for row in budgetReader:
        monthList.append(row[0])
        total += int(row[1])
        changeTotal = int(row[1])

        print(row)

    print("Financial Analysis")
    print("-"*25)
    print(f'Total No. of Months: {len(monthList)}')
    print(f'Gross Value: ${total}')
    print(f'Average Change: ${changeTotal}')