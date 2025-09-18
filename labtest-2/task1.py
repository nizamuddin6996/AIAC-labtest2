import csv

input_file = 'employeetest.csv'

with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = list(reader)

# Sort by Dept (column 1), then by Salary descending (column 2)
rows_sorted = sorted(rows, key=lambda x: (x[1], -int(x[2])))

print(','.join(header))
for row in rows_sorted:
    print(','.join(row))