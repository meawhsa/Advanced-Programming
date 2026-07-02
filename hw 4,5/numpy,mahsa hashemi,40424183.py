import numpy as np
#homework 1
matrix = np.full((13,13),1)
nums_2= [1,6,11]
nums_3= [3,4,8,9]
for i in nums_2:
    matrix[i,:] = 2
    matrix[:, i] = 2
for i in nums_3:
    for j in nums_3:
        matrix[i,j] = 3
   
print(matrix)

#homework 2 

hi = np.array(([96,15,80,4],[49,43,96,85],[81,92,66,94]))
bye_row1 = []
bye_row2 = []
num = [0,1,2]
num1 = [0,2]
for i in num:
    for j in num1:
        bye_row1.append(hi[i,j])
        bye_row2.append(hi[i,j+1])
bye = np.array((bye_row1,bye_row2))
print(hi)
print(bye)

