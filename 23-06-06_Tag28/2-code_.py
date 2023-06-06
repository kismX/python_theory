# l1 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# print(len(l1))

# #Step 1
# print(len(l1) // 2 )  # we get the middle index of l1
# print(l1[len(l1)// 2]) # is this higher or lower than my item: 76 > 57
# l2 = l1[:len(l1)//2] # we discarded half of our list
# print(l2)

# #Step2
# print(l2[len(l2)//2])
# print('NOT FLOOR',len(l2)/2)
# print('FLOOR',len(l2)//2)
# l3 = l2[:len(l2)//2]
# print(l3)

# # Step3
# print(l3[len(l3)//2]) # Done!



l1 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]


# def binary_search(lst_sorted, value):
#     if lst_sorted[len(lst_sorted) // 2] == value:
#         return True
#     else: 
#         new_list = lst_sorted[:len(lst_sorted) // 2]
#         return binary_search(new_list, value)
        
        

# print(binary_search(l1, 50))



def binary_search(lst_sorted, value):
    step=0
    while len(lst_sorted) > 1:
        step+=1
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True, step
    return False, step


print(binary_search(range(1,4_000_001),4000000)) # --> tuple binary_search(lst,)



# X = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
# Y = [binary_search(range(1, N+1), N) for N in X]

# print(Y)

# import matplotlib.pylab as plt

# plt.plot(X, Y, label="binary_search")
# plt.xlabel("input size")
# plt.ylabel("Number of steps")
# plt.legend()
# plt.title("Binary Search")
# plt.show()


