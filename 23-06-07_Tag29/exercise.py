# # Exercise(pivot choice):
# # In the Quicksort algorithm, the choice of the pivot can affect the efficiency of the sorting process:
# # First or Last Element: One simple approach is to select the first or last element of the array as the pivot. 
# # This strategy is easy to implement but can be inefficient for already sorted or nearly sorted arrays.
# # Random Element: Choosing a random element from the array as the pivot helps to eliminate bias in the pivot selection. 
# # Randomized pivot selection can provide good average-case performance, but it may still suffer from poor performance in certain scenarios.

# def quicksort(lst):
#     if len(lst) < 2:
#         return lst  #[2]
#     else:
#         pivot = lst[1]
#         less = [num for num in lst[:1] + lst[2:] if num <= pivot]
#         greater = [num for num in lst[:1] + lst[2:] if num > pivot]
#         print('##############')
#         print(f"pivot: {pivot}")
#         print(f"less: {less}")
#         print(f"greater: {greater}")

#     return quicksort(less) + [pivot] + quicksort(greater) 



import random
import time 
from collections import defaultdict
results = defaultdict(list)


def measure_time(func):
    def time_func(bla):
        starttime = time.time()

        result = func(bla)
        
        endtime = time.time()
        elapsed = endtime - starttime
        results[func.__name__].append(elapsed)
        return result
    return time_func

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[1]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        # print('##############')
        # print(f"pivot: {pivot}")
        # print(f"less: {less}")
        # print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater)



def quicksort_rand(lst):
    
    if len(lst) < 2:
        return lst
    else:
        random_num = random.randint(0,len(lst)-1)
        #print(random_num, " ", len(lst))
        pivot = lst[random_num]
        less = [num for num in lst[:pivot] + lst[pivot:] if num <= pivot]
        greater = [num for num in lst[:pivot] + lst[pivot:] if num > pivot]
        # print('##############')
        # print(f"pivot: {pivot}")
        # print(f"less: {less}")
        # print(f"greater: {greater}")

    return quicksort_rand(less) + quicksort_rand(greater)

@measure_time
def wrapper_rand(lst):
    quicksort_rand(lst)

@measure_time
def wrapper_normal(lst):
    quicksort(lst)


X = range(1, 1001)
X = [num for num in X if num % 4 == 0]

for num in X:
    my_list1 = list(range(num))
    random.shuffle(my_list1)
    wrapper_rand(my_list1)

for num in X:
    my_list2 = list(range(num))
    random.shuffle(my_list2)
    wrapper_normal(my_list2)

#print(results)

import matplotlib.pyplot as plt

plt.plot(X, results["wrapper_rand"])
plt.plot(X, results["wrapper_normal"])
plt.show()
