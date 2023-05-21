import csv

csv_path = "Resources/election_data - Copy.csv"

votes=0

candidates={}



with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
   # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        
        votes += 1
        #get the candidate
        #if the candidate is in the dictionary, add 1 to the value
        #else, init with a vote of one
        candidate= row[2]
        if candidate in candidates.keys():
            candidates[candidate]+=1
        else:
            candidates[candidate]=1

print(votes)
print(candidates)

#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner = max(candidates, key=candidates.get)
print(winner)

output = f"""Election Results
-------------------------
Total Votes: {votes}
-------------------------\n"""


for key in candidates.keys():
    perc =  round(100*candidates[key]/votes, 3)
    newline = f"{key}: {perc}% ({candidates[key]})\n"
    output += newline

lastline = f"""
-------------------------
Winner: {winner}
-------------------------
"""

output += lastline
print(output)

output2 = f"""Election Results
-------------------------
Total Votes: {votes}
-------------------------
# Charles Casper Stockham: {round(100*candidates['Charles Casper Stockham']/votes, 3)}% ({candidates['Charles Casper Stockham']})
# Diana DeGette: {round(100*candidates['Diana DeGette']/votes, 3)}% ({candidates['Diana DeGette']})
# Raymon Anthony Doane: {round(100*candidates['Raymon Anthony Doane']/votes, 3)}% ({candidates['Raymon Anthony Doane']})
# -------------------------
# Winner: {winner}
# -------------------------
# """


with open('output_carlos1_pypoll.txt','w')as txt_file:
    txt_file.write(output)