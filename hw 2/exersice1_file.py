n = int(input('please enter the number of student'))
y401 = open('1401.txt' ,'w')
y400 =  open('1400.txt' ,'w')
for i in range(n):
    name = input('please enter the name of student:')
    year = int(input('please enter the year'))
    score = list(map(float,input('please enter scores').split()))
    avarage = 0
    for j in score :
               avarage += j
    avarage /= 3
    if year == 1401:
               y401.write(f' name : {name} , {year} , scores : {score} , avarage = {avarage:.2f}\n')
    else:
               y400.write( f' name : {name} , {year} , scores : {score} , avarage = {avarage:.2f}\n' )
y401.close()
y400.close()

    