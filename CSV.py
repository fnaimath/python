import csv
import pandas as pd
arr = []


fields = ['Name', 'Grade Percentage']

rows = [['Bob', '75'],
        ['Jim', '80'],
        ['Andy', '90'],
        ['George', '72'],
        ['Sal', '86']]

filename = 'student_records.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

df = pd.read_csv(filename)

for row in df.values:
    if int(row[1]) > 75:
        arr.append(row[0])

print(arr)