import csv
import numpy as np

csv_path = "Resources/budget_data.csv"


# for each row 
# add 1 to some counter for month
# add column 2 (b) to some profit counter 

months = 0
total_profit = 0

is_first_row = True
last_month_profit = 0
changes = []
month_changes = []

# max change
# max month
max_change = -99999999999
max_month = ""

# min change
# min month
min_change = 999999999999999999999
min_month = ""


with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

   # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        row_profit = int(row[1])

         # check if first row (no change in first month but need to init last_month_profit)
        if is_first_row:
            last_month_profit = row_profit
            is_first_row = False
        else:
            change = row_profit - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset for the next month
            last_month_profit = row_profit

            # compared to max/min
            if change > max_change:
                 max_change = change
                 max_month = row[0]

            if change < min_change:
                min_change = change
                min_month = row[0]


        months += 1
        total_profit += int(row[1])
        
    print('###############################')
    print(months)
    print(total_profit)
        
    avg_changes = sum(changes) / len(changes)
    print(avg_changes)

    print(max_month, max_change)
    print(min_month, min_change)


#create output
with open('output_carlos.txt','w')as txt_file:
    output=f"""Financial Analysis
------------------------------
total Months:{months}
Total:${total_profit}
Average Change:${round(avg_changes,2)}
Greatest Increase in Profits:{max_month} (${max_change})
Greatest Decrease in Profits:{min_month} (${min_change})"""
    txt_file.write(output)
