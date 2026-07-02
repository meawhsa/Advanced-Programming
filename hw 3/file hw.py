result = []
with open('std_info_4042.txt') as f:
    lines = f.readlines()

keys = lines[0].strip().split(",")

for line in lines[1:]:
    values = line.strip().split(',')
    student_dict = dict(zip(keys , values))
    result.append(student_dict)

print(result)

import csv

with open('std_info_4042.csv' ,'w') as c :
    writer = csv.DictWriter(c , fieldnames = result[0].keys())
    writer.writeheader()
    writer.writerows(result)
