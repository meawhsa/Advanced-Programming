import time
from fastapi import FastAPI
import random
#question 1
'''O(1)'''
def return1(l):
    if len(l) == 0 :
        return None
    else :
        return l[0]

#question 2
'''O(log(n))'''
def divid2(n) :
    num = 0
    while n!= 1 :
        num += 1
        n //= 2
    return num

#question 3
'''O(n)'''
def find_large(l):
    largest = l[0]
    for x in l[1:]:
        if x > largest:
            largest = x
    return largest

#question 4
'''O(n^2)'''               
def find_equal(l):
    num = 0 
    for i in range(len(l)):
        for j in range(i+1 , len(l)):
            if l[i] == l[j] :
              num += 1
    return num
                          
def count_time(func,lst):
    output = {}
    for i in lst:
        start = time.perf_counter()
        func(i)
        end = time.perf_counter()
        if isinstance(i,list):
           output[len(i)] = end - start
        else :
            output[i] = end - start
    return output

l_1 = [random.randint(1, 1000) for _ in range(100)]
l_2 = [random.randint(1, 1000) for _ in range(10000)]
l_3 = [random.randint(1, 1000) for _ in range(1000000)]
l_4 = [random.randint(1, 1000) for _ in range(10000000)]

q1_list = [l_1,l_2,l_3,l_4]
q1_test = count_time(return1,q1_list)
print('question 1 running time results')
for i in q1_test.items():
    print(i)

q2_list = [2,16,64,128,1024,2048]
q2_test = count_time(divid2,q2_list)
print()
print('question 2 running time results')
for i in q2_test.items():
    print(i)

l1 = [random.randint(1, 1000) for _ in range(10000)]
l2 = [random.randint(1, 1000) for _ in range(20000)]
l3 = [random.randint(1, 1000) for _ in range(40000)]
l4 = [random.randint(1, 1000) for _ in range(80000)]
l5 = [random.randint(1, 1000) for _ in range(160000)]
l6 = [random.randint(1, 1000) for _ in range(320000)]

q3_list = [l1,l2,l3,l4,l5,l6]
q3_test = count_time(find_large,q3_list)
print()
print('question 3 running time results')
for i in q3_test.items():
    print(i)

li1 = [random.randint(1, 1000) for _ in range(500)]
li2 = [random.randint(1, 1000) for _ in range(1000)]
li3 = [random.randint(1, 1000) for _ in range(2000)]
li4 = [random.randint(1, 1000) for _ in range(4000)]
li5 = [random.randint(1, 1000) for _ in range(8000)]
q4_list = [li1,li2,li3,li4,li5]
q4_test = count_time(find_equal,q4_list)
print()
print('question 4 running time results')
for i in q4_test.items():
    print(i)