# Task 2

# initialize the first two numbers in the series
a, b = 1, 1

# print out the first two numbers
print(a)
print(b)

# use a loop to generate and print the remaining numbers in the series
for i in range(2, 50):
    # calculate the next number in the series as the sum of the previous two
    c = a + b
    
    # print out the next number in the series
    print(c)
    
    # update the previous two numbers to prepare for the next iteration
    a, b = b, c