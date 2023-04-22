import csv

csv_path = "Resources/election_data - Copy.csv"

votes=0

candidates={}



with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
   # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

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
for key in candidates:
    print(key,100*candidates[key]/votes)
#create output
with open('output_carlos1_pypoll.txt','w')as txt_file:
    output=f"""Election Results
            ------------------------------
total votes:{votes}
Total:{candidates}"""
    txt_file.write(output)