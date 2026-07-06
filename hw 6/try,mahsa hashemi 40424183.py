result = []
try:
 f=open('std_info_4042.txt')
except FileNotFoundError:
    print("file not found")
else:
    
    keys = lines[0].strip().split(",")
    for line in lines[1:]:
      values = line.strip().split(',')
      student_dict = dict(zip(keys , values))
      result.append(student_dict)
    print(result)
