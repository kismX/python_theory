# TASK
# Write a decorator measure_time  which measures how long the function takes.
# mesure the time for X = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
# plot the time against X
# Hint: the inner function of decorator should return the time only. (edited) 


# import time 

# def measure_time(func):
#     def time_func(lst_sorted, value):
#         starttime = time.time()

#         func(lst_sorted, value)
        
#         endtime = time.time()
#         elapsed = endtime - starttime
#         print(f"{elapsed} sec.")
#         return elapsed
#     return time_func


    

# @measure_time
# def binary_search(lst_sorted, value):
    
#     while len(lst_sorted) > 1:
#         middle = len(lst_sorted) // 2
#         if lst_sorted[middle] != value:
#             if lst_sorted[middle] > value:
#                 lst_sorted = lst_sorted[:middle]
#             elif lst_sorted[middle] < value:
#                 lst_sorted = lst_sorted[middle:]
#         else:
#             return True
#     return False 

# x = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]


# a = binary_search(x, 100)
# b = binary_search(x, 1_000)
# c = binary_search(x, 10_000)
# d = binary_search(x, 100_000)
# e = binary_search(x, 1_000_000)
# f = binary_search(x, 10_000_000)


# print('----------------------------------')

# import matplotlib.pyplot as plt


# result = [] 
# x = [num for num in range(1,1001) if num % 4 == 0]
# for zahl in x:
#     result.append(binary_search(x,-1))

# #x = ["100", "1_000", "10_000", "100_000", "1_000_000", "10_000_000"]

# y = result


# plt.plot(x,y, ":o", label="Bananenjoghurt")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("KOole Grafik")
# plt.legend()
# plt.show()

# Solution 1
import time
import matplotlib.pyplot as plt
def measure_time(func):
    def wrapper(*args, **kwargs):
        steps = 20
        times = []
        for i in range(steps):
            start_time = time.process_time_ns()
            func(*args, **kwargs)
            end_time = time.process_time_ns()
            execution_time = end_time - start_time
            times.append(execution_time)
        return sum(times)/len(times) # average
    return wrapper

@measure_time
def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False

X = range(1, 50_001)
X = [num for num in X if num % 10 == 0]
# X = [100, 1_000, 10_000, 100_000]

execution_times = []
for x in X:
    lst_sorted = list(range(1,x+1))
    execution_time = binary_search(lst_sorted, -1)
    execution_times.append(execution_time)
plt.plot(X, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()