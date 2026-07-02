import numpy as np

#create a vector with 6 elements between 0, 2𝜋
import math
ans=np.linspace(0,math.pi*2,6)
print('vector = ' , ans)

#compute the following sigma
nums = np.arange(1,11)
sum_sigma=np.sum((-1)**(nums-1)/2**(nums-1))
print('The result of the summation is' , sum_sigma)

#compute derivative of Sine function

def derivative_sin(x, h=1e-5):
    return (np.sin(x + h) - np.sin(x)) / h

x = np.linspace(0, 2*np.pi, 1000)
d = derivative_sin(x)

y = np.sin(x)
dy_dx = np.gradient(y, x)   

print('Numerical derivative of sine without using NumPy',d)
print('Numerical derivative of sine using NumPy',dy_dx)

# creating [1 9 3 6 5 3 7 0 9 -3 11]
vector = np.ones(11)
num = 9
for i in range(len(vector)):
    if i%2 == 0:
        vector[i] = i+1 
    else :
        vector[i] = num
        num -= 3
print(vector)