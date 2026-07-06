import random
import time
#bubble sort
#O(n^2)
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l

#merge sort
#O(nlogn)
def merge(left, right):
    ans = []

    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1

        else:
            ans.append(right[j])
            j += 1

    while i < len(left):
        ans.append(left[i])
        i += 1

    while j < len(right):
        ans.append(right[j])
        j += 1

    return ans
    
def merge_sort(l) :
    if len(l) < 2 :
        return l[:]
    
    middle = len(l)//2
    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])

    return merge(left, right)

def count_time(func,lst):
    output = {}
    for i in lst:
        start = time.perf_counter()
        func(i.copy())
        end = time.perf_counter()
        output[len(i)] = end - start
    return output
    

l1 = [random.randint(1, 1000) for _ in range(100)]
l2 = [random.randint(1, 1000) for _ in range(1000)]
l3 = [random.randint(1, 1000) for _ in range(5000)]
l4 = [random.randint(1, 1000) for _ in range(10000)]
l = [l1,l2,l3,l4]

bubble_result = count_time(bubble_sort,l)
merge_result = count_time(merge_sort,l)

print('bubble sort running time results')
for i in bubble_result.items():
    print(i)
print()
print('merge sort running time results')
for i in merge_result.items():
    print(i)